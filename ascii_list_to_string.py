import sys
import re
line = sys.argv[1]
x = re.findall('[0-9]+', line)
print(x)
for i in x:
  print(chr(int(i)), end="")
print()
