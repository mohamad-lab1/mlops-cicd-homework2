from app.features import hash_feature
from app.model import predict

def test_prediction_pipeline():
    feature = hash_feature("user_1", 50)
    result = predict(feature)
    assert result >= 0
