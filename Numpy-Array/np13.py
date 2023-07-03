import numpy as np

# Membuat matriks dengan tipe data
a = np.array(([1,2,3], [3,4,5]) , dtype = float)

# Membuat array dengan FUNCTION

def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return baris + kolom

b = np.fromfunction(kuadrat,(1,10),dtype=int)
c = np.fromfunction(jumlah,(1,10),dtype=float)
print(b)
print(c)

# Membuat array atau matrix dengan menggunakan iterable

iterable = (x*2 for x in range(10))

d = np.fromiter(iterable,dtype=int)

# Multiple array 

dtipe = [('Nama', 'S225'), ('tinggi',int)]

data = [
    ('ucup', 150),
    ('otong', 160),
    ('mario', 180),
    ('jono',190)
]

e = np.array(data,dtype = dtipe)

print(e)
