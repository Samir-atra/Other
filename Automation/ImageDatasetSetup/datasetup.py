from obj_det import setup
from classification import setupclass
import sys


def main():
    x = input("Dataset type, one of (classification, obj_det): ")

    if x == "obj_det":
        try:
            sety = setup(sys.argv[1])
        except IndexError:
            sys.exit(
                "InputError:example usage: python DatasetSetup.py /data/set/directory/path/"
            )
        fun = input(
            "Input function, one of (renamer, first_splitter, second_splitter, editor): "
        )
        if fun == "first_splitter" or fun == "second_splitter":
            try:
                sety.directory_creator()
            except FileExistsError:
                pass
        if fun == "first_splitter":
            sety.first_counter = input("Type the number of training images: ")
        getattr(sety, fun)
    elif x == "classification":
        try:
            sety = setupclass(sys.argv[1])
        except IndexError:
            sys.exit(
                "InputError:example usage: python DatasetSetup.py /data/set/directory/path/"
            )
        fun = input("Input function, one of (renamer, splitter): ")
        if fun == "splitter":
            try:
                sety.directory_creator()
            except FileExistsError:
                pass
            sety.trainimgs, sety.valimgs, sety.testimgs = input(
                "Type the number of splits images: "
            ).split()
        getattr(sety, fun)


if __name__ == "__main__":
    main()
