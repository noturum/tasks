def od(nums:list):
    lod=[]
    for i in range(2,min(nums)):
        if all([1 if num%i==0 else 0 for num in nums]):
            lod.append(i)
    return lod
