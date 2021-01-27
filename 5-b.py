s = input()
s1 = s.replace('h','H')
if s[0] == 'h':
    s[0] = 'H'
if s[-1] == 'H':
    s[-1] = 'h'
print(s1)
