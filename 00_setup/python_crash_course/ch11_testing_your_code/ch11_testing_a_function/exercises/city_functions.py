from __future__ import annotations

def encode_with_length(s: str) -> str:
    """
    Encodes a string as: "<len>:<string>"
    Let's make concatenation injective (uniquely decodable).
    """
    s = s.strip()
    return f"{len(s)}:{s}"


def city_country_injective(city: str, country: str) -> str:
    """
    Injective pairing:
        f(city, country) = Enc(city) + '|' + Enc(country)
    Different (city, country) pairs will not collide, even if strings contain commas, pipes, etc.
    """
    return f"{encode_with_length(city)}|{encode_with_length(country)}"


# --- Decode (to prove unique decodability / injectivity) ---

def _decode_one(encoded: str, start: int = 0) -> tuple[str, int]:
    """
    Decodes one length-prefixed chunk starting at 'start'.
    Returns (decoded_string, next_index).
    """
    colon = encoded.find(":", start)
    if colon == -1:
        raise ValueError("Invalid encoding: missing ':'")

    length_str = encoded[start:colon]
    if not length_str.isdigit():
        raise ValueError("Invalid encoding: length is not a number")

    n = int(length_str)
    chunk_start = colon + 1
    chunk_end = chunk_start + n

    if chunk_end > len(encoded):
        raise ValueError("Invalid encoding: chunk length exceeds input size")

    return encoded[chunk_start:chunk_end], chunk_end

def decode_city_country_injective(encoded: str) -> tuple[str, str]:
    """
    Decodes the injective encoding back into (city, country).
    Format: "<len>:<city>|<len>:<country>"
    """
    city, i = _decode_one(encoded, 0)

    if i >= len(encoded) or encoded[i] != "|":
        raise ValueError("Invalid encoding: missing '|' separator after city")
    i += 1  # skip '|'

    country, j = _decode_one(encoded, i)

    if j != len(encoded):
        raise ValueError("Invalid encoding: extra trailing data")

    return city, country

if __name__ == "__main__":
    x = city_country_injective("Rio de Janeiro", "Brazil")
    print(x)  # 14:Rio de Janeiro|5:Brasil

    print(decode_city_country_injective(x))  # ('Rio de Janeiro', 'Brazil')
    #Keep it safe
    y = city_country_injective("A|B", "C, D")
    print(y)
    print(decode_city_country_injective(y))