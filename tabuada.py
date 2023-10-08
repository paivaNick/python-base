#!/usr/bin/env python3


__version__ = "0.1"
__author__ = "nick"
print("\N{party popper} tabuada")

for i in range(1,11):
    template = "{:-^12}".format(str(i))
    print(f"{str(i)}".center(12,"-"))
    #print(template)
    for j in range(1, 11):
        print("{:^12}".format(f"{i} x {j} = {i*j}"))
        j+=1
    print("#" * 14)
    i+=1
