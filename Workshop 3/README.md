
# Assignment 3
## Set up
### Running the application
```sh
uv  sync
uv  run  python  main.py
```

### Dependencies
- OpenAI
<Add  libraries  that  are  required>

## Scenario
The multi-agents system aims to simulate

"***A forum-like discussion between members from different age groups regarding a phenomenon that is occurring in Singapore.***"

## Implementation

### 1. Agents

#### 1.1. Person
The agents are depicted as persons from 3 different age groups engaging in a forum-like discussion regarding a phenomenon that is happening in Singapore.
- Each actor will attempt to identify the cause(s) and provide solution(s) based on their life experience(s) and accessible current affairs.
- Each actor will also rebut / agree with the cause(s) / solution(s) shared by the other actors.

##### Student
The student is the youngest of the age groups.
<Add  some  description  with  relation  to  the  persona>

##### Working Adult
The working adult is the middle of the age groups.
<Add  some  description  with  relation  to  the  persona>

##### Retiree
The retiree is the oldest of the age groups.
<Add  some  description  with  relation  to  the  persona>

#### 1.2. Summarizer
Agent that will summarize the highlighted cause(s) for the phenomenon and the potential solution(s) from the discussion held by the person agents.
  
#### 1.3. Coordinator
Agent that will facilitate and coordinate the discussion held by the person agents.
- Each person agent will only speak when given the opportunity.
- Each person agent is given at least 1 opportunity to speak.

### 2. Tools


### 3. XXXX

ORIGINAL FROM README:
## Starter steps
1. Sketch Graph
1. Go through dependencies
1. Define State
1. Define Tools (time)
1. Define Agents
1. Define Nodes
1. Define Graph (main.py)
<IDK  what  this  is>