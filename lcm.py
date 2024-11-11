def gcd_lcm(num1, num2):
def gcd(a, b):
while b:
a, b = b, a % b
return a
def lcm(a, b):
return a * b // gcd(a, b)
return gcd(num1, num2), lcm(num1, num2)
num1 = 12
num2 = 18
print("GCD:", gcd_lcm(num1, num2)[0])
print("LCM:", gcd_lcm(num1, num2)[1])
