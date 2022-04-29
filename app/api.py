from flask import request, jsonify, Response


def get_prediction(prediction_service):
    query = request.args.get('query')
    prediction = {
        "label": "None",
        "score": "None",
        "elapsed_time": "None"
    }
    if query is not None:
        prediction = prediction_service.predict(query)

    return jsonify(prediction), 200, {"Access-Control-Allow-Origin": "*"}
