from morse import morse, reverse_morse
import re

ans = input("Enter a message: ").lower()
ans = re.sub(r"[^a-z0-9 ]", "", ans)
output = []
output_reverse = []

output = [morse.get(x, " ") for x in ans]
output_reverse = [reverse_morse.get(x, " ") for x in output]

''' Otherway
for letter in ans:
    output.append(morse.get(letter, " "))
output = [x.get(letter, " ") for x in morse]

for code in output:
    output_reverse.append(reverse_morse.get(code, " "))
'''

print("".join(output))
print(f"It means: {''.join(output_reverse)}")
