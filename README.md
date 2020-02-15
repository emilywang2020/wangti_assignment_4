# wangti_assignment_4
1. This program takes command line arguments for standard input and output.

2. It takes two command line arguments followed by python
   *i. main.py and a comma-separated list of integers (for instance: 1,2,3,4,5,10) with no space in between

3. The input is a list of comma-separated integers.

4. The output is sets of X and the number of integers in set X. If there is no solution found (the lenght of set X equals to zero), the message "no result" will be displayed. 
 
5. The function partial_digest(parameter) takes the list of integers from input into the parameter. This function performs the partial digest algorithm.

6. When the partial_digest(multiset) function is called, the width element (w) will be set to the maximum value from the multiset,
     and w will be removed from the multiset. The set X is initialize with 0 and the width, which is a list of integers such that DX=L. 
      A function called place(multiset, X) will be called to perform the recursive subroutine of the algorithm.

7. The distance(y, X, L) function will compute the pair distance between y and each point in the set X.

8. The remove_elements(y, X, L) function will remove a length of distance from set L if the length exists in set L.

9. The subset(y, X, L) function will check if a distance between point y and a point in set X is in the set L. If the subset exists, then true will be returned. Otherwise, false will be returned.

10. The function place(L, X, multiset) will perform the recursive rountine of the algorithm.
