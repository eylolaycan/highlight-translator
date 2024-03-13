import cv2
import numpy as np
import pytesseract
from pytesseract import Output
from oragearea import orange_area_coordinates
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Set the tesseract path in the script
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the image
image = cv2.imread('C:\\Users\\aycan\\OneDrive\\Belgeler\\projects\\image.jpg')

# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to recognize text from the image
d = pytesseract.image_to_data(gray, output_type=Output.DICT)

# Iterate over each word
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(f'Word: {d["text"][i]}, Coordinates: ({x}, {y}, {w}, {h})')

words_coordinates = []

for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(f'Word: {d["text"][i]}, Coordinates: ({x}, {y}, {w}, {h})')
        # Save the word and its coordinates to the list
        words_coordinates.append({'word': d["text"][i], 'coordinates': (x, y, w, h)})

# Initialize a variable to store the word
word_with_orange_box = None

# Iterate over the list of words and coordinates
for word_coordinate in words_coordinates:
    word = word_coordinate['word']
    (x, y, w, h) = word_coordinate['coordinates']
    
    # Check if the orange box's coordinates are inside the word's coordinates
    if (orange_area_coordinates[0] >= x and orange_area_coordinates[0] + orange_area_coordinates[2] <= x + w and orange_area_coordinates[1] >= y and orange_area_coordinates[1] + orange_area_coordinates[3] <= y + h):
        print(f'Orange box is inside the word "{word}".')
        word_with_orange_box = word
        break

# Translate the word
if word_with_orange_box is not None:
    translation = translator.translate(word_with_orange_box, dest='tr')
    print(f'The translation of "{word_with_orange_box}" is "{translation.text}".')
else:
    print('No word to translate.')

# Display the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the list of words and coordinates
#print(words_coordinates)