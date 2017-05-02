#!/usr/bin/python3
# coding: utf-8
##################################################################
# str.replace(old, new[, max])
# old: to be replaced; new: replace old substring; max: only the first count occurrences are replaced.
str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))  # thwas was string example....wow!!! thwas was really string
print(str.replace("is", "was", 3)) # thwas was string example....wow!!! thwas is really string
