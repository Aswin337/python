class twosum:
    def test_twosum(arr,tar):
        pair={}
        for i,v in enumerate(arr):
            dff=tar-v
            if dff in pair:
                return [pair[dff],i]
            pair[v]=i
arr=[2,1,5,1]
tar=3
print(twosum.test_twosum(arr,tar))