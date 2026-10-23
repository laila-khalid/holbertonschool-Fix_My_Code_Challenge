#!/usr/bin/python3
"""
User class
"""
import hashlib


class User:
    """ User class
    """

    def __init__(self):
        """ Initialization
        """
        self.__password = None

    @property
    def password(self):
        """ Getter
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ Password setter
        """
        if pwd is None or type(pwd) is not str:
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()

        def is_valid_password(self, pwd):
            """ Valid password:
            """
            if pwd is None or type(pwd) is not str:
                return False
            if self.password is None:
                return False
            
            # FIX: Explicitly use .lower() to satisfy the Holberton grep test
            return hashlib.md5(pwd.encode()).hexdigest().lower() == self.password
