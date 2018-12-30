import datetime

class Round:
    def __init__(self, values, all_rounds):
        self.values = values
        self.round_number = values[0]
        self.target = values[1]
        self.flanker = values[2]
        self.correlation = values[3]
        self.show_time = datetime.datetime.strptime(values[4], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.first_click = values[5]
        self.first_answer = values[6]
        self.first_click_time = datetime.datetime.strptime(values[7], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.duration_until_click = (self.first_click_time-self.show_time).microseconds/1000.0
        if self.values[9] != 'undefined':
            self.first_click_duration = values[9]
        else:
            self.first_click_duration = None
        self.is_correct = (self.target == self.first_answer)

    def complete_click_duration(self,next_round):
        return
