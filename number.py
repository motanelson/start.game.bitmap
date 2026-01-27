import struct
print( "\033c\033[40;37m\n ? ")
a="my.dat"
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
f1=open(a,"wb")
for c in b:
    f1.write(struct.pack("i",c))
f1.close()
