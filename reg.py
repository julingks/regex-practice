import re
pattern = r"(\w+) (\w+)"
string = "Isaac Newton, physicist"
m = re.match(pattern, string)
print(m.group(0))
