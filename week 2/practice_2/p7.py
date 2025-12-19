text = '''Given a line. Convert it by replacing with asterisks all the letters "n" that occur among the first n/2 characters. Here n is the length of the string.'''

new_text = text[:(len(text)//2)]

print(new_text)