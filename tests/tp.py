# Aucun n'import ne doit être fait dans ce fichier


def nombre_entier(n: int) -> str:
    return "S" * n + "0"


def S(n: str) -> str:
    return f"S{n}"


def addition(a: str, b: str) -> str:
    if a == "0":
        return b
    else:
        return S(addition(a[1:], b))


def multiplication(a: str, b: str) -> str:
    if a == "0":
        return "0"
    elif b == "0":
        return "0"
    else:
        return addition(b, multiplication(a[1:], b))


def facto_ite(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def facto_rec(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * facto_rec(n - 1)


def fibo_rec(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_ite(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


def golden_phi(n: int) -> int:
    if n == 0:
        return 1
    return 1 + 1/golden_phi(n-1)


def sqrt5(n: int) -> int:
    phi = golden_phi(n+1)
    return 2 * phi - 1


def pow(a: float, n: int) -> float:
    if n == 0:
        return 1
    return a * pow(a, n-1)


# On veut log_2(n)

#a^n = a*a^'(n-1)

#a^0 = 1

#a^n = a^(n // 2 + n // 2) si n est pair
#a^n = a^(n / 2) * a^(n / 2) si n est pair

#