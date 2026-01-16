class Replayer:
    def __init__(self, trace):
        self.trace = trace
        self.index = 0

    def step_forward(self):
        if self.index < len(self.trace):
            event = self.trace[self.index]
            self.index += 1
            return event

    def step_backward(self):
        if self.index > 0:
            self.index -= 1
            return self.trace[self.index]
        
    def diff_locals(prev, curr):
        changes = {}
        all_keys = set(prev.keys()) | set(curr.keys())

        for k in all_keys:
            if prev.get(k) != curr.get(k):
                changes[k] = {
                    "before": prev.get(k),
                    "after": curr.get(k)
                }
        return changes

