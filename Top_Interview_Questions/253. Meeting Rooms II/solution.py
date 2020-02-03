from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # sort the intervals by their starting time
        intervals.sort(key=lambda x: x[0])
        rooms = []
        
        heappush(rooms, intervals[0][1])
        
        for s,e in intervals[1:]:
            # a room is available if its endtime is same or less than the new meeting's start time
            # in which case we want to free up that room
            if rooms[0] <= s:
                heappop(rooms)
            
            heappush(rooms, e)
        
        return len(rooms)