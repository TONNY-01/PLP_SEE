#!/usr/bin/env python3
"""
file_transformer.py

1. Reads an input file and writes a modified version to an output file.
2. Prompts for filenames and handles errors if the input file cannot be opened.

Usage:
    python file_transformer.py
"""

def calculate_transformation(line: str) -> str:
    """
    Define your transformation here.
    For demonstration, we:
      - Strip trailing whitespace
      - Uppercase the text
      - Prefix each line with its original line number
    """
    return line.strip().upper()

def transform_file(input_path: str, output_path: str) -> None:
    """
    Reads from `input_path`, applies a line-by-line transformation,
    and writes results to `output_path`.
    """
    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
        for idx, raw_line in enumerate(fin, start=1):
            new_line = calculate_transformation(raw_line)
            fout.write(f"{idx}: {new_line}\n")

def main():
    print("\n📂 File Read & Write Challenge")
    # Prompt for the source and destination filenames
    source = input("Enter the input filename (e.g., data.txt): ").strip()
    destination = input("Enter the output filename (e.g., data_transformed.txt): ").strip()

    try:
        transform_file(source, destination)
    except FileNotFoundError:
        print(f"❌ Error: The file '{source}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{source}' or write to '{destination}'.")
    except IsADirectoryError:
        print(f"❌ Error: One of the paths is a directory, not a file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    else:
        print(f"✅ Success! Transformed file saved to '{destination}'.")

if __name__ == "__main__":
    main()
