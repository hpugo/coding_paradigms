def sort_and_flatten(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
        return sorted(arr)
    
result = sort_and_flatten([[1, 2], [10, 20], [15]])
print(result)

'''
How does this solution ensure data immutability?

    it is not altering the original array provided and it alters 'arr' we create, creating a different array. Therefore,
    our original data is unaltered

Is this solution a pure function? Why or why not?
    it is not a pure function because it initalizes the empty array 'arr' and iterates over the items in array. then it appends
    to the new 'arr' list

Is this solution a higher order function? Why or why not?
    No, the provided solution sort_and_flatten is not a higher-order function. A higher-order function is a function that
    either takes one or more functions as arguments or returns a function as its result.

Would it have been easier to solve this problem using a different programming style?
    Yes, it's possible that using a different programming style, such as functional programming, 
    might make the solution more concise and easier to understand. 

Why in particular is functional programming a helpful paradigm when solving this problem?
    Functional programming emphasizes expressing computations as the evaluation of functions. 

'''


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod:
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2
class SubulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def flame_jet(self, other):
        other.condition = "thrashed"

'''

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    These aspects of OOP help to organize code, promote reusability,
    and facilitate the modeling of real-world systems by capturing relationships and behaviors between different entities.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    I don't think it would've been easier because the pillars of OOP is to help better understand and write code having 
    encapsulation, inheritance, polymorphism, and abstraction. While not all pillars are being used, it makes writting and reading
    the code much easier.

How in particular did Object Oriented Programming assist in the solving of this problem?
    Object-Oriented Programming provided a structured and intuitive approach to modeling the problem domain, enabling us to 
    represent different types of podracer vehicles and their behaviors in a clear and concise manner.

'''