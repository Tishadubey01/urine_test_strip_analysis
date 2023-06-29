

from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image found in the request'}), 400
    
    image = request.files['image']
    
    # Perform image analysis using OpenCV
    # Load the image
    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    # Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Extract RGB values of color boxes
    colors = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        color_box = img[y:y+h, x:x+w]
        average_color = np.mean(np.mean(color_box, axis=0), axis=0)
        average_color = average_color.astype(int)
        colors.append(average_color.tolist())
    
    # Define the result dictionary
    result = {
        'URO': colors[0],
        'BIL': colors[1],
        'KET': colors[2],
        'BLD': colors[3],
        'PRO': colors[4],
        'NIT': colors[5],
        'LEU': colors[6],
        'GLU': colors[7],
        'SG': colors[8],
        'PH': colors[9]
    }
    
    # Return the result as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run()
