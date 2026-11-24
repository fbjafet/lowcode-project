from datetime import datetime, timezone
from email.utils import parseaddr
import re
import secrets
from flask import Flask, jsonify, request

app = Flask(__name__)

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)


def is_valid_email(value: str) -> bool:
    if len(value) > 254:
        return False
    _, parsed = parseaddr(value)
    return parsed == value and bool(EMAIL_REGEX.fullmatch(value))


@app.post("/hooks/signup")
def signup_webhook():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Request body must be a valid JSON object."}), 400

    required_fields = ("name", "email", "company")
    missing = [
        field
        for field in required_fields
        if not isinstance(payload.get(field), str) or not payload[field].strip()
    ]
    if missing:
        return jsonify(
            {"error": f"Missing or empty required field(s): {', '.join(missing)}"}
        ), 400

    email = payload["email"].strip()
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email address."}), 400

    date_part = datetime.now(timezone.utc).strftime("%Y%m%d")
    random_part = f"{secrets.randbelow(10000):04d}"
    reference = f"CB-{date_part}-{random_part}"

    return jsonify({"reference": reference}), 200