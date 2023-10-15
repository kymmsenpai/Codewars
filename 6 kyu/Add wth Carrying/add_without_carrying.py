def addition_without_carrying(a,b):
    max_len = max(len(str(a)), len(str(b)))
    padded_a = str(a).zfill(max_len)
    padded_b = str(b).zfill(max_len)
    return int("".join([str(int(padded_a[n])+int(padded_b[n]))[-1] for n in range(max_len)]))