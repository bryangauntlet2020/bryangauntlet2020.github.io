import sys
string = sys.argv[1]
print("[", end='')
for x in range(len(string)):
  print(ord(string[x]), end='')
  if(x < len(string) - 1):
    print(", ", end='')
print("]")