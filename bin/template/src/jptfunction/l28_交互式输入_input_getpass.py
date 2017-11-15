#!/usr/bin/python3
# coding: utf-8
##################################################################
## input(): python 中已经将 raw_input 换为 input()
str = input('Your Name:')
print(str)
##################################################################
## getpass
import getpass
user = getpass.getuser()  # no argument, auto get you system username
print(user)  # coder352
passwd = getpass.getpass('Your Password:')
print(passwd)
