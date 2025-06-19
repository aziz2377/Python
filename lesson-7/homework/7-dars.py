#1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

#2
def digit_sum(k):
    total=0
    while k>0:
        total += k % 10
        k//= 10
    return total

print(digit_sum(346))

#3
def print_powers_of_two(n):
    x = 2
    while x <= n:
        print(x, end=' ')
        x *= 2
print(print_powers_of_two(33))
