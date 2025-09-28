================
Hạng của ma trận
================

.. prf:definition:: Hạng của ma trận
    :label: def-mat-rank
    
    Cho ma trận :math:`\bm{A}_{m \times n}`. **Hạng** của ma trận là cấp của ma trận con lớn nhất có định thức khác :math:`0`.

Nghĩa là, một ma trận vuông mà là ma trận con (lấy một phần của ma trận ban đầu) kích thước :math:`r \times r` mà có định thức khác :math:`0` và :math:`r` lớn nhất, thì hạng của ma trận khi đó là :math:`r`. 

.. prf:remark:: 
    :label: rmk-mat-rank

    Ma trận con kích thước :math:`r \times r` là ma trận con của ma trận kích thước :math:`m \times n` nên :math:`r \leqslant \min(m, n)`.

.. prf:example:: 
    :label: exp-mat-rank

    Ma trận :math:`\bm{A} = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 2 & 4 \end{pmatrix}` có định thức :math:`\det(\bm{A}) = 0`. 

    Nhưng ma trận con của :math:`\bm{A}` là :math:`\bm{B} = \begin{pmatrix} 2 & 3 \\ 2 & 4 \end{pmatrix}` (lấy dòng 1 và 3, lấy cột 2 và 3) có định thức :math:`\det(\bm{B}) = 2 \neq 0`, do đó

    .. math:: r = \text{rank} \ (\bm{A}) = 2,

    với :math:`\text{rank} \ (\bm{A})` nghĩa là hạng của :math:`\bm{A}`.
