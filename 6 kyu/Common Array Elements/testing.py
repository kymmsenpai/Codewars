from common_array import common

lst_questions = [
  common([1,2,3],[5,3,2],[7,3,2]),
  common([1,2,2,3],[5,3,2,2],[7,3,2,2]),
  common([1],[1],[1]),
  common([1],[1],[2])
]

print([lq for lq in lst_questions])