import re
import sys

# Reguły w kolejności priorytetu
# Zmiany w->v oraz j->y wykonujemy najpierw, aby nie nadpisać 'w' powstałego z 'ł' oraz 'j' z 'dż/dź'
RULES = [
    # 1. Kolizje podstawowe (konieczne przed zbitkami i diakrytykami)
    (r"w", "v"),  # Polskie 'w' brzmi jak angielskie 'v'
    (r"j", "y"),  # Polskie 'j' brzmi jak angielskie 'y'
    # 2. Złożone zbitki spółgłoskowe
    (r"szcz", "shch"),
    (r"dżdż", "j-j"),
    (r"drz", "dzh"),
    (r"trz", "tsh"),
    (r"prz", "psh"),
    (r"krz", "ksh"),
    (r"dż", "j"),
    (r"dź", "j"),
    # 3. Zmiękczenia 'dzi'
    (r"dzi(?=[aąeęioóuy])", "j"),
    (r"dzi", "ji"),
    (r"dz", "ds"),
    # 4. Zmiękczenia przed samogłoskami (cia, cie, sia, sie, nia, nie...)
    (r"ci(?=[aąeęioóuy])", "ch"),
    (r"si(?=[aąeęioóuy])", "sh"),
    (r"zi(?=[aąeęioóuy])", "zh"),
    (r"ni(?=[aąeęioóuy])", "ny"),
    # 5. Głoski szumiące i zwarte
    (r"cz", "ch"),
    (r"sz", "sh"),
    (r"rz", "zh"),
    (r"ch", "kh"),
    # 6. Zmiękczenia przed spółgłoskami lub na końcu wyrazu
    (r"ci", "chi"),
    (r"si", "shi"),
    (r"zi", "zhi"),
    (r"ni", "ni"),
    # 7. Samogłoski nosowe (om/em przed b/p, on/en w pozostałych)
    (r"ą(?=[pbPB])", "om"),
    (r"ę(?=[pbPB])", "em"),
    (r"ą", "on"),
    (r"ę", "en"),
    # 8. Diakrytyki pojedyncze
    (r"ć", "ch"),
    (r"ś", "sh"),
    (r"ź", "zh"),
    (r"ż", "zh"),
    (r"ń", "ny"),
    (r"ó", "oo"),
    (r"ł", "w"),  # Polskie 'ł' brzmi jak angielskie 'w'
    # 9. Spółgłoska c -> angielskie ts
    (r"c", "ts"),
]


def match_case(original: str, replacement: str) -> str:
    """Zachowuje styl wielkości liter: UPPER, Title, lower."""
    if original.isupper():
        return replacement.upper()
    if original[0].isupper():
        return replacement.capitalize()
    return replacement.lower()


def polish_to_english_phonetics(text: str) -> str:
    result = text
    for pattern, repl in RULES:
        regex = re.compile(pattern, re.IGNORECASE)

        def replace_fn(match: re.Match, target: str = repl) -> str:
            return match_case(match.group(0), target)

        result = regex.sub(replace_fn, result)
    return result


def main():
    print("=" * 60)
    print("  TRANSLITERATOR PL -> EN-PHONETIC")
    print("  Wpisz zdanie i wcisnij Enter.")
    print("  Wpisz 'q', 'exit' lub wcisnij Ctrl+C, aby zakonczyc.")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("PL > ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"q", "exit", "wyjdz", "quit"}:
                print("\nKoniec pracy programu.")
                break

            output = polish_to_english_phonetics(user_input)
            print(f"EN > {output}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nPrzerwano dzialanie programu.")
            sys.exit(0)


if __name__ == "__main__":
    main()