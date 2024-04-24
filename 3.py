def sn(minn:int,maxn:int):
    simp= lambda x: False if x<2 else True if not any([True if x%i==0 else False for i in range(2,x)]) else False
    return [i for i in range(minn,maxn+1) if simp(i)]
