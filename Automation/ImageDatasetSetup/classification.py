# Imports
import shutil
import glob
import os
import fnmatch


class setupclass:
    """
    A class to set up a classification dataset.

    This class provides methods to rename image files, create directories,
    and split the data into training, validation, and test sets.

    Attributes:
        datapath (str): The path to the dataset directory.
        trainimgs (int): The number of images for the training set.
        valimgs (int): The number of images for the validation set.
        testimgs (int): The number of images for the test set.
    """

    def __init__(self, datapath):
        """
        Initializes the setupclass object.

        Args:
            datapath (str): The path to the dataset directory.
        """
        self.datapath = datapath
        self.trainimgs = 0
        self.valimgs = 0
        self.testimgs = 0

    @property
    def renamer(self):
        """
        Renames image files sequentially.
        """
        os.chdir(self.datapath)
        counter = 0
        inames = []

        # Get all jpg file names
        for file_name in os.listdir(self.datapath):
            if file_name.endswith(".jpg"):
                inames.append(file_name)

        # Rename files
        for nam in inames:
            print(f"Renaming {nam} to {counter + 1}.jpg")
            counter += 1
            os.rename(
                os.path.join(self.datapath, nam),
                os.path.join(self.datapath, f"{counter}.jpg"),
            )

    def directory_creator(self):
        """
        Creates the directory structure for train, validation, and test sets.
        """
        directory = rf"{self.datapath}"
        destinations = ["train/", "validation/", "test/"]
        for element in destinations:
            path = os.path.join(directory, element)
            os.makedirs(path, exist_ok=True)

    @property
    def splitter(self):
        """
        Splits the dataset into training, validation, and test sets.
        """
        directory = rf"{self.datapath}"
        train_dir = os.path.join(directory, "train/")
        val_dir = os.path.join(directory, "validation/")
        test_dir = os.path.join(directory, "test/")
        length = len(fnmatch.filter(os.listdir(directory), "*.jpg"))

        for fily in range(1, length + 1):
            image_path = os.path.join(directory, f"{fily}.jpg")
            if fily <= int(self.trainimgs):
                print(f"Moving {fily} to training set")
                shutil.move(image_path, train_dir)
            elif int(self.trainimgs) < fily <= (int(self.trainimgs) + int(self.valimgs)):
                print(f"Moving {fily} to validation set")
                shutil.move(image_path, val_dir)
            elif (int(self.trainimgs) + int(self.valimgs)) < fily <= (
                int(self.trainimgs) + int(self.valimgs) + int(self.testimgs)
            ):
                print(f"Moving {fily} to test set")
                shutil.move(image_path, test_dir)

    @splitter.setter
    def splitter(self, values):
        """
        Setter for the splitter attributes.

        Args:
            values (tuple): A tuple containing the number of images for
                            training, validation, and test sets.
        """
        self.trainimgs, self.valimgs, self.testimgs = values

