"""
Chapter # 2 : Solution(Root) of equations in one variable:
1.    The Bisection or Binary-search method.
2.    Fixed Point iteration. (x=g(x))
3.    Newton’s Raphson
4.    Secant Method
5.    Method of False position (Regula falsi).
"""


class Root_of_Eq:

    def bisection(self, f, a, b, eps, store=False):
        fa = self.f_x(f, a)
        if fa * self.f_x(f, b) > 0:
            return None, 0, 0
        if store:
            info = [(a, b, fa)]
        i = 0  # iteration counter
        while b - a > eps:
            i += 1
            m = (a + b) / 2.0
            fm = self.f_x(f, m)
            if float(fa) * float(fm) <= 0:
                b = m  # root is in left half of [a,b]
            else:
                a = m  # root is in right half of [a,b]
                fa = fm
            if store:
                info.append((a, b, fa))
        return m, i, info

    def newton(self, f, x, df_dx, epsilon=1.0E-7, N=100, store=False):
        f_value = self.f_x(f, x)
        n = 0
        if store:
            info = [(x, f_value)]
        while abs(f_value) > epsilon and n <= N:
            df_dx_value = float(self.f_x(df_dx, x))
            if abs(df_dx_value) < 1E-14:
                raise ValueError("Newton: f’(%g)=%g" % (x, df_dx_value))
            x = x - f_value / df_dx_value
            n += 1
            f_value = self.f_x(f, x)
            if store:
                info.append((x, f_value))
        if store:
            return x, info
        else:
            return x, n, f_value



