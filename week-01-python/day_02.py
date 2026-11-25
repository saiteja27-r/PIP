# dictionary
#Count the frequency of each character in a string.
text = "Saiteja"
freq = {}

for char in text:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
print(freq)

# Merge two dictionaries.
dict1 = {"a":20,"b":30}
dict2 = {"c":10,"d":40}
dict1.update(dict2)
print(dict1)

#Remove duplicate values from a dictionary.

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}
res = {}

for key,value in data.items():
    if value not in res.values():
        res[key] = value
print(res)

# Sort a dictionary by values.
marks = {
    "Python": 85,
    "Java": 90,
    "SQL": 75
}      

res = dict(sorted(marks.items(),key = lambda x:x[1]))
print(res)


#sets
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
un = a.union(b)
int = a.intersection(b)
diff = a.difference(b)
sys_diff = a.symmetric_difference(b)
sub = a.issubset(b)
dis = a.isdisjoint(b)


print(f'the union in the given numbers are:{un}')
print(f'the intersection in the given numbers are:{int}')
print(f'the difference in the given numbers are:{diff}')
print(f'the symmetric_difference in the given numbers are:{sys_diff}')
print(f'the subset in the given numbers are:{sub}')
print(f'the disjoint in the given numbers are:{dis}')







