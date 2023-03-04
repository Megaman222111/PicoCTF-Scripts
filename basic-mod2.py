nums = "104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370 ".split()

for x in nums:
    x = int(x)
    y = pow(x, -1, 41)
    y = y-1
    
    if(y<=25):
        if(y==0):
            print("a", end="")
        if(y==1):
            print("b", end="")
        if(y==2):
            print("c", end="")
        if(y==3):
            print("d", end="")
        if(y==4):
            print("e", end="")
        if(y==5):
            print("f", end="")
        if(y==6):
            print("g", end="")
        if(y==7):
            print("h", end="")
        if(y==8):
            print("i", end="")
        if(y==9):
            print("j", end="")
        if(y==10):
            print("k", end="")
        if(y==11):
            print("l", end="")
        if(y==12):
            print("m", end="")
        if(y==13):
            print("n", end="")
        if(y==14):
            print("o", end="")
        if(y==15):
            print("p", end="")
        if(y==16):
            print("q", end="")
        if(y==17):
            print("r", end="")
        if(y==18):
            print("s", end="")
        if(y==19):
            print("t", end="")
        if(y==20):
            print("u", end="")
        if(y==21):
            print("v", end="")
        if(y==22):
            print("w", end="")
        if(y==23):
            print("x", end="")
        if(y==24):
            print("y", end="")
        if(y==25):
            print("z", end="")
    if(y<=35 and y>=26):
        if(y==26):
            print(0, end="")
        if(y==27):
            print(1, end="")
        if(y==28):
            print(2, end="")
        if(y==29):
            print(3, end="")
        if(y==30):
            print(4, end="")
        if(y==31):
            print(5, end="")
        if(y==32):
            print(6, end="")
        if(y==33):
            print(7, end="")
        if(y==34):
            print(8, end="")
        if(y==35):
            print(9, end="")
    if(y==36):
        print('_', end="")
