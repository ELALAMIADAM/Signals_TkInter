class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not callable(getattr(obs,"update")) :
            raise ValueError("Observer must have  an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if obs in self.observers :
            self.observers.remove(obs)

class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.__data=0
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data=data
    def increase(self):
        self.__data+=1
        self.notify()
    def decrease(self):
        self.__data-=1
        self.notify()

class Observer:
    def __init__(self):
        pass
    def update(self,subject):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def __init__(self,name):
        self.name=name
    def update(self,subject):
        print("ConcreteObserver : ",self.name)
        print("update : ",subject.get_data())

if __name__ == "__main__":
    subject=ConcreteSubject()
    print("One observer")
    obs=ConcreteObserver("Observer 1")
    subject.attach(obs)
    subject.increase()
    subject.decrease()
    subject.increase()
    # print("two observers")
    # obs=ConcreteObserver("Observer 2")
    # subject.attach(obs)
    # subject.increase()
    # subject.detach(obs)
    # subject.decrease()

