import json
import sys
import random

def parse_version(version_str):
    return tuple(map(int, version_str.split('.')))

def generate_versions(pattern, count=2):
    parts = pattern.split('.')
    star_positions = [i for i, part in enumerate(parts) if part == '*']

    versions = []

    for _ in range(count):
        new_parts = parts[:]
        for pos in star_positions:
            new_parts[pos] = str(random.randint(0, 99))
        versions.append('.'.join(new_parts))

    return versions

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <версия> <файл_конфига>")
        return

    input_version_str = sys.argv[1]
    config_file = sys.argv[2]

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        sys.exit(1)

    all_versions = []

    for key, pattern in config.items():
        versions = generate_versions(pattern)
        all_versions.extend(versions)

    version_tuples = [(v, parse_version(v)) for v in all_versions]

    sorted_versions = sorted(version_tuples, key=lambda x: x[1])

    sorted_version_strings = [v[0] for v in sorted_versions]

    target_version = parse_version(input_version_str)

    older_versions = [v[0] for v in sorted_versions if v[1] < target_version]

    print("Все версии (отсортированные):")
    print(sorted_version_strings)

    print("\nВерсии старше", input_version_str + ":")
    print(older_versions)

if __name__ == "__main__":
    main()