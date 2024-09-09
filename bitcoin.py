from hashlib import sha256


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    nounce = 1
    prefix_str = '0' * prefix_zeros

    while True:
        text = str(block_number) + transactions + previous_hash + str(nounce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            return new_hash, nounce
        nounce += 1


if __name__ == '__main__':
    transactions = '''
    davil->bhavan->20,
    mando->rolex->45
    '''
    difficulty = 4
    previous_hash = '0000000x33fff365gfhdu77777fyw542gf'
    new_hash, nounce = mine(5, transactions, previous_hash, difficulty)
    print(f"New Hash: {new_hash}")
    print(f"Nounce: {nounce}")
