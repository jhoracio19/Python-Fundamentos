
letters = ['a', 'b', 'o', 'c', 'z', 'h','d', 'e']
print(letters)

# sort() (ordena una lista)
letters.sort()

# sorted() 
# new_letters = sorted(letters)
# print(new_letters)

# new_letters = letters[:] # List Slicing
new_letters = letters.copy()
new_letters.sort()

# reverse()
letters.reverse()

print(letters)