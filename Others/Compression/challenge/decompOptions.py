def decompZlib(text):
    import zlib
    decompText = zlib.decompress(text)
    return decompText


def decompGzip(text):
    import gzip
    decompText = gzip.decompress(text)
    return decompText


def decompBz2(text):
    import bz2
    decompText = bz2.decompress(text)
    return decompText
