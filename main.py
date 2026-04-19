def fibonacci(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    limit = int(input("Fibonacci ketma-ketligi chegarasini kiriting: "))
    fib_sequence = fibonacci(limit)
    print("Fibonacci ketma-ketligi:", fib_sequence)

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.fib_sequence = [0, 1]

    def generate_fibonacci(self):
        while self.fib_sequence[-1] + self.fib_sequence[-2] <= self.limit:
            self.fib_sequence.append(self.fib_sequence[-1] + self.fib_sequence[-2])

    def get_fibonacci(self):
        return self.fib_sequence

def fibonacci_with_class(limit):
    fib = Fibonacci(limit)
    fib.generate_fibonacci()
    return fib.get_fibonacci()

def main_with_class():
    limit = int(input("Fibonacci ketma-ketligi chegarasini kiriting: "))
    fib_sequence = fibonacci_with_class(limit)
    print("Fibonacci ketma-ketligi:", fib_sequence)

def compare_fibonacci_functions():
    limit = int(input("Fibonacci ketma-ketligi chegarasini kiriting: "))
    fib_sequence_function = fibonacci(limit)
    fib_sequence_class = fibonacci_with_class(limit)
    print("Fibonacci ketma-ketligi (funksiya):", fib_sequence_function)
    print("Fibonacci ketma-ketligi (klass):", fib_sequence_class)

if __name__ == "__main__":
    while True:
        print("1. Fibonacci ketma-ketligi (funksiya)")
        print("2. Fibonacci ketma-ketligi (klass)")
        print("3. Fibonacci ketma-ketligi (funksiya va klass bilan solishtirish)")
        choice = input("Tanlang: ")
        if choice == "1":
            main()
        elif choice == "2":
            main_with_class()
        elif choice == "3":
            compare_fibonacci_functions()
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")