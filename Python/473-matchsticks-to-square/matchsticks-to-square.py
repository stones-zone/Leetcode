# -*- coding:utf-8 -*-


# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
#
#  Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.
#
# Example 1:
#
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
#
#
#
# Example 2:
#
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the matchsticks.
#
#
#
# Note:
#
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
#
#


class Solution(object):
    def makesquare(self, nums):
        primeter=sum(nums)
        if primeter<=0 or primeter%4!=0:
            return False
        target=primeter/4
        if max(nums)>target:
            return False
        self.color,self.result=[0]*len(nums),[False]*4
        self.nums=sorted(nums)
        self.count=0
        print self.nums,target
        for i in range(len(self.nums)-1,-1,-1):
            if self.nums[i]==target:
                self.color[i]=1
                self.count+=1
                continue
            if self.color[i]==0:
                self.explored=set([i])
                result=self.visit(i,target-self.nums[i],[i])
                #print 'result',result
        return self.count==4

    def visit(self,current,remain,used):
        # print '-'*80
        # print 'current is',current
        # print 'remain is',remain
        # print 'used is',used
        if remain==0:
            for index in used:
                self.color[index]=1
            # print 'self.color',self.color
            self.explored=set(range(len(self.nums)))
            self.count+=1
            return True
        for next_point in range(current-1,-1,-1):
            if self.color[next_point]==0 and next_point not in self.explored and remain-self.nums[next_point]>=0:
                self.visit(next_point,remain-self.nums[next_point],used+[next_point])
    
    def makesquare1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_len = sum(nums)
        if total_len % 4:
            return False
        side_len = total_len / 4
        fullset = (1 << len(nums)) - 1
        
        used_subsets = []
        valid_half_subsets = [0] * (1 << len(nums)) 
        for subset in xrange(fullset + 1):
            n_total = 0
            for i in xrange(len(nums)):
                if subset & (1 << i):
                    n_total += nums[i]
            if n_total == side_len:
                for used_subset in used_subsets:
                    if used_subset & subset == 0:
                        valid_half_subset = used_subset | subset
                        valid_half_subsets[valid_half_subset] = 1
                        if valid_half_subsets[fullset ^ valid_half_subset]:
                            return True
                used_subsets.append(subset)
        return False
                
                
        
