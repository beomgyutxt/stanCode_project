"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
The program can remove people from a series of photos
(amount >= 3) which were taken at the same place.

The program compares pixels in different photos and
calculates the color distance. The pixels with smallest
color distance ,which means no people,are adopted and
repaint on a new canvas.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixel_n = 0
    total_red = 0
    total_green = 0
    total_blue = 0
    for pixel in pixels:
        pixel_n += 1
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    rbg = [total_red/pixel_n, total_green/pixel_n, total_blue/pixel_n]
    return rbg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best_pixel = 0
    avg_r = get_average(pixels)[0]
    avg_g = get_average(pixels)[1]
    avg_b = get_average(pixels)[2]
    smallest_dist = 0
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_r, avg_g, avg_b)
        if smallest_dist == 0 or dist < smallest_dist:  # find pixel with smallest color distance
            smallest_dist = dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)          # blank
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):                             # position of a pixel (x, y)
        for y in range(height):
            p_list = []                                # pixels from different photos
            for i in range(len(images)):
                img = images[i]
                pixel = img.get_pixel(x, y)
                p_list.append(pixel)
            best = get_best_pixel(p_list)              # best pixel in these photos

            result_pixel = result.get_pixel(x, y)      # draw best pixels on a new canvas
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
