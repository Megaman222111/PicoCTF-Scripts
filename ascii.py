# A simple function to convert decimal to ascii. Usefull for RSA challenges.

def ascii(s):
    b = hex(s)[2:-1]
    return ''.join([chr(int(b[i:i+2], 16)) for i in range(0, len(b), 2)])

