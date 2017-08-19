#!/usr/bin/env python
#coding=utf-8
import sys

print sys.argv
print sys.argv[0]
print sys.argv[1]

print 'hello';print 'world'

if True:
    print "True"
else:
    print "False"
#this is a comment
'''
this is
a
multiline
comment
'''
"""
multiline
comment
"""
a = "hello"
b = "world"
c = a + \
    b
print c

print 'a',
print 'b'
