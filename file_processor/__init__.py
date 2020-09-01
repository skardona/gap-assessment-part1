def get_largest_word_reversed(words_file_name):
    """
    Reads a txt file with a word on each line, and prints the largest word and the largest word reversed
    :param words_file_name: String with txt file relative path
    """

    words_file = open(words_file_name, "r")
    file_lines = words_file.readlines()

    if file_lines:
        clean_lines = []
        for line in file_lines:
            clean_line = line.strip()
            if " " in clean_line:
                print("There is more than one word per line")
                words_file.close()
                return
            else:
                clean_lines.append(clean_line)

        largest_word = max(clean_lines, key=len)
        largest_word_reversed = largest_word[::-1]

        print(largest_word)
        print(largest_word_reversed)

    else:
        print("File has no words")

    words_file.close()
