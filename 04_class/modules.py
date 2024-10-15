class Person:
    national = 'korea'
    def greeting(self):
        return 'hello. this is python'

class Learner:
    def greeting(self):
        return 'hello. i am learner'
    
    def learn(self):
        return 'i am learning python'
    
class Student(Person, Learner):
    pass