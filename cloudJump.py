def jumpingOnClouds(c):
    steps=0
    jump=0
    end=len(c)
    while jump <(end-1):
        if jump+2<end and c[jump+2]==0:
            jump+=2
            steps+=1
        else:
            jump+=1
            steps+=1
    return steps  
