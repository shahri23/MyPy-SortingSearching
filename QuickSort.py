# QUICK SORT: Choose a pivot, then use it as divider

def quick_sort (B):                                          # Main Funciton
    quick_sort2(B,0,len(B)-1)
    
def quick_sort2 (B,low,hi):                                  # Sub-funciton
    if low < hi:
        p = partition(B, low, hi)
        quick_sort2(B, low, p-1)                             # Recursive Call
        quick_sort2(B, p+1, hi)

def get_pivot(B,low,hi):                                     # Get Pivot
    mid = (hi+low)//2
    pivot =hi
    if B[low] < B[mid]:
        if B[mid] < B [hi]:
            pivot =mid
    elif B[low] < B[hi]:
        pivot = low
    return pivot

def partition (B, low, hi):                                  # Partition Function                             
    pivotIndex =get_pivot (B,low,hi)
    pivotValue =B[pivotIndex]
    B[pivotIndex],B[low]=B[low],B[pivotIndex]
    border = low

    for i in range(low,hi+1):
        if B[i] < pivotValue:
            border +=1
            B[i],B[border] = B[border],B[i]
    B[low],B[border] = B[border], B[low] 
