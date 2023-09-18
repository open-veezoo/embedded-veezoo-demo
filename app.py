from flask import Flask, render_template
import jwt
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Note: private_key should be a string in PEM format. It typically starts with
    # '-----BEGIN PRIVATE KEY-----' and ends with '-----END PRIVATE KEY-----'.
private_key = """INSERT PRIVATE KEY HERE"""

def generate_jwt(payload, private_key, expiration_minutes=30):
    headers = {
        "typ": "JWT",
        "alg": "RS256"
    }
    # "iat" (Issued At) claim
    iat = datetime.utcnow()
    # "exp" (Expiration Time) claim
    exp = iat + timedelta(minutes=expiration_minutes)
    # Update the payload with "iat" and "exp" claims
    payload.update({
        "iat": iat,
        "exp": exp,
    })
    # Generate JWT
    encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256", headers=headers)
    return encoded_jwt

@app.route('/')
def index():
    return render_template('index.html')


def Admin():
    jti = str(uuid.uuid1())
    a_payload = {
        # This is the ID for the tenant you configured in Veezoo Admin in a previous step
        "tenantId": "0",
        "jti": jti,
        # This is an ID for the user
        "sub": "AdminSub",
        "email": "anna@cozy.com",
        "firstName": "Anna",
        "lastName": "Ackermann",
    }
    jwt = generate_jwt(a_payload, private_key)
    veezoo_url = f"https://embedded-demo.app.veezoo.com?jwt={jwt}&embedded=true"
    return render_template('Admin.html', veezoo_url=veezoo_url)

@app.route('/Flavia.html')
def Flavia():
    # Your view logic for the blank page goes here
    jti = str(uuid.uuid1())
    f_payload = {
        # This is the ID for the tenant you configured in Veezoo Admin in a previous step
        "tenantId": "1",
        "jti": jti,
        # This is an ID for the user
        "sub": "FurSub",
        "email": "flavia@cozy.com",
        "firstName": "Flavia",
        "lastName": "Fisher",
    }
    jwt = generate_jwt(f_payload, private_key)
    veezoo_url = f"https://embedded-demo.app.veezoo.com?jwt={jwt}&embedded=true"
    return render_template('Flavia.html', veezoo_url=veezoo_url)

@app.route('/Tom.html')
def Tom():
    # Your view logic for the blank page goes here
    jti = str(uuid.uuid1())
    t_payload = {
        # This is the ID for the tenant you configured in Veezoo Admin in a previous step
        "tenantId": "3",
        "jti": jti,
        # This is an ID for the user
        "sub": "TechSub",
        "email": "tom@trendytech.com",
        "firstName": "Tom",
        "lastName": "Tucker",
    }
    jwt = generate_jwt(t_payload, private_key)
    veezoo_url = f"https://embedded-demo.app.veezoo.com?jwt={jwt}&embedded=true"
    return render_template('Tom.html', veezoo_url=veezoo_url)

@app.route('/Oliver.html')
def Oliver():
    # Your view logic for the blank page goes here
    jti = str(uuid.uuid1())
    t_payload = {
        # This is the ID for the tenant you configured in Veezoo Admin in a previous step
        "tenantId": "2",
        "jti": jti,
        # This is an ID for the user
        "sub": "OffSub",
        "email": "oliver@assistancetothemanager.com",
        "firstName": "Oliver",
        "lastName": "O'Neil",
    }
    jwt = generate_jwt(t_payload, private_key)
    veezoo_url = f"https://embedded-demo.app.veezoo.com?jwt={jwt}&embedded=true"
    return render_template('Oliver.html', veezoo_url=veezoo_url)

if __name__ == '__main__':
    app.run()

