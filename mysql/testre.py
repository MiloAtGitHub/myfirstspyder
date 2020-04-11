import re
line = "I have been told that cats are smarter than dogs a lot."
matchobj = re.search(r"are (.*?) (.*)", line, re.M | re.I)
if matchobj:
    print("matchobj.group(): ", matchobj.group())
    print("matchobj.group(1): ", matchobj.group(1))
    print("matchobj.group(2): ", matchobj.group(2))
else:
    print("no match.")
