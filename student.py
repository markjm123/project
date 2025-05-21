class Student:
    def __init__(self, name, subject_count):
        self.name = name
        self.total_subjects = subject_count
        self.scores = [0.0] * subject_count
        self.average_score = 0.0

    def record_score(self, index, score):
        """Store the score at the given subject index."""
        if 0 <= index < self.total_subjects:
            self.scores[index] = float(score)

    def compute_average(self):
        """Calculate the average of all scores."""
        if self.total_subjects > 0:
            self.average_score = sum(self.scores) / self.total_subjects
