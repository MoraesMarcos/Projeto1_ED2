import random
import hashlib

class MinHash:
    def __init__(self, num_hashes=100):
        self.num_hashes = num_hashes
        self.seeds = self._generate_seeds()

    def _generate_seeds(self):
        random.seed(42)
        return [random.randint(0, 1e9) for _ in range(self.num_hashes)]

    def _hash(self, value, seed):
        value = value.encode('utf-8')
        return int(hashlib.sha256(value + str(seed).encode('utf-8')).hexdigest(), 16)

    def assinatura(self, shingles):
        assinatura = []
        for seed in self.seeds:
            hash_min = min([self._hash(shingle, seed) for shingle in shingles])
            assinatura.append(hash_min)
        return assinatura
