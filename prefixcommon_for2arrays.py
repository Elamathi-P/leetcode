class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common=0
        lst1=[]
        set1=set()
        for i in range(len(A)):
            if A[i] in set1:
                common+=1
            else:
                set1.add(A[i])
            if B[i] in set1:
                common+=1
            else:
                set1.add(B[i])
            lst1.append(common)
        return lst1