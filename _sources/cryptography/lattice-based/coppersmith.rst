=======================
Phương pháp Coppersmith
=======================

Phương pháp Coppersmith được dùng để tìm nghiệm nhỏ 
của đa thức trên modulo. Phần này mình tham khảo chính 
từ :cite:`Galbraith`.

--------
Ý tưởng
--------

Giả sử ta có phương trình :math:`F(x) \equiv 0 \bmod M`. 
Với số :math:`X` cố định cho trước, phương pháp Coppersmith 
cho phép tìm nghiệm :math:`x_0` nhỏ thỏa mãn :math:`\lvert x_0 \rvert \leqslant X`.

Ý tưởng của phương pháp này là thay vì tìm nghiệm 
:math:`x_0` của :math:`F(x)` trên modulo :math:`M`, chúng 
ta sẽ mở rộng lên, tìm một hàm :math:`G(x)` nào đó mà 
có nghiệm :math:`x_0` trên :math:`\mathbb{Z}`.

Đơn giản nhất là

.. math:: G(x) = k \cdot F(x) + M \cdot g(x), \ k \in \mathbb{Z}

và :math:`\deg g(x) \leqslant \deg F(x)`. Rõ ràng khi 
modulo hai vế cho :math:`M` thì :math:`G(x_0) = F(x_0) = 0 \bmod M`.

Phương pháp này giúp tìm nghiệm của một đa thức bậc nhỏ 
modulo :math:`M`. Do đó giả sử đặt:

.. math:: F(x) = a_0 + a_1 x + \cdots + a_d x^d

với :math:`a_i \in \mathbb{Z}`.

Lúc này chúng ta sẽ tìm hàm :math:`G(x)` trên với hệ 
số nhỏ.

Giả sử

.. math:: g(x) = b_0 + b_1 x + \cdots + b_d x^d

với :math:`b_i \in \mathbb{Z}`.

Khi đó

.. math:: G(x) = (k \cdot a_0 + M \cdot b_0) + (k \cdot a_1 + M \cdot b_1) x + \cdots + (k \cdot a_d + M \cdot b_d) x^d.

Ta mong muốn các hệ số :math:`k \cdot a_0 + M \cdot b_0`, 
:math:`k \cdot a_1 + M \cdot b_1`, 
:math:`\cdots`, :math:`k \cdot a_d + M \cdot b_d` nhỏ so 
với :math:`M`.

Do đó với số :math:`X` cho trước, nếu ta xây lattice 
(:math:`d+2` vector) sau:

.. math:: 

	\begin{array}{cccccccc}
		\bm{v}_0 & \Leftarrow & M & 0 & 0 & \cdots & 0 & 0 \\
		\bm{v}_1 & \Leftarrow & 0 & MX & 0 & \cdots & 0 & 0 \\
		\vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
		\bm{v}_d & \Leftarrow & 0 & 0 & 0 & \cdots & 0 & MX^d \\
		\bm{v}_{d+1} & \Leftarrow & a_0 & a_1 X & a_2 X^2 & \cdots & a_{d-1} X^{d-1} & a_d X^d
	\end{array}

Khi đó hệ số của mỗi dòng từ :math:`\bm{v}_0` tới 
:math:`\bm{v}_d` là :math:`b_0` tới :math:`b_d`. Còn 
hệ số của :math:`\bm{v}_{d+1}` là :math:`k`.

Tuy nhiên chúng ta thường sẽ biến đổi để đa thức trở thành 
monic (:math:`a_d = 1`). Khi đó chúng ta bỏ đi :math:`v_d` và 
còn :math:`d+1` vector trong lattice.

-------------------
Cải tiến thuật toán
-------------------

^^^^^^^^^^^^^^
Dạng đơn giản
^^^^^^^^^^^^^^

Giả sử :math:`k(x)` có bậc là :math:`h`. Đặt 
:math:`k(x) = c_0 + c_1 x + \cdots + c_h x^h`.

