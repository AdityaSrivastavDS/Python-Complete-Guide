import cv2
import numpy as np
import pyautogui
from pyautogui import pyscreeze

from PIL import ImageGrab

# Capture screen using Pillow
def capture_screen():
    screenshot = ImageGrab.grab()
    screen_np = np.array(screenshot)
    frame = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)
    return frame


# Preprocess the image
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (84, 84))
    return resized

# Main loop
while True:
    screen = capture_screen()
    processed_image = preprocess_image(screen)

    # Object detection (example using template matching)
    template = cv2.imread('template_image.png', 0)
    res = cv2.matchTemplate(processed_image, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    w = template.shape[1]
    h = template.shape[0]
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow('Game', screen)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
