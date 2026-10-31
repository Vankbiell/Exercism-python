def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """

    comple = ' :: ' + vocab_words[0]
    words_comple = vocab_words[0] + comple.join(vocab_words[1:])
    return vocab_words[0] + ' :: ' + words_comple


vocab_words = 'auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete','echolalia', 'encoder', 'biography'
print(make_word_groups(vocab_words))
