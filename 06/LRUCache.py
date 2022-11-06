class LRUCache:
    def __init__(self, limit=42):
        self.key_order_list = []
        self.dictionary = {}
        self.maxsize = limit

    def __update_priority(self, key):
        self.key_order_list.remove(key)
        self.key_order_list.insert(0,key)

    def get(self, key):
        result = self.dictionary.get(key)
        if result:
            self.__update_priority(key)
        return result

    def set(self, key, value):
        if self.dictionary.get(key):
            self.__update_priority(key)
            return

        if len(self.key_order_list) == self.maxsize:
            less_used_key = self.key_order_list.pop()
            self.dictionary.pop(less_used_key)

        self.dictionary[key] = value
        self.key_order_list.insert(0, key)
