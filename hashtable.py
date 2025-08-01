class KeyNotFoundError(Exception):
    """Raised when a key is not found in the hash table."""
    pass

#Define class for HashMap
class HashMap:

#Define hashtable capacity
    def __init__(self, capacity: int = 40):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]

#Define hash key based on capacity
    def _hash(self, key: int) -> int:
        return hash(key) % self.capacity

#Define insert funtion to insert into hashtable based on key-value
    def insert(self, key: int, value: object) -> None:
        bucket = self.buckets[self._hash(key)]
        for idx, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

#Define lookup function that returns value from hashtable based on key-value
    def lookup(self, key: int) -> object:
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return None

#Define remove function that item from hashtable based on key-value
    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                return
            #Error check that passess to KeyNotFoundError if key-value is not found
        raise KeyNotFoundError(f"Key {key} not found.")

#Define return string from hashtable
    def __str__(self):
        return str([bucket for bucket in self.buckets if bucket])
