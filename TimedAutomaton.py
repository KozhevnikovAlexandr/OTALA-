from Transition import *

class TimedAutomaton:
    transitions = []
    states = []
    current_state = []

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def create_new_state(self, state):
        self.states.append(state)
        if len(self.current_state) == 0:
            self.current_state = self.states[-1]
        return self.states[-1]

    def create_new_transition(self, source, time, destination):
        self.transitions.append(Transition(source, time, destination))

    def find_transition(self, start, end):
        for i in self.transitions:
            if i.source == start and end == i.destination:
                return i
        return False

    def find_nearest_transition(self, input):
        for i in self.transitions:
            if i.source == self.current_state and i.destination[0] == input:
                return i
        return False

    def find_transition_with_given_time(self, start, end, time):
        for i in self.transitions:
            if i.source == start and i.destination == end and time == i.time:
                return i
        return False

    def make_transition(self, start, end):
        for i in self.transitions:
            if i.source == start and end == i.destination:
                return i.destination
        return False

    def adapt_timing_information(self, transition, time):
        if time < transition.time:
            transition.time = time
            return True
        return False

    def get_result(self, input):
        a = self.find_nearest_transition(input)
        self.current_state = a.destination
        return self.current_state[1]