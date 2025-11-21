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
    
    Nếu :math:`a_n \neq 0` thì số tự nhiên :math:`n` được gọi là **bậc** của đa thức (hay **degree**, **степень**) và ta kí hiệu :math:`\deg P = n`.

So sánh, cộng, trừ và nhân hai đa thức một biến
===============================================

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

Phép chia đa thức một biến
==========================

Khi chia đa thức :math:`A(x)` cho đa thức :math:`B(x)`, ta tìm đa thức :math:`Q(x)` và :math:`R(x)` sao cho

.. math:: A(x) = Q(x) \cdot B(x) + R(x), \ \text{và} \ 0 \leqslant \deg R(x) < \deg B(x).

Phân tích trên còn được gọi là phép chia Euclid cho đa thức.

Xét phép chia đa thức :math:`x^3 + 4 x^2 - 3` cho đa thức :math:`x - 2`. Tương tự phép chia hai số nguyên, đa thức :math:`x^3 + 4 x^2 - 3` là đa thức bị chia, :math:`x - 2` là đa thức chia, và ta cần tìm thương và số dư.

Đầu tiên, ta viết tất cả hệ số của đa thức bị chia, bao gồm các hệ số :math:`0`:

.. math:: x^3 + 4 x^2 - 0 x - 3,

và viết lên sơ đồ.

.. figure:: ../../figures/polynomials/univariate-01.*

Bước 1. Ta chia hạng tử có bậc cao nhất của đa thức bị chia là :math:`x^3` cho đa thức chia là :math:`x` và nhận được :math:`x^3 : x = x^2`. Ta viết :math:`x^2` vào phần thương (ở trên cùng).

.. figure:: ../../figures/polynomials/univariate-02.*

Bước 2. Ta nhân phần tử vừa nhận được của thương là :math:`x^2` cho đa thức chia, tức là

.. math:: x^2 \cdot (x - 2) = x^3 - 2 x^2,

và viết xuống hàng dưới.

.. figure:: ../../figures/polynomials/univariate-03.*

Bước 3. Ta trừ đa thức chia cho :math:`x^3 - 2 x^2`.

.. figure:: ../../figures/polynomials/univariate-04.*

Lặp lại các bước 1, 2, 3 nhưng hạng tử lớn nhất hiện tại là :math:`6x^2`.

Bước 1a. Ta chia :math:`6x^2` cho hạng tử bậc cao nhất của số chia và được :math:`6x^2 : x = 6x`. Ta viết :math:`+6x` vào phần thương ở trên cùng.

.. figure:: ../../figures/polynomials/univariate-05.*

Bước 2a. Ta nhân :math:`6x` cho đa thức chia

.. math:: 6x \cdot (x - 2) = 6 x^2 - 12 x,

và viết xuống hàng dưới.

.. figure:: ../../figures/polynomials/univariate-06.*

Bước 3a. Ta trừ đa thức chia, lúc này là :math:`6x^2`, cho tích vừa tìm được.

.. figure:: ../../figures/polynomials/univariate-07.*

Tiếp tục lặp lại bước 1, 2, 3.

.. figure:: ../../figures/polynomials/univariate-08.*

.. figure:: ../../figures/polynomials/univariate-09.*
    
.. figure:: ../../figures/polynomials/univariate-10.*

Sau khi thực hiện phép trừ ở bước cuối ta có đa thức thương :math:`x^2 + 6x + 12` và đa thức dư :math:`21` có bậc là :math:`0`, nhỏ hơn bậc của đa thức chia :math:`x - 2` là :math:`1`.

Phép chia đa thức nhiều biến
============================

Ở phần này kí hiệu :math:`\mathrm{LT}(f)` là leading term của đa thức nhiều biến theo thứ tự đơn thức (monomial order) cho trước (lex, deglex, ...).

Input: hàm :math:`f` và các hàm :math:`g_1`, ..., :math:`g_a` trên vành đa thức :math:`K[x_1, \ldots, x_n]` với trường :math:`K` và thứ tự đơn thức nào đó.

Output: số dư :math:`r` và các đa thức :math:`q_1`, ..., :math:`q_a` thỏa mãn

1. Không có đơn thức nào của :math:`r` chia hết :math:`\mathrm{LT}(g_i)` với mọi :math:`i`.
2. :math:`\mathrm{LT}(g_i \cdot q_i) \leqslant \mathrm{LT}(f)`.

Khi đó

.. math:: f = r + q_1 g_1 + \cdots + q_a g_g.

.. prf:algorithm:: 
    :label: alg-multivariate-polydiv

    1. Khởi tạo :math:`p \gets f`; :math:`f`, :math:`q_1`, ..., :math:`q_a \gets 0`; :math:`i \gets 0`
    2. While :math:`p \neq 0` do

       - :math:`i \gets i + 1`
       - if :math:`\mathrm{LT}(g_i) \mid \mathrm{LT}(p)` then
         
         - :math:`q_i \gets q_i + \mathrm{LT}(p) / \mathrm{LT}(g_i)`
         - :math:`p \gets p - \mathrm{LT}(p) / \mathrm{LT}(g_i)`
         - :math:`i \gets 0`

       - if :math:`i = a` then

         - :math:`r \gets r + \mathrm{LT}(p)`
         - :math:`p \gets p - \mathrm{LT}(p)`
         - :math:`i \gets 0`

    3. Return :math:`r`, :math:`q_1`, ..., :math:`q_a`

Lưu ý:

- thứ tự đơn thức ảnh hưởng kết quả thuật toán;
- :math:`r \neq 0` không có nghĩa :math:`f` không là tổ hợp tuyến tính của các đa thức :math:`g_i`.
