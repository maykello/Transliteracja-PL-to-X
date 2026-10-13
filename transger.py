import re
import sys

RULES = [
    # 1. Zbitki 4- i 3-znakowe
    (r"szcz", "schtsch"),
    (r"dżdż", "dschdsch"),
    (r"drz", "dsch"),
    (r"trz", "tsch"),
    (r"prz", "psch"),
    (r"krz", "ksch"),
    (r"dż", "dsch"),
    (r"dź", "dsch"),
    (r"dz", "ds"),
    (r"cz", "tsch"),
    (r"sz", "sch"),
    (r"rz", "sch"),
    (r"ch", "ch"),
    # 2. Zmiękczenia przed samogłoskami (cia, cie, sia, sie...)
    (r"ci(?=[aąeęioóuy])", "tsch"),
    (r"si(?=[aąeęioóuy])", "sch"),
    (r"zi(?=[aąeęioóuy])", "s"),
    (r"ni(?=[aąeęioóuy])", "nj"),
    # 3. Zmiękczenia przed spółgłoskami lub na końcu
    (r"ci", "tschi"),
    (r"si", "schi"),
    (r"zi", "si"),
    # 4. Samogłoski nosowe (om/em przed b/p, w reszcie on/en)
    (r"ą(?=[pbPB])", "om"),
    (r"ę(?=[pbPB])", "em"),
    (r"ą", "on"),
    (r"ę", "en"),
    # 5. Diakrytyki pojedyncze
    (r"ć", "tsch"),
    (r"ś", "sch"),
    (r"ź", "s"),
    (r"ż", "sch"),
    (r"ó", "u"),
    (r"ł", "l"),
    # 6. Spółgłoska c -> niemieckie z
    (r"c", "z"),
]


def match_case(original: str, replacement: str) -> str:
    """Zachowuje styl wielkości liter: UPPERCASE, Titlecase lub lowercase."""
    if original.isupper():
        return replacement.upper()
    if original[0].isupper():
        return replacement.capitalize()
    return replacement.lower()


def polish_to_german_phonetics(text: str) -> str:
    result = text
    for pattern, repl in RULES:
        regex = re.compile(pattern, re.IGNORECASE)

        def replace_fn(match: re.Match, target: str = repl) -> str:
            return match_case(match.group(0), target)

        result = regex.sub(replace_fn, result)
    return result


def main():
    print("=" * 60)
    print("  TRANSLITERATOR PL -> DE-PHONETIC")
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

            output = polish_to_german_phonetics(user_input)
            print(f"DE > {output}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nPrzerwano dzialanie programu.")
            sys.exit(0)


if __name__ == "__main__":
    main()