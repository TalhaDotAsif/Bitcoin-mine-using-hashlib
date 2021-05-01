import hashlib


NONCE_LIMIT=100000000000

zeroes = 4

def mine(block_number,transactions,previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try=hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash with Nonce:{nonce}")
            return hash_try

    return -1

block_number = 24
transactions = "294893jcdj3921"
previous_hash = "3rmkmr43e23c31"

#combined_text = str(block_number) + transactions + previous_hash
#print(hashlib.sha256(combined_text.encode()).hexdigest())
mine(block_number,transactions,previous_hash)