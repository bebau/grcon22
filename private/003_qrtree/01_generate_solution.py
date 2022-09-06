#!/usr/bin/env python3
'''wolfram rule 30 + QR'''
from PIL import Image
import numpy as np

HEIGHT, WIDTH = 107, 97
np.random.seed(seed=0xDEADBEEF+55000)

# load rule 30
rules = {
    0b111: 0,
    0b110: 0,
    0b101: 0,
    0b100: 1,
    0b011: 1,
    0b010: 1,
    0b001: 1,
    0b000: 0,
}

# seed background
bg = np.random.random((HEIGHT, WIDTH)) > .5
# bg = np.zeros((HEIGHT, WIDTH), dtype=bool)
# bg[0, 0] = True

for rdx in range(1, HEIGHT):
    for cdx in range(1, WIDTH-1):
        for key, value in rules.items():
            above = np.packbits(np.pad(bg[rdx-1, cdx-1: cdx+1], (5, 0)))
            if above == key:
                bg[rdx, cdx] = value

final = Image.fromarray(bg.astype(np.uint8)*255, mode='L').convert('1')
final.save('qr_bg.png')

# paste QR to center
with Image.open('qr.png') as img:
    x_offset = (WIDTH - img.size[0]) // 2
    y_offset = (HEIGHT - img.size[1]) // 2
    final.paste(img, (x_offset, y_offset))
    final.save('qr_padded.png')
    # npimg = np.asarray(final)
    # display(final)

print('done')