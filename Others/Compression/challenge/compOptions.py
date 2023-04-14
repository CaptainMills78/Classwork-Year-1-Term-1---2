def compZlib(text):
    import zlib
    compText = zlib.compress(text.encode('utf-8'))
    return compText


def compGzip(text):
    import gzip
    compText = gzip.compress(text.encode('utf-8'))
    return compText


def compBz2(text):
    import bz2
    compText = bz2.compress(text.encode('utf-8'))
    return compText


if __name__ == "__main__":
    s = "Hello there, general kenobi"
    print(len(s))
    print(s.encode("utf-8"))
    print(compGzip(s))
    print(compGzip(s).decode('utf-8'))
    print(compZlib(s))
    print(compBz2(s))

