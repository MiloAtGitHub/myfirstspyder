
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
  #  print(keywords)
  #  for kw in keywords:
  #      print(kw, ":", keywords[kw])


kws = {'shopkeeper': "Michael Palin", 'client': "John Cleese", 'sketch': "Cheese Shop Sketch"}
kwstr = ''
for kw in kws:
    kwstr += kw + "=" + kws[kw] + ','

print(kwstr)
# print(kw)
#cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", kw)
