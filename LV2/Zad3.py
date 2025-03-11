import cv2
import numpy as np

# Load the image
image = cv2.imread("C:\\Users\\domin\\OneDrive\\Desktop\\Strojno Ucenje\LV2\\tiger.png")  # Replace with 'tiger.png' if using another file

# a) Increase brightness
def increase_brightness(img, value=50):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.clip(v + value, 0, 255)
    bright_hsv = cv2.merge((h, s, v))
    bright_img = cv2.cvtColor(bright_hsv, cv2.COLOR_HSV2BGR)
    return bright_img

bright_image = increase_brightness(image)

# b) Rotate the image by 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# c) Mirror (flip) the image horizontally
mirrored_image = cv2.flip(image, 1)

# d) Reduce resolution by a factor of 10
scale_factor = 10
small_image = cv2.resize(image, (image.shape[1] // scale_factor, image.shape[0] // scale_factor))

# e) Display only the second quarter in width, keeping full height
black_background = np.zeros_like(image)
height, width, _ = image.shape
x_start, x_end = width // 4, width // 2  # Define the second quarter
black_background[:, x_start:x_end] = image[:, x_start:x_end]

# Display results
cv2.imshow("Brightened Image", bright_image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Mirrored Image", mirrored_image)
cv2.imshow("Reduced Resolution Image", small_image)
cv2.imshow("Quarter Width Image", black_background)

cv2.waitKey(0)
cv2.destroyAllWindows()
