"""2 byte
3 bit - counter
3 bit - type indicator
nibble  - metadata
6 bit - data

101 - text
011 - command
110 - image

###/0 11/00 ##/00 0000 - I'm going to send
###/0 11/00 ##/00 0001 - Please send
###/0 11/00 ##/00 0010 - Sending
###/0 11/01 ##/** **** - ***** is back ground infrared (01##) is background inidicator

### 011/0 0##/0 0011 - end message

data - 6 bit
0# #### - lower
1# #### - upper
0 0000<= # #### <= 11010 for letters
01 1011 -> .
01 1110 -> ?
01 1111 -> ,
11 1011 -> ;
11 1110 -> -
11 1111 -> '

###/1 01/01 ##/** **** - letters
###/1 01/10 ##/** **** - number
###/1 01/11 ##/** **** - punctuation

in the txt file # means either 0 or 1
    * means wait untill this is recieved
"""
global count
count = 0
def count_out(num,len_): #returns the count for the packet with the correct length (2 count variables so made general)
    a = str(bin(num)[2:])
    for i in range(0,len_-len(a)):
        a = "0"+a
    return a;

def add_text(text_parts,file): #text parts are the sections that aren't # in the general map (see above)
    for i in range(0,3):
        temp = count_out(count,3)+text_parts[0]+count_out(i,2)+text_parts[1]+"\n"
        file.write(temp)
        count_add()

def count_add(): #keeps a count (mod 8) of the number of total packets sent so far
    global count
    count += 1
    count %= 8

def file_setup():
    file = open("packet_list.txt","w")
    file.write("")
    file.close()
    file = open("packet_list.txt","a")
    return file;
file=file_setup()
add_text(["01100","000000"],file)
temp = "*###01100##000001\n"
file.write(temp)
add_text(["01100","000010"],file)
file.close()
