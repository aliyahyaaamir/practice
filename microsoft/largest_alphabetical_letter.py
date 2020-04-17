
def largest_alphabetical_letter(S: str) -> str:
    if len(S) <= 1:
        return ''
    
    upper_letters_seen = set()
    lower_letters_seen = set()

    largest_alpha_seen = ' '

    # O(n) pass through
    for letter in S:
        if ord(letter) < ord('a'):
            upper_letters_seen.add(letter)
        else:
            lower_letters_seen.add(letter)

    for letter in S:
         if ord(letter) < ord('a') and letter.lower() in lower_letters_seen:
            curr_val = ord(largest_alpha_seen)
            if curr_val < ord(letter):
                largest_alpha_seen = letter

    return largest_alpha_seen

if __name__ == "__main__":
    S = "ameDCABM"

    largest_letter = largest_alphabetical_letter(S)