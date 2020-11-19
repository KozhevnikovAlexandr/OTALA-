from Transition import *

class TimedAutomaton():
    transitions = []
    states = []

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def create_new_state(self, state):
        self.states.append(state)
        return self.states[-1]

    def create_new_transition(self, source, trigger, destination):
        self.transitions.append(Transition(source, trigger, destination))

    def find_transition(self, start, end):
        for i in self.transitions:
            if i.source == start and i.destination == end:
                return i
        return False
