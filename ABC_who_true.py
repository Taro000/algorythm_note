def A_speak(A, B):
    if A:
        B = False
    else:
        B = True
    return B


def B_speak(B, C):
    if B:
        C = False
    else:
        C = True
    return C


def C_speak(C, A, B):
    if C:
        A, B = [False, False]
    else:
        A, B = [True, True]
    return A, B


if __name__ == "__main__":
    A = False
    B = False
    C = False

    A_speak(A, B)
    B_speak(B, C)
    C_speak(C, A, B)

    print(A, B, C)
