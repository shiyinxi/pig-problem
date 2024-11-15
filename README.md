# pig-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

Create a function that takes a string consisting of one or more all-lowercase words separated by spaces. It should return a new string converted to "pig Latin," where each word has its first letter moved to the back and the letters "ay" are added to the end of the word. However, words starting with a vowel (a, e, i, o, or u) should not be altered.

## Examples:

pig_latin("something") # should return "omethingsay"

pig_latin("awesome") # should return "awesome" (words starting with a vowel should not be altered)

pig_latin("latin is a hard language") # should return "atinlay is a ardhay anguagelay"

pig_latin("y") # should return "yay"

pig_latin("e") # should return "e"