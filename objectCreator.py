#!/usr/bin/python3
# creates a class file with given instance variables, a constructor, and getters and setters

from StringToken import stringToken
import sys

def createClass(name, variables, outFile): # pass variables in a list
	outputFile = open(outFile, "w")

	fileText = "class " + name + ":\n\tdef __init__(self, "
	# function declaration
	for i in range(0, len(variables) - 1):
		fileText += variables[i] + ", "
	fileText += variables[len(variables) - 1] + "):\n"
	# lines of the function
	for i in range(0, len(variables)):
		fileText += "\t\tself." + variables[i] + " = " + variables[i] + "\n"
	fileText += "\n"
	# make getters
	for i in range(0, len(variables)):
		fileText += "\tdef get_" + variables[i] + "(self):\n\t\treturn self." + variables[i] + "\n\n"
	# make setters
	for i in range(0, len(variables)):
		fileText += "\tdef set_" + variables[i] + "(self, new_" + variables[i] + "):\n\t\tself." + variables[i] + " = new_" + variables[i] + "\n\n"

	outputFile.write(fileText)
	outputFile.close()

inFile = open(sys.argv[1], "r") # expect infile to be formatted in this way: 1st line is filename, 2nd line is classname, and rest of lines are variables
fileText = stringToken(inFile.read(), "\n")
inFile.close()

createClass(fileText[1], fileText[2:], fileText[0])
