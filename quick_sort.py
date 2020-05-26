#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:05:50 2020

Quick Sort
快速排序

@author: xueqiwang
"""

def partition(nums, left, right):
    i = left
    j = right
    temp = nums[i]
    
    while i < j:
        # 从右往左找小于temp的数
        while i < j and nums[j] >= temp:
            j -= 1
        if i < j:
            # 交换
            nums[i] = nums[j]
            i += 1
        # 从左往右找大于temp的数
        while i < j and nums[i] <= temp:
            i += 1
        if i < j:
            # 交换
            nums[j] = nums[i]
            j -= 1
    
    nums[i] = temp
    
    return nums, i
        

def QuickSort(nums, left, right):
    if left < right:
        nums, i = partition(nums, left, right)
        #print(nums)
        nums = QuickSort(nums, left, i-1)
        #print(nums)
        nums = QuickSort(nums, i+1, right)
        #print(nums)
        
    return nums

nums = [5,5,4,3,2,1,6]
print(QuickSort(nums, 0, 6))