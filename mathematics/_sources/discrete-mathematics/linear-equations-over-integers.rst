Phương trình tuyến tính với nghiệm nguyên
=========================================

Phần này xét một phương trình tuyến tính trên :math:`\mathbb{Z}`. Đây là
bài toán nghiệm nguyên, không phải phép khử Gauss trên một trường hữu hạn.
Các phép biến đổi cột đều là unimodular nên bảo toàn song ánh giữa các nghiệm
nguyên.

Xét trường hợp khi hệ chỉ có một phương trình

.. math::
   :label: integer-linear-equation

   a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = d

với :math:`a_i`, :math:`d \in \mathbb{Z}`.

Ta viết các hệ số của phương trình trên dưới dạng ma trận

.. math:: A = \begin{pmatrix} a_1 & \cdots & a_n \\ 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \end{pmatrix}

kích thước :math:`(n + 1) \times n` với hàng đầu là hệ số :math:`a_i`, ở dưới là ma trận đơn vị.

Ta thực hiện các bước

1. Chọn trên hàng đầu của :math:`A` phần tử khác :math:`0` có giá trị tuyệt đối nhỏ nhất là :math:`a_i`.
2. Chọn số :math:`j \neq i` mà :math:`a_j \neq 0`.
3. Thực hiện chia :math:`a_j = q a_i + r` với :math:`0 \leqslant r < \lvert a_i \rvert`.
4. Trừ cột :math:`j` của ma trận :math:`A` từ cột :math:`i` nhân với :math:`q`.

Như vậy, ma trận mới sẽ có phần tử ở vị trí :math:`a_j = 0` nếu :math:`r = 0`, hoặc có phần tử mới có giá trị tuyệt đối nhỏ hơn :math:`a_i`, nghĩa là

.. math:: (\ldots, a_j, \ldots, a_i, \ldots) \Longrightarrow (\ldots, r, \ldots, a_i, \ldots).

Rõ ràng, sau một lượt thực hiện các bước từ 1 tới 4 thì ma trận sẽ có dạng

.. math:: \begin{pmatrix} 0 & \cdots & 0 & \lambda & 0 & \cdots & 0 \\ c_{11} & \cdots & c_{1, s-1} & c_{1,s} & c_{1, s+1} & \cdots & c_{1,n} \\ \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\ c_{n, 1} & \cdots & c_{n, s-1} & c_{n,s} & c_{n,s+1} & \cdots & c_{n,n} \end{pmatrix}

với :math:`\lambda`, :math:`c_{ii} \in \mathbb{Z}`, :math:`\lambda \neq 0`. Nếu :math:`\lambda \nmid d` thì phương trình ban đầu không có nghiệm. Nếu :math:`\lambda \mid d` thì phương trình có nghiệm tổng quát dạng

.. math:: \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = t_1 \bar{c}_1 + \cdots + t_{s-1} \bar{c}_{s-1} + \dfrac{d}{\lambda} \bar{c}_s + t_{s+1} \bar{c}_{s+1} + \cdots + t_n \bar{c}_n

với :math:`t_1`, ..., :math:`t_{s-1}`, :math:`t_{s+1}`, ..., :math:`t_n` tùy ý thuộc :math:`\mathbb{Z}`, còn :math:`\bar{c}_i` là vector cột của ma trận

.. math:: \begin{pmatrix} 0 & \cdots & \lambda & \cdots & 0 \\ & & \bm{C} & & \end{pmatrix}.

Trong một lần lặp của thuật toán thì ma trận :math:`A` biến thành ma trận :math:`A D_{ij}` với :math:`D_{ij}` có kích thước :math:`n \times n`, trên đường chéo chính là :math:`1`; phần tử tại hàng :math:`i`, cột :math:`j` là :math:`-q`; các phần tử còn lại bằng :math:`0`.

Ma trận :math:`D_{ij}` là ma trận nguyên với :math:`\det(D_{ij}) = 1`, nghịch đảo của :math:`D_{ij}` cũng là ma trận nguyên.

Viết :eq:`integer-linear-equation` dưới dạng vector

.. math:: (a_1, \ldots, a_n) \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = b \Longrightarrow (a_1, \ldots, a_n) D_{ij} D_{ij}^{-1} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = b.

Xét biến mới

.. math:: \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} = D_{ij}^{-1} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.

Khi đó ta có phương trình mới

.. math:: a_1' y_1 + \cdots + a_n' y_n = b

với :math:`(a_1', \ldots, a_n') = (a_1, \ldots, a_n) \cdot D_{ij}`.

Giá trị :math:`y_1`, ..., :math:`y_n` là **nguyên** khi và chỉ khi :math:`x_1`, ..., :math:`x_n` cũng nguyên.

Nếu ta thực hiện thuật toán :math:`k` lần với giá trị tại chỉ số :math:`(i_1, j_1)`, :math:`(i_2, j_2)`, ..., :math:`(i_k, j_k)` thì hệ trở thành hệ theo các biến :math:`z_1`, ..., :math:`z_n`

.. math:: \begin{pmatrix} z_1 \\ \vdots \\ z_n \end{pmatrix} = D_{i_k j_k}^{-1} \cdots D_{i_1 j_1}^{-1} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.

Nếu khi đó, hàng đầu ma trận :math:`A` có dạng

.. math:: (0, 0, \ldots, 0, \lambda, 0, \ldots, 0) = (a_1, \ldots, a_n) D_{i_1 j_1} \cdots D_{i_k j_k}

thì hệ có dạng :math:`\lambda z_1 = b` (8).

Nếu :math:`\lambda \nmid b` thì hệ vô nghiệm, còn :math:`\lambda \mid b` thì (8) có nghiệm dạng

.. math:: (z_1, \ldots, z_n) = (t_1, \ldots, t_{s-1}, \dfrac{b}{\lambda}, t_{s+1}, \ldots, t_n)

với :math:`t_1, \ldots, t_n \in \mathbb{Z}` tùy ý. Khi đó

.. math:: \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = D_{i_1 j_1} \cdots D_{i_k j_k} \begin{pmatrix} t_1 \\ \vdots \\ t_{s-1} \\ b / \lambda \\ t_{s+1} \\ \vdots \\ t_n \end{pmatrix}.

Chú ý: ma trận :math:`C` ở (6) bằng :math:`D_{i_1 j_1} \cdots D_{i_k j_k}` vì với các hàng còn lại của ma trận :math:`A` ta đã làm cho hàng đầu (ma trận đơn vị :math:`n \times n`) nhân với một dãy :math:`D_{i_1 j_1}`, :math:`D_{i_2 j_2}`, ..., :math:`D_{i_k j_k}`.
