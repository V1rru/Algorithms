import heapq

# Class that describes the node of the three
class Node:

    def __init__(self, frequency, character, leftNode = None, rightNode = None):
        self.frequency = frequency
        self.character = character
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.direction = ""

    def __lt__(self, next):
        return self.frequency < next.frequency

    def getCharacter(self):
        return self.character        


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
    nodesByPriority = []
    for element in range(len(list(lettersWithTheirAmount.items()))):
        heapq.heappush(nodesByPriority, Node(list(lettersWithTheirAmount.items())[element][1], list(lettersWithTheirAmount.items())[element][0]))

    # Do till there is more than one node in the queue
    while len(nodesByPriority) > 1:

        # Removing the two nodes of highest priority (lowest frequency) from the queue
        leftNode = heapq.heappop(nodesByPriority)
        rightNode = heapq.heappop(nodesByPriority)

        # Assigning directional values to these two nodes
        leftNode.direction = 0
        rightNode.direction = 1

        # Creating the parent node with its frequency consistion of the sum of its children frequencies
        parentNode = Node(leftNode.frequency + rightNode.frequency, leftNode.character + rightNode.character, leftNode, rightNode)

        # Adding the newest parent node to the priority queue
        heapq.heappush(nodesByPriority, parentNode)

    # Saving the root of the Huffman tree
    root = nodesByPriority[0]

    # Printing the code for each letter
    print("Huffman codes are:" + "\n")
    printNodes(nodesByPriority[0])


# Method that prints the Huffman code for each unique letter from the text
def printNodes(root, val=""):

 # Huffman code for current node
    newVal = val + str(root.direction)
 
    # If node is not an edge node then traverse inside it
    if (root.leftNode):
        printNodes(root.leftNode, newVal)
    if (root.rightNode):
        printNodes(root.rightNode, newVal)
 
    # If node is edge node then display its huffman code
    if (not root.leftNode and not root.rightNode):
        print(f"{root.character} = {newVal}")


# Method that is used to start building Huffman code tree
def activateCoding():
    text = "some kind of text that should be coded"
    createDictionaryOfLetters(text)


# Calling the start method
activateCoding()
