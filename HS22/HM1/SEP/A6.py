import numpy as np


def huserjan_neusccyr_S10_Aufg3a(A, b, x0, tol, opt):
    # L-D-R-Zerlegung für A
    def decomposite_A(A):
        D = np.diag(np.diag(A))
        D_inv = np.linalg.inv(D)
        L = np.tril(A, -1)
        R = np.triu(A, 1)

        return [D, D_inv, L, R]


    # Mittels a-priori die geschätzten Iterationen,
    # um die Toleranz tol zu erreichen, berechnen
    def estimate_iteration(B, x0, x1, tol):
        B_norm = np.linalg.norm(B, np.inf)
        x_norm = np.linalg.norm(x1 - x0, np.inf)

        n = np.log(((1 - B_norm) / x_norm) * tol) / np.log(B_norm)

        return n


    # Mittels a-posteriori die Fehlerabschätzung
    # von x und x+1 berechnen
    def error(B, x, xn):
        B_norm = np.linalg.norm(B, np.inf)
        x_norm = np.linalg.norm(xn - x, np.inf)

        err = (B_norm / (1 - B_norm)) * x_norm

        return err


    # Berechnet für ein gegebenes Verfahren und B den Wert x
    def execute(B, x0, tol, calculate_xn):
        x1 = calculate_xn(x0)
        print ("X1",x1)
        est_iteration = estimate_iteration(B, x0, x1, tol)

        iteration = 0
        x = x0
        while True:
            iteration += 1
            xn = calculate_xn(x)

            if error(B, x, xn) <= tol:
                break
            else:
                x = xn

        return [xn, iteration, est_iteration]


    def jacobi(A, b, x0, tol):
        [D, D_inv, L, R] = decomposite_A(A)
        B = np.dot(-1, D_inv.dot(np.add(L, R)))

        def calculate_xn(x):
            return np.add(B.dot(x), D_inv.dot(b))

        return execute(B, x0, tol, calculate_xn)


    def gauss_seidel(A, b, x0, tol):
        [D, D_inv, L, R] = decomposite_A(A)
        B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(R))

        def calculate_xn(x):
            return np.add(B.dot(x), np.linalg.inv(np.add(D, L)).dot(b))

        return execute(B, x0, tol, calculate_xn)

    if opt == "JAC":
        return jacobi(A, b, x0, tol)
    elif opt == "GASE":
        return gauss_seidel(A, b, x0, tol)
    else:
        raise Exception("unknown opt '" + opt + "'")


if __name__ == "__main__":
    A = np.array([[4, -1, 1],
                  [-2, 5, 1],
                  [1, -2, 5]])

    b = np.array([[5, 11, 12]]).reshape(3, 1)
    x = np.array([[0, 0, 0]]).reshape(3, 1)

    [xn, n, n2] = huserjan_neusccyr_S10_Aufg3a(A, b, x, 1e-4, "JAC")

    print(xn, n, n2)