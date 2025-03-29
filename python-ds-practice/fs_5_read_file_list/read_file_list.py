def read_file_list(filename):
    """Read file and print out each line separately with a '-' before it."""
    with open(filename) as file:
        for line in file:
            print(f"- {line.strip()}")
