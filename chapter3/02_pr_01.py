name = input("Enter your name\n")
date = input("Enter your date\n")
# print("Good afternoon, " + name)

letter = '''\n\nDear <|NAME|>
You are selected!

Date: <|DATE|>
'''

letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)

print(letter)