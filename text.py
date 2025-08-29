from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(item))   # ✅ ensure string
                else:
                    odd_numbers.append(str(item))    # ✅ ensure string
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        # alternating caps reverse string
        concat_string = ""
        letters = "".join([a for a in data if a.isalpha()])[::-1]
        for i, ch in enumerate(letters):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()

        # 🟢 Response (order maintained)
        response = {
            "is_success": True,
            "user_id": "maithili_gupta_13122003",
            "email": "maithili.gupta2022@vitstudent.ac.in",
            "roll_number": "22BEC0733",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return Response(
            json.dumps(response, indent=2, sort_keys=False),
            mimetype="application/json"
        )

    except Exception as e:
        error_response = {
            "is_success": False,
            "error": str(e)
        }
        return Response(
            json.dumps(error_response, indent=2, sort_keys=False),
            mimetype="application/json"
        )

if __name__ == "__main__":
    app.run(debug=True)
