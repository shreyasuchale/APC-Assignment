x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, 2 * n, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum = sum + sign * (x ** i) / fact
    sign *= -1

print("Cosine series value =", sum)