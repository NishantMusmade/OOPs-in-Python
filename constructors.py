# contructors are used to initialize(Assign values) the data members of the class when an object is created.
# there is no need to call constructores explicitly, it is automatially called when the object is created
# __init__() method is called the constructor

# 3 types of constructor
# 1. Default constructor: It does not take any argument, it is also called zero-argument constructor
# 2. Parmaterized constructor: Tt takes argument to initialize an object when it is created 
# 3. Copy contructor: This constructor initialize an object using another object of the same class

# 1. Default constructor implementation
class person:
    def __init__(self):
        print('This is the constructor body')

print('Implementation of Default constructor: ')
print('Here we are creating object, so constructor will get called automatically')
person_1 = person()

print('-------------------------------------------------------------------------------------------------------------------------')

# 2. Paramterized constructor implementation
class person_info:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'The person name is {self.name} and his age is {self.age}')

print('\nImplementation of Parametrized constructor: ')
person_2 = person_info('Nishant', '22')
person_2.info()


print('-------------------------------------------------------------------------------------------------------------------------')

#3. Copy constructor
# Two types: 1. Shallow copy constructor: It copies references to the existing object, means changes in copied object relfect changes in original object
#            2. Deep copy constructor: It copies elements of the existing object, means changes in copied object do not affect changes in original object

# Shallow copy constructor implementation
import copy
class person_marks:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def marks_info(self):
        print(f'Marks of {self.name}:',self.marks )

    def shallow_copy(self):
        return copy.copy(self)
    
    def deep_copy(self):
        return copy.deepcopy(self)
    

print('\nImplementation of Shallow copy constructor: ')
original_object = person_marks('Nishant',[67,78,89])
# copying the references to the object, i.e., Shallow copy constructor
copy_object = original_object.shallow_copy()

print('\nOriginal object: ',original_object.marks)
print('Copied object: ',copy_object.marks)

copy_object.marks.append(90)

print('\nAfter modifying copied object with Shallow copy constructor-- changes will alod be reflected in the original object')
print('Original object: ',original_object.marks)
print('Copied object: ',copy_object.marks)


print('\nImplementation of Deep copy constructor: ')
original_object = person_marks('Nishant',[67,78,89])
#copying elements of the objects, i.e., Deep copy Constructor
copy_object = original_object.deep_copy()

print('\nOriginal object: ',original_object.marks)
print('Copied object: ',copy_object.marks)

copy_object.marks.append(90)

print('\nAfter modifying copied object with Shallow copy constructor-- changes will not be reflected in the original object')
print('Original object: ',original_object.marks)
print('Copied object: ',copy_object.marks)





