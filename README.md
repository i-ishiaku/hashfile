A program to calculate and print the hash of any given file from user
========================================================================================================================================================================
The hash function takes an arbitrary amount of data and returns a fixed length bit string. The output of the function is called the digest message.

They are widely used in cryptography for authentication purposes.
There are many hash functions like MD5, SHA-1, etc.

In the example a program is written to demonstrate how to hash a file using SHA-1 and MD5 hashing algorithm.

Breaking the file into small pieces will make the processing memory efficient because some files are very large to fit in memory at once.

The file is opened in binary mode in this program.
The hashlib module includes hash functions.
Using a while loop, the program loop through the file until the end.
An empty bytes object is received at the end.

Only 1024 bytes is read (this number can be adjusted based on preferences) from the file and update the hashing method throughout each loop.
Finally, the hexdigest() method is used to return the digest message in hexadecimal form.
