import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operation. Must multiply by a scalar or another vector.")

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))
    # Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          

# Addition
v3 = v1 + v2
print(v3)          

# Subtraction
v4 = v2 - v1
print(v4)          

# Dot product
dot_product = v1 * v2
print(dot_product) 

# Scalar multiplication
v5 = 3 * v1
print(v5)          

# Magnitude
print(v1.magnitude())  

# Normalization
v_unit = v1.normalize()
print(v_unit)      