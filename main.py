#Emre Karabağ 210201053
def transitive_reflexive_closure(a):
    closure = set(a)
    while True:
        new_relations = set((x, w) for x, y in closure for q, w in closure if q == y)
        new_relations2 = set((x, x) for x, y in closure)
        new_relations3 = set((y, y) for x, y in closure)

        closure_until_now = closure | new_relations
        closure_until_now2 = closure_until_now | new_relations2
        closure_until_now3 = closure_until_now2 | new_relations3

        if closure_until_now3 == closure:
            break

        closure = closure_until_now3

    return closure


print(transitive_reflexive_closure([('a', 'a'), ('c', 'x'), ('b', 'w'), ('w', 'y')]))
print(transitive_reflexive_closure([(1, 2), (1, 3), (3, 4)]))
