def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  return nums[2] + nums[1] + nums[0]

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  return [max(nums[0], nums[2])]*3

def sum2(nums):
  a = 0
  if (len(nums)):
    a = a + nums[0]
    if (len(nums) > 1):
      a = a + nums[1]
  return a
 
def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  return nums[0] in [2, 3] or nums[1] in [2, 3]



def centered_average(nums):
  return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2) 

def has22(nums):
  for i in xrange(len(nums) - 1):
    if (nums[i] == 2 and nums[i+1] == 2):
      return True
  return False

def big_diff(nums):
  min = 2^63 - 1
  max = (2^63 - 1) * -1 - 1
  for i in nums:
    if i < min:
      min = i
    if i > max:
      max = i
  return (max - min)

def count_evens(nums):
  return sum(((x+1)%2) for x in nums)