# File not found exception

try:
    # Try things
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError:
    # Exception for the file not being found
    file = open('a_file.txt', 'w')
    file.write('Hello world!')
except KeyError as error:
    # Exception for keyerror
    print(f'The key {error} does not exist!')
else:
    # If the try is successful
    content = file.read()
    print(content)
finally:
    # Execute no matter what
    file.close()
    print('File closed.')

# Use `raise:` to raise your own errors