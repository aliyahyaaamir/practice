"""
Text justification to max width
Left and Right aligned

Last line should be left justified with no spaces between words

Greedy approach to pack in as many words as possible
' ' between should be as evenly distributed as possible

Cases to consider

    1) word_length + line_length <= max_width -> append word
    2) word_length + line_length  > max_width -> do not append word, line ends; need to pad number of spaces from left to right
    (evenly distributed if possible)
    3) need to consider if this is the last line being inserted (implies do not add extra space between words)


"""

def get_justified_words_per_line(words: list, max_width: int) -> list:

    justified_words_per_line = []
    justified_words = []

    for word in words:
        num_words = len(justified_words)
        words_length = len(''.join(justified_words))

        if len(justified_words) + words_length + len(word) > max_width:
            justified_words_per_line.append(justified_words)
            justified_words = [word]
        else:
            justified_words.append(word)
    
    if justified_words:
        justified_words_per_line.append(justified_words)

    return justified_words_per_line



def text_justification(words: list, max_width: int) -> list:
    """
    Last line is left justified

    A line is complete when the length(words + next word) + length(spaces) > max_width
    Different cases, even distribution of spaces between words
    Round robin, more in the beginning
    No need to add extra spaces
    Single word on line

    """

    justified_lines = []

    # Create a function that returns a list of words for each line
    justified_lines_array = get_justified_words_per_line(words, max_width)
    print(justified_lines)

    for justified_words in justified_lines_array[:-1]:
        
        num_words = len(justified_words)
        words_length = len(''.join(justified_words))
        spaces_to_add = max_width - words_length

        if spaces_to_add % (num_words - 1) == 0:
            print('here')
            num_spaces = spaces_to_add//(num_words - 1)
            justified_lines.append((' ' * num_spaces).join(justified_words))
        elif num_words == 1:
            justified_lines.append(justified_words[0] + ' ' * spaces_to_add)
        else:
            num_spaces = spaces_to_add//(num_words - 1)
            index_with_extra_space = spaces_to_add % (num_words - 1)
            leftover_spaces = spaces_to_add - num_spaces

            first_delimiter = " " *(num_spaces+1)
            print(first_delimiter, len(first_delimiter))
            second_delimiter = " " *(num_spaces)
            justified_lines.append(first_delimiter.join(justified_words[0:index_with_extra_space]) + first_delimiter + second_delimiter.join(justified_words[index_with_extra_space:]))
                    

    # handle last line here
    if justified_lines_array != [-1]:
        justified_line = ' '.join(justified_lines_array[-1])
        spaces_to_pad = max_width - len(justified_line)

        justified_lines.append(justified_line + ' ' * spaces_to_pad)

    return justified_lines

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16

    output = text_justification(words, max_width)