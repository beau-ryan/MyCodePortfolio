# Type Annotations for decimal values is (float) , whole numbers (int)
# 20 * ________+ ________ = 65535 ?? 
# Optional Exercise:
# Ask yourself why you didn't solve the problem in a different way. 
# Write it down and try to think about the reasons for choosing the method that you chose. 
# Answer: Below is what I came up with I didnt think to hard  about it.
# just simply had a go at this Exercise and I came up with this.

x = 20
a: float = 1638.375 
b: float = 1638.375
'''
1. first calcuation
------------------------
'''
a1: float = 3276.75
b1: float = 3276.75
s: float = 3276.75
'''
2. added to equation
------------------------
'''
a2: int  = 2
b2: int  = 10
t: int  = 65535
'''
3. changed equation
------------------------
'''
print(int(x * (a + b) ))
print(int(x * a1 + b1- s))
print(int(t / a2 * x / b2))