import csv

def compare_tsv_files(file1, file2):
    """
    Compare two TSV files and print differences.

    Parameters:
    - file1 (str): Path to the first TSV file.
    - file2 (str): Path to the second TSV file.
    """
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        reader1 = csv.reader(f1, delimiter="\t")
        reader2 = csv.reader(f2, delimiter="\t")

        # Read headers
        header1 = next(reader1)
        header2 = next(reader2)

        if header1 != header2:
            print("Headers differ:")
            print(f"File 1 Header: {header1}")
            print(f"File 2 Header: {header2}")
            return

        print("Headers are identical. Proceeding to compare rows...")

        rows1 = list(reader1)
        rows2 = list(reader2)

        # Find rows that are in file1 but not in file2
        only_in_file1 = [row for row in rows1 if row not in rows2]

        # Find rows that are in file2 but not in file1
        only_in_file2 = [row for row in rows2 if row not in rows1]

        if not only_in_file1 and not only_in_file2:
            print("The two files are identical.")
        else:
            print("\nRows in File 1 but not in File 2:")
            for row in only_in_file1:
                print(row)

            print("\nRows in File 2 but not in File 1:")
            for row in only_in_file2:
                print(row)


# Example usage
if __name__ == "__main__":
    file1 = "sub.tsv"
    file2 = "articles_output2.tsv"
    compare_tsv_files(file1, file2)

        



    








 





