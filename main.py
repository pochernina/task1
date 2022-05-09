from PIL import Image
import argparse
import numpy as np

parser = argparse.ArgumentParser(description = 'Image processing tool')
parser.add_argument('command', type = str, choices = ['mirror', 'extract', 'rotate', 'autorotate'])
parser.add_argument('parameters', nargs = '*')
parser.add_argument('input_file', type = str)
parser.add_argument('output_file', type = str)
args = parser.parse_args()

im = Image.open(args.input_file)
if args.command == 'mirror':
    if args.parameters[0] == 'h':
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    elif args.parameters[0] == 'v':
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif args.parameters[0] == 'd':
        im = im.transpose(Image.FLIP_TOP_BOTTOM).rotate(-90, expand = 1)
    elif args.parameters[0] == 'cd':
        im = im.transpose(Image.FLIP_TOP_BOTTOM).rotate(90, expand = 1)

elif args.command == 'extract':
    left_x = int(args.parameters[0])
    top_y = int(args.parameters[1])
    width = int(args.parameters[2])
    height = int(args.parameters[3])
    area = (left_x, top_y, left_x + width, top_y + height)
    im = im.crop(area)

elif args.command == 'rotate':
    angle = int(args.parameters[1])
    if args.parameters[0] == 'cw':
        angle = - angle
    im = im.rotate(angle, expand = 1)

else:
    max_i, max_inten = 0, 0
    im = im.convert("L")
    for i in range(4):
        inten1, inten2 = 0, 0 
        arr = np.array(im)
        len = np.size(arr) // np.size(arr[0])
        for j in range(0, len // 2):
            for elem in arr[j]:
                inten1 += elem
        for k in range(len // 2, len):
            for elem in arr[k]:
                inten2 += elem
        if inten1 - inten2 > max_inten:
            max_inten = inten1 - inten2
            max_i = i
        im = im.rotate(90, expand = 1)
    im = im.rotate(90 * max_i, expand = 1)

im.save(args.output_file)