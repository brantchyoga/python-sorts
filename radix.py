
aduck = [1,18,7,1090,139,43,45,98,54]


def radix_sort(alit):
  RADIX = 10
  big = max(alit)
  placement = 1
  print(len(str(big)))

# loop for as many times as the max numbers digit place
  for _ in range(len(str(big))):
    # create 10 lists 0-9
    buckets = [list() for _ in range( RADIX )]
    #loop through array
    for i in alit:
    # find the bucket index that corresponds to that elements digit
    # ie i=11 where placement=1 for ones digit and append that number
      buckets[(i//placement)%RADIX].append(i)
    print(buckets)
    #initiate a count so as to keep an index for the array
    count = 0
    #loop through every bucket with that buckets elements
    for b in buckets:
        #then loop through the elements in that bucket
      for bs in b:
        # at the counts index set that element
        alit[count]=bs
        count+=1
        # count up to new index
    placement*=RADIX
    #the loop * 10 to placement so next loop looks at 10 digit and so on...
  return alit


print(radix_sort(aduck))
s = 'hello'
print(s[::-1])
