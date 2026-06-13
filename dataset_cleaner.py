import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python dataset_cleaner.py input.csv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]


def read_csv(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        columns = reader.fieldnames
        return rows, columns


def clean_row(row):
    cleaned = {}
    missing_count = 0
    for column, value in row.items():
        value = value.strip()

        if value == "":
            value = 'UNKNOWN'
            missing_count += 1

        cleaned[column] = value

    return cleaned, missing_count


def clean_rows(rows):
    cleaned_rows = []
    seen = set()

    stats = {
        "original_rows": len(rows),
        "cleaned_rows": 0,
        "duplicates_removed": 0,
        "missing_values_filled": 0
    }

    for row in rows:
        cleaned_row, missing = clean_row(row)
        stats["missing_values_filled"] += missing

        row_signature = tuple(cleaned_row.items())

        if row_signature in seen:
            stats["duplicates_removed"] += 1
            continue

        seen.add(row_signature)
        cleaned_rows.append(cleaned_row)

    stats['cleaned_rows'] = len(cleaned_rows)

    return cleaned_rows, stats


def write_csv(filename, rows, columns):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def write_report(input_file, output_file, stats, columns):
    with open('cleaning_report.txt', mode='w', encoding='utf-8') as file:
        file.write("Cleaning Report\n\n")

        file.write(f"Input file: {input_file}\n")
        file.write(f"Output file: {output_file}\n\n")

        file.write(f"Original rows: {stats['original_rows']}\n")
        file.write(f"Cleaned rows: {stats['cleaned_rows']}\n")
        file.write(f"Duplicate rows removed: {stats['duplicates_removed']}\n")
        file.write(f"Missing values filled: {stats['missing_values_filled']}\n\n")

        file.write("Columns:\n")

        for column in columns:
            file.write(f"{column}\n")


def main():
    rows, columns = read_csv(input_file)
    if not rows:
        print('CSV file is empty')
        sys.exit(1)

    cleaned_rows, stats = clean_rows(rows)

    write_csv(output_file, cleaned_rows, columns)
    write_report(input_file, output_file, stats, columns)


if __name__ == "__main__":
    main()
