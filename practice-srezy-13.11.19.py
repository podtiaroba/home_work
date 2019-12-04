def x (ss):
	return (ss.lower())
def y (ss):
	return (ss.upper())
s = ["oijhojh", "OIOIUOIU", "KiJJideO"]
new_list = list(map(x, s))
old_list = list(map(y, s))
print(new_list)
print(old_list)