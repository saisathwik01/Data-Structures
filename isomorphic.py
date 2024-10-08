# Question: Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. No two characters may map to the same character, 
# but a character may map to itself.


#CODE:

def isIsomorphic(s,t):
    map1 = []
    map2 = []

    for i in s:
        map1.append(s.index(i))
    for i in t:
        map2.append(t.index(i))
    if map1 == map2:
        return True
    return False