from model import SystemInfo

class TxtFileReader:
    @staticmethod
    def read(path):
        with open(path, "r") as f:
            lines = f.read().splitlines()

        return SystemInfo(lines[0], lines[1], lines[2])


