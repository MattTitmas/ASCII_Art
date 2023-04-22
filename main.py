import argparse

import numpy as np
import cv2

ascii_chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.            '


def main(image_location: str, output_location: str) -> None:
    image = cv2.imread(image_location)
    ratio = 800 / image.shape[1]
    image = cv2.resize(image, (int(image.shape[1] * ratio), int(image.shape[0] * 0.33 * ratio)))
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_scale = np.floor(gray_scale * ((len(ascii_chars)-1) / 255)).astype(int)
    toWrite = ''
    for i in range(0, len(gray_scale)):
        for j in range(0, len(gray_scale[i])):
            toWrite += ascii_chars[(len(ascii_chars) - 1) - gray_scale[i][j]]
        toWrite += '\n'

    with open(output_location, 'w') as f:
        f.write(toWrite)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert an image to ASCII")
    parser.add_argument('-i', '--image', required=True, type=str,
                        help='Image location.')
    parser.add_argument('-o', '--output', required=False, default='ASCII_art.txt',
                        help='Output location. (default=ASCII_art.txt')
    args = parser.parse_args()
    main(args.image, args.output)
