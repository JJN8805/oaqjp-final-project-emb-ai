from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask("Emotion Detector")


# Route to render the main HTML page
@app.route("/")
def render_index_page():
    return render_template('index.html')


# Route for emotion detection
@app.route("/emotionDetector")
def emo_detector():
    # Get input text from GET request
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detection function
    response = emotion_detector(text_to_analyze)

    # Extract values
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    # Handle invalid input
    if dominant is None:
        return "Invalid input! Please try again."

    # Format output EXACTLY as required
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)