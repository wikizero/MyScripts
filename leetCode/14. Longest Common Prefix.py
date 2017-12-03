# coding:utf-8

'''
求取最长公共前缀
'''
# my way:
lst = ['qaaab', 'qataa', 'qaaauiu', 'qaaatt', 'qaaaasd', 'qaaasdf']
flag = False
temp= ''
for i, v in enumerate(lst[0]):
	for j in lst[1:]:
		if len(j) < i+1 or v != j[i]:
			flag = True
			break
	if flag:
		break
	temp += v
print 'temp:', temp

print zip(*lst)
print min(lst)


# the better way
def longestCommonPrefix(strs):
	if not strs:
		return ""

	for i, letter_group in enumerate(zip(*strs)):
		print letter_group
		if len(set(letter_group)) > 1:
			return strs[0][:i]
	else:
		return min(strs)

print longestCommonPrefix(lst)
