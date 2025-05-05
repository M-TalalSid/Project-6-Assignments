class MathUtils:
    @staticmethod                  # Static method jo do numbers ka sum return karta hai
    def add(a, b):
        return a + b               # a aur b ko jorr kar result return karega

# Static method ko class ke Instance ke baghair direct call karein gaye
result = MathUtils.add(5, 7)
print(f"Sum: {result}")            # Result print karega