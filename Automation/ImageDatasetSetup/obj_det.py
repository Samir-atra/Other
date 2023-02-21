import shutil
import glob
import os
import xml.etree.ElementTree as ET
import sys
import fnmatch


class setup:
    def __init__(self, datapath):
        self.datapath = datapath
        self.first_counter = int()

    @property
    def renamer(self):
        ### to rename the annotations and images ###
        directory = os.chdir(f"{self.datapath}")
        inames = []
        anames = []
        counter = 0
        for file_name in os.listdir(directory):
            name, ext = os.path.splitext(file_name)
            if ext == ".jpg":
                inames.append(name)
                continue
            elif ext == ".xml":
                anames.append(name)
                continue
        for image_name in inames:
            counter += 1
            for excel_name in anames:
                if image_name == excel_name:
                    print(counter)
                    os.rename(
                        f"{self.datapath}" + image_name + ".jpg",
                        f"{self.datapath}" + str(counter) + ".jpg",
                    )
                    os.rename(
                        f"{self.datapath}" + image_name + ".xml",
                        f"{self.datapath}" + str(counter) + ".xml",
                    )

    def directory_creator(self):
        directory = rf"{self.datapath}"
        destinations = [
            "train/images/",
            "train/annotations/",
            "validation/images/",
            "validation/annotations/",
        ]
        for element in destinations:
            path = os.path.join(directory, element)
            os.makedirs(path)

    @property
    def first_splitter(self):
        ### to split training and validation ###
        directory = rf"{self.datapath}"
        dir = f"{directory}train/"
        dic = f"{directory}validation/"
        length = len(fnmatch.filter(os.listdir(directory), "*.jpg"))
        for fily in range(1, length + 1):
            if fily <= int(self.first_counter):
                print(fily)
                x = glob.glob(rf"{self.datapath}{fily}.jpg")[0]
                shutil.move(x, dir)
                y = glob.glob(rf"{self.datapath}{fily}.xml")[0]
                shutil.move(y, dir)
                continue
            elif fily > int(self.first_counter):
                print(fily)
                x = glob.glob(rf"{self.datapath}{fily}.jpg")[0]
                shutil.move(x, dic)
                y = glob.glob(rf"{self.datapath}{fily}.xml")[0]
                shutil.move(y, dic)
                continue

    @first_splitter.setter
    def first_splitter(self, first_counter):
        self.first_counter = first_counter

    @property
    def second_splitter(self):
        ### to split annotations from images ###
        destinations = [
            "train/images/",
            "train/annotations/",
            "validation/images/",
            "validation/annotations/",
        ]
        files = ["train/*.jpg", "train/*.xml", "validation/*.jpg", "validation/*.xml"]
        for num in range(len(destinations)):
            dest_dir = f"{self.datapath}{destinations[num]}"
            for file in glob.glob(rf"{self.datapath}{files[num]}"):
                shutil.move(file, dest_dir)

    @property
    def editor(self):
        ### to edit the xml files ### just a draft #####
        dir = sys.argv[1]
        for file in os.listdir(dir):
            name2, ext2 = os.path.splitext(file)
            tree = ET.parse(dir + str(name2) + ".xml")
            root = tree.getroot()
            child1 = root.findall("filename")[0]
            child2 = root.findall("path")[0]
            child1.text = str(name2 + ".jpg")
            child2.text = str(name2 + ".jpg")
            tree.write(dir + file)
