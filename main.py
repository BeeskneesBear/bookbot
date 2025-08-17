import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    def get_book_text():
        with open(sys.argv[1]) as f:
            file_contents = f.read()
        return file_contents

    book_text = get_book_text()

    from stats import count_words, character_count, sorted_dict
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}
    ----------- Word Count ----------
    """)
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    raw_char_counts = character_count(book_text)
    final_sorted_list = sorted_dict(raw_char_counts)
    for entry in final_sorted_list:
        print(f'{entry["char"]}: {entry["num"]}')
    print("============= END ===============")

main()
