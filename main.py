import numpy as np
from dodecahedron import Dodecahedron

def main():
    """define a 2d shape (polygon) and pass the coordinates
    of the vertices as a (n, 2)-array to `Dodecahedron.draw`
    in order to draw an instance at every face of the dodecahedron.
    Ideally this shape has a 2*pi/5 rotational symmetry.
    The x-axis of the local coordinate system of the faces
    points towards a vertex of the dodecahedron."""
    l = []
    n = 5
    def polar2rect(r, k):
        return [r * np.cos(2 * k * np.pi / n), r * np.sin(2 * k * np.pi / n)]
    for k in range(5):
        if ornate_star := True:
            r = 1.0514622242382672  # radius of center of pentagon to vertex
            l.append(polar2rect(r, k))
            r = 2.75  # guesstimated distance to point of star - who's got time for algebra?
            l.append(polar2rect(r, k + 0.5))
            l.append(polar2rect(2.0, k + 0.6))
            l.append(polar2rect(1.2, k + 0.4))
            l.append(polar2rect(0.5, k + .8))
            l.append(polar2rect(1.05, k+1))
    shape = np.array(l)
    if show_mpl := False:
        import matplotlib.pyplot as plt
        plt.plot(shape[:, 0], shape[:, 1], 'o-')
        plt.show()
    d = Dodecahedron()
    d.draw(shape=shape)



if __name__ == '__main__':
    main()
