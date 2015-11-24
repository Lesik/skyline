#!/usr/env python3

import random

class Backend:

	field_dimens = 4

	def compare_fields(self, correct, check):
		all_correct = True
		for row in range(self.field_dimens):
			for column in range(self.field_dimens):
				if not correct[row][column] == check[row][column]:
					all_correct = False
		return all_correct

	def riilain(self, list, index, item):
		"""Replace item in list, append if needed (RIILAIN).
		:param list: the list in question
		:param index: index of where item should ideally go
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
				for column in range(self.field_dimens):
					self.riilain(field[row], column, heights[column])
				# uncomment this to see how many tries it takes until a
				# fitting combination was found, quite amusing
				#print(field[row])

				cont = True
				for column in range(self.field_dimens):
					for previous_row in range(len(field) - 1):
						if (field[previous_row][column]	== \
								field[row][column]):
							cont = False
			#print(field[row])
		return field