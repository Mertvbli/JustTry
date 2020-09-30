# 10.10 Frequent Words

def read_files(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().count('there')
        print(f"The file {filename} has about {words} words 'the' ")

filename = 'The White Czar.txt'
read_files(filename)

