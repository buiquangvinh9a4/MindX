class Employee:
    name = 'default'
    position = 'default'
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def say_hi(self):
        print(f'Hi, my name is {self.name}')
    
    def tell_position(self):
       print(f'I am a {self.position}')
    

e1 = Employee('Vinh', 'Software Engineer')
e1.say_hi()
e1.tell_position()
    