Khi đó:

.. math:: 

	G(x) = & k(x) \cdot F(x) + M \cdot g(x) \\
	= & (c_0 + c_1 x + \cdots c_h x^h) \cdot (a_0 + a_1 x + \cdots + x^d) + M \cdot (b_0 + b_1 x + \cdots + b_d x^d) \\
	= & c_0 \cdot F(x) + c_1 \cdot xF(x) + \cdots c_h \cdot x^h F(x) + M \cdot (b_0 + b_1 x + \cdots b_d x^d)

Lúc này mỗi đại lượng :math:`F(x)`, :math:`xF(x)`, ..., 
:math:`x^h F(x)` sẽ khiến hệ số của :math:`F(x)` ban đầu 
tăng bậc. Nói cách khác hệ số :math:`a_i` của :math:`x^i` 
trong :math:`F(x)` sẽ là hệ số của :math:`x^{i+j}` trong 
:math:`x^j F(x)`.

Sách giáo khoa nói rằng nếu mình chọn :math:`h = d - 1` thì 
phương pháp Coppersmith sẽ cho ra kết quả nếu :math:`X` được 
chọn thỏa :math:`X \approx M^{1/(2d-1)}`.

Tương tự, mình sẽ có các vector trong lattice như sau:

.. math:: 

    \begin{array}{ccccccccccc}
        \bm{v}_0 & \Leftarrow & M & 0 & 0 & \cdots & 0 & 0 & 0 & 0 & \cdots \\
        \bm{v}_1 & \Leftarrow & 0 & MX & 0 & \cdots & 0 & 0 & 0 & 0 & \cdots \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        \bm{v}_{d-1} & \Leftarrow & 0 & 0 & 0 & \cdots & MX^{d-1} & 0 & 0 & 0 & \cdots \\
        \bm{v}_d & \Leftarrow & a_0 & a_1 X & a_2 X^2 & \cdots & a_{d-1} X^{d-1} & X^d & 0 & 0 & \cdots
    \end{array}

Sau đó thêm các vector khi shift vào, tương ứng với 
:math:`xF(x)`, :math:`x^2 F(x)`, ...

.. math:: 

    \begin{array}{cccccccccccc}
        \bm{v}_{d+1} & \Leftarrow & 0 & a_0 X & a_1 X^2 & a_2 X^3 & \cdots & a_{d-1} X^d & a_d X^{d+1} & 0 & 0 & \cdots \\
        \bm{v}_{d+2} & \Leftarrow & 0 & 0 & a_0 X^2 & a_1 X^3 & \cdots & a_{d-2} X^d & a_{d-1} X^{d+1} & a_d X^{d+2} & 0 & \cdots
    \end{array}

Tuy nhiên vấn đề ở đây là bound của nghiệm bị thu hẹp lại. 
Ban nãy mình nói rằng nếu chọn :math:`h=d-1` thì nghiệm cho 
kết quả nếu :math:`X \approx M^{1/(2d-1)}`. Ở đây :math:`M = 10001` 
nên :math:`X \approx 4`. Trong khi ở bài viết trước thì 
:math:`X = 10`. Do đó có thể thấy việc mở rộng này đôi khi 
kém hiệu quả tùy thuộc vào :math:`h`.

^^^^^^^^^^^^^^
Dạng nâng cao
^^^^^^^^^^^^^^

Coppersmith đã đề xuất ý tưởng như sau:

.. prf:lemma:: Coppersmith
    :label: lem-coppersmith

    Với :math:`0 < \epsilon < \min \{0,18; 1/d\}`. Đặt 
    :math:`F(x)` là đa thức monic bậc :math:`d` có một 
    hoặc nhiều nghiệm :math:`x_0` trên modulo :math:`M` 
    sao cho :math:`\lvert x_0 \rvert \leqslant \frac{1}{2} M^{1/d-\epsilon}`. 
    Khi đó :math:`x_0` có thể tính với thời gian đa thức 
    giới hạn bởi :math:`d`, :math:`1/\epsilon` và 
    :math:`\log(M)`.

