# Imports
import shutil
import glob
import os
import sys
import fnmatch


class setupclass:
    def __init__(self, datapath):
        self.datapath = datapath
        self.trainimgs = int()
        self.valimgs = int()
        self.testimgs = int()

    @property
    def renamer(self):
        ### to rename the annotations and images ###
        directory = os.chdir(f"{self.datapath}")
        counter = 0
        inames = []
        for file_name in os.listdir(directory):
            name, ext = os.path.splitext(file_name)
            if ext == ".jpg":
                inames.append(name)
                continue
        for nam in inames:
            print(nam)
            counter += 1
            os.rename(
                f"{self.datapath}" + nam + ".jpg",
                f"{self.datapath}" + str(counter) + ".jpg",
            )
    # create a train, test, and validation  directories for the dataset to be split into
    def directory_creator(self):
        directory = rf"{self.datapath}"
        destinations = ["train/", "validation/", "test/"]
        for element in destinations:
            path = os.path.join(directory, element)
            os.makedirs(path)

    @property
    def splitter(self):
        ### to split training and validation ###
        directory = rf"{self.datapath}"
        train_dir = f"{directory}train/"
        val_dir = f"{directory}validation/"
        test_dir = f"{directory}test/"
        length = len(fnmatch.filter(os.listdir(directory), "*.jpg"))
        for fily in range(1, length + 1):
            if fily <= int(self.trainimgs):
                print(fily)
                x = glob.glob(rf"{self.datapath}{fily}.jpg")[0]
                shutil.move(x, train_dir)
                continue
            elif (
                (int(self.valimgs) + int(self.trainimgs)) >= fily > int(self.trainimgs)
            ):
                print(fily)
                x = glob.glob(rf"{self.datapath}{fily}.jpg")[0]
                shutil.move(x, val_dir)
                continue
            elif (
                (int(self.testimgs) + int(self.valimgs) + int(self.trainimgs))
                >= fily
                > (int(self.valimgs) + int(self.trainimgs))
            ):
                print(fily)
                x = glob.glob(rf"{self.datapath}{fily}.jpg")[0]
                shutil.move(x, test_dir)
                continue

    @splitter.setter
    def splitter(self, trainimgs, valimgs, testimgs):
        self.trainimgs = trainimgs
        self.valimgs = valimgs
        self.testomgs = testimgs

