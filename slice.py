from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import os

def getImage(window):
    """
    Open a file dialog to select an image, and return the path of the selected image.
    """
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName(window, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
    if fileName:
        print(f"Selected file: {fileName}")
        return fileName
    return None

def sliceImage(imagePath, numSlices, saveDir):
    """
    Slice the image into the specified number of slices horizontally (left to right) and save them in the specified directory.
    """
    if not imagePath or numSlices < 1:
        print("Invalid image path or number of slices")
        return

    if not saveDir:  # Ensure there's a save directory specified.
        print("No save directory specified")
        return

    try:
        img = Image.open(imagePath)
        imgWidth, imgHeight = img.size

        sliceWidth = imgWidth // numSlices
        for i in range(numSlices):
            box = (i * sliceWidth, 0, (i + 1) * sliceWidth if (i < numSlices - 1) else imgWidth, imgHeight)
            slice_img = img.crop(box)
            # Construct the file path using the save directory and slice index.
            slicePath = os.path.join(saveDir, f"horizontal_slice_{i}.png")
            slice_img.save(slicePath)
            print(f"Horizontal slice {i} saved to {slicePath}.")
    except Exception as e:
        print(f"Error slicing image: {e}")

