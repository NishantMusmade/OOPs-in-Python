#self parameter
#self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class
print('\nImplementation using self word')
class person:
    name = 'Nishant'
    job = 'Python Developer'

    def info(self):
        print(f'Hi, I am {self.name} working as a {self.job}')
    
a = person()

print('Name of the person: ',a.name)
print('Job of a person: ',a.job)

a.info()


# It is not mandatory to use word self as a reference to the object, we can use other words also

print('\nImplementation using a word other than self')
class person:
    name = 'Nishant'
    job = 'Python Developer'

    def info(someone):
        print(f'Hi, I am {someone.name} working as a {someone.job}')
    
a = person()

print('Name of the person: ',a.name)
print('Job of a person: ',a.job)

a.info()