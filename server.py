'''
We'll use Flask to make our text classification pipelines accessible via HTTP protocol.
'''
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load in our text-classification pipelines
mlp_pipeline = joblib.load('mlp_pipeline.joblib')
nbayes_pipeline = joblib.load('nbayes_pipeline.joblib')

@app.route('/mlp/predict', methods=['POST'])
def mlp_predict():
    data = request.get_json()
    
    # Make sure the input is valid
    # Our JSON payload has this format {'text': input text}
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" key in request body'}), 400
    
    user_text = data['text']
    
    try:
        # Retrieve the prediction & confidence in the prediction 
        prediction = mlp_pipeline.predict([user_text])[0]
        probabilities = mlp_pipeline.predict_proba([user_text])[0]
        max_prob = float(max(probabilities))

        # Convert numpy types to native Python types
        if hasattr(prediction, 'item'):  
            prediction = prediction.item()

        if hasattr(max_prob, 'item'):  
            max_prob = max_prob.item()
        
        # Return the result as JSON
        return jsonify({
                        'text': user_text,
                        'prediction': prediction,
                        'confidence': max_prob
                        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/nbayes/predict', methods=['POST'])
def nbayes_predict():
    data = request.get_json()
    
    # Make sure the input is valid
    # Our JSON payload has this format {'text': input text}
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" key in request body'}), 400

    user_text = data['text']
    
    try:
        # Retrieve the prediction & confidence in the prediction 
        prediction = nbayes_pipeline.predict([user_text])[0]
        probabilities = nbayes_pipeline.predict_proba([user_text])[0]  
        max_prob = float(max(probabilities))

        # Convert numpy types to native Python types
        if hasattr(prediction, 'item'):  
            prediction = prediction.item()

        if hasattr(max_prob, 'item'):  
            max_prob = max_prob.item()
        
        # Return the result as JSON
        return jsonify({
                        'text': user_text,
                        'prediction': prediction,
                        'confidence': max_prob
                        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Debug mode allows us to update our server in real time
    app.run(host='0.0.0.0', port=5000, debug=True)
