def bubble_sort(array):
  count = 0
  for i in range(0,len(array)-1):
    # print(array)
    if array[i] > array[i+1]:
      count += 1
      array[i],array[i+1] = array[i+1],array[i]
      bubble_sort(array)
  return array

hoo = [3,2,4,8,9,7,8, 1]
# print(bubble_sort(hoo))

def bubble_sorts(array):
  not_sorted = True
  while(not_sorted):
    not_sorted = False
    for i in range(0,len(array)-1):
      if array[i] > array[i+1]:
        not_sorted = True
        array[i],array[i+1] = array[i+1],array[i]
  return array

# print(bubble_sorts(hoo))
