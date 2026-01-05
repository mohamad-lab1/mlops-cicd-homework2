import time
import requests

time.sleep(5)

response = requests.get(
    "http://localhost:8000/predict?user_id=test_user"
)

assert response.status_code == 200
print("Smoke test passed")
