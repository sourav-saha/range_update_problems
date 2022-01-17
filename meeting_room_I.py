'''
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if len(intervals) == 0:
            return True 

        ''' method 1
        intervals_sorted = sorted(intervals, key=lambda x:x.start)
       
        for i in range(len(intervals_sorted)-1):
            if intervals_sorted[i].end > intervals_sorted[i+1].start:
                return False
            
        return True
        '''

        #method 2: optimized 
        end = -1
        for interval in (sorted(intervals, key=lambda x:x.start)):
            if interval.start < end:
                return False
            end = interval.end
        
        return True
      
      
