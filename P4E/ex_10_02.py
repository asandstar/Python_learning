"""Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below."""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
hours = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    #print(time)
    h, m, s = time.split(':')
    h = int(h)
    H = '%02d' % h
    hours.append(H)
#print(hour)
hours.sort()
counts = dict()
for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1
#t = counts.items()

#print(t)
for h, count in counts.items():
    Hour = h
    c = count
    print(Hour, c)
