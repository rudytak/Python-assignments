import * as readline from 'node:readline';

class Grid{
    constructor(x){
        this.size = x;
        this.possibleColumns = []
        this.columns={}

        for(var i = 0; i < this.size; i++){
            var le=String.fromCharCode(65+i)
            this.possibleColumns.push(le);

            this.columns[le] = []
            for(var j = 0; j < this.size; j++){
                this.columns[le].push(false)
            }
        }
    }

    getValueAt(coord = "A1"){
        var t,num;
        [t,num] = Grid.decodeCoordinate(coord)

        return this.columns[t][num-1]
    }

    setValueAt(coord, value){
        var t,num;
        [t,num] = Grid.decodeCoordinate(coord)

        this.columns[t][num] = value;

        return value
    }

    static decodeCoordinate(coord){
        var t = coord.substring(0,1)
        var num = parseInt(coord.substring(1))

        return [t, num]
    }

    writeOut(){

    }

    get readable(){
        var txt = ""
        for(var le of this.possibleColumns){
            for(var i = 0; i < this.size; i++){
                txt += this.getValueAt(le+i)?"X":".";
            }
            txt +="\n";
        }

        return txt
    }
}

var my_g = new Grid(10);

my_g.setValueAt("B2", true)
console.log(my_g.readable)