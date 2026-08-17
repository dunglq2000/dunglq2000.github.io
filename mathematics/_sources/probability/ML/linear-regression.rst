=================
Linear Regression
=================

Giả sử ta có :math:`N` điểm dữ liệu đầu vào :math:`\bm{x}_1`, :math:`\bm{x}_2`, ..., :math:`\bm{x}_N` với :math:`\bm{x}_i \in \mathbb{R}^d`. Ứng với từng điểm dữ liệu đầu vào :math:`\bm{x}_i` ta có một đầu ra :math:`y_i`, nghĩa là ta có :math:`N` cặp dữ liệu :math:`(\bm{x}_i, y_i)`. Khi đó :math:`y_i` được gọi là **nhãn** (hay **label**) tương ứng với điểm dữ liệu :math:`\bm{x}_i`.

Mục tiêu là xây dựng hàm số :math:`\hat{y} = f(x_1, x_2, \ldots, x_d)` sao cho tổng sai số của :math:`y_i` và :math:`\hat{y}_i` là nhỏ nhất, tức là

.. math:: \sum_{i=1}^N \lVert y_i - \hat{y}_i \rVert^2 \to \min.

Để hàm số đạt giá trị nhỏ nhất (hoặc lớn nhất) ta tìm cực trị của hàm số và khảo sát. Tuy nhiên không phải hàm số nào cũng đạo hàm được. Một cách tiếp cận đơn giản là sử dụng hàm tuyến tính, dễ xây dựng và luôn khả vi. Ta đặt

.. math:: \hat{y} = f(x_1, x_2, \ldots, x_d) = w_0 + w_1 x_1 + w_2 x_2 + \ldots + w_d x_d.

Lúc này, hàm mất mát có dạng

.. math:: \mathcal{L} = \sum_{i=1}^N \lVert y_i - (w_0 + w_1 x_{i1} + w_2 x_{i2} + \ldots + w_d x_{id}) \rVert^2.

Bình phương chuẩn Euclid chính là bình phương của vector. Do đó dưới dấu tổng là các hàm số bình phương. Khi đạo hàm riêng theo :math:`w_j` ta có

.. math:: \dfrac{\partial \mathcal{L}}{\partial w_j} = \sum_{i=1}^N 2 x_{ij} \cdot \left[ y_i - (w_0 + w_1 x_{i1} + w_2 x_{i2} + \ldots + w_d x_{id}) \right]

với :math:`1 \leqslant j \leqslant d`.

Với :math:`j = 0` có chút khác biệt:

.. math:: \dfrac{\partial \mathcal{L}}{\partial w_0} = \sum_{i=1}^N 2 \cdot \left[ y_i - (w_0 + w_1 x_{i1} + \ldots + w_d x_{id}) \right].

Ta cho các đạo hàm riêng :math:`\dfrac{\partial \mathcal{L}}{\partial w_j}` bằng :math:`0` thì được

.. math:: \sum_{i=1}^N x_{ij} (w_0 + w_1 x_{i1} + w_2 x_{i2} + \ldots + w_d x_{id}) & = \sum_{i=1}^N x_{ij} y_i \\ \Leftrightarrow w_0 \sum_{i=1}^N x_{ij} + w_1 \sum_{i=1}^N x_{ij} x_{i1} + w_2 \sum_{i=1}^N x_{ij} x_{i2} \\ + \cdots + w_d \sum_{i=1}^N x_{ij} x_{id} & = \sum_{i=1}^N x_{ij} y_i.
    
Bây giờ chúng ta cần biểu diễn các dấu tổng lại thành dạng đại số (ma trận, vector) vì chúng sẽ được sử dụng để nhân với vector :math:`\bm{w} = (w_0, w_1, \ldots, w_d)`.

Ta có

