# Import necessary libraries
import numpy as np
import os
import cv2


def dataset(data_path):
    """
    Loads and preprocesses image data from a specified directory.

    This function assumes a directory structure where subdirectories of `data_path`
    are class labels (e.g., 'meningioma_tumor', 'no_tumor'). It reads all images,
    resizes them, normalizes the pixel values, and assigns class labels based on
    the directory they are in.

    Args:
        data_path (str): The path to the root directory of the dataset.

    Returns:
        tuple: A tuple containing two numpy arrays:
               - The first array holds the preprocessed image data.
               - The second array holds the corresponding class labels.
    """
    img_data_array = []
    class_name = []

    # Iterate through each class directory
    for dir1 in os.listdir(data_path):
        class_path = os.path.join(data_path, dir1)
        if not os.path.isdir(class_path):
            continue

        # Iterate through each image file in the class directory
        for file in os.listdir(class_path):
            image_path = os.path.join(class_path, file)

            # Read and preprocess the image
            image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
            if image is None:
                print(f"Warning: Could not read image {image_path}")
                continue

            image = cv2.resize(image, (64, 64))
            image = np.array(image)
            image = image.astype('float32')
            image /= 255.0  # Normalize pixel values to be between 0 and 1

            if len(image.shape) < 3:
                continue

            # Assign class labels based on the directory name
            if dir1 == "meningioma_tumor":
                img_data_array.append(image)
                class_name.append(1)
            elif dir1 == "no_tumor":
                img_data_array.append(image)
                class_name.append(0)

    # Convert lists to numpy arrays
    img_data_array = np.stack(img_data_array, axis=0)
    class_name = np.stack(class_name, axis=0)

    return img_data_array, class_name
