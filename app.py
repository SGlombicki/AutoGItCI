from flask import Flask, request, abort
import GitCommands
import hashlib
import hmac

app = Flask(__name__)
WEBHOOK_SECRET = 'password'  # Replace with your actual webhook secret

def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        abort(403, description="x-hub-signature-256 header is missing!")
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        abort(403, description="Request signatures didn't match!")

@app.route('/update', methods=['POST'])
def update():
    signature = request.headers.get('X-Hub-Signature-256')
    payload = request.data
    verify_signature(payload, WEBHOOK_SECRET, signature)
    GitCommands.gitChange()
    return 'Good'

if __name__ == '__main__':
    app.run()
