from flask import Flask, request, jsonify
from minigroqqle import MiniGroqqle

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    searcher = MiniGroqqle(num_results=5)
    results = searcher.search(query, json_output=True)
    return results

if __name__ == '__main__':
    app.run(debug=True)
