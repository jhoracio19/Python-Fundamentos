
total = 0
tax = 16

def change_global():
    global tax
    tax = 18
    return tax

print(change_global())
print(tax)