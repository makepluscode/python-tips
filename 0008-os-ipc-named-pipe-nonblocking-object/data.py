from struct import * 

data = pack('<BH', \
    0x1,  #SOF \
    0xffff
)

print(data)
