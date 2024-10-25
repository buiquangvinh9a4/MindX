class DragonBall:
    name = "default"
    level = 1
    hair = "black"
    power = 0
    
    def __init__(self, name, level, hair, power):
        self.name = name
        self.level = level
        self.hair = hair
        self.power = power
    
    def level_up(self):
        self.level += 1
        self.hair = "yellow"
        self.power += 1000
    
    def show(self):
        print(f'Name: {self.name}')
        print(f'Level: {self.level}')
        print(f'Hair Color: {self.hair}')
        print(f'Power: {self.power}')
        print('---------------------')
        
def main():
    Goku = DragonBall("Goku", 1, "black", 1000)
    print('Before level up!')
    Goku.show()
    
    print('After level up!')
    Goku.level_up()
    Goku.show()
    
    print('After level up 2!')
    Goku.level_up()
    Goku.show()
    
    people = list()
    for i in range(3):
        name = input('Enter name: ')
        level = int(input('Enter level: '))
        hair = input('Enter hair color: ')
        power = int(input('Enter power: '))
        person = DragonBall(name, level, hair, power)
        people.append(person)
        print('----------------------------')
    
    for person in people:
        person.show()
    
    
if __name__ == '__main__':
    main()
    