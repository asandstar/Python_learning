import re

sum = 0
name = 'regex_sum_1518455.txt'
handle = open(name)
for line in handle:
    line = line.rstrip()
    #print(line)
    num = re.findall('[0-9]+', line)
    num = list(map(int, num))
    for n in num:
        sum = n + sum
print(sum)
