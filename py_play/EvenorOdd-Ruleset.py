def EvenorOdd(nums):
    classify={"odd":[],"even":[]}
    for i in nums:
        if i % 2 ==0:
            classify["odd"].append(i)
        else:
            classify["even"].append(i)
    return classify
nums=[1,2,3,4,5,6,7]
print(EvenorOdd(nums))