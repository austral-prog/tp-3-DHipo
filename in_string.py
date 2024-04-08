def check_vowels():
    # Código a implementar utilizando input.
    vowels = ('a', 'e', 'i', 'o', 'u')
    nombre = input("> ").lower()

    for vowel in vowels:
        print(f'Contiene {vowel}:', (vowel in nombre))

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
