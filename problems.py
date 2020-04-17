
def decode_string_helper(string: str, i: int) -> tuple:
    
    curr_string = ''
    count = 0
    index = i
    last_integer = False
    while True:
        if index > len(string) - 1:
            break

        char = string[index]

        if char == '[':
            substring, r_index = decode_string_helper(string, index + 1)
            curr_string += count * substring
            count = 0
            index = r_index
        elif char == ']':
            return (curr_string, index)
        elif char.isalpha():
            curr_string += char
        else:
            str_count = ''
            # create count from iterating from this point onwards
            for subchar in string[index:]:
                if not subchar.isdigit():
                    break
                str_count += subchar
                index += 1

            index -= 1
            count = int(str_count)


        index += 1

    return (curr_string, index)

def decode_string(s: str) -> str:
    return decode_string_helper(s, 0)

if __name__ == "__main__":
    input_string = '3[a]2[bc]'
    input_string = '3[a2[c]]'
    input_string = '2[abc]3[cd]ef'
    input_string = '100[leetcode]'
    print(decode_string_helper(input_string, 0))