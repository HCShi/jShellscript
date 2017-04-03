#!/usr/bin/python3
# coding: utf-8
str = input('Your Name:')
print(str)

import getpass
user = getpass.getuser()  # no argument, auto get you system username
print(user)  # coder352
passwd = getpass.getpass('Your Password:')
print(passwd)
