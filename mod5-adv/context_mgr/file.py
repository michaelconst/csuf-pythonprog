class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # def __exit__(self, *args):
    #     self.file.close()
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type == ValueError:
            print("error opening the file {} in {} mode: {}"
                  .format(self.filename, self.mode, str(exc_value)))
            return True


if __name__ == '__main__':
    files = []
    for _ in range(1000):
        with File('foo.txt', 'w') as wfile:
            wfile.write('foo')
            files.append(wfile)

    print('opened the file {} times'.format(len(files)))
    
    files.clear()
    with File('foo.txt', 'r') as rfile:
        data = rfile.read(128)
        if data == 'foo':
            raise ValueError('foo is wrong')