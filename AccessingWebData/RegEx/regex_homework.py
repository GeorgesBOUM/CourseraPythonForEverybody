import re

total = 0
with open('actual_data.txt', 'r') as actual_file:
    for line in actual_file:
        total += sum(list(map(int, re.findall('[0-9]+', line))))
print(total)