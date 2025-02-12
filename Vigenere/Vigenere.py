## Librerias importadas
import pandas as pd
from collections import Counter
import unicodedata

freq_df = pd.read_csv("sp_frequencies.txt", sep="\t")
spanish_freqs = {row["Letter"]: float(row["Spanish_Frequency"].strip('%')) / 100 for _, row in freq_df.iterrows()}

# Definir el alfabeto de 27 letras
alphabet = "abcdefghijklmnñopqrstuvwxyz"









