# Type Annotations for decimal values is (float) , whole numbers (int)

x = 20
a: float= 1638.375 
b: float= 1638.375 
a1: float = 3276.75
b1: float = 3276.75
s: float = 3276.75
a2: int  = 2
b2: int  = 10
t: int  = 65535

print(int(x * (a + b) ))
print(int(x * a1 + b1- s))
print(int(t / a2 * x / b2))