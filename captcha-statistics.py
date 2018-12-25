#!/usr/bin/python3

# A Script for simple captcha recognition through recursive statistical improvement

# NOTE: After un-noising an image, u can run tesseract right away,
# but that would destroy the whole statistics idea, right? :)

import sys

from PIL import Image
from os import stat

modifications = 0

def modify(original):
    global modifications
    f = original.split('.')[:-1]
    modified = f[0]
    for i in f[1:]: modified += '.' + i
    modifications += 1
    modified += '#modified-%d.png' % modifications
    return modified

def un_noise(image):
    # Hold a grayscale version
    img = Image.open(image).convert('L')
    matrix = img.load()
    # Remove borders
    for x in [0, img.width-1]:
        for y in range(0, img.height): matrix[x,y] = 255
    for y in [0, img.height-1]:
        for x in range(0, img.width): matrix[x, y] = 255
    # Threshold, Whiten non-Blacks
    for x in range(0, img.width):
        for y in range(0, img.height):
            if matrix[x, y] != 0: matrix[x, y] = 255
    # Remove salt, progressively
    c = stat(image).st_size
    s = c + 1
    while s > c:
        s = c
        for x in range(1, img.width-1):
            for y in range(1, img.height-1):
                # if at least 3 out of 4 adjacent pixels are white, whiten
                if matrix[x-1, y] + matrix[x+1, y] + matrix[x, y-1] + matrix[x, y+1] > 510:
                    matrix[x, y] = 255
        f = modify(image)
        img.save(f)
        c = stat(f).st_size
    print('Ran %d linear salt removal(s)!' % modifications)

# DEBUG STUFF
# def save_matrix(matrix, f, width, height):
#     with open(f, 'w') as o:
#         for x in range(0, width):
#             for y in range(0, height):
#                 o.write(str(matrix[x,y]) + ' ')
#             o.write('\n')

if __name__ == '__main__':
    #s = '/home/amr/captcha-research/captcha.png'
    s = sys.argv[1]
    print('Un-noising %s' % s)
    un_noise(s)
