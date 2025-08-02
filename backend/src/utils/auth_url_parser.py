import urllib

def generate_x_user_data(x_user_data, auth_date, signature, hash_value):
    return f"{x_user_data}&auth_date={auth_date}&signature={signature}&hash={hash_value}"

def extract_auth_params(full_query):
    decoded = urllib.parse.unquote(full_query)

    params = urllib.parse.parse_qs(decoded)

    auth_date = params.get('auth_date', [None])[0]
    signature = params.get('signature', [None])[0]
    hash_value = params.get('hash', [None])[0]

    return auth_date, signature, hash_value
