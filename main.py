import sys
from stats import print_bookbot_analysis

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print_bookbot_analysis(book_path)

if __name__ == "__main__":
    main()