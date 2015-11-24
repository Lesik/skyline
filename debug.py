#!/usr/env python3
__author__ = "6040608: Phillip Berger"
import backend

game_backend = backend.Backend()
game_backend.generate_field()
print(game_backend.get_field())
true = game_backend.compare_fields(eval(input()))
#true = game_backend.compare_fields([[2, 3, 1, 4], [4, 1, 2, 3], [1, 4, 3, 2], [3, 2, 4, 1]])
print(true)
