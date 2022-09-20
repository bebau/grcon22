import numpy as np
import huffman

#import sigmf meta globals 
#there's a dict in there called 
import sigmf

handle = sigmf.sigmffile.fromfile('grcon22/tx_msg')
freqMap = handle.get_global_info()["freqMap"]

phantom_string = ""
for key in freqMap.keys():
    phantom_string += key*freqMap[key]

_, tree = huffman.Huffman_Encoding(phantom_string)

with open("grcon22/rx_msg.bin", mode='rb') as file:
    loadedbits = file.read()
bits = ''.join(format(byte, '01b') for byte in loadedbits)
decoding = huffman.Huffman_Decoding(bits[16::1056], tree)
print(decoding)
