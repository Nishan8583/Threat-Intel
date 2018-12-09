#!/usr/bin/python

def get_key(text):
	'''Pass the string and get the key'''
	file = open("config.txt")
	for i in file.readlines():
		if text in i:
			key = i.split(":")[1].split("\n")[0]
			return key
