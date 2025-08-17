def count_words(book_text):
    newlist = book_text.split()
    return len(newlist)

    word_count = count_words(book_text)
    print(f"Found {word_count} total words")

def character_count(book_text):
    char_counts = {}
    for character in book_text:
        lowercase = character.lower()
        if lowercase in char_counts:
    	    char_counts[lowercase] += 1
        else:
            char_counts[lowercase] = 1
    return char_counts

def sorted_dict(char_counts):
    sorted = []
    for char, num in char_counts.items():
        if char.isalpha():
            sorted.append({"char": char, "num": num})
            sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(items):
    return items["num"]

