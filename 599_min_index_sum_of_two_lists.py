class Solution:
    def findRestaurant(self, list1, list2):
        data = {}
        
        for i, element in enumerate(list1):
            if element in list2:
                data[element] = sum([i, list2.index(element)])
        
        lowest_val = sorted(data.values())[0]
        
        return [k for k, v in data.items() if v == lowest_val]

test = Solution()
test.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
test.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])