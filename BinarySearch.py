# Binary Search (Search a given number in a sorted list)
# Strategy: Start at the middle, compare the given number, divide the list and use 
# left half if number is less than mid-value else use the right half, keep doing it.

 def binSearch(L, number):
     List=sorted(L)                                             # make sure list is sorted
     size = len(List)
     start=0
     end=size-1
     
     while start<end:
         test = (start+end)//2
         if List[test] == number:
             return "Number found at {0}th ".format(test+1)   
         elif List[test] > number:
             end=test                                          # If mid-number > given-number, move end index lower
         else:
             start=test                                        # If mid-number < given-number, move start index higher
     if List[start] == number:
         return "number index: ", start
     else:
         return "number not in the list"
         
binSearch([1,2,3,4,5,6,7,8,9],1)
