==================
Ma trận nghịch đảo
==================

.. prf:definition:: Ma trận nghịch đảo
    :label: def-mat-inv
    
    Ma trận :math:`\bm{A}^{-1}` được gọi là **ma trận nghịch đảo** của ma trận vuông :math:`\bm{A}` nếu
    
    .. math:: \bm{A}^{-1} \cdot \bm{A} = \bm{A} \cdot \bm{A}^{-1} = \bm{I},
        
    trong đó :math:`\bm{I}` là ma trận đơn vị cùng kích thước với :math:`\bm{A}`.

.. math:: \bm{A}^{-1}=\frac{1}{\det(\bm{A})}[(A_{ij})_n]^\top=\frac{1}{\det(\bm{A})}\begin{pmatrix} A_{11} & A_{21} & \cdots & A_{n1} \\ A_{12} & A_{22} & \cdots & A_{n2} \\ \cdots & \cdots & \cdots & \cdots \\ A_{1n} & A_{2n} & \cdots & A_{nn} \end{pmatrix},

trong đó, :math:`A_{ij}` cũng được định nghĩa tương tự như khi tính định thức bằng khai triển theo dòng hoặc cột. Gọi :math:`\bm{M}_{ij}` là ma trận có được từ ma trận :math:`\bm{A}` khi bỏ đi hàng :math:`i` và cột :math:`j` của ma trận :math:`\bm{A}` và kí hiệu :math:`A_{ij}=(-1)^{i+j} \det (\bm{M}_{ij})`.

Như vậy, điều kiện cần và đủ để một ma trận có nghịch đảo là định thức khác :math:`0`.
