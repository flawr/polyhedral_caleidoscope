import numpy as np
from polyhedra import Polyhedron, Face

def main():
    d = Dodecahedron()
    d.draw()
    cs = d.faces[0].coordinate_system
    print(cs)


class Dodecahedron(Polyhedron):
    def __init__(self):
        self.faces = []
        d = DodecaFace()
        self.faces.append(d)
        new = [d.copy().mirror(axis=0) for d in self.faces]
        self.faces.extend(new)
        new = [d.copy().mirror(axis=2) for d in self.faces]
        self.faces.extend(new)
        new = [d.copy().rot111() for d in self.faces]
        self.faces.extend(new)
        new = [d.copy().rot111() for d in new]
        self.faces.extend(new)

phi = (1+np.sqrt(5))/2

class DodecaFace(Face):
    def __init__(self):
        self.coords = np.array(
            [[1, 1, 1],
             [1/phi, 0, phi],
             [1, -1, 1],
             [phi, -1/phi, 0],
             [phi, 1/phi, 0]
             ])



if __name__ == '__main__':
    main()
