class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def gram_schmidt(self):
        basis = []
        for i in range(len(self.matrix)):
            vector = self.matrix[i]
            for j in range(i):
                projection = self.projection(vector, basis[j])
                vector = self.subtract(vector, projection)
            if self.norm(vector) > 0:
                basis.append(self.normalize(vector))
        return basis

    def projection(self, vector1, vector2):
        scalar_product = self.dot_product(vector1, vector2)
        norm_squared = self.norm(vector2) ** 2
        projection = [coord * scalar_product /
                      norm_squared for coord in vector2]
        return projection

    def subtract(self, vector1, vector2):
        result = [coord1 - coord2 for coord1, coord2 in zip(vector1, vector2)]
        return result

    def dot_product(self, vector1, vector2):
        result = sum(coord1 * coord2 for coord1,
                     coord2 in zip(vector1, vector2))
        return result

    def norm(self, vector):
        result = (sum(coord**2 for coord in vector)) ** 0.5
        return result

    def normalize(self, vector):
        norm_value = self.norm(vector)
        normalized = [coord / norm_value for coord in vector]
        return normalized


matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [
                9, 10, 11, 12], [13, 14, 15, 16]])

basis_vectors = matrix.gram_schmidt()

print(basis_vectors)
