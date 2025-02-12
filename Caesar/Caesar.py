## Librerias usadas
import numpy as np
import pandas as pd
from collections import Counter

freq_df = pd.read_csv("sp_frequencies.txt", sep="\t")
spanish_freqs = {row["Letter"]: float(row["Spanish_Frequency"].strip('%')) for _, row in freq_df.iterrows()}

with open("Caesar/cipher1.txt", "r", encoding="utf-8") as f:
    cipher1_text = f.read()

# Alfabeto de 27 letras
alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Función para descifrar un texto con cifrado César
def decrypt_caesar(ciphertext, shift, alphabet):
    decrypted_text = []
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text.append(alphabet[index])
        else:
            decrypted_text.append(char)
    return "".join(decrypted_text)

# Función para calcular la diferencia de frecuencias
def frequency_score(text, alphabet, reference_freqs):
    text_counter = Counter(c for c in text if c in alphabet)
    total_chars = sum(text_counter.values())
    text_freqs = {char: (text_counter.get(char, 0) / total_chars) * 100 for char in alphabet}
    
    # Calcular diferencia absoluta entre frecuencias
    score = sum(abs(text_freqs.get(char, 0) - reference_freqs.get(char, 0)) for char in alphabet)
    return score

# Probar todas las rotaciones y encontrar la mejor clave
best_shift = None
best_score = float("inf")
best_decryption = None

for shift in range(1, 31):  # ROT máximo 30
    decrypted_text = decrypt_caesar(cipher1_text, shift, alphabet)
    score = frequency_score(decrypted_text, alphabet, spanish_freqs)
    
    if score < best_score:
        best_score = score
        best_shift = shift
        best_decryption = decrypted_text

# texto decifrado
best_shift, best_decryption[:500]
print("Texto decifrado")
print(best_decryption)