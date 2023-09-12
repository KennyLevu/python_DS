# hashtable.py

# special constant for creating abrand new object to represent
# blank spaces within HashTable

BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.pairs = capacity * [BLANK]

    def _index(self, key):
        return hash(key) % len(self)
    
    def __len__(self):
        return len(self.pairs)
    
    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = value

    def __getitem__(self, key):
        value = self.pairs[self._index(key)]
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
        if key in self:
            self[key] = BLANK
        else: 
            raise KeyError(key)