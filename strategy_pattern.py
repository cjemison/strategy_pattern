#!/usr/bin/env python

__author__ = 'Cornelius Jemison'
__version__ = 0.1

import abc


class CantFlyException(Exception):
    pass


class FlyBehavior(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def fly(self):
        """This is the fly method"""


class QuackBehavior(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def quack(self):
        """This is the fly method"""


class FlyNoWay(FlyBehavior):

    def __init__(self):
        FlyBehavior.__init__(self)

    def fly(self):
        raise CantFlyException("""I can't fly.""")


class Fly(FlyBehavior):

    def __init__(self):
        FlyBehavior.__init__(self)

    def fly(self):
        return 'I can fly!'


class Squeak(QuackBehavior):

    def __init__(self):
        QuackBehavior.__init__(self)

    def quack(self):
        return 'I can squeak.'


class Quack(QuackBehavior):

    def __init__(self):
        QuackBehavior.__init__(self)

    def quack(self):
        return 'I can quack.'


class Duck(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    @property
    def fly_behavior(self):
        return self._fly_behavior.fly()

    @fly_behavior.setter
    def fly_behavior(self, fb):
        if fb:
            self._fly_behavior = fb

    @property
    def quack_behavior(self):
        return self._quack_behavior.quack()

    @quack_behavior.setter
    def quack_behavior(self, qb):
        if qb:
            self._quack_behavior = qb

    @abc.abstractmethod
    def display(self):
        """This is suppose to display what kind of duck this is."""


class Mallard(Duck):

    def __init__(self):
        Duck.__init__(self)
        self.fly_behavior = Fly()
        self.quack_behavior = Squeak()

    def display(self):
        return 'I am a mallard duck.'


def main():
    m = Mallard()
    print m.display()
    print m.fly_behavior
#    m.fly_behavior = FlyNoWay()
#    print m.fly_behavior

if __name__ == '__main__':
    main()