Để chứng minh bổ đề này thì Coppersmith đã xây dựng một 
hệ lattice để tính toán và cũng là cách xây dựng lattice 
sẽ đề cập tới đây.

Chúng ta biết rằng :math:`x_0` là nghiệm của đa thức 
:math:`F(x) \equiv 0 \bmod M`. Do đó ta suy ra 
:math:`F(x_0)^k \equiv 0 \bmod M^k`.

Từ nhận xét này, mình mở rộng phần cơ bản lên tìm nghiệm 
trong modulo :math:`M^{h-1}` với :math:`h` là một số được 
chọn trước.

Với :math:`k(x) = c_0 + c_1 x + \cdots + c_{d-1} x^{d-1}` 
biểu diễn việc shift thành :math:`F(x)`, :math:`xF(x)`, 
:math:`x^2 F(x)`, ..., :math:`x^{d-1} F(x)`.

Ta xét :math:`h` đa thức sau:

.. math:: 

    \begin{array}{ccc}
        M^{h-1} F(x)^0 k(x) & \equiv & 0 \bmod M^{h-1} \\
        M^{h-2} F(x)^1 k(x) & \equiv & 0 \bmod M^{h-1} \\
        \cdots & \ddots & \cdots \\
        M^0 F(x)^{h-1} k(x) & \equiv & 0 \bmod M^{h-1}
    \end{array}

Với mỗi đa thức :math:`M^{h-1-j} F(x)^j` chúng ta có :math:`d` 
lần shift tương ứng với từng hệ số của :math:`k(x)`. Cụ thể là 
:math:`M^{h-1-j}F(x)^j`, :math:`M^{h-1-j}F(x)^j x`, 
:math:`M^{h-1-j}F(x)^j x^2`, ..., :math:`M^{h-1-j}F(x)^j x^{d-1}`.

Do đó có tất cả :math:`dh` vector trong lattice. Số :math:`h` 
thường được chọn sao cho :math:`dh \approx \epsilon`. Và chặn 
nghiệm :math:`X` có thể chọn là :math:`\frac{1}{2}M^{1/d - \epsilon}` 
theo như bổ đề.

Như vậy mình xây lattice như sau:

- Bước 1. Với :math:`M^{h-1} F(x)^0` thì các vector sau lần lượt tương ứng với

.. math:: M^{h-1} F(x)^0, M^{h-1} F(x)^0 x, \ldots, M^{h-1} F(x)^0 x^{d-1}

Nói cách khác thì:

.. math:: 

    \begin{array}{ccccccccc}
        \bm{v}_0 & \Leftarrow & M^{h-1} & 0 & 0 & \cdots & 0 & 0 & \cdots \\
        \bm{v}_1 & \Leftarrow & 0 & M^{h-1} X & 0 & \cdots & 0 & 0 & \cdots \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
        \bm{v}_{d-1} & \Leftarrow & 0 & 0 & 0 & \cdots & M^{h-1} X^{d-1} & 0 & \cdots
    \end{array}

- Bước 2. Với :math:`M^{h-2} F(x)` thì các vector sau lần lượt tương ứng với

.. math:: M^{h-2} F(x)^1, M^{h-2} F(x)^1 x, \ldots, M^{h-2} F(x)^1 x^{d-1}.

Nói cách khác thì:

.. math:: 

    \begin{array}{cccccccccc}
        \bm{v}_d & \Leftarrow & Ma_0 & M a_1 X & M a_2 X^2 & \cdots & M a_{d-1} X^{d-1} & M X^d & \cdots & \cdots \\ 
        \bm{v}_{d+1} & \Leftarrow & 0 & Ma_0 X & Ma_1 X^2 & \cdots & M a_{d-2} X^{d-1} & M a_{d-1} X^d & M X^{d+1} & \cdots \\
        \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
        \bm{v}_{2d-1} & \Leftarrow & 0 & 0 & 0 & \cdots & M a_0 X^{d-1} & M a_1 X^d & \cdots & \cdots
    \end{array}

