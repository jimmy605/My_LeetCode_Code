class Solution:
    def hardestWorker(self, n, logs):
        leave_time = 0
        log_data = []
        highest_time = 0
        
        for log in logs:
            time = abs(leave_time - log[1])
            
            if time > highest_time:
                highest_time = time 
                log_data = [log[0]]
            elif time == highest_time:
                log_data.append(log[0])
            
            leave_time = log[1] 
        
        return sorted(log_data)[0]

test = Solution()
print(test.hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))
print(test.hardestWorker(2, [[0,10],[1,20]]))