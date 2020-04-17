from collections import Counter

def reorganize_string(string: str) -> str:
    count_dict = Counter(string)
    str_length = len(string)

    if str_length == 0:
        return ""

    most_common = count_dict.most_common(1)[0][1]

    if str_length - most_common < most_common - 1:
        return ""

    output_string = ""
    # Iterate and construct string
    # for char, count in sorted(count_dict.items(), key=lambda x: x[1], reverse=True):
    #     print(char, count)
    #     output_string += char
    last_letter = ''
    while True:

        most_common = count_dict.most_common(1)
        if not most_common:
            break

        letter, count = most_common[0]
        if letter == last_letter:
            # get next letter
            letter = [char for char in count_dict.keys() if char != last_letter ][0]
            count = count_dict[letter]

        if count == 1:
            del count_dict[letter]
        else:
            count_dict[letter] -= 1
        last_letter = letter
        output_string += letter

    return output_string

if __name__ == "__main__":
    string = 'aab'
    output_string = reorganize_string(string)