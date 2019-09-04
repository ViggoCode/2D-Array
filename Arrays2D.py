class Array1D:
    def __init__(self, _values):
        self.values = _values
        self.array = []
        self.createArray()
    def createArray(self):
        self.array = self.values
class Array2D:
    def __init__(self, _values, _x = 0, _y= 0):
        self.values = _values
        self.x = _x
        self.y = _y
        if self.x <= 0 or self.y <= 0:
            self.x = len(self.values)/2
            self.y = 2
        self.array = self.createArray()
    def createArray(self):
        array = []
        if int(self.x * self.y) == int(len(self.values)):
            for i in range(self.y):
                g = []
                for j in range(self.x):
                    g.append(self.values[i*2 + j ])
                array.append(Array1D(g))
            return array
        else:
            return None
    def printArray(self):
        if self.array == None:
            print ("The array is corupt or not created")
            return False
        for i in range(len(self.array)):
            print(self.array[i].array)
    def getItem(self, y, x):
        return self.array[y].array[x]
