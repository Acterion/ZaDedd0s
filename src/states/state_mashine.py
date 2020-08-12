class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.is_running = False

    def exec(self):
        self.is_running = True
        while self.current_state:
            self.current_state.run()
            self.current_state = self.current_state.next()
