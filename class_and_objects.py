class person:
    name = 'Nishant'
    job = 'Python Developer'

    def info(self):
        print(f'Hi, I am {self.name} working as a {self.job}')
    
a = person()

print('Name of the person: ',a.name)
print('Job of a person: ',a.job)

a.info()

b = person()
b.name = 'Deven'
b.job = 'ML ENgineer'

print('\nName of the person: ',b.name)
print('Job of a person: ',b.job)

b.info()