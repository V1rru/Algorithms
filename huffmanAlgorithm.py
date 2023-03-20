from queue import PriorityQueue
import heapq

# Class that describes the node of the three
class Node:

    def __init__(self, frequency, character, leftNode = None, rightNode = None):
        self.frequency = frequency
        self.character = character
        self.leftNode = leftNode
        self.rightNode = rightNode

    def __lt__(self, next):
        return self.frequency < next.frequency


# class PriorityEntry(object):
#     def __init__(self, priority, data):
#         self.data = data
#         self.priority = priority

#     def __lt__(self, other):
#         return self.priority < other.priority
        

# Method creates a dictionary of each letter from the text
def createDictionaryOfLetters(text):
    
    # A dictionary for every letter in the text with amount of its entries
    lettersWithTheirAmount = dict()
    
    # Filling the dictionary with letters from the text
    for index in range(len(text)):

        if text[index] not in lettersWithTheirAmount:
            lettersWithTheirAmount[text[index]] = 0
        
        lettersWithTheirAmount[text[index]] = lettersWithTheirAmount.get(text[index], 0) + 1

    # Sorting the dictionary in reversed order
    lettersWithTheirAmount = {key: value for key, value in reversed(sorted(lettersWithTheirAmount.items(), key=lambda item: item[1]))}
    
    # Filling the priority queue with letters and their frequences
    nodesByPriority = heapq
    for element in range(len(list(lettersWithTheirAmount))):
        # nodesByPriority.put(lettersWithTheirAmount.get(element))
        heapq.heappush(nodesByPriority, Node())

    # print(nodesByPriority)
    print(list(lettersWithTheirAmount.items())[0][1])



def activateCoding():
    text = "text as example"
    createDictionaryOfLetters(text)

activateCoding()