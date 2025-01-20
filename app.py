from flask import Flask, jsonify
from helper import get_video_transcript
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app deployed on AWS Lambda!"})

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/get-transcript/<video_id>')
def get_transcript(video_id):
    for i in range(400000000):
        ...
    return jsonify({
        "asdf":"afg"
    })
    try:
        transcript = get_video_transcript(f"https://www.youtube.com/watch?v={video_id}")
        return jsonify({"transcript": transcript})
    except Exception as e:
        print(e)
        return jsonify({
            "error":True,
            "message":str(e)
        })
    
if __name__ == "__main__":
    app.run(debug=True)
