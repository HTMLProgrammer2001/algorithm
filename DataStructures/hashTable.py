class HashTable:
    items = {}

    @staticmethod
    def generateHash(key):
        size = sum([ord(letter) for letter in key])

        return size % 199

    def setItem(self, key, val):
        if not key:
            raise Exception('No key was defined')

        if not isinstance(key, str):
            raise Exception('Key must be string')

        hashKey = self.generateHash(key)
        item = {
                'next': None,
                'key': key,
                'val': val
            }

        if not hashKey in self.items:
            self.items[hashKey] = item
        else:
            cur = self.items[hashKey]
            
            while cur:
                if cur['key'] == key:
                    cur['val'] = val
                    return
                
                cur = cur['next']

            cur['next'] = item

    def getItem(self, key):
        if not key:
            raise Exception('No key was defined')

        if not isinstance(key, str):
            raise Exception('Key must be string')

        hashKey = self.generateHash(key)

        if not hashKey in self.items:
            raise Exception('Key was not found')

        cur = self.items[hashKey]

        while cur['key'] != key:
            if not cur['next']:
                raise Exception('Key was not found')
            
            cur = cur['next']

        return cur['val']
        
