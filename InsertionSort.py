# INSERTION SORT
# used only for small data dets as nested forloops

def insertion_sort(B):

    for i in range(1, len(B)):
        curNum=B[i]
        for j in range (i-1,-1,-1):          # this range will stop at 0th index
            if B[j] > curNum:                # cuz python index stop 1 less range
                B[j+1]= B[j]
                B[j] = curNum
            else:
                B[j+1] = curNum
                break
