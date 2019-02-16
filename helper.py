def is_isbn_or_key(word):
    '''
    判断搜索的是书名还是isbn
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(word.replace('-', '')) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
