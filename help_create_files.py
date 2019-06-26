import os
from PIL import Image

w = r'/home/matheus/Downloads/by_write/hsf_0/f0000_14/jj'
a = os.listdir(r'/home/matheus/Downloads/by_write/hsf_0/f0000_14/jj')
a.sort()
textList = ["We", "the", "People", "of", "the", "United", "States", "in", "order", "to form", "a more", "perfect", "Union", "establish", "Justice", "insure", "domestic"]
# textList = list(text)
#print(a)

for x in range(len(a)):
    print(x)
    b = a[x]
    c = b[:-3]
    arq = open(w+"//"+c+"gt.txt", "w+")
    arq2 = arq.write("%s\n" % (textList[x]))
    im = Image.open(w+"/"+b)
    im.save(w+"//"+c+"tif")
    print("%s\n" % (textList[x]))
