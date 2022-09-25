import json


def count_keywords(keyword):
    if keyword not in dict_statistics:
        dict_statistics[keyword] = 1
    else:
        dict_statistics[keyword] += 1


def parse_json(json_str: str, required_fields=None, keywords=None, *, keyword_callback):
    json_doc = json.loads(json_str)
    if required_fields is None or keywords is None or len(json_doc) == 0:
        return

    for key, value in json_doc.items():
        if key in required_fields:
            splitted_value = value.split()
            for word in splitted_value:
                if word in keywords:
                    keyword_callback(word)


if __name__ == '__main__':
    dict_statistics = {}

    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', [], ['word2'],
               keyword_callback=count_keywords)
    assert dict_statistics == {}

    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', ['key2'], [],
               keyword_callback=count_keywords)
    assert dict_statistics == {}

    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}', ['key1', 'key2'], ['Word1', 'word2', 'word3'],
               keyword_callback=count_keywords)

    assert dict_statistics == {'Word1': 1, 'word2': 2, 'word3': 1}

    parse_json('{"programming": "Python C++ Java Scala", "math": "combinatorics geometries"}', ['programming'],
               ['geometries', 'C++'],
               keyword_callback=count_keywords)

    assert dict_statistics == {'C++': 1, 'Word1': 1, 'word2': 2, 'word3': 1}

    print('ok')
