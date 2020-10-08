import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import transforms

def cv2_clipped_zoom(img, zoom_factor):
    import cv2
    import numpy as np
    """
    Center zoom in/out of the given image and returning an enlarged/shrinked view of 
    the image without changing dimensions
    Args:
        img : Image array
        zoom_factor : amount of zoom as a ratio (0 to Inf)
    """
    height, width = img.shape[:2] # It's also the final desired shape
    new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)

    ### Crop only the part that will remain in the result (more efficient)
    # Centered bbox of the final desired size in resized (larger/smaller) image coordinates
    y1, x1 = max(0, new_height - height) // 2, max(0, new_width - width) // 2
    y2, x2 = y1 + height, x1 + width
    bbox = np.array([y1,x1,y2,x2])
    # Map back to original image coordinates
    bbox = (bbox / zoom_factor).astype(np.int)
    y1, x1, y2, x2 = bbox
    cropped_img = img[y1:y2, x1:x2]

    # Handle padding when downscaling
    resize_height, resize_width = min(new_height, height), min(new_width, width)
    pad_height1, pad_width1 = (height - resize_height) // 2, (width - resize_width) //2
    pad_height2, pad_width2 = (height - resize_height) - pad_height1, (width - resize_width) - pad_width1
    pad_spec = [(pad_height1, pad_height2), (pad_width1, pad_width2)] + [(0,0)] * (img.ndim - 2)

    result = cv2.resize(cropped_img, (resize_width, resize_height))
    result = np.pad(result, pad_spec, mode='constant')
    assert result.shape[0] == height and result.shape[1] == width
    return result

# 1. plt.figimage
fig = plt.figure(figsize=(16,16))
img1 = img.imread("cost_37_100.png")
img1 = cv2_clipped_zoom(img1, 0.5)
img1 = img1[50:, 50:, 0]
trs = transforms.Affine2D().rotate_deg(45)
plt.figimage(img1, fig.bbox.xmax/2, fig.bbox.ymax/2, alpha= 0.5, cmap='Blues', transform = trs)
plt.show()

# 2. plt.imshow()
image1 = img.imread('cost_37_100.png')
fig = plt.figure(tight_layout=True)
grid = plt.GridSpec(6, 5, hspace=0.5)
plt.subplot(grid[0:4,0:4])
plt.imshow(image1)
plt.subplot(grid[4:6,0:2])
plt.imshow(image1)
plt.subplot(grid[4:6,2:4])
plt.imshow(image1)
plt.show()
