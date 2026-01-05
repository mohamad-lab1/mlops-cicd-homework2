from app.features import hash_feature

def test_hash_feature_range():
    result = hash_feature("mlops", 10)
    assert isinstance(result, int)
    assert 0 <= result < 10
