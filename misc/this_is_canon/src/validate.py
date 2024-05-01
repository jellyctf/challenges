with open('flag.txt', 'r') as f:
    lengths, symbols, data = [x.strip("\n") for x in f.readlines()]
    lengths = lengths.lstrip('(').rstrip(')').split(',')
    symbols = symbols.lstrip('(').rstrip(')').split(',')

def createCodebook(lengths, symbols):
    codebook = {}
    value = 0

    curr_length_idx = 0
    symbols_processed_at_current_length = 0
    
    for s in symbols:
        while (symbols_processed_at_current_length >= int(lengths[curr_length_idx])):
            symbols_processed_at_current_length = 0
            curr_length_idx += 1
            value = value << 1
            if curr_length_idx == len(lengths):
                break

        l = curr_length_idx + 1
        codeword = f'{value:0{l}b}'
        codebook[codeword] = s
        value += 1
        symbols_processed_at_current_length += 1

    return codebook

codebook = createCodebook(lengths, symbols)
print("Reconstructed codebook: ", codebook)

buff = ''
result = ''

for i in data:
    buff += i

    if (buff in codebook.keys()):
        result += codebook[buff]
        buff = ''

assert(buff == '')

print(result)