.. math:: 
    
    \sum_{i=1}^N x_{ij} = \begin{pmatrix}
        1 & 1 & \cdots & 1
    \end{pmatrix} \cdot \begin{pmatrix}
        x_{1j} \\ x_{2j} \\ \vdots \\ x_{Nj}
    \end{pmatrix}.

Ta cũng có

.. math:: 
    
    \sum_{i=1}^N x_{ij} x_{i1} = \begin{pmatrix}
        x_{11} & x_{21} & \cdots & x_{N1}
    \end{pmatrix} \cdot \begin{pmatrix}
        x_{1j} \\ x_{2j} \\ \vdots \\ x_{Nj}
    \end{pmatrix}.

Cứ tương tự như vậy, ta xếp các dấu sigma thành dạng cột thì tương đương với 

.. math:: 
    
    \begin{pmatrix}
        * & \sum_{i=1}^N x_{ij} & * \\ * & \sum_{i=1}^N x_{ij} x_{i1} & * \\ \vdots & \vdots & \vdots \\ * & \sum_{i=1}^N x_{ij} x_{id} & *
    \end{pmatrix} = \begin{pmatrix}
        1 & 1 & \cdots & 1 \\ x_{11} & x_{21} & \cdots & x_{N1} \\ \cdots & \cdots & \ddots & \cdots \\ x_{1d} & x_{2d} & \cdots & x_{Nd} 
    \end{pmatrix} \cdot \begin{pmatrix}
        * & x_{1j} & * \\ * & x_{2j} & * \\ \vdots & \vdots & \vdots \\ * & x_{Nj} & *
    \end{pmatrix}.

Ghép các cột theo thứ tự :math:`j` từ :math:`0` tới :math:`d` ta có

.. math:: 
    
    \begin{pmatrix}
        w_0 & w_1 & \cdots & w_d
    \end{pmatrix} & \cdot \begin{pmatrix}
        1 & 1 & \cdots & 1 \\ x_{11} & x_{21} & \cdots & x_{N1} \\ \cdots & \cdots & \ddots & \cdots \\ x_{1d} & x_{2d} & \cdots & x_{Nd}
    \end{pmatrix} \\ & \times \begin{pmatrix}
        1 & x_{11} & \cdots & x_{1d} \\ 1 & x_{21} & \cdots & x_{2d} \\ \cdots & \cdots & \ddots & \cdots \\ 1 & x_{N1} & \cdots & x_{Nd}
    \end{pmatrix} \\ = \begin{pmatrix}
        y_1 & y_2 & \cdots & y_N
    \end{pmatrix} & \cdot \begin{pmatrix}
        1 & x_{11} & \cdots & x_{1d} \\ 1 & x_{21} & \cdots & x_{2d} \\ \cdots & \cdots & \ddots & \cdots \\ 1 & x_{N1} & \cdots & x_{Nd}
    \end{pmatrix}.

Hay nói cách khác, nếu ta đặt :math:`\bm{w} = (w_0, w_1, \ldots, w_d)` là ma trận hàng, :math:`\bm{X}` là ma trận có các hàng là các input, thì phương trình trên được viết lại là :math:`\bm{w} \bm{X}^T \bm{X} = \bm{y} \bm{X}`.

Nếu đặt :math:`\bm{A} = \bm{X}^T \bm{X}` và :math:`\bm{b} = \bm{y} \bm{X}` thì đây là hệ phương trình theo các ẩn :math:`w_0`, :math:`w_1`, ..., :math:`w_d`. Tuy nhiên không phải lúc nào :math:`\bm{A}` cũng khả nghịch nên chúng ta sẽ sử dụng một khái niệm gọi là **giả nghịch đảo** (hay **pseudo-inverse**) để tìm nghiệm cho hệ phương trình.

Kí hiệu :math:`\bm{A}^\dagger` là giả nghịch đảo của ma trận :math:`\bm{A}`. Khi đó nghiệm của hệ phương trình là :math:`\bm{w} = \bm{b} \bm{A}^\dagger`.
