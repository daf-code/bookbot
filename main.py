from collections import Counter

cur_book = "books/frankenstein.txt"



def main():
    with open(cur_book) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        char_count = Counter(char.lower() for char in file_contents)
        sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        #print(file_contents)
        print(f"--- Begin report of {cur_book} ---")
        print(f"{word_count} words found in the document")
        print("")
        for char, count in sorted_char_count:
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")
        print("--- End report ---")


main()