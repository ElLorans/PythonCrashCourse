# The robot has an amazing text synthesizer only that you find it really boring. How to make it
# funnier? After a lot of time spent thinking about solutions such as making him speak in reverse
# order you decide to make it funnier using the La-La-Land logic. In order to make it possible
# you have to write a function called py_py_python that takes a string containing only letters [AZa-z],
# the four symbols that are common in every day sentences [.,’?] and spaces, and outputs
# the string in the style of La La Land.

# Example:
# py_py_python('Land')
# Should output:
# 'La La Land'
# To be more specific, take the letters up to, and including, the first vowel group, and returns it
# twice adding a space each time, then returns the whole string. Note that y is a vowel in this
# challenge. Punctuation and capitalization should be kept.
# You may assume that all strings contain at least one vowel, and that all strings start with a
# letter.

def py_py_python():