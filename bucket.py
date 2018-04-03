num_list = [3,2,5,4,2,3,1,5,0]

num_list2 = [32,26,51,44,21,31,17,52,33,400,455,98,1030,579,800,0]


def bucket_sort(array, bucket_count):
  if len(array)==0 or len(array)==1:
    return array

  maxs = max(array)

  buckets = [list() for _ in range(bucket_count)]

  bucket_range = (maxs / bucket_count)

  for i in range(0, len(array)):
    if array[i] == 0:
      buckets[0].insert(0,array[i])
      # for some reason 0 turns in 8
    else:
      buckets[math.ceil(array[i] / bucket_range)-1].append(array[i])
      #You have to -1 to index in the use case that your max number is equal to your bucket_count. Alternatively you can do the range(bucket_count+1) to create an extra list like laurens code had but I feel like that defeats the purpose of the bucket_count parameter.

  newArray = []
  for b in buckets:
    if len(b)==1:
      newArray.append(b[0])
    else:
      for i in range(1,len(b)):
        while i>0 and b[i-1]>b[i]:
          b[i],b[i-1]=b[i-1],b[i]
          i -=1

      newArray.extend(b)

  return newArray


# print(bucket_sort(num_list2, 5))

from contextlib import contextmanager
from timeit import default_timer

@contextmanager
def elapsed_timer():
    start = default_timer()
    elapser = lambda: default_timer() - start
    yield lambda: elapser()
    end = default_timer()
    elapser = lambda: end-start


with elapsed_timer() as elapsed:
    sorted_list = bucket_sort(num_list, 5)
    print(elapsed())
    print(sorted_list)
