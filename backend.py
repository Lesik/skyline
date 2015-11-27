#!/usr/env python3

"""Docstring goes here!"""

import random

__author__ = "6082200: Oles Pidgornyy, 6040608: Phillip Berger"


class Backend:

	field = None
	field_dimens = 4

	def get_field_dimens(self):
		return self.field_dimens

	def set_field_dimens(self, field_dimens):
		self.field_dimens = field_dimens

	def start_game(self):
		self.generate_field()

	def compare_fields(self, field):
		all_correct = True
		for row in range(self.field_dimens):
			for col in range(self.field_dimens):
				if not self.field[row][col] == field[row][col]:
					all_correct = False
		return all_correct

	def hints_count(self, items):
		hints, hightest_item = 0, 0
		for item in items:
			if (item > hightest_item):
				hightest_item = item
				hints += 1
		return hints

	def get_row(self, row):
		return self.field[row]

	def get_col(self, col):
		coll = []
		for row in self.field:
			coll.append(row[col])
		return coll

	def get_hints(self, row, col):
		"""Helper function for GUI to get hints by coordinates
		:return: list of hints for coordinates
		"""
		if (col == 5):
			return self.generate_hints(0)
		elif (col == 0):
			return self.generate_hints(1)
		elif (row == 0):
			return self.generate_hints(2)
		elif (row == 5):
			return self.generate_hints(3)

	def generate_hints(self, side):
		"""Generates hints
		:param side: the side on which to generate hint, as int
		 0 is right
		 1 is left
		 2 is top
		 3 ist bottom
		:return: list of hints for side
		"""
		hints = []
		for row in range(self.field_dimens):
			if (side == 0):
				values = self.get_row(row)
			elif (side == 1):
				values = reversed(self.get_row(row))
			elif (side == 2):
				values = self.get_col(row)
			elif (side == 3):
				values = reversed(self.get_col(row))
			else:
				raise ValueError("unknown side")
			hints.append(self.hints_count(values))
		return hints

	def get_field(self):
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
		self.field = field
