def rgb(r, g, b):
    rs = hex(max(0,min(r, 255)))[2:].upper().zfill(2)
    gs = hex(max(0,min(g, 255)))[2:].upper().zfill(2)
    bs = hex(max(0,min(b, 255)))[2:].upper().zfill(2)
    return rs+gs+bs