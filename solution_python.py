class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0
        self.events = []
        self.undo_events = []

    def add(self, num: int):
        self.events.append(num)
        self.value += num

    def subtract(self, num: int):
        self.events.append(-num)
        self.value -= num

    def undo(self):
        if len(self.events) == 0:
            return
        last_event = self.events.pop()
        self.value -= last_event
        self.undo_events.append(last_event)

    def redo(self):
        if len(self.undo_events) == 0:
            return
        redo_event = self.undo_events.pop()
        self.value += redo_event

    def bulk_undo(self, steps: int):
        for i in range(steps):
            if len(self.events) > 0:
                self.undo()
            else:
                break

    def bulk_redo(self, steps: int):
        for i in range(steps):
            if len(self.undo_events) > 0:
                self.redo()
            else:
                break;