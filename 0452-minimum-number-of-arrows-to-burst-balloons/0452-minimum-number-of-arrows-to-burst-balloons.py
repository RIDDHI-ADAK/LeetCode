class Solution:
    def findMinArrowShots(self, points):
        
        # Sort according to starting point
        points.sort()
        
        arrows = 1
        prev_end = points[0][1]
        
        for i in range(1, len(points)):
            
            current_start = points[i][0]
            current_end = points[i][1]
            
            # No overlap
            if current_start > prev_end:
                arrows += 1
                prev_end = current_end
            
            # Overlap
            else:
                prev_end = min(prev_end, current_end)
        
        return arrows