#!/usr/env python3

"""Docstring goes here!"""

import random

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"


class Backend:

	field = None
	field_dimens = 4

	def compare_fields(self, field):
		all_correct = True
		for row in range(self.field_dimens):
			for col in range(self.field_dimens):
				if not self.field[row][col] == field[row][col]:
					all_correct = False
		return all_correct

	def get_field(self):
		return self.field

	def riilain(self, list, index, item):
		"""Replace item in list, append if needed (RIILAIN).
		:param list: the list in question
		:param index: index of where item shoul  ideally go
		:param item: item that should be inserted
		:return: nothing
		"""
		if (index < len(list)):
			list[index] = item
		else:
			list.append(item)

	def generate_field(self):
		"""Generate a game field, no duplicates allowed.
		:return: game field as list
		"""
		field = []

		for row in range(self.field_dimens):
			field.insert(row, [])
			heights = list(range(1, self.field_dimens + 1))

			cont = False
			while not cont:
				random.shuffle(heights)
				for col in range(self.field_dimens):
					self.riilain(field[row], col, heights[col])
				# uncomment this to see how many tries it takes until a
				# fitting combination was found, quite amusing
				#print(field[row])

				cont = True
				for col in range(self.field_dimens):
					for previous_row in range(len(field) - 1):
						if (field[previous_row][col] == field[row][col]):
							cont = False
			#print(field[row])
		self.field = field
