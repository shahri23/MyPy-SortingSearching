# SELECTION SORT (find smallest, put in spot# 0, move to next, put in spot # 1 and so on)

def selection_sort(B):
    for i in range (0,len(B)-1):
        minIndex=i
        for j in range (i+1,len(B)):
            if B[j] < B[minIndex]:
                minIndex =j
        if minIndex !=i:
            B[i],B[minIndex] = B[minIndex],B[i]
