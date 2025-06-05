def mdc (a, b):
    maior =  max(a,b)
    menor =  min(a,b)
    if maior % menor == 0:
        return menor
    else:
        return mdc(menor, maior % menor)
    
print(mdc(32, 18)) #2
print(mdc(7,3)) #1