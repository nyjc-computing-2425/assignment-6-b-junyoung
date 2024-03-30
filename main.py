from datetime import datetime
import time


# Part 1
def clock(n):
  """
  Shows the time and updates it once every second, for n number of seconds

  Parameter
  ---------
  n: int
    the number of seconds

  Returns
  ---------
  nothing (print only)

  Example:
  >>> clock(3)
  12:59:17
  """

  for i in range (n):
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%H:%M:%S")
    print(formatted_date, end='\r')
    time.sleep(1)


# Part 3 (done first as lcm calls gcf)
def gcf(a, b):
  """
  Calculates the greatest common factor of a and b

  Parameters
  ---------
  a: int, b: int
    the values which the gcf will be derived from

  Returns
  ---------
  gcf as an int

  Example:
  >>> gcf(60, 48)
  12
  >>> gcf(70, 14)
  14
  """

  while (b != 0):
    temp = a
    a = b
    b = temp % b
  return a


# Part 2
def lcm(a, b):
  """
  Calculates the lcm of a and b

  Parameters
  ---------
  a: int, b: int
    the values which the lcm will be derived from

  Returns
  ---------
  lcm as an int

  Example:
  >>> lcm(2, 3)
  6
  >>> lcm(12, 5)
  60
  """

  return (a * b) // gcf(a, b)