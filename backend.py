#!/usr/env python3

"""Docstring goes here!"""

import random
import re
import collections

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

	def count_hints(self, items):
		hint, hightest_item = 0, 0
		for item in items:
			if (item > hightest_item):
				hightest_item = item
				hint += 1
		return hint

	def get_regex(self, dictionary, regex):
		dictionary_return = []
		for key in dictionary.keys():
			if re.match(key, regex):
				dictionary_return.append(dictionary[key])
		return dictionary_return

	def get_row(self, row):
		rowl = {}
		print("row in getrow", row)
		for key in self.field.keys():
			if key[0] == row:
				rowl[key[1]] = self.field[key]
		x = [y for y in rowl]
		return x

	def get_col(self, col):
		rowl = {}
		for key in self.field.keys():
			if key[1] == col:
				rowl[key[0]] = self.field[key]
		x = [y for y in rowl]
		return x

	def get_hints(self, row, col):
		"""Helper function for GUI to get hints by coordinates
		:return: list of hints for coordinates
		"""
		if (row == 0):
			return self.count_hints(self.get_col(col))
		elif (col == 0):
			return self.count_hints(self.get_row(row))
		elif (row == 5):
			return self.count_hints(reversed(self.get_col(col)))
		elif (col == 5):
			return self.count_hints(reversed(self.get_row(row)))

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
		print(side, hints)
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
		field = {}

		for row in range(self.field_dimens):
			#field.insert(row, [])
			heights = list(range(1, self.field_dimens + 1))

			cont = False
			while not cont:
				random.shuffle(heights)
				for col in range(self.field_dimens):
					#self.riilain(field[row], col, heights[col])
					field[(row, col)] = heights[col]
				# uncomment this to see how many tries it takes until a
				# fitting combination was found, quite amusing
				#print(field[(row, col)])

				cont = True
				for col in range(self.field_dimens):
					for previous_row in range(row):
						if (field[(previous_row, col)] == field[(row, col)]):
							cont = False
		self.field = field
		print(self.field)
		for k, v in self.field.items():
			print(k, ":", v)
		for row2 in range(self.field_dimens):
			print(self.get_row(row2))