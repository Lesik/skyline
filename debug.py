#!/usr/env python3

"""This is a debugging class. Do not count this file
into the final mark. Some conventions may not have been followed."""

import backend

__author__ = "6040608: Phillip Berger, 6040608: Phillip Berger"
__email__ = "pidgornyy@informatik.uni-frankfurt.de," \
			"berger.phillip@hotmail.com"


game_backend = backend.Backend()
game_backend.generate_field()
print(game_backend.get_field())

# uncomment to test comparison
"""
true = game_backend.compare_fields(eval(input()))
#true = game_backend.compare_fields([[2, 3, 1, 4], [4, 1, 2, 3], [1, 4, 3, 2], [3, 2, 4, 1]])
print(true)


print()

# uncomment to test hint generation
print("right hints:", game_backend.generate_hints(0))
print("left hints:", game_backend.generate_hints(1))
print("top hints:", game_backend.generate_hints(2))
print("bottom hints:", game_backend.generate_hints(3))
print()

# uncomment to test hint generation by GUI
x = "egal"
print("right hints:", game_backend.get_hints(x, 5))
print("left hints:", game_backend.get_hints(x, 0))
print("top hints:", game_backend.get_hints(0, x))
print("bottom hints:", game_backend.get_hints(5, x))

print()

# uncomment to test getting rows and cols
print("third row:", game_backend.get_row(2))
print("second col:", game_backend.get_col(1))"""