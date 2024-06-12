def read_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    return lines

def main():
    print("Enter lines of text. Press Enter on an empty line to finish.")
    user_lines = read_lines()
    for line in user_lines:
        print(line)

if __name__ == "__main__":
    main()