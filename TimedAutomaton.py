from Transition import *

class TimedAutomaton:
    transitions = []
    states = []
    current_state = []

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def create_new_state(self, state):
        self.states.append(state)
        return self.states[-1]

    def create_new_transition(self, source, time, destination):
        self.transitions.append(Transition(source, time, destination))

    def find_transition(self, start, end):
        for i in self.transitions:
            if i.source == start and end == i.destination:
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
