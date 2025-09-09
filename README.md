# Project Showcase

This repository contains a collection of projects and code samples that demonstrate my skills in various programming languages and domains. Each directory in this repository represents a distinct project or experiment.

## Directories

### 1. Automation

This directory contains a Python tool for automating the setup of image datasets for machine learning tasks. It can handle both image classification and object detection datasets.

**Features:**

*   **Rename images and annotations:** Sequentially renames all image and annotation files in a directory.
*   **Split datasets:** Splits the data into training, validation, and (for classification) test sets.
*   **Create directory structure:** Automatically creates the necessary subdirectories for the split datasets.
*   **Edit annotation files:** For object detection, it updates the XML annotation files to reflect the new file names.

**How to use:**

1.  Navigate to the `Automation/ImageDatasetSetup` directory.
2.  Run the `datasetup.py` script from the command line:
    ```bash
    python datasetup.py /path/to/your/dataset
    ```
3.  The script will prompt you to choose the dataset type (`classification` or `obj_det`) and the function you want to perform.

### 2. C

This directory contains a simple expense tracker program written in C. It's a command-line application that allows you to record your monthly budget and track your withdrawals. The transaction data is saved in a CSV file named `month.csv`.

### 3. Capsa_experience

This directory showcases my experience with the `capsa-lite` wrappers for building deep learning models. It includes:

*   A Python script (`array_dataset.py`) for loading and preprocessing image data.
*   A Jupyter notebook (`Capsa_Copy_of_Train&Test.ipynb`) that demonstrates the training and testing of a model built with `capsa-lite`.

For more information about `capsa-lite`, please visit the official repository: [https://github.com/themis-ai/capsa](https://github.com/themis-ai/capsa)

### 4. Regression

This directory contains a Python script that demonstrates simple polynomial curve fitting using the `numpy` and `matplotlib` libraries. The script fits a 2nd-degree polynomial to a small dataset and then visualizes the result.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.