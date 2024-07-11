import re

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'                 # regular expression to capture song name
    match = re.search(pattern,command,re.IGNORECASE)         # using search to find match in command
    return match.group(1)                                    # if match found - return song name ; otherwise - return None

def remove_words(input_string,words_to_remove):

    words=input_string.split()                                                          # split input string in words
    filtered_words= [ word for word in words if word.lower() not in words_to_remove]    # remove unwanted words
    result_string = ' '.join(filtered_words)                                            # join the remaining woords back in a string
    return result_string

# example usage
#input_string=" make a whatsapp text to shrey"
#words_to_remove = ["make","a",'to','phone','call','send,','whatsapp','text']
#result= remove_words(input_string,words_to_remove)
#print(result)
