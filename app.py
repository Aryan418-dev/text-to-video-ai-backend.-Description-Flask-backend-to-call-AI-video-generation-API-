from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
RUNWAY_API_KEY = "your_runwayml_api_key"  # Replace with your actual key

@app.route("/generate-video", methods=["POST"])
def generate_video():
    prompt = request.json.get("prompt")
    response = requests.post(
        "https://api.runwayml.com/v1/generate/video",
        headers={"Authorization": f"Bearer {RUNWAY_API_KEY}"},
        json={"prompt": prompt, "duration": 4, "resolution": "512x512"}
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()