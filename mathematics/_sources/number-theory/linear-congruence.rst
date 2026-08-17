Phương trình đồng dư tuyến tính
*******************************

Cho :math:`n` là số nguyên dương và :math:`a`, :math:`b` là các số nguyên dương nhỏ hơn :math:`n`. Phương trình đồng dư tuyến tính modulo :math:`n` có dạng

.. math:: 
    :label: eq-lin-cong
    
    a x \equiv b \pmod n

với :math:`x` là ẩn.

.. prf:remark:: 
    :label: rmk-lin-cong

    Đặt :math:`d = \gcd(a, n)`. Khi đó, phương trình đồng dư có nghiệm khi và chỉ khi :math:`d \mid b`.

    Nếu :math:`x_0` là nghiệm thì phương trình có đúng :math:`d` nghiệm không đồng dư theo modulo :math:`n`.

Việc chứng minh điều kiện đủ của nhận xét trên cho ta điều kiện để phương trình có nghiệm, trong khi chứng minh điều kiện cần sẽ cho ta cách tìm nghiệm đó.

Do :math:`d = \gcd(a, n)`, khi đó tồn tại các số nguyên :math:`a_1` và :math:`n_1` sao cho :math:`a = d a_1` và :math:`n = d n_1`.

**Điều kiện đủ**. Giả sử phương trình có nghiệm :math:`x_0`, khi đó phương trình tương đương với

.. math:: a x_0 - b = k n \Longleftrightarrow d a_1 x_0 - b = k n = k d n_1, \ k \in \mathbb{Z}.

Như vậy ta có

.. math:: d \mid (d a_1 x_0 - k d n_1 = b),

hay :math:`d \mid b`.

**Điều kiện cần**. Nếu ta có :math:`d \mid b` thì ta suy ra

.. math:: a x \equiv b \pmod n \Longrightarrow \frac{a}{d} x \equiv \frac{b}{d} \pmod{\frac{n}{d}}.

Đặt :math:`b_1 = b / d`. Vì :math:`d = \gcd(a, n)` nên :math:`\gcd(a_1, n_1) = 1`, Theo bổ đề Bezout thì tồn tại các số :math:`u, v \in \mathbb{Z}` sao cho

.. math:: a_1 u + n_1 v = 1 \Longrightarrow d a_1 u + d n_1 v = d \Longleftrightarrow a u + n v = d.

Nhân hai vế đẳng thức cuối với :math:`b_1` ta có

.. math:: a b_1 u + n b_1 v = d b_1 = b \Longrightarrow a (b_1 u) \equiv b \pmod n.

Như vậy :math:`x_0 = b_1 u` là một nghiệm của phương trình đồng dư :math:`ax \equiv b \pmod n`.

Tiếp theo chúng ta chứng minh phương trình có :math:`d` nghiệm không đồng dư modulo :math:`n`. Giả sử :math:`x_1` là một nghiệm khác :math:`x_0`. Khi đó

.. math:: a (x_1 - x_0) \equiv 0 \pmod n \Longrightarrow n \mid a(x_1 - x_0).

Do :math:`d = \gcd(a, n)` nên ta suy ra :math:`n_1 \mid a_1 (x_1 - x_0)`, và do :math:`\gcd(a_1, n_1) = 1` từ trên nên ta tiếp tục suy ra :math:`n_1 \mid (x_1 - x_0)`. Như vậy tồn tại :math:`k \in \mathbb{Z}` để :math:`x_1 = x_0 + k n_1`, nghĩa là mọi nghiệm của phương trình đều có dạng :math:`x_0 + k n_1` với :math:`k \in \mathbb{Z}`.

Ngoài ra, theo thuật chia Euclid, với hai số nguyên :math:`k` và :math:`d` luôn tồn tại hai số nguyên :math:`q` và :math:`r` để :math:`k = qd + r` với :math:`0 \leqslant r < d`. Khi đó

.. math:: x_1 = x_0 + k n_1 = x_0 + (qd + r) n_1 = x_0 + (d n_1) q + r n_1 = x_0 + r n_1 + n q,

nói cách khác nghiệm :math:`x_1` đồng dư theo dạng

.. math:: x_1 \equiv x_0 + r n_1 \pmod n.

Vì :math:`0 \leqslant r < d` nên ta có họ các nghiệm không đồng dư của phương trình ban đầu là

.. math:: x_0 + 0 \cdot n_1, x_0 + 1 \cdot n_1, \ldots, x_0 + (d-1) \cdot n_1.

.. prf:example:: 
    :label: exp-lin-cong

    Xét phương trình :math:`9x \equiv 6 \bmod 12`. Vì :math:`3 = \gcd(9, 12)` và :math:`3 \mid 6` nên phương trình có nghiệm.

    Chia các vế của phương trình cho :math:`3` ta được :math:`3x \equiv 2 \bmod 4`. Như vậy, dùng thuật toán Euclid mở rộng, ta tính

    .. math:: x_0 \equiv 3^{-1} \cdot 2 \equiv 3 \cdot 2 \equiv 2 \bmod 4.

    Các nghiệm của phương trình là

    .. math:: x_0 = 2 + 0 \cdot 4 = 2, x_1 = 2 + 1 \cdot 4 = 6, x_2 = 2 + 2 \cdot 4 = 10.
