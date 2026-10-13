import re

REPLACEMENTS = [
    ("Dzi", "Дзі"),
    ("dzi", "дзі"),
    ("Dź", "Дзь"),
    ("dź", "дзь"),
    ("Dż", "Дж"),
    ("dż", "дж"),
    ("Dz", "Дз"),
    ("dz", "дз"),
    ("Sz", "Ш"),
    ("sz", "ш"),
    ("Cz", "Ч"),
    ("cz", "ч"),
    ("Rz", "Ж"),
    ("rz", "ж"),
    ("Ch", "Х"),
    ("ch", "х"),
    ("Si", "Сі"),
    ("si", "сі"),
    ("Ci", "Ці"),
    ("ci", "ці"),
    ("Zi", "Зі"),
    ("zi", "зі"),
    ("Ja", "Я"),
    ("ja", "я"),
    ("Ju", "Ю"),
    ("ju", "ю"),
    ("Je", "Є"),
    ("je", "є"),
    ("a", "а"),
    ("A", "А"),
    ("ą", "он"),
    ("Ą", "Он"),
    ("b", "б"),
    ("B", "Б"),
    ("c", "ц"),
    ("C", "Ц"),
    ("ć", "ць"),
    ("Ć", "Ць"),
    ("d", "д"),
    ("D", "Д"),
    ("e", "е"),
    ("E", "Е"),
    ("ę", "ен"),
    ("Ę", "Ен"),
    ("f", "ф"),
    ("F", "Ф"),
    ("g", "г"),
    ("G", "Г"),
    ("h", "г"),
    ("H", "Г"),
    ("i", "і"),
    ("I", "І"),
    ("j", "й"),
    ("J", "Й"),
    ("k", "к"),
    ("K", "К"),
    ("l", "л"),
    ("L", "Л"),
    ("ł", "в"),
    ("Ł", "В"),
    ("m", "м"),
    ("M", "М"),
    ("n", "н"),
    ("N", "Н"),
    ("ń", "нь"),
    ("Ń", "Нь"),
    ("o", "о"),
    ("O", "О"),
    ("ó", "у"),
    ("Ó", "У"),
    ("p", "п"),
    ("P", "П"),
    ("r", "р"),
    ("R", "Р"),
    ("s", "с"),
    ("S", "С"),
    ("ś", "сь"),
    ("Ś", "Сь"),
    ("t", "т"),
    ("T", "Т"),
    ("u", "у"),
    ("U", "У"),
    ("w", "в"),
    ("W", "В"),
    ("y", "и"),
    ("Y", "И"),
    ("z", "з"),
    ("Z", "З"),
    ("ź", "зь"),
    ("Ź", "Зь"),
    ("ż", "ж"),
    ("Ż", "Ж"),
]


def transliterate_to_cyrillic(text: str) -> str:
    pattern = re.compile(
        "|".join(re.escape(k) for k, _ in REPLACEMENTS), flags=re.UNICODE
    )
    mapping = dict(REPLACEMENTS)
    return pattern.sub(lambda m: mapping[m.group(0)], text)


def main():
    print("Wpisz zdanie po polsku (wpisz 'exit' lub naciśnij Ctrl+C, aby wyjść):\n")
    while True:
        try:
            line = input("> ")
            if line.strip().lower() == "exit":
                break
            result = transliterate_to_cyrillic(line)
            print(f"-> {result}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nKoniec programu.")
            break


if __name__ == "__main__":
    main()