class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is ", name, "and i am ", age, ". My tracks are ", tracks, "and i scored .", score)
    def speak (self):
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name = input("Enter your name: ")
Bob.change_age = int(input("Enter your age: "))
Bob.add_track = input("Enter your tracks: ")
Bob.get_score = float(input("Enter your score: "))

print(Bob.get_score)