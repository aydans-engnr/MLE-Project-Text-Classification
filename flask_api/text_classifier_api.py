'''
We'll build a Python-based API to access our text classification pipelines.
'''
import json
import requests

class TextClassifier:

    def mlp_predict(payload):
        '''Provide access to the mlp pipeline'''
        mlp_endpoint = "http://127.0.0.1:5000/mlp/predict"
        mlp_response = requests.post(mlp_endpoint, json=payload)

        if mlp_response.status_code == 200:
            pretty_json = json.dumps(mlp_response.json(), indent=4, sort_keys=True)
            return pretty_json
        else:
            return f"Status Code: {mlp_response.status_code}"

    def nbayes_predict(payload):
        '''Provide access to the nbayes pipeline'''
        nbayes_endpoint = "http://127.0.0.1:5000/nbayes/predict"
        nbayes_response = requests.post(nbayes_endpoint, json=payload)

        if nbayes_response.status_code == 200:
            pretty_json = json.dumps(nbayes_response.json(), indent=4, sort_keys=True)
            return pretty_json
        else:
            return f"Status Code: {nbayes_response.status_code}"


if __name__ == "__main__":

    payload = {'text': "This is the best product ever!!"}
    
    # Test the mlp_predict method
    print(TextClassifier.mlp_predict(payload))

    print()

    # Test the nbayes_predict method
    print(TextClassifier.nbayes_predict(payload))