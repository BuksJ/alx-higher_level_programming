#!/usr/bin/python3


class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("Attribute can only be set for 'first_name'")
        self.__dict__[name] = value


