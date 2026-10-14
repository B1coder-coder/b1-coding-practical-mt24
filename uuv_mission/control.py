class PDController:
    def __init__(self):
        self.KP = 0.15
        self.KD = 0.6
        self.prev_error = 0

    def control(self, reference, observation):
        error = reference - observation
        u = self.KP * error + self.KD * (error - self.prev_error)
        self.prev_error = error
        return u

    def reset(self):
        self.prev_error = 0