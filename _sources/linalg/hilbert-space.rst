Không gian Hilbert
******************

Không gian metric
=================

Cho tập hợp :math:`E` khác rỗng và :math:`d` là ánh xạ :math:`E \times E \to \mathbb{R}` thỏa mãn

1. :math:`d(x, y) \geqslant 0` với mọi :math:`x, y \in E` (tính phân biệt dương).
2. :math:`d(x, y) = 0` khi và chỉ khi :math:`x = y`.
3. :math:`d(x, y) = d(y, x)` với mọi :math:`x, y \in E` (tính đối xứng).
4. :math:`d(x, z) \leqslant d(x, y) + d(y, z)` với mọi :math:`x, y, z \in E` (bất đẳng thức tam giác).

Khi đó :math:`d` được gọi là **khoảng cách** hay **metric trên** :math:`E`, còn :math:`(E, d)` được gọi là **không gian metric**.

Sau đây là một số không gian metric thông dụng trên :math:`E = \mathbb{R}`.

Cho :math:`\bm{x} = (x_1, x_2, \ldots, x_n)` và :math:`\bm{y} = (y_1, y_2, \ldots, y_n)` là các vector trên :math:`\mathbb{R}^n`.

.. prf:example:: 
    :label: exp-metric-space-1

    Metric xác định bởi tổng khoảng cách giữa từng tọa độ

    .. math:: d(\bm{x}, \bm{y}) = \sum_{i=1}^n \lvert x_i - y_i \rvert.

.. prf:example:: 
    :label: exp-metric-space-2

    Metric Euclid là khoảng cách Euclid quen thuộc

    .. math:: d(\bm{x}, \bm{y}) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}.

    Tổng quát hơn với số mũ bất kì

    .. math:: d(\bm{x}, \bm{y}) = \left[\sum_{i=1}^n (x_i - y_i)^p\right]^{1/p}.

.. prf:example:: 
    :label: exp-metric-space-3

    Metric xác định bởi

    .. math:: d(\bm{x}, \bm{y}) = \max_{1 \leqslant i \leqslant 1} \lvert x_i - y_i \rvert.

.. prf:example:: 
    :label: exp-metric-space-4

    Metric rời rạc

    .. math:: d(\bm{x}, \bm{y}) = \begin{cases} 0, \bm{x} = \bm{y} \\ 1, \bm{x} \neq \bm{y} \end{cases}

.. prf:example:: 
    :label: exp-metric-space-5

    Metric

    .. math:: d(\bm{x}, \bm{y}) = \begin{cases} 0, \ x_i = y_i \\ \lvert x_i - y_i \rvert, \ x_i \neq y_i \end{cases} \ \text{với mọi} \ i \geqslant 2.

Tiếp theo ta có một số không gian metric trên tập các hàm số.

.. prf:example:: Metric trên không gian hàm số từ tập :math:`A` bất kì vào không gian metric :math:`(X, d)`
    :label: exp-metric-space-6

    Với :math:`f, g: A \to (X, d)` xác định

    .. math:: d(f, g) = \sup_{x \in A} d(f(x), g(x)).

.. prf:example:: Metric trên không gian các hàm liên tục trên :math:`[a, b]` vào :math:`\mathbb{R}`
    :label: exp-metric-space-7

    Với :math:`f, g: [a, b] \to \mathbb{R}` liên tục, xác định

    .. math:: d(f, g) = \int\limits_a^b \lvert f(x) - g(x) \rvert \, dx.

Không gian Hilbert
==================

Không gian Hilbert là không gian vector :math:`H` trên trường :math:`\mathbb{R}` hoặc :math:`\mathbb{C}` đồng thời trang bị tích vô hướng :math:`\langle \cdot, \cdot, \rangle` thỏa các điều kiện sau:

1. :math:`H` là không gian vector tuyến tính (phép cộng và phép nhân vô hướng).
2. **Tích trong** (hay **inner product**, **tích vô hướng**) là ánh xạ :math:`H \times H \to \mathbb{R}` hoặc :math:`\mathbb{C}` thỏa

   * tuyến tính theo biến đầu

   .. math:: \langle a \bm{x} + b \bm{y}, \bm{z} \rangle = a \langle \bm{x}, \bm{z} \rangle + b \langle \bm{y}, \bm{z} \rangle,

   * đối xứng liên hợp

   .. math:: \langle \bm{x}, \bm{y} \rangle = \overline{\bm{y}, \bm{x}},

   * xác định dương

   .. math:: \langle \bm{x}, \bm{x} \rangle \geqslant 0 \ \text{và} \ \langle \bm{x}, \bm{x} \rangle = 0 \Leftrightarrow \bm{x} = \bm{0}.

3. Độ dài và chuẩn: **chuẩn** (hay **norm**) của vector :math:`\bm{x}` là :math:`\lVert \bm{x} \rVert = \langle \bm{x}, \bm{x} \rangle`.
4. Đầy đủ: :math:`H` là không gian metric đầy đủ dưới chuẩn :math:`\lVert \bm{x} - \bm{y} \rVert`, nghĩa là giới hạn của mọi dãy Cauchy trong :math:`H` cũng là phần tử trong :math:`H`.

.. prf:remark:: 
    :label: rmk-hilbert-space-1

    Nếu các điều kiện 1, 2, 3 thỏa còn 4 không thỏa thì :math:`H` được gọi là không gian tích trong.

.. prf:remark:: 
    :label: rmk-hilbert-space-2

    Không gian Hilbert là trường hợp riêng của không gian Banach (chỉ yêu cầu về chuẩn mà có thể không có tích trong).
    