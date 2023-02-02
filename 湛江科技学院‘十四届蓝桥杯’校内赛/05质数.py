n = 2022

prime = []
st = [True] * 2030


def get_prime(n):
    for i in range(2, n + 1):
        if st[i]:
            prime.append(i)

        for j in prime:
            if i * j > n:
                break
            st[i * j] = False
            if i % j == 0:
                break


get_prime(n)

f = [-100010] * 2030

f[0] = 0

for i in range(1, len(prime) + 1):
    for j in range(2022, prime[i - 1] - 1, -1):
        f[j] = max(f[j], f[j - prime[i - 1]] + 1)

print(f[2022])
