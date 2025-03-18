# Streamified

Apparently I'm supposed to scan this or something... but I don't really get it.

by Caleb (@eden.caleb.a on discord)

---
The challenge provied a text file named `bitstring.txt`

Opened the file, I got a `binary` string with `625 bits`.  
As the description mentioned - "it supposed to **scan** this", may be this binary string is a `QR code` or Bar code

And due to the total size is `625 bits`, the result could be a `25x25` QR code

# Solution

Let's write a really simple Python script that takes the binary string and converts it into a 25x25 black-and-white image, then saves that image

```Python
from PIL import Image
import numpy as np

obf = '1111111000011110101111111100000100110101100100000110111010110110111010111011011101010101001101011101101110101001010010101110110000010100101111010000011111111010101010101111111000000001011110100000000010111110001110110011111000111010101100000010100000100011110111100101110111100000100001010100010000011000001000000001011011111100010001010111011100011010100010101001111100110111011100001001100110000011100001100110101011111111100000000110000001000110101111111001111001101010011100000101101001010001000010111010111100011111111011011101011001110011010011101110101010011110010010110000010011011001011100011111111010101010000010111'

width = 25
height = 25

img_pixels = np.zeros([25, 25])

for line_nr in range(25):
    start = line_nr * width
    stop = (line_nr + 1) * width
    line = obf[start:stop]
    for pixel_nr, pixel in enumerate(line):
            if pixel == '1':
                img_pixels[line_nr][pixel_nr] = 255
            elif pixel == '0':
                img_pixels[line_nr][pixel_nr] = 0
img = Image.fromarray(img_pixels.astype('uint8'))
img.save('qrcoder.png')
```

After executed the script, I got a really beautiful QR code 😍

![QR code contains flag](\image\qrcoder.png)

# Flag
Scanned the QR code, got the flag `utflag{b!t_by_b!t}`
