import copy as copy

def constrain(val,_min,_max):
    return max(min(val,_max),_min)

class Sudoku:
    def __init__(self, blocks_x, blocks_y, block_x, block_y):
        self.block_dim = {
            0:block_x,
            1:block_y,
            "x":block_x,
            "y":block_y
        }
        self.blocks_dim = {
            0:blocks_x,
            1:blocks_y,
            "x":blocks_x,
            "y":blocks_y
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
                out[i].append(Tile(None, False))
        return out

    def input(self, x,y,val):
        x=constrain(x,self.max_x-1,0)
        y=constrain(y,self.max_y-1,0)
        val=constrain(val,self.block_dim[0] * self.block_dim[1],1)

        bs_x=x//self.block_dim[0]
        bs_y=y//self.block_dim[1]
        b_x=x%self.block_dim[0]
        b_y=y%self.block_dim[1]

        self.blocks[bs_x][bs_y][b_x][b_y].overwrite(val)

    def print(self):
        arr = self.createEmpty2DArray(self.max_y,self.max_x)

        for bs_x, block_col in enumerate(self.blocks):
            for bs_y, block in enumerate(block_col):
                for b_x, col in enumerate(block):
                    for b_y, tile in enumerate(col):
                        arr[bs_y*self.block_dim[1]+b_y][bs_x*self.block_dim[0]+b_x] = tile.value

        for x,col in enumerate(arr):
            line=""
            if(x!=0 and x!=self.max_x-1 and not x%(self.block_dim[1])):
                line = "="*(4*(self.max_x + self.blocks_dim["x"]-1)-1)
            print("\n"+line)

            for y, t in enumerate(col):
                sep = " "
                if(y!=0 and not y%(self.block_dim[0])):
                    sep = "|"

                print(sep+str(t), end="")

class Tile:
    def __init__(self, value, constant = False):
        self.value = value
        self.constant = constant

    def overwrite(self, new):
        if(self.constant):
            return False
        else:
            self.value = new
            return True

def main():
    s = Sudoku(3,3,3,3)
    s.print()

main()

