def cekPrima(n):
    if(n == 0 or n == 1):
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

print("Bilangan awal: ", end="")
awal = int(input())
print("Bilangan akhir: ", end="")
akhir = int(input())

for x in range(awal, akhir):
    if(cekPrima(x)):
        print(x, end=" ")