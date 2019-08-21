class Vector (object):
    def __init__(self, coordinates):
        if coordinates:
            if 0< len(coordinates)< 4:
                self.dimensionality = len(coordinates)
                self.coordinates= tuple(coordinates)
            else: 
                print("error in dimensionality of the coordinates")
        else:
            print("please provide coordinates in a coolection")

    def __str__(self):
        return "vector :{}".format(self.coordinates)
    
    def __eq__ (self, v):
        return self.coordinates == v. coordinates

