# key - func name, value : what it does
words = [{"word": "sha1", "meaning": "sha1"},
            {"word":"sha224", "meaning": "sha224"},
            {"word":"sha256", "meaning": "sha256"},
            {"word":"sha384", "meaning": "sha384"},
            {"word":"sha512", 'meaning': "sha512"},
            {"word":"blake2b", "meaning": "cryptographic hash function defined in RFC 7693"},
            {"word":"blake2s", "meaning": "cryptographic hash function defined in RFC 7693"},
            {"word":"md5", "meaning": "md5"},
            {"word":"sha3_224", "meaning": "sha3_224"},
            {"word":"sha3_256", "meaning": "sha3_256"},
            {'word':"sha3_384", "meaning": "sha3_384"},
            {"word":"sha3_512", "meaning": "sha3_512"},
            {"word":"shake_128", "meaning": "shake_128"},
            {"word":"shake_256", 'meaning': "shake_256"},
            {"word":"scrypt", "meaning": "The function provides scrypt password-based key derivation function as defined in RFC 7914"}]


def get_words() -> list[object]:
    return words
