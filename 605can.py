# -*- coding:utf-8 -*-
__author = 'Phoenix'

'''
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''


class Solution(object):
    def canPlaceFlowers(self,flowerbed,n):
        numberofzero=1      #why inifinate 1???
        result=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                numberofzero+=1
            else:
                result+=(numberofzero-1)/2
                numberofzero=0
                print result
        if flowerbed[-1]==0:
            result+=numberofzero/2
        return result>=n

if __name__=='__main__':
    flow=[1,0,0,0,1]
    n=1
    s=Solution()
    print s.canPlaceFlowers(flowerbed=flow,n=n)

