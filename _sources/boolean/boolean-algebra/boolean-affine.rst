Hàm affine và hàm tuyến tính
============================

Hàm affine và hàm tuyến tính
----------------------------

.. prf:definition:: Hàm boolean affine
    :label: def-bool-affine
    
    Xét hàm boolean :math:`n` biến :math:`f(x_1, x_2, \ldots, x_n)`. Khi đó :math:`f` được gọi là hàm boolean **affine** nếu nó có dạng

    .. math:: f(x_1, x_2, \ldots, x_n) = a_0 \oplus a_1 x_1 \oplus a_2 x_2 \oplus \ldots \oplus a_n x_n.

    Khi :math:`a_0 = 0` thì ta gọi là hàm boolean **tuyến tính** (**linear**).

Ta thấy rằng chỉ có các hạng tử dạng :math:`a_i x_i` xuất hiện trong biểu diễn đa thức Zhegalkin tương ứng của hàm boolean đó, hay nói cách khác hàm boolean là affine khi :math:`\deg(f) = 1`.

.. prf:example:: 
    :label: exp-bool-affine-linear
    
    Hàm boolean :math:`f(x, y) = x \oplus y` là hàm boolean affine và cũng tuyến tính.
    
    Hàm boolean :math:`f(x, y) = x \oplus xy` không là hàm boolean affine.

Số lượng hàm affine và hàm tuyến tính
-------------------------------------

Ở phần trên ta đã tính được

.. math:: \lvert \mathcal{F}_n \rvert = 2^{2^n}.

Số lượng hàm boolean affine là số cách chọn các hệ số :math:`a_0`, :math:`a_1`, ..., :math:`a_n`. Như vậy cần chọn :math:`n+1` số trong :math:`\mathbb{F}_2` nên

.. math:: \lvert \mathcal{A}_n \rvert = 2^{n+1}.

Đối với hàm boolean tuyến tính thì chọn từ :math:`a_1` tới :math:`a_n` nên cần chọn :math:`n` số, suy ra

.. math:: \lvert \mathcal{L}_n \rvert = 2^n.
