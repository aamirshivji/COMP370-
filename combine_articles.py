import csv

def add_unique_rows(file1, file2, output_file):
    """
    Add rows from file2 to file1 if they are not already in file1,
    and save the result to a new file.

    Parameters:
    - file1 (str): Path to the first TSV file.
    - file2 (str): Path to the second TSV file.
    - output_file (str): Path to the output TSV file.
    """
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        reader1 = csv.reader(f1, delimiter="\t")
        reader2 = csv.reader(f2, delimiter="\t")

        # Read headers and rows
        header1 = next(reader1)
        header2 = next(reader2)

        # Ensure headers match
        if header1 != header2:
            raise ValueError("Headers do not match between the two files!")

        rows1 = list(reader1)
        rows2 = list(reader2)

        # Find rows in file2 that are not in file1
        unique_rows = [row for row in rows2 if row not in rows1]

    # Write the combined data to the output file
    with open(output_file, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(header1)  # Write the header
        writer.writerows(rows1)  # Write rows from file1
        writer.writerows(unique_rows)  # Write unique rows from file2

    print(f"File created: {output_file}")
    print(f"Added {len(unique_rows)} unique rows from {file2} to {file1}.")


# Example usage
if __name__ == "__main__":
    file1 = "articles_output2.tsv"
    file2 = "other_movies.tsv"
    output_file = "other_movies.tsv"
    add_unique_rows(file1, file2, output_file)
