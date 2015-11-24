#!/usr/env python3
__author__ = "6040608: Phillip Berger"
import backend

game_backend = backend.Backend()
game_backend.generate_field()
print(game_backend.get_field())

# uncomment to test comparison
"""
true = game_backend.compare_fields(eval(input()))
#true = game_backend.compare_fields([[2, 3, 1, 4], [4, 1, 2, 3], [1, 4, 3, 2], [3, 2, 4, 1]])
print(true)
"""

print()

# uncomment to test hint generation
print("left hints:", game_backend.generate_hints(1))
"""
print("right hints:", game_backend.generate_hints("l"))
print("top hints:", game_backend.generate_hints("t"))
print("bottom hints:", game_backend.generate_hints("b"))
"""

# uncomment to test hint generation by GUI
print("left hints:", game_backend.get_hints(100, 0))

print()

# uncomment to test getting rows and cols
print("third row:", game_backend.get_row(2))
print("second col:", game_backend.get_col(1))