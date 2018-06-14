# Closed hashing data into 0 ... M - 1
M = 10


# Convert to integer.
# Each char is converted to Ascii code number.
def hashing(data):
    hash_data = [-1 for i in range(M)]
    key_data = [-1 for i in range(len(data))]
    for i, d in enumerate(data):
        sum = 0
        for x in d:
            sum += ord(x)
        sum %= M
        while hash_data[sum] is not -1:
            sum += 1
            sum %= M
        hash_data[sum] = d
        key_data[i] = sum

    return hash_data, key_data

#def get_data(hash_data, :

data = ["abc", "name", "school", "KHU", "a"]
hash_data, key_data = hashing(data)
for i in key_data:
    print(hash_data[i])