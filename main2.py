from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
        def move(self):
            print("Human walks on two legs.")
class Dog(Animal):
    def move(self):
        print("Dog runs on four legs.")
choice = input("Enter an animal (human/dog): ").lower()
if choice == "human":
    a = Human()
    a.move()
elif choice == "dog":
    a = Dog()
    a.move()
else:
    print("Unknown animal.")