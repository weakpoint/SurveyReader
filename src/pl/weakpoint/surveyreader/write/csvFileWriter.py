class CSVFileWriter:

    _file = None

    def __init__(self, path):
        self._file = open(path, 'a')

    def write(self, line):
        if self._file is not None:
            self._file.write(line + '\n')

    def close(self):
        self._file.close()


