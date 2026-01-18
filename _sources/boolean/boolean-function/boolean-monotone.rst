Hàm đơn điệu
============

.. prf:definition:: Vector so sánh được
    :label: def-vector-comparable
    
    Xét hai vector :math:`\bm{a} = (a_1, a_2, \ldots, a_n)` và :math:`\bm{b} = (b_1, b_2, \ldots, b_n)` với :math:`a_i, b_i \in \mathbb{F}_2`.
    
    Ta nói :math:`\bm{a}` **so sánh được nhỏ hơn** :math:`\bm{b}` nếu với mọi :math:`i = 1, 2, \ldots, n` ta có :math:`a_i \leqslant b_i`. Kí hiệu :math:`\bm{a} \preccurlyeq \bm{b}`.

.. prf:example:: 
    :label: exp-vector-comparable

    Ta có :math:`(1, 0, 0) \preccurlyeq (1, 0, 1)`, còn :math:`(1, 0, 0)` và :math:`(0, 1, 0)` thì không so sánh được (vị trí thứ nhất và thứ hai).

.. prf:definition:: Hàm boolean đơn điệu
    :label: def-bool-monotone

    Hàm boolean :math:`n` biến :math:`f(x_1, x_2, \ldots, x_n)` được gọi là hàm **đơn điệu** (hay **monotone**) nếu với mọi vector :math:`(a_1, a_2, \ldots, a_n) \preccurlyeq (b_1, b_2, \ldots, b_n)` thì ta có

    .. math:: f(a_1, a_2, \ldots, a_n) \leqslant f(b_1, b_2, \ldots, b_n).

.. prf:example:: 
    :label: exp-bool-monotone

    Xét hàm boolean :math:`f(x, y) = (0, 1, 0, 1)`.

    Ta thấy rằng:
    
    * :math:`(0, 0) \preccurlyeq (0, 1)` và :math:`f(0, 0) = 0 \leqslant 1 = f(0, 1)`;
    * :math:`(0, 0) \preccurlyeq (1, 0)` và :math:`f(0, 0) = 0 \leqslant 0 = f(1, 0)`;
    * :math:`(0, 0) \preccurlyeq (1, 1)` và :math:`f(0, 0) = 0 \leqslant 1 = f(1, 1)`;
    * :math:`(0, 1)` và :math:`(1, 0)` không so sánh được nên bỏ qua;
    * :math:`(0, 1) \preccurlyeq (1, 1)` và :math:`f(0, 1) = 1 \leqslant 1 = f(1, 1)`;
    * :math:`(1, 0) \preccurlyeq (1, 1)` và :math:`f(1, 0) = 0 \leqslant 1 = f(1, 1)`.

    Vậy đây là hàm đơn điệu.
