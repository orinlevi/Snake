#################################################################
# FILE : apple.py
# WRITER : orin levi
# EXERCISE : intro2cs2 ex10 2021
# DESCRIPTION: class Apple
#################################################################

class Apple:
	"""
	Class apple creates an apple object. the class has three "geters" methods
	that are giving back the apple's attributes- apple's coordinate,
	the score that given when eating the apple and apple's color
	"""

	def __init__(self, coordinate, score):
		self.__coordinate = coordinate
		self.__score = score
		self.__color = "green"

	def get_coordinate(self):
		"""
		the methods return the coordinates of the apple
		"""
		return self.__coordinate

	def get_color(self):
		"""
		the methods return the color of the apple
		"""
		return self.__color

	def get_score(self):
		"""
		the methods return the score of the apple
		"""
		return self.__score
