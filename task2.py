dengi = int(input())
golova = int(input())
for a in range(1, dengi // 20 + 1):
    for b in range((dengi - a * 20) // 10 + 1):
        c = golova - a - b
        if a * 20 + b * 10 + c * 5 == dengi:
            print(a, b, c)

