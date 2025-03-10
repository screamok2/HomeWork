def popular_words (text, words):
    text1 =text.lower()
    text2 = text1.split()
    result = {}
    x = 0
    for item in words:
        result1 = {item :text2.count(words[x])}
        x = x + 1
        result.update(result1)
    print(result)

popular_words("When I was One I had just begun When I was Two I was nearly new",['i', 'was', 'three', 'near'])
