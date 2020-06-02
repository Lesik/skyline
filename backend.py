#!/usr/env python3

"""Backend for the game Skyline.
Can do the following:
- generate field
- compare a second field with the generated one
- count hints
- other helper functions
"""

import random

class Backend:

	field = None
	field_dimens = 4

	def get_field_dimens(self):
		"""Gets field dimensions.
		:return: field dimensions
		"""
		return self.field_dimens

	def set_field_dimens(self, field_dimens):
		"""Sets field dimensions.
		:param field_dimens: field dimensions
		"""
		self.field_dimens = field_dimens

	def start_game(self):
		"""Synonym function to generate field.
		"""
		self.generate_field()

	def compare_fields(self, field):
		"""Compares two fields.
		:param field: second field to compare with generated one
		:return: returns True if everything correct
		"""
		all_correct = True
		for row in range(self.field_dimens):
			for col in range(self.field_dimens):
				if not self.field[row][col] == field[row][col]:
					all_correct = False
		return all_correct

	def count_hints(self, items):
		"""Counts hints for one row or column.
		:param items: list with items of row/column
		:return: amounts of hints
		"""
		hints, hightest_item = 0, 0
		for item in items:
			if (item > hightest_item):
				hightest_item = item
				hints += 1
		return hints

	def get_row(self, row):
		"""Returns all values from requested row as list
		:param row: number of row from which to collect values
		:return: values of row
		"""
		return self.field[row]

	def get_col(self, col):
		"""Returns all values from requested column as list
		:param col: number of column from which to collect values
		:return: values of column
		"""
		coll = []
		for row in self.field:
			coll.append(row[col])
		return coll

	def get_hints(self, row, col):
		"""Helper function for GUI to get hints by coordinates
		:return: list of hints for coordinates
		"""
		if (row == 0):
			return self.count_hints(self.get_col(col - 1))
		elif (row == 5):
			return self.count_hints(reversed(self.get_col(col - 1)))
		elif (col == 0):
			return self.count_hints(self.get_row(row - 1))
		elif (col == 5):
			return self.count_hints(reversed(self.get_row(row - 1)))

	def get_field(self):
		"""Returns field (only for debugging purposes!)
		:return: field
		"""
		return self.field

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
		#print(self.field)
		self.field = field
