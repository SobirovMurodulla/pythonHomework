import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operation")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.components])

def get_vector_input(prompt):
    components = input(prompt).split()
    return Vector(*map(float, components))


v1 = get_vector_input("Enter the components of the first vector: ")
v2 = get_vector_input("Enter the components of the second vector: ")

print(f"v1: {v1}")
print(f"v2: {v2}")

v3 = v1 + v2
print(f"v1 + v2: {v3}")

v4 = v2 - v1
print(f"v2 - v1: {v4}")


dot_product = v1 * v2
print(f"v1 * v2 (dot product): {dot_product}")

scalar = 3
v5 = scalar * v1
print(f"{scalar} * v1: {v5}")

print(f"|v1|: {v1.magnitude()}")

v_unit = v1.normalize()
print(f"v1 normalized: {v_unit}")