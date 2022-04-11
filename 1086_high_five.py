class Solution:
    def highFive(self, items):
        
        student_data = {}
        
        for student in items:
            user = student[0]
            score = student[1]

            if user in student_data:
                student_data[user].append(score)
            else:
                student_data[user] = [score]
        
        students_average = []
        
        for student in sorted(student_data.keys()):
            scores = student_data[student]
            print(scores)
            average = sum(sorted(scores, reverse=True)[:5]) // 5
            students_average.append([student, average])
        
        return students_average

test = Solution()
test.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
test.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]])
test.highFive([[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]])