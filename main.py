def is_prime(x):
  '''
  Determina daca un numar este prim sau nu
  '''
  ok = True
  if x < 2:
    ok = False
  else:
    for i in range(2, x // 2 + 1):
      if x % i == 0:
        ok = False
  if ok == True:
    print('Numarul este prim')
  else:
    print('Numarul nu este prim')


def get_produs(n):
  '''
  Determina produsul a n numere naturale
  '''
  p = 1
  for i in range(n):
    x = int(input('Dati numarul '))
    p = p * x
  return p


def get_cmmdc_v1(a, b):
  '''
  Determina cel mai mare divizor comun a 2 numere
  '''
  if a < 0:
    a = -a
  if b < 0:
    b = -b

  if a == b:
    return a
  elif a < b:
    b = b - a
  else:
    a = a - b
  return a


def get_cmmdc_v2(a, b):
  '''
  Determina cel mai mare divizor comun a 2 numere
  '''
  if a < 0:
    a = -a
  if b < 0:
    b = -b

  while (b != 0):
    t = b
    b = a % b
    a = t

  return a


def test_cmmdc1():
  assert get_cmmdc_v1(3, 6) == 3
  assert get_cmmdc_v1(2, 2) == 2
  assert get_cmmdc_v1(15, 90) == 15


def test_cmmdc2():
  assert get_cmmdc_v2(3, 6) == 3
  assert get_cmmdc_v2(8, 40) == 8
  assert get_cmmdc_v2(15, 90) == 15


def print_menu():
  print('1.Determina daca un numar este sau nu prim')
  print('2.Produsul a n numere naturale')
  print('3.Cmmdc1 ')
  print('4.Cmmdc2 ')


def main():
  while True:
    print_menu()
    opt = int(input('Dati optiunea: '))
    if opt == 1:
      x = int(input('Dati numarul: '))
      is_prime(x)
    elif opt == 2:
      n = int(input('Dati cate numere doriti sa introduceti: '))
      print(get_produs(n))
    elif opt == 3:
      a = int(input('Dati numarul a: '))
      b = int(input('Dati numarul b: '))
      print(get_cmmdc_v1(a, b))
    elif opt == 4:
      a = int(input('Dati numarul a: '))
      b = int(input('Dati numarul b: '))
      print(get_cmmdc_v2(a, b))
    else:
      break


test_cmmdc2()
test_cmmdc1()
main()

if __name__ == '__main__':
  main()
