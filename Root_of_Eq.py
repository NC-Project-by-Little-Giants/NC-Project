"""
Chapter # 2 : Solution(Root) of equations in one variable:
1.    The Bisection or Binary-search method.
2.    Fixed Point iteration. (x=g(x))
3.    Newton’s Raphson
4.    Secant Method
5.    Method of False position (Regula falsi).
6.    Steffensen Method
"""


class Root_of_Eq:

    def bisection(self, f, a, b, eps, store=False):
        fa = self.f_x(f, a)
        if fa * self.f_x(f, b) > 0:
            return None, 0, 0
        if store:
            info = [(a, b, 0.0,  fa, b-a)]
        i = 0  # iteration counter
        while abs(b - a) > eps:
            i += 1
            m = (a + b) / 2.0
            fm = self.f_x(f, m)
            if float(fa) * float(fm) <= 0:
                b = m  # root is in left half of [a,b]
            else:
                a = m  # root is in right half of [a,b]
                fa = fm
            if store:
                info.append((a, b, m, fa, b-a))
            if fm == 0:
                break
        return m, i, info

    def regulaFalsi(self, f, a, b, eps, store=False):
        i = 1
        fa = self.f_x(f, a)
        if store:
            info = [(a, b, 0.0,  fa, b-a)]

        while abs(b - a) > eps:
            p = (a * self.f_x(f, b) - b * self.f_x(f, a)) / (self.f_x(f, b) - self.f_x(f, a))
            fp = self.f_x(f, p)

            if fp == 0:
                break
            i = i + 1
            if fa * fp > 0:
                a = p
            else:
                b = p
            if store:
                info.append((a, b, p, fp, b-a))
        return p, info

    def newton(self, f, x, df_dx, eps=1.0E-7, store=False):
        f_value = self.f_x(f, x)
        n = 0
        if store:
            info = [(x, f_value, 0.0)]
        while abs(f_value) > eps:
            df_dx_value = float(self.f_x(df_dx, x))
            if abs(df_dx_value) < 1E-14:
                raise ValueError("Newton: f’(%g)=%g" % (x, df_dx_value))
            if store:
                info.append((x, f_value, (x - f_value / df_dx_value) - x))
            try:
                x = x - f_value / df_dx_value
            except ZeroDivisionError:
                print("Error! - denominator zero for x = ", x)
                exit(1)  # Abort with error
            n += 1
            f_value = self.f_x(f, x)
        if store:
            return x, info
        else:
            return x, n, f_value

    def secant(self, f, a, b, eps, store=False):
        f_a = self.f_x(f, a)
        f_b = self.f_x(f, b)
        if store:
            info = [(a, b, 0.0,  0.0, b - a)]
        while abs(f_b) > eps or abs(b - a) > eps:
            try:
                denominator = float(f_b - f_a) / (b - a)
                x = b - float(f_b) / denominator
            except ZeroDivisionError:
                print("Error! - denominator zero for x = ", x)
                exit(1)  # Abort with error
            if store:
                info = [(a, b, x, self.f_x(f, x), b - a)]
            a = b
            b = x
            f_a = f_b
            f_b = self.f_x(f, b)
            if store:
                info.append((a, b, x, f_b, b - a))
        # Here, either a solution is found, or too many iterations
            if f_b == 0:
                break
        return x, info

    # def fixed_point_iteration(self, f, p, eps, store=False):
    #     error = 1
    #     iterations = 0
    #     if store:
    #         info = [(p, 0.0)]
    #     while error > eps or p_new > eps:
    #         print("hello")
    #         p_new = self.f_x(f, p)
    #         error = abs(p_new - p)
    #         p = p_new
    #         if store:
    #             info.append((p, abs(p_new - p)))
    #     return p, info
