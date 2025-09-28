
=====================
Giới thiệu về đa thức
=====================

.. prf:definition:: Đa thức một biến
    :label: def-univariate-poly
    
    **Đa thức theo một biến** :math:`x` là hàm số có dạng

    .. math:: 

        P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0.

Các số :math:`a_i` được gọi là **hệ số** (hay **coefficient**, **коэффициент**).

Hệ số bậc cao nhất là :math:`a_n`. Hệ số tự do là :math:`a_0`.

Biểu thức :math:`a_k x^k` được gọi là **hạng tử bậc** :math:`k`. Hạng tử bậc cao nhất là :math:`a_n x^n`.

1. Nếu :math:`a_i \in \mathbb{R}` thì ta nói :math:`P(x)` là đa thức với hệ số thực.
2. Nếu :math:`a_i \in \mathbb{Q}` thì ta nói :math:`P(x)` là đa thức với hệ số hữu tỷ.
3. Nếu :math:`a_i \in \mathbb{Z}` thì ta nói :math:`P(x)` là đa thức với hệ số nguyên.

.. prf:definition:: Bậc của đa thức
    :label: def-deg-poly
    
    Nếu :math:`a_n \neq 0` thì số tự nhiên :math:`n` được gọi là **bậc của đa thức** (hay **degree**, **степень**) và ta kí hiệu :math:`\deg P = n`.

======================================
So sánh, cộng, trừ và nhân hai đa thức
======================================

Hai đa thức

.. math:: P(x) = a_m x^m + a_{m-1} x^{m-1} + \cdots + a_1 x + a_0

và

.. math:: Q(x) = b_n x^n + b_{n-1} x^{n-1} + \cdots + b_1 x + b_0

bằng nhau khi và chỉ khi :math:`m = n`, và :math:`a_k = b_k` với mọi :math:`k = 0, 1, \ldots, m`.

Khi cộng và trừ hai đa thức :math:`P(x)` và :math:`Q(x)` ta thực hiện theo từng hệ số của :math:`x^k`, nghĩa là

.. math:: P(x) \pm Q(x) = \sum_{k=0}^{\max(m, n)} (a_k \pm b_k) \ x^k.

.. prf:example:: 
    :label: exp-pm-poly

    Xét hai đa thức

    .. math::

        P(x) & = x^3 - 4 x^2 - 5 x + 3, \\
        Q(x) & = x^4 - 3 x^3 + 5 x^2 - x - 1.

    Lúc này hệ số của hai đa thức :math:`P(x)` và :math:`Q(x)` là

    .. math::

        a_4 = 0, a_3 = 1, a_2 = -4, a_1 = -5, a_0 = 3, \\
        b_4 = 1, b_3 = -3, b_2 = 5, b_1 = -1, b_0 = -1.

    Như vậy ta có tổng và hiệu

    .. math::

        P(x) + Q(x) & = (0 + 1) \cdot x^4 + [1 + (-3)] \cdot x^3 + (-4 + 5) \cdot x^2 + [-5 + (-1)] \cdot x + [3 + (-1)] \\
        & = x^4 - 2 x^3 + x^2 - 6x + 2. \\
        P(x) - Q(x) & = (0 - 1) \cdot x^4 + [1 - (-3)] \cdot x^3 + (-4 - 5) \cdot x^2 + [-5 - (-1)] \cdot x + [3 - (-1)] \\
        & = -x^4 + 4x^3 - 9x^2 - 4x + 4.

Khi nhân hai đa thức :math:`P(x)` và :math:`Q(x)` ta nhận được đa thức bậc :math:`m+n` là

.. math:: R(x) = \sum_{k=0}^{m+n} c_k x^k

với hệ số :math:`c_k` được xác định bởi

.. math:: c_k = \sum_{i=0}^k a_i b_{k-i}.

.. prf:remark:: 
    :label: rmk-poly-0
    
    Nếu đa thức :math:`P(x)` nhận mọi giá trị :math:`x \in \mathbb{R}` làm nghiệm thì :math:`P(x) \equiv 0`.

.. prf:theorem:: Bậc của tổng, hiệu và tích của các đa thức
    :label: thr-deg-pm-poly

    Cho :math:`P(x)` và :math:`Q(x)` là các đa thức bậc :math:`m` và :math:`n` tương ứng. Khi đó
    
    1. :math:`\deg (P \pm Q) \leqslant \max(m, n)`, trong đó
   
       - Nếu :math:`\deg P \neq \deg Q` thì dấu bằng xảy ra.
       - Nếu :math:`\deg P = \deg Q`, hay :math:`m = n`, thì :math:`\deg(P \pm Q)` có thể nhận bất kì giá trị nào nhỏ hơn hoặc bằng :math:`m`.

    2. :math:`\deg (P \cdot Q) = m + n`.


.. prf:example:: 
    :label: exp-thr-pm-poly

    Xét đa thức :math:`P(x) = -x + 1` và :math:`Q(x) = x + 1`. Khi đó

    .. math:: \deg P = 1, \quad \deg Q = 1

    và

    .. math:: P(x) + Q(x) = 2, \quad P(x) - Q(x) = -2x.

    Như vậy

    .. math::
        
        \deg (P+Q) = 0 < \max(\deg P, \deg Q),

        \deg (P-Q) = 1 = \max(\deg P, \deg Q).
