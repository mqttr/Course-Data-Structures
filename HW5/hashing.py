def getHash(key) -> int:
    '''
    Takes a string, adds padding, and jumbles the bits to obtain a number to then be optionally compressed into a table.
    O(n) time complexity.

    :param str key: String to be hashed.

    :return: Returns the raw hash
    :rtype: int
    '''
    hash = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in str(key)])))

    # # Adds predictable padding to increase unpredictability of bit_list
    # # Concatonates first half by every -2nd value and second half by every -3rd value to the original bits 
    # while len(hash) < 300: 
    #     hash = hash + hash[0:len(hash)//2:-2] + hash[len(hash)//2::-3]

    # # Obtains 256-long slice with crop_start offset from the start
    # crop_start = 16
    # hash = hash[crop_start:(crop_start+256)]
    

    base_10: int = 0
    for i, bit in enumerate(hash[::-1]):
        base_10 += bit * 2**i 

    # Returns base 10 representation or base 10 modulo mod
    return int(base_10)

class HashTable:
    def __init__(self, table_size: int):
        '''
        Initiates the HashTable to begin accepting hashes
        :param int table_size: Desired size of desired table, forces the table to be a prime number >= table_size.
        '''
        self.table_size = self.next_prime(table_size-1)
        self.table: list[None | int] = [None]*self.table_size
        self.element_count = 0

    def insert(self, key: int | str | float) -> int:
        last_inserted_index = self.__insert(key, getHash(key) % self.table_size)

        if self.element_count > self.table_size // 2:
            self.rehash()
            return self.__insert(key, getHash(key) % self.table_size) # Gets location on rehashed table

        return last_inserted_index

    def __insert(self, key: int | str | float , position: int) -> int:
        position = position % self.table_size
        
        # Adds if location is empty
        if self.table[position] == None:
            self.table[position] = key
            self.element_count += 1
            return position
        
        # Returns located index if element is located
        if self.table[position] == key:
            self.table[position] = key
            return position


        return self.__insert(key, position + self.calculate_difference(key))

    def delete(self, key: int | str | float) -> bool:
        return self.__delete(key, getHash(key))

    def __delete(self, del_element: int | str | float, position) -> bool:
        position = position % self.table_size

        table_element = self.table[position]

        if table_element == None:
            return False
        
        if table_element == del_element:
            table_element = False
            return True
        
        return self.__delete(del_element, position + self.calculate_difference(del_element))

    def contains(self, key: int | str | float) -> bool:
        index = getHash(key) % self.table_size

        return self.__contains(key, index)

    def __contains(self, key: int | str | float, position: int) -> bool:
        position = position % self.table_size

        table_element = self.table[position]

        if table_element == None: 
            return False
        
        if table_element == key:
            return True

        return self.__contains(key, position + self.calculate_difference(key))

    def count_all(self) -> int:
        return sum([0 if element is None else 1 for element in self.table])

    def count_active(self) -> int:
        return sum([0 if element is None else 1 for element in self.table])

    def rehash(self):
        self.element_count = 0
        old_table = self.table

        self.table_size = self.next_prime(self.table_size * 2)
        self.table = [None]*self.table_size

        for element in old_table:
            if element is None :
                continue

            self.insert(element)

    def next_prime(self, value: int) -> int:
        '''
        Calculates the next largest prime number by brute force.
        :param int value: Start checking for prime numbers above this value
        :return int: The next largest prime number
        '''
        while True:
            value += 1

            if all(value % i for i in range(2, value)):
                return value

    def calculate_difference(self, key: any) -> int:
        # input(element.hash)
        return 7 - getHash(getHash(key)) % 7
    
    def get_element(self, index: int) -> int:
        return self.table[index % self.table_size]

    def __str__(self) -> str:
        return str([None if element is None else element for element in self.table])

if __name__ == "__main__":
    table = HashTable(3)

    # for x in range(51):
    #     print(x, HashElement(x).getHash(11))

    table.insert(23)
    print(table)
    table.insert(50)
    print(table)
    table.insert(41)

    print(table.contains(41))
    # table.delete(41)
    print(table)
    print(table.count_all())
