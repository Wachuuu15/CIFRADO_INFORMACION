## Librerias importadas
import pandas as pd
from collections import Counter
import unicodedata

freq_df = pd.read_csv("sp_frequencies.txt", sep="\t")
spanish_freqs = {row["Letter"]: float(row["Spanish_Frequency"].strip('%')) / 100 for _, row in freq_df.iterrows()}

# Definir el alfabeto de 27 letras
alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Función para limpiar el texto cifrado de tildes
def clean_text(text):
    replacements = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    text = text.lower()
    return ''.join(replacements.get(c, c) for c in text if c in alphabet)

# Función para calcular la frecuencia de letras en el texto
def get_frequency(text):
    total_chars = sum(1 for c in text if c in alphabet)
    return {char: text.count(char) / total_chars if total_chars > 0 else 0 for char in alphabet}

# Función para calcular la distancia de frecuencias con el español
def calculate_distance(observed, reference_freqs):
    return sum(abs(observed.get(char, 0) - reference_freqs.get(char, 0)) for char in reference_freqs)

# Función para calcular el inverso modular
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Función para descifrar con el Cifrado Afín
def decrypt_affine(text, a, b, alphabet):
    a_inv = mod_inverse(a, len(alphabet))
    if a_inv is None:
        return None
    
    return ''.join(alphabet[(a_inv * (alphabet.index(c) - b)) % len(alphabet)] if c in alphabet else c for c in text)

# Leer el archivo cifrado
with open("Affine/cipher2.txt", "r", encoding="utf-8") as f:
    cipher2_text = f.read()

# Limpiar el texto cifrado
cleaned_cipher2 = clean_text(cipher2_text)

# Aplicar descifrado con la clave correcta (a=5, b=15)
decrypted_text = decrypt_affine(cleaned_cipher2, 5, 15, alphabet)

# texto decifrado
print("Texto Descifrado:\n")
print(decrypted_text)
