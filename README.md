# Brain Tumour Image Classification with PyTorch 🧠

This project uses PyTorch to classify brain tumour images using a custom CNN and transfer learning with ResNet18.

## Results
For the custom CNN, using very low epoch sizes and little hyperparameter tuning, accuracy was 71.83%. With data augmentiation e.g. rotations and colour jitter, accuracy increased to 84.41%. 

Using ResNet18 an accuracy of 100% was achieved.

## Dataset
Dataset has 155 images containing a tumour and 98 images without. Taken from: https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection/data