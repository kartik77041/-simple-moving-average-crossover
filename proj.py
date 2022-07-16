import read
record = read.final
count = 1
sum = 0
sum2=0
s = {}
flag = 0
for i in record:
    sum = sum + i[3]
    if count>=50:
        a = sum/50
        if a>i[3] and flag==0:
            s[count]="Buy"
            M = i[3]
            flag = 1
        if a<i[3] and flag==1:
            s[count]="sell"
            m = i[3]
            flag = 0
            sum2=sum2+(M-m)
        sum = sum - record[count - 50][3]
    count +=1
print("The serial number and whether we should buy or sell is shown in dictionary below..\n")
print(s)
print("\n\nThe loss or profit by simple moving average crossover strategy on low prices of each day is ",sum2)

# for unit testing
def string_datetime():
    for i in record:
        return i[0]

def string_instrument():
    for i in record:
        return i[6]

def float_close():
    for i in record:
        return i[1]

def float_high():
    for i in record:
        return i[2]

def float_low():
    for i in record:
        return i[3]

def float_open():
    for i in record:
        return i[4]

def int_volume():
    for i in record:
        print(type(i[5]))
        return i[5]

