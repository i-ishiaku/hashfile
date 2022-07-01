# a program to calculate and print the hash of any given file from user
import hashlib as hl

print(""""This function returns the SHA-1  and MD5 hash
    of the file passed into it based on users preference
    =============================================================
    """)


def hash_file(filename):

    # make a hash object
    h = hl.sha1()
    m = hl.md5()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        choice = input("Enter (M to hash md5) or (H for sha1): ")
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
            m.update(chunk)
            if (choice == "h") or (choice == "H"):
                # return the hex representation of digest
                return h.hexdigest()
            elif (choice == "m") or (choice == "M"):
                # return the hex representation of digest
                return m.hexdigest()


message = hash_file(input(r"Enter a directory: "))
print(message)
