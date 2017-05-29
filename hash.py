# Code For getting string for the given hash

LETTERS = 'acdegilmnoprstuw'
FIRST_LETTER = LETTERS[0]

class Hash:
    
    def __init__(self, hash):
        self.hash = hash
        
    def get_strings(self):
        '''Will return strings in list for the given numbers'''
        strings = []
        for each_hash in self.hash:
            strings.append(self.compute_string(each_hash))
        return strings
        
    def compute_hash(self, string):
        '''Will Compute hash for the given characters'''
        h = 7
        for char in string:
            h = h * 37 + LETTERS.index(char)
        return h

    def compute_string(self, hash):
        '''Compute strings iterating over the given hash'''
        hash = int(hash)
        # Quick find string length:
        hash_length = len(str(hash))
        string_length = 0
        while True:
            current_string = FIRST_LETTER * (string_length + 1)
            current_hash = self.compute_hash(current_string)
            if len(str(current_hash)) > hash_length:
                break
            string_length += 1
    
        chars = []
        for i in range(string_length):
            previous_char = None
            for char in LETTERS:
                current_string = ''.join(chars) + char + FIRST_LETTER * (string_length - i - 1)
                current_hash = self.compute_hash(current_string)
                if current_hash == hash:
                    # String found!
                    return current_string
                elif current_hash > hash:
                    # Add previous character to chars[]
                    chars.append(previous_char or FIRST_LETTER)
                    break
                else:
                    # Update previous character
                    previous_char = char
        # Unable to find the string
        raise ValueError('Cannot find string for hash %s.' %(hash))

if __name__ == '__main__':
    '''Program Execution starts here'''
    given_numbers = Hash([680131659347, 910897038977002])
    strings = given_numbers.get_strings()
    for string in strings:
        print(string)