# import logging
DEBUG=True

class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        if DEBUG :
            print(type(self).__name__+".notify()")
        for obs in self.observers:
            obs.update(self)           # call Observer.update(self,subject) method
    def attach(self, obs):
        if DEBUG :
            print(type(self).__name__+".attach()")
            name=obs.get_name()
            print(type(obs).__name__+".get_name() : ", name)
        if not callable(getattr(obs,"update")) :
            raise ValueError("Observer must have  an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if DEBUG :
            print(type(self).__name__+".detach()")
            print(type(obs).__name__+".getname() : ", obs.get_name())
        if obs in self.observers :
            self.observers.remove(obs)

class Observer:
    def __init__(self):
        pass
    def update(self,subject):
        raise NotImplementedError

class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.__data=0
    def get_data(self):
        if DEBUG :
            print(type(subject).__name__+".get_data()")
        return self.__data
    def set_data(self,data):
        if DEBUG :
            print(type(subject).__name__+".set_data()")
        self.__data=data

    def increase(self):
        if DEBUG :
            print(type(self).__name__+".increase()")
        self.__data+=1
        self.notify()       # call observers update() method
    def decrease(self):
        if DEBUG :
            print(type(self).__name__+".decrease()")
        self.__data-=1
        self.notify()       # call observers update() method

class ConcreteObserver(Observer):
    def __init__(self,name):
        self.name=name
    def get_name(self) :
        if DEBUG :
            print(type(self).__name__+".get_name()")
        return self.name
    def set_name(self,name) :
        if DEBUG :
            print(type(self).__name__+".set_name()")
        self.name=name

    def update(self,subject):
        if DEBUG :
            print(type(self).__name__+".update()")
        data=subject.get_data()
        print(self.name, "has updated data : ",data)

if __name__ == "__main__":
    subject=ConcreteSubject()
    name="Observer1"
    obs=ConcreteObserver(name)
    name=obs.get_name()
    print("attach : ",name)
    subject.attach(obs)
    print("before increase : ",subject.get_data())
    subject.increase()

    name="Observer2"
    obs=ConcreteObserver(name)
    name=obs.get_name()
    print("attach : ",name)
    subject.attach(obs)
    print("before increase : ",subject.get_data())
    subject.increase()
 
    print("detach : ", name)
    subject.detach(obs)
    print("before decrease : ",subject.get_data())
    subject.decrease()