class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

def main():
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Alice")

    print(f"{student1.name} == {student2.name}: {student1 == student2}")
    print(f"{student1.name} == {student3.name}: {student1 == student3}")
    print(f"{student1.name} < {student2.name}: {student1 < student2}")
    print(f"{student2.name} < {student1.name}: {student2 < student1}")
    print(f"{student1.name} >= {student2.name}: {student1 >= student2}")
    print(f"{student2.name} >= {student1.name}: {student2 >= student1}")
    print(f"{student1.name} >= {student3.name}: {student1 >= student3}")

if __name__ == "__main__":
    main()