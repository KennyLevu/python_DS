# hashtable.py

# special constant for creating abrand new object to represent
# blank spaces within HashTable

BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def _index(self, key):
        return hash(key) % len(self)
    
    def __len__(self):
        return len(self.values)
    
    def __setitem__(self, key, value):
        self.values[self._index(key)] = value

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value
    
    def __contains__(self,key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    def get(self, key, default = None):
        try:
            return self[key]
        except KeyError:
            return default
  
    def __delitem__(self, key):
        self.values[self._index(key)] = BLANK    