'''
https://www.lintcode.com/problem/919/

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        # create the timeline array
        cal = [0]*1000000
        for interval in intervals:
            cal[interval.start] += 1
            cal[interval.end] -= 1
        
        # prefix sum array
        pa = []
        pa.append(cal[0])
        for i in range(1, len(cal)):
            pa.append(pa[i-1] + cal[i])

        return max(pa)
      
      