- Bước thứ :math:`j`. Cứ như vậy với :math:`M^{h-1-j}F(x)^j`.

Chạy LLL trên lattice trên sẽ cho kết quả ^^.

----------------
Code thử nghiệm
----------------

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
So sánh ví dụ đơn giản với small_roots của SageMath
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from sage.all import *

    def small_roots(f, M, X):
        d = f.degree()

        P = f.base_ring()
        B = []
        for i in range(d):
            b = [0] * (d + 1)
            b[i] = M * X**i
            B.append(b)
        B.append([j*X**i for i,j in enumerate(f.coefficients())])
        B = Matrix(ZZ, B)
        B = B.LLL()
        bf = B[0]
        g = sum((j//(X**i)) * x**i for i,j in enumerate(bf))
        roots = g.roots()
        return [root[0] for root in roots]

    M = 10001
    X = 10
    P = PolynomialRing(ZZ, 'x')
    Q = PolynomialRing(Zmod(M), 'xn')
    x = P.gen()
    xn = Q.gen()
    f = x**3 + 10*x**2 + 5000*x - 222
    g = f.change_ring(Q).subs(x=xn)
    print(small_roots(f, M, X))
    print(g.small_roots(X=10))

^^^^^^^^^^^^^^^^^^^^^^^
Cải tiến dạng đơn giản
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from sage.all import *

    def small_roots(f, M, X):
        d = f.degree()
        B = []
        for i in range(d):
            b = [0] * (2*d)
            b[i] = M * X**i
            B.append(b)
        for i in range(d):
            g = x**i * f
            b = [v * X**u for u, v in enumerate(g.coefficients(sparse=False))]
            b = b + [0] * (2*d - len(b))
            B.append(b)
        B = Matrix(ZZ, B)
        B = B.LLL()
        bf = B[0]
        g = sum((j // (X**i)) * x**i for i, j in enumerate(bf))
        roots = g.roots()
        return [root[0] for root in roots]

    M = 10001
    X = 10
    P = PolynomialRing(ZZ, 'x')
    x = P.gen()
    f = x**3 + 10*x**2 + 5000*x - 222
    print(small_roots(f, M, X))

^^^^^^^^^^^^^^^^^^^^^^^
Cải tiến dạng nâng cao
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from sage.all import *

    def small_roots(f, M, h = None, epsilon = None, X = None):
        d = f.degree()
        if not h:
            h = d
        if not epsilon:
            epsilon = 1/(d*h)
        if not X:
            X = round(0.5*M**(1/d-epsilon))
        B = []
        for j in range(h):
            g = M**(h-1-j) * f**j
            for i in range(d):
                k = g * x**i
                b = [v * X**u for u, v in enumerate(k.coefficients(sparse=False))]
                b = b + [0] * (d*h - len(b))
                B.append(b)

        B = Matrix(ZZ, B)
        B = B.LLL()
        bf = B[0]
        g = sum((j // (X**i)) * x**i for i, j in enumerate(bf))
        roots = g.roots()
        return [root[0] for root in roots]

    # Test theo sách giáo khoa

    M = (2**30 + 3)*(2**32 + 15)
    P = PolynomialRing(ZZ, 'x')
    x = P.gen()
    f = 1942528644709637042 + 1234567890123456789*x + 987654321987654321*x**2 + x**3
    print(small_roots(f, M))

    # Tự test

    M = (2**20 + 7)*(2**21 + 17)
    P = PolynomialRing(ZZ, 'x')
    x = P.gen()
    f = x**3 + (2**25 - 2883584)*x**2 + 46976195*x + 227
    print(small_roots(f, M, X = 2**9))
