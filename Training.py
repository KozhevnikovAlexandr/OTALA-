def training(timed_automata, data, convergence_number=1000):
    current_state = timed_automata.create_new_state(data[0])
    state_exist = False
    n_conv = 0
    state_count = 1
    transition_count = 0
    observation_count = 0
    time_was_changed = False
    time = 0

    for new_observation in data:
        observation_count += 1
        for state in timed_automata.states:
            if new_observation == state:
                state_exist = True
                transition = timed_automata.find_transition(current_state, state)
                if transition:
                    time_was_changed = timed_automata.adapt_timing_information(transition, time)
                else:
                    timed_automata.create_new_transition(current_state, time, state)
                current_state = state
        if not state_exist:
            s_new = timed_automata.create_new_state(new_observation)
            timed_automata.create_new_transition(current_state, time, s_new)
            current_state = s_new
        state_exist = False
        if n_conv > convergence_number:
            break
        if transition_count == len(timed_automata.transitions) and state_count == len(
                timed_automata.states) and not time_was_changed:
            n_conv += 1
        else:
            n_conv = 0
        time_was_changed = False
        state_count = len(timed_automata.states)
        transition_count = len(timed_automata.transitions)
    return timed_automata
