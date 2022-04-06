# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
show=fh.read()
show=show.rstrip()
print(show.upper())
