import hashlib


def hash_feature(value: str, num_buckets: int = 100) -> int:
    hashed = hashlib.md5(value.encode("utf-8")).hexdigest()
    return int(hashed, 16) % num_buckets
