import re
def count_smileys(arr):
    smile_face = re.findall(r'[:;][-~][)D]|[:;][)D]', ''.join(arr))
    return smile_face

