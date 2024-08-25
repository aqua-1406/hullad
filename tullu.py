from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

    if request.method == 'POST':
        data = request.json.get("data", [])
        numbers = []
        alphabets = []
        highest_alphabet = ""

        for item in data:
            if isinstance(item, (int, float)):  # Check if it's a number
                numbers.append(item)
            elif isinstance(item, str) and len(item) == 1 and not item.isdigit():
                alphabets.append(item)
                if not highest_alphabet or item.upper() > highest_alphabet.upper():
                    highest_alphabet = item

        return jsonify({
            "is_success": True,
            "user_id": "sanhita17",
            "email": "sanhita.kundu2020@vitstudent.ac.in",
            "roll_number": "20BEC0215",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }), 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)
