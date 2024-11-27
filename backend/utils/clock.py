class Clock:
    def __init__(self, a_closure_for_current_time, a_closure_for_limit):
        self.current_time_generator = a_closure_for_current_time
        self.limit_generator = a_closure_for_limit
        self.creation_date = self.current_time_generator()

    def current(self):
        return self.current_time_generator()

    def limit_date(self):
        return self.creation_date + self.limit_generator()
