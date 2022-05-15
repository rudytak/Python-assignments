from operator import truediv

op = [
    [-2, 1],
    [-2, -1],
    [2, 1],
    [2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2]
]

def list_sum(list1, list2):
    return [sum(x) for x in zip(list1, list2)]

class grid:
    def __init__(self, data):
        self.raw = data
        self.parse()

    def parse(self):
        self.grid = self.raw.split("\n")
        for i in range(0,len(self.grid)):
            self.grid[i] = list(self.grid[i])
    
    def reset(self):
        self.parse()

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]
    
    def set(self,pos,val, force = False):
        # also returns the value replaced/or that would've been replaced
        try:
            if(pos[0] >= 0 and pos[1] >= 0):
                if self.grid[pos[0]][pos[1]] == "_" or force:
                    old = self.grid[pos[0]][pos[1]]
                    self.grid[pos[0]][pos[1]] = val
                    return old
                else:
                    return self.grid[pos[0]][pos[1]]
        except:
            return None
    
    def find(self, val, occ = 1):
        found = self.find_all(val)
        if(len(found) > 0):
            return found[occ - 1]
        else:
            return None
    
    def find_all(self, val):
        out = []
        for x in range(len(self.grid)):
            row = self.grid[x]
            for y in range(len(row)):
                el = row[y]
                if (el == val):
                    out.append([x,y])
        return out

    def set_jump_places(self, k_place = None, depth = 1):
        if k_place == None:
            k_place = self.find("K")
        
        # accumulate all the places replaced
        out = []
        for o in op:
            out.append(self.set(list_sum(k_place,o), str(depth)))

        return out

    def path_find(self, no_reset = False):        
        places = self.find_all("K")
        depth = 0
        max_depth = 100

        while True:
            for place in places:
                replaced_by_jump = self.set_jump_places(place, depth+1)
                if "C" in replaced_by_jump:
                    if not no_reset:
                        self.reset()
                    return depth+1
            depth+=1
            places = self.find_all(str(depth))

            if depth > max_depth:
                if not no_reset:
                    self.reset()
                return -1
    
    def write(self):
        p = ""
        for row in self.grid:
            p+="".join(row)+"\n"
        print(p)

        return p

g = grid(open("./vstup.txt").read())
print(g.path_find())
# g.write()