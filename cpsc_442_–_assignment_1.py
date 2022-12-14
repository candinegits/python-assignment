# -*- coding: utf-8 -*-
"""CPSC 442 – Assignment #1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Rbu_0b-ha6xwp2hciyf1Usqj7cKtvWb

**Problem 1:** Write a function that computes the roots of a quadratic equation. The input to the function
are the coefficients a, b, c of the quadratic equation e.g., with general form:

𝑎𝑥2 + 𝑏 𝑥 + 𝑐 = 0

For example, if

𝑥2 + 5 𝑥 + 6 = 0

Then compute_quadratic_roots function will be called as: compute_quadratic_roots(1,5,6)
"""

import math

def compute_quadratic_roots(a,b,c):
  """Return the roots of a quadratic equation with coefficients a, b and c.
  >>> compute_quadratic_roots(1,5,6)
  (-2.0, -3.0)
  """  
  equation = b*b - 4 * a * c
  sqrt = math.sqrt(abs(equation))
  r1 = 0
  r2 = 0
  if(equation > 0):
    # real and different roots
    r1 = (-b + sqrt) / (2 * a)
    r2 = (-b - sqrt) / (2 * a)

  elif(equation == 0):
    # real and same roots
    r1 = (-b / (2 * a))

  else:
    #Complext roots
    r1 =  b / (2 * a), " + i", sqrt
    r2 =  b / (2 * a), " - i", sqrt

  return r1, r2

compute_quadratic_roots(1,5,6)

"""**Problem #2:** Write a function that will return the total amount due for a loan after borrowing amount amt
for n months with an interest rate of r%.
The formula for compound interest rate calculation is:
𝑇𝑜𝑡𝑎𝑙 𝐴𝑚𝑜𝑢𝑛𝑡 = P (1 + r)𝑛/12
Where P is the starting principle amount. For example, if you borrowed $10,000 for 36 months at an
interest rate of 5%, the amount after 36 months will be: 10000 ∗ (1 + 0.05)36/12 = 11576.25
The input to the compute_total_mount_with_compound_interest function will be p, r, and n.
"""

def compute_total_mount_with_compound_interest(p, r, n):
  """Return the total amount due for a loan after borrowing amount amt for n months with an interest rate of r%.
  >>> compute_total_mount_with_compound_interest(10000,5,36)
  11576.250000000002
  """  
  return p*(1+(r/100))**(n/12)

compute_total_mount_with_compound_interest(10000, 5, 36)

"""Problem #3: Write a function that will return the monthly payment for a loan amount amt, interest rate
r, and loan duration in months n. The formula for calculating the monthly payment is:
monthly payment = amt ∗ 𝑟
1200
(1 + 𝑟
1200 )𝑛
(1 + 𝑟
1200 )𝑛 − 1
The inputs to the compute_monthly_payment function will be amt, r, and n
"""

def compute_monthly_payment(amt, r, n):
  """Return the monthly payment for a loan amount of amt, interest rate r, and loan duration in months n.
  >>> compute_monthly_payment(10000,5,36)
  299.70897104665556
  """
  return amt * ((r/1200)*(((1+(r/1200))**n)/(((1+(r/1200))**n) -1)))

compute_monthly_payment(10000, 5, 36)

"""**Problem #4:** Write a function that will compute the average of the highest and lowest number in a list."""

def list_high_low_avg(items):
  """Return the average of the highest and lowest number in a list, items
  >>> list_high_low_avg([1,2,3,4,5,7,0,9])
  4.5
  """
  lowest = min(items)
  highest = max(items)

  return (lowest+highest)/2

list_high_low_avg([1,2,3,4,5,7,0,9])

"""**Problem #5:** Write a function that will convert a given temperature in Fahrenheit to Centigrade. The
formula relating the Fahrenheit and Centigrade is: 𝐶 5 = (𝐹 − 32) 9
𝐶
5 = (F − 32)
9
"""

def fahrenheit_to_centigrade(degree_fah):
  """Return the centigrade value for a value in fahrenheit units degree_fah
  >>> fahrenheit_to_centigrade(25)
  -3.888888888888889
  """  
  return 5*((degree_fah-32)/9)

fahrenheit_to_centigrade(25)

"""**Problem #6:** Write a function to convert temperature given in Centigrade to Fahrenheit."""

def centigrade_to_fahrenheit(degree_cent):
  """Return the fahrenheit value for a value in centigrade units degree_cent
  >>> centigrade_to_fahrenheit(-3.888888888888889)
  25.0
  """
  return ((9*degree_cent)/5)+32

centigrade_to_fahrenheit(-3.888888888888889)

"""**Problem #7:** Write a function to compute the area of a circle, given its radius."""

def area_of_circle(r):
  """Return the area of a circle given the radius, r
  >>> area_of_circle(2)
  12.56636
  """  
  PI = 3.14159
  return PI*(r**2);

area_of_circle(2)

"""**Problem #8:** Write a function to compute the volume of a cylinder given its length and diameter."""

def volume_of_cylinder(l, d):
  """Return the volume of a cylnder given the length and diameter l and d
  >>> volume_of_cylinder(4, 2)
  12.56636
  """   
  PI = 3.14159
  return PI*((d/2)**2)*l

volume_of_cylinder(4, 2)

import doctest

# call the testmod function
if __name__ == '__main__':
    doctest.testmod(verbose = True)

