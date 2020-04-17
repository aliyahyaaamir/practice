class Solution(object):
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output = []
        temp_text = []
        length_so_far = 0
        for word in words:
            if length_so_far + len(word) + len(temp_text) > max_width:
                if len(temp_text) == 1:
                    output.append(ljust(temp_text[0], max_width, " "))
                else:
                    spaces_count = (max_width - length_so_far) // (len(temp_text) -1)
                    index_with_extra_space = (max_width - length_so_far) % (len(temp_text) -1)
                    if index_with_extra_space == 0:
                        delimiter = " "*(spaces_count)
                        output.append(delimiter.join(temp_text))
                    else:
                        first_delimiter = " "*(spaces_count+1)
                        second_delimiter = " "*(spaces_count)
                        output.append(first_delimiter.join(temp_text[0:index_with_extra_space])+ first_delimiter + second_delimiter.join(temp_text[index_with_extra_space:]))
                    
                temp_text = [word]
                length_so_far = len(word)
            else:
                temp_text.append(word)
                length_so_far += len(word)
        
        output.append(ljust(" ".join(temp_text), max_width, " "))
        
        return output
            
            