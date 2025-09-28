Các bài toán sưu tầm
********************

Олимпиада Якут
==============

.. exercise:: 
    :label: yakut-1

    Tính :math:`\lim\limits_{t \to +\infty} t \sum\limits_{k=1}^{+\infty} \dfrac{1}{k^2 + t^2}`.

Ta có công thức thông dụng

.. math:: \int \frac{dx}{x^2 + t^2} = \frac{1}{t} \arctan \frac{x}{t}.

Ta có chặn

.. math:: \frac{1}{(k+1)^2 + t^2} \leqslant \int\limits_{k}^{k+1} \frac{dx}{x^2 + t^2} \leqslant \frac{1}{k^2 + t^2},

suy ra

.. math:: \frac{1}{k^2 + t^2} \leqslant \int\limits_{k-1}^k \frac{dx}{x^2 + t^2}.

Cộng tất cả phương trình trên với :math:`k=1, 2, \ldots` thì

.. math:: \sum_{k=1}^\infty \frac{1}{k^2 + t^2} \leqslant \int\limits_0^{+\infty} \frac{dx}{x^2 + t^2} = \frac{1}{t} \cdot \arctan \frac{x}{t} \Big|_0^{+\infty} = \frac{1}{t} \cdot \frac{\pi}{2}.

Tương tự

.. math:: 

    & \int\limits_{k}^{k+1} \frac{dx}{x^2 + t^2} \leqslant \frac{1}{k^2 + t^2} \\
    \Rightarrow & \int\limits_{1}^\infty \frac{dx}{x^2 + t^2} \leqslant \sum_{k=1}^\infty \frac{1}{k^2 + t^2}

Do

.. math:: \int\limits_1^\infty \frac{dx}{x^2 + t^2} = \frac{1}{t} \arctan \frac{x}{t} \Big|_1^\infty = \frac{1}{t} \left( \frac{\pi}{2} - \arctan \frac{1}{t} \right)

nên

.. math:: \left( \frac{\pi}{2} - \arctan \frac{1}{t} \right) \leqslant t \sum_{k=1}^\infty \frac{1}{k^2 + t^2} \leqslant \frac{\pi}{2}.

Như vậy

.. math:: \lim\left(\frac{\pi}{2} - \arctan \frac{1}{t}\right) = \lim \frac{\pi}{2} = \frac{\pi}{2}

khi :math:`t \to \infty`.

.. exercise:: 

    Giải phương trình

    .. math:: 19^x - 13^x = 9^x - 3^x.

Dễ thấy :math:`x = 0` là một nghiệm của phương trình.

Giả sử phương trình có nghiệm khác :math:`0` là :math:`x`.

Cố định :math:`x`, đặt :math:`g(t) = t^x`.

Theo định lí Lagrange, tồn tại :math:`\xi \in (a, b)` để :math:`g(a) - g(b) = g'(\xi) \cdot (a - b)`.

Như vậy

.. math:: g'(\xi) \cdot (19 - 13) = g'(\eta) \cdot (9 - 6)

với :math:`\xi \in (13, 19)` và :math:`\eta \in (6, 9)`. Suy ra :math:`g'(\xi) = g'(\eta)`, nói cách khác là

.. math:: x \cdot \xi^{x-1} = x \cdot \eta^{x-1}

mà :math:`x \neq 0` nên :math:`\left(\dfrac{\xi}{\eta}\right)^{x-1} = 1`. Điều này chỉ xảy ra khi :math:`x-1 = 0`, hay :math:`x = 1`.

Kết luận: phương trình có hai nghiệm là :math:`x = 0` và :math:`x = 1`.
