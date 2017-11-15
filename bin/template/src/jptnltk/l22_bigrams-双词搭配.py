#!/usr/bin/python3
# coding: utf-8
from nltk import bigrams
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))  # [('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]
