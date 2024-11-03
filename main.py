def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        words = file_contents.split()
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")

        lowered_words = [word.lower() for word in words]
        char_count = {}
        for word in lowered_words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
                    
        for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
            print(f"The '{char}' character was found {count} times")

main()  