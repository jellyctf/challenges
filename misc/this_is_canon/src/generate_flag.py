# Source: https://favtutor.com/blogs/huffman-coding
# Huffman Coding in python
# Crosscheck with https://www.dcode.fr/huffman-tree-compression
from collections import Counter

def calculateHuffman(string):
    class NodeTree(object):
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

        def children(self):
            return self.left, self.right

        def __str__(self):
            return self.left, self.right


    def huffman_code_tree(node, binString=''):
        '''
        Function to find Huffman Code
        '''
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        d = dict()
        d.update(huffman_code_tree(l, binString + '0'))
        d.update(huffman_code_tree(r, binString + '1'))
        return d


    def make_tree(nodes):
        '''
        Function to make tree
        :param nodes: Nodes
        :return: Root of the tree
        '''
        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        return nodes[0][0]

    freq = dict(Counter(string))
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    return encoding

################################################################

FLAG = "jellyctf{jelly_your_homework_was_due_yesterday}".lower()

print(FLAG)
codebook = calculateHuffman(FLAG)
print("Original codebook: ", codebook)

"""
Canonical conversion: https://en.wikipedia.org/wiki/Canonical_Huffman_code
1. The first symbol in the list gets assigned a codeword which is the same length as the symbol's original codeword but all zeros. This will often be a single zero ('0').
2. Each subsequent symbol is assigned the next binary number in sequence, ensuring that following codes are always higher in value.
3. When you reach a longer codeword, then after incrementing, append zeros until the length of the new codeword is equal to the length of the old codeword. This can be thought of as a left shift.
"""

codebook = sorted(codebook.items(), key = lambda x : (len(x[1]), x[0]))
new_codebook = []
value = 0                               # Step 1
prev_length = len(codebook[0][1])

for char, original_code in codebook:
    length = len(original_code)

    # Step 3: After incrementing, append zero/left shift
    if prev_length != length:
        # Assumption of only 1 left shift here
        assert(length == prev_length + 1)
        value = value << 1

    codeword = f'{value:0{length}b}'
    print(char, codeword, value)
    new_codebook.append((char, codeword))

    # Step 2: Assign next binary number
    value += 1
    prev_length = length

new_codebook = dict(new_codebook)
print("Canonical codebook: ", new_codebook)

encoded_flag = ''
for char in FLAG:
    encoded_flag += new_codebook[char]

code_lengths = Counter([len(x) for x in new_codebook.values()])
print(code_lengths)

length_output = []
for n in range(1, max(code_lengths.keys()) + 1):
    if n not in code_lengths.keys():
        length_output.append('0')
    else:
        length_output.append(str(code_lengths[n]))
length_output = ",".join(length_output)

letters = ",".join(new_codebook.keys())

with open('flag.txt', 'w') as f:
    f.writelines([
        "(" + length_output + ")\n",
        "(" + letters + ")\n",
        encoded_flag])