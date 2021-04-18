import argparse
import os
import sys
import pathlib
from tqdm import tqdm

import PIL
from math import ceil
from PIL import Image


def arguments():
    parser = argparse.ArgumentParser(
        description="Bulk image resizer",
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )
    parser.add_argument(
        "folder",
        metavar="folder",
        type=str,
        nargs="?",
        help="directory of images that will be resized",
    )
    parser.add_argument(
        "-d",
        type=str,
        nargs="?",
        help="resize image by dimension, must be in W:H format",
    )
    parser.add_argument(
        "-o",
        type=str,
        nargs="?",
        default="resized/",
        help="directory output of saved resized bulk image",
    )
    parser.add_argument(
        "-q",
        type=int,
        nargs="?",
        default="50",
        help="set quality of resized image <1-100>, default is 50",
    )
    parser.add_argument(
        "-p",
        type=int,
        nargs="?",
        default=None,
        help="resize image by percentage <1-100>",
    )

    return parser.parse_args()

def main():
    args = arguments()

    if not args.p and not args.d:
        raise Exception(
            "You need to provide the dimensions you want to set, "
            "must be 'width:height' or 'percentage'"
        )

    # saved directory name
    savings_dir = args.o
    # directory of bulk images than need to be resized
    current_dir = (
        str(pathlib.Path(__file__).parent.absolute()) + "\\%s\\" % args.folder
    ).replace("\\", "/")

    # check if the path of the folder is full path directory <c:\users\...>
    # if true then applied it to the current_dir
    temp = (r"%s" % args.folder).replace("\\", "/")
    if os.path.isdir(temp):
        current_dir = "%s/" % temp

    # which will not raise an error if the `path` already exists and it
    # will recursively create the paths, if the preceding path doesn't exist
    maps = (r"%s" % args.o).split("\\")
    # excluded the last last foler, cuz that is the folder that will be created
    temp = "/".join(maps[:-1])
    # output image folder
    save = maps[-1]

    if os.path.isdir(temp):
        savings_dir = temp + "/%s/" % save
        os.makedirs("%s/%s" % (temp, save), exist_ok=True)
    else:
        os.makedirs(
            str(pathlib.Path(__file__).parent.absolute()) + "/%s/" % savings_dir,
            exist_ok=True,
        )

    list_directory = os.listdir(current_dir)
    len_ldirectory = len(list_directory)
    print(f"""
    Target Directory  : {args.folder}
    Target Output     : {args.o}
    Target Dimension  : {args.d}
    Target Percentage : {args.p}%
    Target Quality    : {args.q}/100 pixels
    """)

    for index in tqdm(range(len_ldirectory)):
        images = current_dir + list_directory[index]
        fl, ex = os.path.splitext(current_dir + list_directory[index])
        splits = (r"%s" % fl).split("/")

        img = Image.open(images)
        original_size = img.size

        if args.p:
            size = (
                ceil(original_size[0] * args.p / 100),
                ceil(original_size[1] * args.p / 100),
            )
        else:
            size = tuple(map(int, args.d.split(":")))

        file = savings_dir + splits[-1] + ex
        imgs = img.resize(size, PIL.Image.ANTIALIAS)
        imgs.save(file, quality=args.q)


if __name__ == "__main__":
    main()
