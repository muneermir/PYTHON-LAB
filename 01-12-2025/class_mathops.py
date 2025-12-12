class MathOps:
    @staticmethod
    def factorial(n):
        if n <= 1: return 1
        return n * MathOps.factorial(n-1)

print(MathOps.factorial(6))  # 720
