from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    return str(access_token), str(refresh)

# Then you can add your JWT settings to the `settings.py` like:
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your-secret-key',
}
