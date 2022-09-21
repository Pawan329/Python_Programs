# Need to search the desired element from the list
'''
Things to remember:
1. if list is empty
2. if desired numbers doesn't exist in list
3. if desired number occurs more than one time
'''

cards = [1, 3, 2, 4, 5, 12, 89, 98, 74, 56]
find_card = 4

def searchCard(cards, find_card):
    list_index = 0
    while len(cards)>0:
        if cards[list_index] == find_card:
            return list_index

        list_index += 1

        if list_index == len(cards):
            return -1

result = searchCard(cards, find_card)
print("Index of desired card is ",result)