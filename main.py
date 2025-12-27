from stats import count_words,count_characters,sort_dict
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_to_read = sys.argv[1]
    print(f"Analyzing book found at {file_to_read}")
    text = get_book_text(file_to_read)    
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    sorted_items=sort_dict(count_characters(text))
    print("--------- Character Count -------")
    for item in sorted_items:
        key=item["char"]
        value=item["num"]
        print(f"{key}: {value}")
    print("============= END ===============")
main()

