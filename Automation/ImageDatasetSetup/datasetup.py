# Import necessary classes and modules
from obj_det import setup
from classification import setupclass
import sys


def main():
    """
    Main function to set up an image dataset for object detection or classification.

    This script takes user input to determine the dataset type and the specific
    setup function to execute. The path to the dataset directory should be
    provided as a command-line argument.
    """
    # Prompt the user to choose the dataset type
    x = input("Dataset type, one of (classification, obj_det): ")

    # Handle object detection dataset setup
    if x == "obj_det":
        try:
            # Initialize the setup object with the dataset path from command-line arguments
            sety = setup(sys.argv[1])
        except IndexError:
            # Exit if the dataset path is not provided
            sys.exit(
                "InputError: example usage: python DatasetSetup.py /data/set/directory/path/"
            )

        # Prompt the user to choose the function to perform
        fun = input(
            "Input function, one of (renamer, first_splitter, second_splitter, editor): "
        )

        # Create directories if a splitter function is chosen
        if fun == "first_splitter" or fun == "second_splitter":
            try:
                sety.directory_creator()
            except FileExistsError:
                pass  # Ignore if directories already exist

        # Get the number of training images if first_splitter is chosen
        if fun == "first_splitter":
            sety.first_counter = input("Type the number of training images: ")

        # Call the selected function
        getattr(sety, fun)

    # Handle classification dataset setup
    elif x == "classification":
        try:
            # Initialize the setupclass object with the dataset path from command-line arguments
            sety = setupclass(sys.argv[1])
        except IndexError:
            # Exit if the dataset path is not provided
            sys.exit(
                "InputError: example usage: python DatasetSetup.py /data/set/directory/path/"
            )

        # Prompt the user to choose the function to perform
        fun = input("Input function, one of (renamer, splitter): ")

        # Create directories and get split numbers if splitter is chosen
        if fun == "splitter":
            try:
                sety.directory_creator()
            except FileExistsError:
                pass  # Ignore if directories already exist

            # Get the number of images for train, validation, and test sets
            sety.trainimgs, sety.valimgs, sety.testimgs = input(
                "Type the number of splits images (e.g., '100 50 50'): "
            ).split()

        # Call the selected function
        getattr(sety, fun)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
