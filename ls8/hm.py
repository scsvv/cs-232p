print("""
DOC
Type data in format: WORD IN ENGLISH : word, word, word
""")

vocabulary = dict() 

while True:
    data = input("Type word: ")
    if data == '0':
        break
    
    data = data.split(':')
    if len(data) == 1:
        print("Err 1: Please use ':'")
        continue
    elif len(data) > 2:
        print("Err 2: Use ':' only once")
        continue

    key = data[0]
    data = data[1].split(',') or 'N/A'

    if not(data[0].strip()):
        print("Err 3: data is empty")
        continue

    vocabulary.setdefault(key, data)


print(vocabulary)