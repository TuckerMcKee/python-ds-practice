def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list_phrase = list(phrase)
    for i in range(len(phrase)):
        if i == 0 or list_phrase[i - 1] == ' ':
            list_phrase[i] = list_phrase[i].upper()
        else:
            list_phrase[i] = list_phrase[i].lower()  
    return ''.join(list_phrase)
