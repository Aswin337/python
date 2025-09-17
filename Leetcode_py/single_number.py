from collections import Counter
def single_number(num):
    freq=Counter(num)
    for i in freq.items():
        if i[1]==1:
            return i[0]
        
num=[4,1,2,1]
print(single_number(num))