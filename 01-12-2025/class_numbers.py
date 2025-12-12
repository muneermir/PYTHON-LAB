class Numbers:
    def __init__(self, lst):
        self.lst = lst

    def largest(self):
        if not self.lst:
            return None
        max_val = self.lst[0]
        for x in self.lst[1:]:
            if x > max_val:
                max_val = x
        return max_val

nums = Numbers([10, 55, 3, 88])
print("Largest:", nums.largest())
