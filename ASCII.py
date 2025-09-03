"""ASCII, or American standard code for information Interchange, is a character encoding standard that
users numneric values to represent characters.Each ASCII character is assigned a unique 7-bit or 8-bit binary
numbers, allowing computers to exchange  information and display text in a consistent way. The ASCii values 
range from 0 to 127(for 8-bit ASCII), with each value corresponding to a specific character, such as letters,
digits, punctuation marks, and control characters."""

char = str(input("Enter the character:\n"))
print("The ASCII value of '" + char + "' is", ord(char))