class DistanceMatrix:
	def __init__(self, matrix):
		self.matrix = matrix

	def get_distance(self, i, j):
		return self.matrix[i][j]


distance_matrix = DistanceMatrix([[0, 8, 5, 1, 10, 5, 9],
                                  [9, 0, 5, 6, 6, 2, 8],
                                  [2, 2, 0, 3, 8, 7, 2],
                                  [5, 3, 4, 0, 3, 2, 7],
                                  [9, 6, 8, 7, 0, 9, 10],
                                  [3, 8, 10, 6, 5, 0, 2],
                                  [3, 4, 4, 5, 2, 2, 0]])

class Person:
	def __init__(self, start, end):
		self.start = start
		self.end = end

def init_person(n):
	list_person = []
	for i in n:
		list_person.append(Person(i+1, i+1+n))
	return list_person

