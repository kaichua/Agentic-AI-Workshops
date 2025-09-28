from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import debug


def coordinator(state):
    """
    Select next speaker based on conversation context and ensure that every speaker has spoken at least once.
    Manages volley control and updates state accordingly.

    Updates state with:
    - next_speaker: Selected agent ID or "human"
    - volley_msg_left: Decremented counter

    Returns: Updated state
    """

    debug(state)
    volley_left = state.get("volley_msg_left", 0)
    debug(f"Volley messages left: {volley_left}", "COORDINATOR")

    if volley_left <= 0:
        debug("No volleys left, returning to human", "COORDINATOR")
        return {
            "next_speaker": "human",
            "volley_msg_left": 0
        }

    messages = state.get("messages", [])

    conversation_text = ""
    for msg in messages:
        # Messages are now always dicts
        conversation_text += f"{msg.get('content', '')}\n"

    system_prompt = """You are managing a forum discussion between different age groups regarding phenomenon that is occurring in Singapore.

    Available speakers:
    - student: 15 year old student, top of their class, concerned about reaching his dream university
    - adult: 30 year old salaried worker, engineer at a reputable IT company, concerned about cost of living
    - eldery: 65 year old retiree, living with spouse with no children, concerned about increased medical conditions due to aging

    Based on the conversation flow, select who should speak next to keep the conversation organized and related to the topic.
    Consider:
    - Every speaker should have at least spoken once
    - Who hasn't spoken recently
    - Whose age group would be able to relate to the highlighted issue better
    - Most importantly, who is trying to provide a tangible solution to the issue 
    - Natural forum discussion flow
    - elderly should speak more as they have the most life experience

    Respond with ONLY the speaker ID (student, adult, or eldery).
    """

    user_prompt = f"""Recent conversation:
{conversation_text}

Who should speak next to keep this forum discussion on topic?"""

    debug("Analyzing conversation context...", "COORDINATOR")

    # Call LLM
    try:
        llm = ChatOpenAI(model="gpt-5-nano", temperature=1)

        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])

        # Extract speaker from response
        if isinstance(response.content, list):
            selected_speaker = " ".join(str(item) for item in response.content).strip().lower()
        else:
            selected_speaker = str(response.content).strip().lower()
        debug(f"LLM selected: {selected_speaker}", "COORDINATOR")

        # Validate speaker
        valid_speakers = ["student", "adult", "eldery"]
        if selected_speaker not in valid_speakers:
            # Fallback to round-robin if invalid
            import random
            selected_speaker = random.choice(valid_speakers)
            debug(f"Invalid speaker, fallback to: {selected_speaker}", "COORDINATOR")

    except Exception as e:
        # Fallback selection if LLM fails
        import random
        valid_speakers = ["student", "adult", "eldery"]
        selected_speaker = random.choice(valid_speakers)
        debug(f"LLM error, random selection: {selected_speaker}", "COORDINATOR")

    debug(f"Final selection: {selected_speaker} (volley {volley_left} -> {volley_left - 1})", "COORDINATOR")

    # Return only the updates (LangGraph will merge with existing state)
    return {
        "next_speaker": selected_speaker,
        "volley_msg_left": volley_left - 1
    }
