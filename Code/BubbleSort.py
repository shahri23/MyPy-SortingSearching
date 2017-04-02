# BUBBLE SORT: compare 1st,2nd rearrange, compare 2nd,3rd rearrange
# compare again so on

def bub_sort(List):
    size=len(List)-1

def bubble_sort(B):
    for i in range (0, len(B)-1):
        for j in range(0,len(B)-1-i):
            if B[j]>B[j+1]:
                B[j],B[j+1]= B[j+1],B[j]
    return B
