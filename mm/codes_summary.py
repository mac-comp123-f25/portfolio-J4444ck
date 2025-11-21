# Chapter 7 – Selection (if / Boolean logic)

def grade_letter(score):
    """Return letter grade based on numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Chapter 7 examples:")
print(grade_letter(85))   # B
print(grade_letter(59))   # F
print()


# Chapter 8 – More About Iteration (loops)

def collatz_length(n):
    """Return how many steps it takes to reach 1 in the 3n+1 sequence."""
    steps = 0
    while n != 1:
        if n % 2 == 0:      # even
            n = n // 2
        else:               # odd
            n = 3 * n + 1
        steps += 1
    return steps

print("Chapter 8 examples:")
print(collatz_length(6))  # 8
print()


# Chapter 9 – Strings (text)

def remove_vowels(text):
    """Return a copy of text with all vowels removed."""
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

print("Chapter 9 examples:")
print(remove_vowels("Hello World"))  # Hll Wrld
print()


# Chapter 10 – Lists (collections of items)

def squares_min_max(n):
    """Return (min_square, max_square) for squares of 0..n-1."""
    squares = [k * k for k in range(n)]
    return (min(squares), max(squares))

print("Chapter 10 examples:")
lo, hi = squares_min_max(5)
print(lo, hi)  # 0 16
print()


# Chapter 11 – Files (reading and writing data)

def sum_file(filename):
    """Read a file of one number per line and return the total."""
    total = 0.0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:                # skip empty lines
                total += float(line)
    return total

print("Chapter 11 examples:")
# Uncomment the following line and ensure "numbers.txt" exists:
# print(sum_file("numbers.txt"))
print("(Chapter 11 example: sum_file('numbers.txt'))")
print()


# Chapter 12 – Dictionaries (key–value lookups)

def word_counts(text):
    """Return a dictionary mapping each word to its count."""
    counts = {}
    for word in text.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts

print("Chapter 12 examples:")
print(word_counts("hi hi HI there"))  # {'hi': 3, 'there': 1}
print()


# Chapter 17 – Classes and Objects: Basics

class Point:
    """Point in 2D space with simple movement and distance methods."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

print("Chapter 17 examples:")
p = Point(3, 4)
print(p)                         # (3, 4)
print(p.distance_from_origin())  # 5.0
p.move(1, -2)
print(p)                         # (4, 2)
print()


# Chapter 18 – Classes and Objects: Deeper (Fractions)

from math import gcd

class Fraction:
    """Fraction with automatic reduction and addition support."""
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.num}/{self.den}"

print("Chapter 18 examples:")
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)  # 5/6
print()


# Chapter 20 – Unit Testing (automatic code checking)

def square(n):
    """Return n squared."""
    return n * n

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-3) == 9

print("Chapter 20 examples:")
test_square()  # if the program finishes normally, the tests passed
print("All tests in test_square passed.")
