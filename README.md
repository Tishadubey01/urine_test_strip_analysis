# Urine Test Strip Analysis
## Overview
This project is a simple analysis of urine test strips. The test strips are used to detect the presence of various substances in urine. The test strips are dipped in urine and the color change is compared to a color chart. The color chart is used to determine the concentration of the substance in urine. The test strips are used to detect the presence of the following substances:
* Glucose
* Bilirubin
* Ketones
* Specific Gravity
* Blood
* pH
* Protein
* Urobilinogen
* Nitrite
* Leukocytes

Hence, each test strip has 10 different color patches. The color patches are compared to a color chart to determine the concentration of the substance in urine. 

## Objective
Created a web-interface to analyze the color patches on the test strip. The web-interface allows the user to upload an image of the test strip. The image is then processed to determine the color of each patch. It then returns the results of the analysis in the json format of RGB values. 

## Methodology
The image is uploaded using API. The API is created using Flask. The image is then processed using OpenCV. The image is converted to HSV format. The HSV format is used to determine the color of each patch. The RGB values of each patch are then returned in json format.

### Colour box detection
The boxes of each color are chosen based on image processing techniques such as contour detection and bounding rectangles.
By using contour detection and bounding rectangles, we can identify and extract the individual color boxes on the urine strip image, which allows us to analyze each color separately.
- The uploaded image is preprocessed by converting it to grayscale using cv2.cvtColor() function.

- A thresholding technique (cv2.threshold()) is applied to the grayscale image to obtain a binary image. This helps in segmenting the color regions from the background.

- Contours are detected using cv2.findContours() function on the binary image.Contours are the boundaries of the color regions.

- For each contour, a bounding rectangle is calculated using cv2.boundingRect(). This rectangle represents the area enclosing the color box.

- The bounding rectangle coordinates (x, y, width, height) are used to extract the color box from the original image using array slicing (img[y:y+h, x:x+w]).

- The average color of each box is calculated by taking the mean of each color channel (B, G, R) in the box using np.mean() function.

- The resulting RGB values are stored in the colors list.

## Installation
### Requirements
* Python 3.6
* Flask
* OpenCV
* Numpy

### Steps
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Run the flask
5. Navigate to the url

## Usage
### API
The API is created using Flask. The API is used to upload the image and return the results of the analysis.
#### Upload Image
POST request to upload the image. The image is uploaded using the key 'file'.
```
http://localhost:5000/upload
```



