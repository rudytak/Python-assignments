import copy as copy

def constrain(val,_min,_max):
    return max(min(val,_max),_min)

class Sudoku:
    def __init__(self):
        self.block_dim = {
            0:3,
            1:3,
            "x":3,
            "y":3
        }
        self.blocks_dim = {
            0:3,
            1:3,
            "x":3,
            "y":3
        }

        self.blocks = self.createEmpty2DArray(self.blocks_dim[0], self.blocks_dim[0])
        self.fill2DArray(self.blocks, self.createEmpty2DArray())

        self.max_x = self.blocks_dim[0]*self.block_dim[0]
        self.max_y = self.blocks_dim[1]*self.block_dim[1]

    def fill2DArray(self, arr, value):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = (copy.deepcopy(value))

    def createEmpty2DArray(self, x=None, y=None):
        if(x==None):
            x=self.block_dim[0]
        if(y==None):
            y=self.block_dim[1]
        
        out = []
        for i in range(x):
            out.append([])
            for j in range(y):
                out[i].append(Tile(0, False))
        return out

    def checkBlockInputValidity(self, bs_x,bs_y, val):
        already_in_block = val in map(lambda x: x.value ,sum(self.blocks[bs_x][bs_y],[]))
        return not already_in_block

    def checkColumnAndRowValidity(self,x,y,val):
        arr = self.toSimple()
        already_in_col = val in arr[y]
        already_in_row = val in map(lambda b: b[x], arr)

        return not already_in_col and not already_in_row

    def input(self, x,y,val, makeConstant = False):
        x=constrain(x,0,self.max_x-1)
        y=constrain(y,0,self.max_y-1)
        val=constrain(val,1,self.block_dim[0] * self.block_dim[1])

        bs_x = x // self.block_dim[0]
        bs_y = y // self.block_dim[1]
        b_x = x % self.block_dim[0]
        b_y = y % self.block_dim[1]

        if(self.checkBlockInputValidity(bs_x,bs_y,val)):
            if(self.checkColumnAndRowValidity(bs_y*self.block_dim[1]+b_y, bs_x*self.block_dim[0]+b_x,val)):
                self.blocks[bs_x][bs_y][b_x][b_y].overwrite(val)
                self.blocks[bs_x][bs_y][b_x][b_y].constant = makeConstant
            else:
                print("YOU CANT PLACE THIS VALUE HERE, BECAUSE IT IS ALREADY IN THE ROW OR THE COLLUMN!")
        else:
            print("YOU CANT PLACE THIS VALUE IN THIS BLOCK!")

    def toSimple(self):
        arr = self.createEmpty2DArray(self.max_y,self.max_x)

        for bs_x, block_col in enumerate(self.blocks):
            for bs_y, block in enumerate(block_col):
                for b_x, col in enumerate(block):
                    for b_y, tile in enumerate(col):
                        arr[bs_y*self.block_dim[1]+b_y][bs_x*self.block_dim[0]+b_x] = tile.value
        return arr

    def print(self):
        arr = self.toSimple()

        for x,col in enumerate(arr):
            line=""
            if(x!=0 and x!=self.max_x-1 and not x%(self.block_dim[1])):
                line = "="*(4*self.max_x-1)
            print("\n "+line)

            for y, t in enumerate(col):
                sep = " "
                if(y!=0 and not y%(self.block_dim[0])):
                    sep = "|"

                print(sep+" "+str(t) + " ", end="")

    def loadStartData(self, data):
        for x, col in enumerate(data):
            for y, t in enumerate(col):
                if(t != 0 and t != None):
                    self.input(y,x,int(t), True)

class Tile:
    def __init__(self, value, constant = False):
        self.value = value
        self.constant = constant

    def overwrite(self, new):
        if(self.constant):
            print("YOU CANT OVERWRITE THIS VALUE!")
            return False
        else:
            self.value = new
            return True

def main():
    s = Sudoku()
    s.loadStartData([
        [4,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ])

    while True:
        s.print()
        print("")
        s.input(
            int(input("Input the column number (1-9): "))-1,
            int(input("Input the row number (1-9): "))-1,
            int(input("Input the value to set the tile to: "))
        )

main()

