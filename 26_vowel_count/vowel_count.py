def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    freq_map = {}
    vowels = ['a','e','i','o','u']
    for letter in phrase:
        if letter.lower() in vowels:
            count = phrase.lower().count(letter.lower())
            if not count == 0:
                freq_map[letter.lower()] = count
    return freq_map
