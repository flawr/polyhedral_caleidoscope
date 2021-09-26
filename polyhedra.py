import numpy as np
import pyvista as pv
np.random.seed(0)

class Face:
    def __init__(self):
        """ vertices should be listed in positive orientation (ccw)"""
        self.coords = np.array([[0,0,0], [0,1,0], [1,1,0], [1,0,0]])

    def copy(self):
        copy = type(self)()
        copy.coords = self.coords.copy()
        return copy

    @property
    def normal(self):
        normal = self.coords.sum(axis=0)
        return normal / np.linalg.norm(normal)

    @property
    def center(self):
        return self.coords.mean(axis=0)

    @property
    def coordinate_system(self):
        x_axis = self.coords[0] - self.center
        x_axis /= np.linalg.norm(x_axis)
        z_axis = self.normal
        y_axis = np.cross(z_axis, x_axis)
        cs = np.stack([x_axis, y_axis, z_axis], axis=1)
        # assert np.abs(np.dot(np.cross(x_axis, y_axis), z_axis)-1) < 1e-8, "axes dont seem to form an RHS"
        return cs


    def mirror(self, axis):
        self.coords[:, axis] *= -1
        # reverse order to preserver orientation of vertices
        self.coords = self.coords[::-1, :]
        return self

    def rot111(self, n=1):
        """ rotate by 120° around the vector (1,1,1) """
        n = n % 3
        for _ in range(n):
            self.coords = self.coords[:, [1, 2, 0]]
        return self


class Polyhedron:
    def __init__(self):
        self.faces = [Face()]

    def draw(self, shape=None):
        """ draw the polyhedron with the default faces,
        if a `shape` is defined, we instantiate the `shape` in the
        local coordinate system of each face"""
        if shape is None:
            vertices = np.concatenate([f.coords for f in self.faces], axis=0)
            faces = []
            accum = 0
            for f in self.faces:
                vert_count = f.coords.shape[0]
                faces.append(vert_count)
                faces.extend(list(range(accum, accum+vert_count)))
                accum += vert_count
            faces = np.array(faces, dtype=int)
        else:
            vertices = []
            faces = []
            accum = 0
            for f in self.faces:
                cs = f.coordinate_system
                transformed_shape = shape @ cs[:, 0:2].T
                transformed_shape += f.center
                vertices.append(transformed_shape)
                vert_count = shape.shape[0]
                faces.append(vert_count+1)
                faces.extend(list(range(accum, accum+vert_count)))
                faces.append(accum)
                accum += vert_count

            vertices = np.concatenate(vertices, axis=0)
        surf = pv.PolyData(vertices, faces)
        surf = surf.triangulate()
        surf.plot() #show_edges=True)
