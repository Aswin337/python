from collections import Counter
class sol:
    def __init__(self,nums):
        self.x=nums  
    def is_prime(self,n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i ==0:
                return False
        return True
    def counter(self):
        freq=Counter(self.x)
        for count in freq.values():
            if self.is_prime(count):
                return True
        return False
nums=[1,2,3,4,5,4]
s=sol(nums)
r=s.counter()
print("List  Prime Frequency Presence :",r)


#counter :
num="1,2,3,2,3,7,2"
freq=Counter(num.split(","))
print(freq)
for count in freq.values():
    print(f"count :",count)