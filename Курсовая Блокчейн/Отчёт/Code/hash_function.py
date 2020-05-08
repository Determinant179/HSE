def hasher(str_data):
    alphabet = []
    for i in range(48, 58):
        alphabet.append(chr(i))
    for i in range(65, 91):
        alphabet.append(chr(i))
    for i in range(97, 123):
        alphabet.append(chr(i))
        
    hash_sum = "primitive example of hash function by Pavel Travkin"
    result = ""

    if len(str_data) <= len(hash_sum):
        k = 0
        for i in range(len(str_data)):
            k += ord(str_data[i])
        if k % (26 * 2 + 10) == 0:
            k -= 1
        for i in range(len(hash_sum)):
            result += alphabet[(((ord(hash_sum[i]) & ord(str_data[i % len(str_data)])) * k) % (26 * 2 + 10))]

    else:
        k = 0
        for i in range(len(str_data) - len(hash_sum), len(str_data)):
            k += ord(str_data[i])
        if k % (26 * 2 + 10) == 0:
            k -= 1
        for i in range(len(hash_sum)):
            result += alphabet[(((ord(hash_sum[i]) & ord(str_data[i])) * k) % (26 * 2 + 10))]

    return result