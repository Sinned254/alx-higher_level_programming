#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == "first_name":
            # Allow setting the 'first_name' attribute
            self.__dict__[name] = value
        elif hasattr(self, "first_name"):
            # If 'first_name' attribute exists, raise an exception for new attributes
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        else:
            # If 'first_name' doesn't exist yet, create it
            self.__dict__[name] = value
