charset = ["0","1","2","3","4","5","6","7","8","9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'F', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'f', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','#','$']

class BaseNumber:
    def __init__(self, value, base):
        self.dec=0
        self.val = value
        self.base = base

        if(base != 10):
            for i in range(len(value)):
                val = charset.index(value[i])
                self.dec += val * base ** (len(value) - i -1)
        else:
            self.dec = int(value)
    
    def to_base(self, new_base):
        ret = ""
        value = self.dec
        while value!=0: 
            ret += charset[value%new_base]
            value //= new_base

        return BaseNumber(ret[::-1], new_base)

def input_loop():
    vals = []

    base = int(input())
    dec_val = input()

    while(True):
        vals.append(BaseNumber(dec_val, 10).to_base(base).val)

        base = int(input())
        if not (base >= 2 and base <= 16): break
        dec_val = input()
    
    return vals

def main():
    inp = input_loop()

    for v in inp:
        print(v)

main()
    	