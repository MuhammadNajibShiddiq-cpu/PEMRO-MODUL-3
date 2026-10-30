a, b, c = map(int, input("Masukkan angka: ").split() )
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c: 
    b, c = c, b

print(f"Output: {a} {b} {c}")