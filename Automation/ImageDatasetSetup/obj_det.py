import shutil
import glob
import os
import xml.etree.ElementTree as ET
import sys
import fnmatch


class setup:
    """
    A class to set up an object detection dataset.

    This class provides methods to rename files, create directories, split data,
    and edit XML annotation files.

    Attributes:
        datapath (str): The path to the dataset directory.
        first_counter (int): The number of images to be used for training.
    """

    def __init__(self, datapath):
        """
        Initializes the setup object.

        Args:
            datapath (str): The path to the dataset directory.
        """
        self.datapath = datapath
        self.first_counter = int()

    @property
    def renamer(self):
        """
        Renames images and their corresponding XML annotation files sequentially.
        """
        directory = os.chdir(f"{self.datapath}")
        inames = []
        anames = []
        counter = 0

        # Separate image and annotation file names
        for file_name in os.listdir(directory):
            name, ext = os.path.splitext(file_name)
            if ext == ".jpg":
                inames.append(name)
            elif ext == ".xml":
                anames.append(name)

        # Rename files
        for image_name in inames:
            counter += 1
            for excel_name in anames:
                if image_name == excel_name:
                    print(f"Renaming {image_name} to {counter}")
                    os.rename(
                        os.path.join(self.datapath, f"{image_name}.jpg"),
                        os.path.join(self.datapath, f"{counter}.jpg"),
                    )
                    os.rename(
                        os.path.join(self.datapath, f"{image_name}.xml"),
                        os.path.join(self.datapath, f"{counter}.xml"),
                    )

    def directory_creator(self):
        """
        Creates the directory structure for training and validation sets.
        """
        directory = rf"{self.datapath}"
        destinations = [
            "train/images/",
            "train/annotations/",
            "validation/images/",
            "validation/annotations/",
        ]
        for element in destinations:
            path = os.path.join(directory, element)
            os.makedirs(path, exist_ok=True)

    @property
    def first_splitter(self):
        """
        Splits the dataset into training and validation sets based on first_counter.
        """
        directory = rf"{self.datapath}"
        train_dir = os.path.join(directory, "train/")
        val_dir = os.path.join(directory, "validation/")
        length = len(fnmatch.filter(os.listdir(directory), "*.jpg"))

        for fily in range(1, length + 1):
            image_path = os.path.join(directory, f"{fily}.jpg")
            xml_path = os.path.join(directory, f"{fily}.xml")

            if fily <= int(self.first_counter):
                print(f"Moving {fily} to training set")
                shutil.move(image_path, train_dir)
                shutil.move(xml_path, train_dir)
            else:
                print(f"Moving {fily} to validation set")
                shutil.move(image_path, val_dir)
                shutil.move(xml_path, val_dir)

    @first_splitter.setter
    def first_splitter(self, first_counter):
        """
        Setter for the first_counter attribute.

        Args:
            first_counter (int): The number of training images.
        """
        self.first_counter = first_counter

    @property
    def second_splitter(self):
        """
        Moves images and annotations into their respective subdirectories.
        """
        destinations = {
            "train/images/": "train/*.jpg",
            "train/annotations/": "train/*.xml",
            "validation/images/": "validation/*.jpg",
            "validation/annotations/": "validation/*.xml",
        }

        for dest, pattern in destinations.items():
            dest_dir = os.path.join(self.datapath, dest)
            for file in glob.glob(os.path.join(self.datapath, pattern)):
                shutil.move(file, dest_dir)

    @property
    def editor(self):
        """
        Edits the XML annotation files to update the filename and path fields.

        Note: This method is a draft and may require adjustments.
        """
        dir = sys.argv[1]
        for file in os.listdir(dir):
            if file.endswith(".xml"):
                name2, _ = os.path.splitext(file)
                tree = ET.parse(os.path.join(dir, file))
                root = tree.getroot()

                filename_node = root.find("filename")
                if filename_node is not None:
                    filename_node.text = f"{name2}.jpg"

                path_node = root.find("path")
                if path_node is not None:
                    path_node.text = os.path.join(dir, f"{name2}.jpg")

                tree.write(os.path.join(dir, file))
