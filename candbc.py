import re
import cantools

# command: echo -e 'vcan0  214   [8]  80 4A 0F 00 00 00 00 00 ::' | python3 -m cantools decode motohawk.dbc

db = cantools.database.load_file('motohawk.dbc')

mystring = "  0.350730 2  214       Rx D 8  80  4A  0F  00  00  00  00  00"
mystring = re.sub(' +', ' ', mystring)
mylist = mystring.split(" ")
dataLenght = int(mylist[6], 10)
data = bytearray.fromhex(''.join(mylist[-dataLenght::1]))
print(mylist)
id = int(mylist[3], 16)

print(hex(id))
print(", ".join(hex(b) for b in data))

# id = hex(id)
# data = ", ".join(hex(b) for b in data)

# arbitration_id=0x214
# data=b'\x80\x4A\x0F\x00\x00\x00\x00\x00'
decoded_data = db.decode_message(id, data)
print(decoded_data)