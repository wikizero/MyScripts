
s = 'sdf(sf[sdf]a)dfasd{a)df}faf'
symbol = ['(', ')', '{', '}', '[', ']']
ss = filter(lambda x: x in symbol, s)
print ss

def isValid(s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False

        return stack == []

print isValid(s)


def findLUSlength(A, B):
    if A == B:
        return -1
    return max(len(A), len(B))

# print findLUSlength('avda', 'avdaa')