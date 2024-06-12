def to_title_case(s):
    words = s.split()
    title_cased = ' '.join(word.capitalize() for word in words)

    return title_cased
input_string = "this is an example string"
title_cased_string = to_title_case(input_string)
print(title_cased_string)