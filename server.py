"""
This module serves as the backend for an NLP Emotion Detection web application.
It provides routes for rendering the HTML page and detecting emotions using the 
emotion_detector function.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Ensure the file is present in the correct directory
app = Flask(__name__)
@app.route('/')
def index():
    """
    Serve the index.html file.
    Returns:
        Rendered HTML template for the main page.
    """
    return render_template('index.html')
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Detect emotions from the given text input and return the results in JSON format.
    Returns:
        JSON response with the emotions or an error message for invalid text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    response_message = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_message})
if __name__ == "__main__":
    app.run(debug=True)
