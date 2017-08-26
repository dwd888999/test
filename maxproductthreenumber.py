# -*- coding:utf-8 -*-
__author = 'Phoenix'


class Solution(object):
    def maximumProduct(self,nums):
        nums.sort()
        if len(nums)>6:
            A=nums[:3]+nums[-3:]
            print A
        return max(A[i]*A[j]*A[k]
                   for i in xrange(len(A))
                   for j in xrange(i+1,len(A))
                   for k in xrange(j+1,len(A))
                   )

if __name__=='__main__':
    s=Solution()
    nums=[1,2,3,3,2,3,4,5,7,8,4,44]
    print s.maximumProduct(nums)

