# Gamma Correction Image Processing

This Python project utilizes OpenCV to demonstrate gamma correction techniques on an image. The following operations are performed:
1. **Read the input image**.
2. **Convert the image into grayscale**.
3. **Show the histogram** of the image.
4. **Modify the brightness** of the image using **gamma correction** with a random gamma value, using two methods:
   - **Using a lookup table (LUT)**.
   - **By modifying each pixel individually (without LUT)**.
5. **Compare the execution time** of both gamma correction methods.
6. **Show the histogram after processing** (both methods should produce the same histogram).

## Features

- Convert any image to grayscale.
- Modify image brightness using random gamma values.
- Apply gamma correction with two different methods and compare their execution times.
- Visualize and compare histograms before and after processing.
- Execution time tracking for performance analysis.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Matplotlib (`matplotlib`)
- NumPy (`numpy`)
