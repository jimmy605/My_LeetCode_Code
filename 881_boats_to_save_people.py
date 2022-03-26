class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        # Sort the list descending
        people.sort(reverse=True)
        
        # Start with the highest number
        while len(people) > 0:
            for person in range(len(people)):
                if person == limit:
                    boats += 1
                