import random
from TimedAutomaton import TimedAutomaton
from test_data import Test_data
from Transition import Transition

ta = TimedAutomaton([1, 2, 3, 4, 5])
data = [Test_data([random.randrange(1, 6) for i in range(5)],
                  [random.randrange(0, 2) for j in range(5)], random.randrange(1, 11))
        for x in range(1000)]
currentState = data[0].configuration
stateExist = False

for new_observation in data:
    for state in ta.states:
        if new_observation.configuration == state:
            stateExist = True
            transition = ta.find_transition(currentState, new_observation.configuration)
            if transition:
                'a.adapt_timing_information(transition, i.time)'
            else:
                ta.create_new_transition(currentState, new_observation.event, state)
        currentState = state
    if not stateExist:
        s_new = ta.create_new_state(new_observation.configuration)
        ta.create_new_transition(currentState, new_observation.event, s_new)
        currentState = s_new
    'if ta.learningConverged():'
print(len(ta.states))
print(len(ta.transitions))