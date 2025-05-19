from flask import Flask, request, render_template
from deepface import DeepFace
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            try:
                result = DeepFace.analyze(img_path=filepath, actions=['emotion'])[0]
                emotion = result['dominant_emotion']
                return render_template('result.html', image_path=filepath, emotion=emotion)
            except Exception as e:
                return f"Error: {str(e)}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
