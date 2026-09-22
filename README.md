# AI Dataset Cleaner

A small Python CLI that cleans messy CSV datasets by trimming whitespace, filling missing values, and removing duplicate rows.

## Usage

```bash
python dataset_cleaner.py input.csv output.csv
```

Example with the included sample data:

```bash
python dataset_cleaner.py messy_tickets.csv cleaned_tickets.csv
```

## What it does

- Strips leading/trailing whitespace from every cell
- Replaces empty values with `UNKNOWN`
- Removes fully duplicate rows
- Writes a summary report to `cleaning_report.txt`

## Requirements

- Python 3, standard library only (no external packages)
