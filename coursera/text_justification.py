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

def justify_text(words: list, max_width: int) -> list:
    
    justified_lines = []
    justified_line = ''
    num_words = len(words)
    
    for index, word in enumerate(words):
        word_length = len(word)
        line_length = len(justified_line)
        curr_length = word_length + line_length if index == 0 else word_length + line_length + 1

        if curr_length <= max_width: # the plus 1, is to account for the space that we're adding between words
            if line_length == 0:
                justified_line += word
            else:
                justified_line += ' ' + word
        else:
            spaces_to_pad = max_width - line_length
            words_added = len(justified_line.split())
            spaces_to_add = words_added - 1

            # check if this is the last line; it won't be since we can't fit the next word
            if spaces_to_pad == 0:
                justified_lines.append(justified_line)
            elif spaces_to_add == 0: # means single word, so left justify
                justified_lines.append(justified_line+ ' ' * (spaces_to_pad))
            elif spaces_to_pad % spaces_to_add == 0:
                # evenly distributed
                justified_lines.append(justified_line.replace(' ', ' ' * (spaces_to_pad//spaces_to_add + 1)))
            else:
                leftover_space = spaces_to_pad % spaces_to_add
                justified_line = justified_line.replace(' ', ' ' * (spaces_to_pad//spaces_to_add + 1))
                increment = 0
                for i in range(leftover_space):
                    # go from left to right
                    index = justified_line.find(' ', increment)
                    increment = len(justified_line[:index + 1) + 1
                    justified_line = justified_line[:index] + ' ' + justified_line[index:]
                justified_lines.append(justified_line)

            justified_line = word

    # This is to take care of the last line
    if justified_line != '':
        spaces_to_pad = max_width - len(justified_line)
        justified_lines.append(justified_line + ' ' * spaces_to_pad)
    
    return justified_lines




if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16

    words = ["What","must","be","acknowledgment","shall","be"]

    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    max_width = 20

    words = ["The","important","thing","is","not","to","stop","questioning.","Curiosity","has","its","own","reason","for","existing."]
    max_width = 17

    words = ["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."]
    max_width = 25

    words = ["When","I","was","just","a","little","girl","I","asked","my","mother","what","will","I","be","Will","I","be","pretty","Will","I","be","rich","Here's","what","she","said","to","me","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see","Que","sera","sera","When","I","was","just","a","child","in","school","I","asked","my","teacher","what","should","I","try","Should","I","paint","pictures","Should","I","sing","songs","This","was","her","wise","reply","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see","Que","sera","sera","When","I","grew","up","and","fell","in","love","I","asked","my","sweetheart","what","lies","ahead","Will","there","be","rainbows","day","after","day","Here's","what","my","sweetheart","said","Que","sera","sera","Whatever","will","be","will","be","The","future's","not","ours","to","see","Que","sera","sera","What","will","be,","will","be","Que","sera","sera..."]
    max_width = 60

    justified_text = justify_text(words, max_width)