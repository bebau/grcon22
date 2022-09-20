'''File to encrypt and then decrypt Gort's message'''

import numpy as np

msg = 'my name is Gort the Evil. i have a very important message for you. i am a fearsome presence. i have planted a bomb at an undisclosed but important location. there is no way to stop me. i am just letting you know.'

# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

codes = dict()

def Calculate_Codes(node, val=''):
    '''A helper function to print the codes of symbols by traveling Huffman Tree'''
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


def Calculate_Probability(data):
    '''A helper function to calculate the probabilities of symbols in given data'''
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


def Output_Encoded(data, coding):
    '''A helper function to obtain the encoded output'''
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def Total_Gain(data, coding):
    '''A helper function to calculate the space difference between compressed and non compressed data'''
    before_compression = len(data) * 8 # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):",  after_compression)

def Huffman_Encoding(data):
    nodes = []
    symbol_with_probs = Calculate_Probability(data)
    print(symbol_with_probs)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)



    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0]


def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string

encoding, tree = Huffman_Encoding(msg)

"""
'm': 10, 'y': 5, ' ': 42, 'n': 11, 'a': 17, 'e': 18, 'i': 12, 's': 10, 'G': 1, 'o': 15, 'r': 8, 't': 16, 'h': 4, 'E': 1, 'v': 4, 'l': 5, '.': 6, 'p': 5, 'g': 2, 'f': 2, 'u': 5, 'c': 3, 'd': 3, 'b': 3, 'w': 2, 'j': 1, 'k': 1}
symbols:  dict_keys(['m', 'y', ' ', 'n', 'a', 'e', 'i', 's', 'G', 'o', 'r', 't', 'h', 'E', 'v', 'l', '.', 'p', 'g', 'f', 'u', 'c', 'd', 'b', 'w', 'j', 'k'])
probabilities:  dict_values([10, 5, 42, 11, 17, 18, 12, 10, 1, 15, 8, 16, 4, 1, 4, 5, 6, 5, 2, 2, 5, 3, 3, 3, 2, 1, 1])
symbols with codes {'s': '00000', 'm': '00001', 'e': '0001', 'a': '0010', 'E': '00110000', 'G': '00110001', 'w': '0011001', 'f': '0011010', 'g': '0011011', 'v': '001110', 'h': '001111', 't': '0100', 'o': '0101', 'r': '01100', 'b': '011010', 'd': '011011', 'i': '0111', '.': '10000', 'c': '100010', 'k': '1000110', 'j': '1000111', 'n': '1001', 'u': '10100', 'p': '10101', 'l': '10110', 'y': '10111', ' ': '11'}
Space usage before compression (in bits): 1696
Space usage after compression (in bits): 884
"""


"""SHOULD GET:
('00001101111110010010000010001110111000001100110001010101100010011010000111100011100110000001110011110110100001101111100111100100011100001110010110011100001011001011111011100001101010101011000100001010010100110000100010000000000001000110110001110011010010101100111011101011010010000110111110010000011100101100110100001001001100000000101000010001111010101100000100000000110011000100001100001101111100111100100011100001111010110110001010010100000101101111001011011010010100001011010110010010011001010011110100100101101101110000010001010110010100000000101101111011010101000100110111000011010101010110001000010100101001110110010110001000100100011101011001100001101000011110001011000001110111000001110010101110011001001010111110100010111000000100010110101110000100011000011011111001000001111000111101000000001001110110000101000100011110010011011111011101011010011100011010010101001100110000',
 <Huffman_Encoding.huffman.Node at 0x7f87b29ad480>)
 """

s = b'00001101111110010010000010001110111000001100110001010101100010011010000111100011100110000001110011110110100001101111100111100100011100001110010110011100001011001011111011100001101010101011000100001010010100110000100010000000000001000110110001110011010010101100111011101011010010000110111110010000011100101100110100001001001100000000101000010001111010101100000100000000110011000100001100001101111100111100100011100001111010110110001010010100000101101111001011011010010100001011010110010010011001010011110100100101101101110000010001010110010100000000101101111011010101000100110111000011010101010110001000010100101001110110010110001000100100011101011001100001101000011110001011000001110111000001110010101110011001001010111110100010111000000100010110101110000100011000011011111001000001111000111101000000001001110110000101000100011110010011011111011101011010011100011010010101001100110000'

def array_of_bits(s):
    a = np.zeros(len(s))
    for i, c in enumerate(s):
        #print(c)
        if c == 49:
            a[i] = 1

    return a

### DO GNURADIO STUFF WITH THE FILE USING THE EXAMPLE FSK FLOWGRAPH

decoding = Huffman_Decoding(encoding, tree)