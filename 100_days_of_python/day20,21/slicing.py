piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys)
print(len(piano_keys))
print(piano_keys[0])
print(piano_keys[-1])
print(piano_keys[2:5])
print(piano_keys[5:])
print(piano_keys[:5])
print(piano_keys[2:5:2]) # start, end, increment
print(piano_keys[::2]) # need all in this list with step increment of 2
print(piano_keys[::-1]) # reverse the list
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 7
# a
# g
# ['c', 'd', 'e']
# ['f', 'g']
# ['a', 'b', 'c', 'd', 'e']
# ['c', 'e']
# ['a', 'c', 'e', 'g']
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

piano_tuples = ("do","re","mi","fa","so","la","ti")
