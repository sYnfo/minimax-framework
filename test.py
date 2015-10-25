from games.nim import nim

g = nim(heaps=[3, 4, 5])
assert not g.over()
assert set(g.available_moves()) == set(((0, 1), (0, 2), (0, 3),
                                        (1, 1), (1, 2), (1, 3), (1, 4),
                                        (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)))
assert g.active_turn == "player"

g2 = g.get_new_state((0, 1))
assert not g2.over()
assert g2.heaps == [2, 4, 5]
assert g2.active_turn == "opponent"

g3 = g2.get_new_state((0, 2))
g3 = g3.get_new_state((1, 4))
g3 = g3.get_new_state((2, 5))
assert g3.over()

print("Tests passed AOK!")
