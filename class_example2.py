class Dog ():
    color = ''
    size = ''
    legs = 4
    tail = True
    eyes = 2
    nose = True
    mouth = True

    def validation_tail(self,tail):
        if  tail == True:
            return 1
        return 0

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):
        return f'the dog is {self.color} color, him size {self.size} and he has {self.legs} legs, he has a {self.validation_tail(self.tail)} tail' 

""" if __name__ == "__main__":
    dog = Dog('black','large')
    print(dog) """


    
    
    

        
