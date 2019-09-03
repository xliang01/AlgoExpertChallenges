def caesarCipherEncryptor(string, key):
    chars = list(string)
    offsetString = []
    
    for char in chars:
        ascii = ord(char) - ord("a")
        offset = (ascii + key) % 26
        offsetString.append(chr(offset + ord("a")))
    return ''.join(offsetString)

print(caesarCipherEncryptor("xyz", 2))