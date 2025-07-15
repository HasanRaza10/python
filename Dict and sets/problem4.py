#  What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))

#The length of the set will be 2 because python takes value of a 
# number as 20 amd 20.0 has same value it ignores the data types