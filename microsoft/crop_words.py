"""
Limit of K characters per entry
Crop messages that are too long


May not crop away part of a word
Output message may not end with a space
Output message may not exceed the K-character limit
Output message should be as long as possible

"""

def crop_words(text: str, max_length: int) -> str:
    cropped_word = text[:max_length]

    # need to truncate more
    if text[max_length-1].isalpha() and text[max_length].isalpha():
        cropped_word = text[:cropped_word.rfind(' ', 0, max_length-1)]

    return cropped_word.rstrip()
        

if __name__ == "__main__":
    
    text = 'Codility We test coders'
    max_length = 11

    cropped_word = crop_words(text, max_length)