#Fruits into baskets:
fruits = [1,1,2,2,3,3,2,1]
def totalFruit(fruits):
    fruit_bas={}
    l=0
    max_fruits=0
    for r in range(len(fruits)):
        fruit_bas[fruits[r]]=fruit_bas.get(fruits[r],0)+1
        
        while len(fruit_bas)>2:
                fruit_bas[fruits[l]]-=1
                if fruit_bas[fruits[l]]==0:
                    del fruit_bas[fruits[l]]
                l+=1
        max_fruits=max(max_fruits,r-l+1)
    return max_fruits















print(totalFruit(fruits))