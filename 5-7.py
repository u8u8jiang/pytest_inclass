s = "In the hole in the ground there lived a hobbit"

s = input()
print(s[:s.find('h')] + s[s.rfind('h')+1:])