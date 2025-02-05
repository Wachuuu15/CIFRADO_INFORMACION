def text_to_binary(text):
    #  ASCII y binario de 8 bits
    binary = ''
    for char in text:
        ascii_value = ord(char)
        binary_value = ''
        for i in range(8):
            binary_value = str(ascii_value % 2) + binary_value
            ascii_value //= 2
        binary += binary_value + ' '
    return binary.strip()

def base64_to_binary(b64_text):
    # Tabla de codificación Base64
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    binary = ''
    padding = b64_text.count('=')
    b64_text = b64_text.rstrip('=')
    
    # BASE64 a BINARIO
    value = 0
    bits = 0
    for char in b64_text:
        value = (value << 6) | base64_chars.index(char)
        bits += 6
        
        while bits >= 8:
            bits -= 8
            byte = (value >> bits) & 0xFF
            binary_byte = format(byte, '08b')
            binary += binary_byte + ' '
            
    return binary.strip()

def binary_to_base64(binary_text):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Juntar  los bits
    binary_values = binary_text.split()
    all_bits = ''.join(binary_values)
    
    padding = len(all_bits) % 6
    if padding:
        all_bits += '0' * (6 - padding)
    
    # Convertir cada 6 bits a un carácter Base64
    base64_text = ''
    for i in range(0, len(all_bits), 6):
        chunk = all_bits[i:i+6]
        value = int(chunk, 2)
        base64_text += base64_chars[value]
    
    # Agregar padding si es necesario
    padding = len(binary_values) * 8 % 3
    if padding:
        base64_text += '=' * ((3 - padding) % 3)
    
    return base64_text

def binary_to_text(binary_text):
    binary_values = binary_text.split()
    text = ''
    for binary in binary_values:
        # Convertir cada valor binario a decimal
        decimal = 0
        for bit in binary:
            decimal = decimal * 2 + int(bit)
        # Convertir el decimal a carácter ASCII
        text += chr(decimal)
    return text

def base64_to_text(b64_text):
    binary = base64_to_binary(b64_text)
    return binary_to_text(binary)

def xor_binary(binary_text, key):
    binary_values = binary_text.split()
    key_binary = text_to_binary(key).split()
    key_len = len(key_binary)
    
    xor_result = []
    for i, binary in enumerate(binary_values):
        key_value = key_binary[i % key_len]
        # XOR bit por bit
        result = ''
        for b1, b2 in zip(binary, key_value):
            result += str(int(b1) ^ int(b2))
        xor_result.append(result)
    
    return ' '.join(xor_result)

def generate_key(length):
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    key = ''
    for _ in range(length):
        index = int.from_bytes(bytes([ord(chr(ord('a') + (_ * 7) % 26))]), 'big') % len(abecedario)
        key += abecedario[index]
    return key

def encrypt_with_fixed_key(text, key):
    binary_text = text_to_binary(text)
    return xor_binary(binary_text, key)

def encrypt_with_dynamic_key(text):
    key = generate_key(len(text))
    return encrypt_with_fixed_key(text, key), key

# main
if __name__ == "__main__":
    text = "Hola Jenny"
    
    # Conversión ASCII a Binario
    binary = text_to_binary(text)
    print(f"Texto a Binario: {binary}")
    
    #  texto en Base64 manualmente para el ejemplo
    texto_base64 = binary_to_base64(binary)
    print(f"Texto a Base64: {texto_base64}")
    
    # Base64 a Binario
    binary_from_b64 = base64_to_binary(texto_base64)
    print(f"Base64 a Binario: {binary_from_b64}")
    
    # Binario a texto ASCII
    restored_text = binary_to_text(binary)
    print(f"Binario a Texto: {restored_text}")
    
    # XOR con clave
    xor_result = xor_binary(binary, "clave")
    print(f"XOR con clave: {xor_result}")
    
    # Cifrado con llave dinámica
    dynamic_cipher, dynamic_key = encrypt_with_dynamic_key(text)
    print(f"Cifrado dinámico: {dynamic_cipher}")
    print(f"Llave dinámica: {dynamic_key}")
