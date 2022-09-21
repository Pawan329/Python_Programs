# Need to search the desired element from the list
'''
Things to remember:
1. if list is empty
2. if desired numbers doesn't exist in list
3. if desired number occurs more than one time
'''

cards = [1, 2, 3, 5, 7, 8, 9, 10]
query = 4

def searchCard(cards, query):

    low, hi = 0, (len(cards) -1)
    mid = len(cards)//2
    
    while len(cards)>0:

        if (low+hi)//2 == low:
            return -1
        
        if query == cards[low]:
            return low

        elif query == cards[hi]:
            return hi

        elif query == cards[mid]:
            return mid

        elif query < cards[mid]:
            hi = mid-1
            mid = (hi + low)//2

        elif query > cards[mid]:
            low = mid + 1
            mid = (hi + low)//2


result = searchCard(cards, query)
print("Index of desired card is ",result)