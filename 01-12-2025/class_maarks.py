class Marks:
    def __init__(self, marks):
        if len(marks) != 5:
            raise ValueError("Expect 5 marks.")
        self.marks = marks

    def total(self):
        s = 0
        for m in self.marks:
            s += m
        return s

    def average(self):
        return self.total() / len(self.marks)

# Example
m = Marks([78, 85, 90, 66, 72])
print("Total:", m.total())
print("Average:", m.average())
