#!/usr/bin/env python

import plistlib

class TracedCall:
	def __init__(self, clazz, method, args, returnValue):
		self.clazz = clazz
		self.method = method
		self.args = plistlib.readPlistFromString(args.encode('utf-8'))
		self.return_value = plistlib.readPlistFromString(returnValue.encode('utf-8'))

	def __str__(self):
		return "%s:%s\n\tArguments:%s\n\tReturning:%s" % (self.clazz, self.method, self.args, self.return_value)