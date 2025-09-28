=================
Định thức ma trận
=================

.. prf:definition:: Nghịch thế
    :label: def-inversion
    
    Cho tập hợp :math:`A = \{1, 2, \cdots, n\}` và xét hoán vị :math:`\sigma` trên :math:`A`.
    
    Ta gọi hai phần tử :math:`i` và :math:`j` tạo thành **nghịch thế** (hay **inversion**) nếu :math:`i < j` và :math:`\sigma(i) > \sigma(j)`.

    Đặt :math:`\sigma = \begin{pmatrix} 1 & 2 & \ldots & n \\ k_1 & k_2 & \cdots & k_n \end{pmatrix}` là một hoán vị của :math:`A`. Ta kí hiệu :math:`P(\sigma)` là số lượng nghịch thế của :math:`\sigma` và đặt :math:`(-1)^{P(\sigma)} = \text{sign} \ \sigma`.

.. prf:example:: 
    :label: exp-inversion
    
    Với :math:`n = 4`, :math:`A = \{1, 2, 3, 4\}`.
    
    Xét hoán vị :math:`\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 2 & 1 & 3 \end{pmatrix}`.

    Ta nhận thấy các cặp nghịch thế :math:`(1, 2)`, :math:`(1, 3)`, :math:`(1, 4)`, :math:`(2, 3)` gồm bốn cặp nghịch thế. Vậy :math:`P(\sigma) = 4` và :math:`\text{sign} \ \sigma=(-1)^4=1`.

.. prf:definition:: Định thức
    :label: def-det

    Khi đó **định thức** của ma trận

    .. math:: \bm{A} = \begin{pmatrix}a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \cdots & \cdots & \cdots & \cdots \\ a_{n1} & a_{n2} & \cdots & a_{nn}\end{pmatrix}

    được định nghĩa là:

    .. math:: \det(\bm{A})=\displaystyle{\sum_{(i_1, i_2, \cdots, i_n)} a_{1, i_1} \cdot a_{2, i_2} \cdot a_{n, i_n} \cdot \text{sign} \sigma}

    với mọi hoán vị :math:`\sigma = \begin{pmatrix} 1 & 2 & \ldots & n \\ i_1 & i_2 & \cdots & i_n \end{pmatrix}` của tập :math:`\{ 1, 2, \ldots, n \}`. Như vậy có :math:`n!` phần tử cho tổng trên.

.. prf:example:: 
    :label: exp-det
 
    Tính định thức ma trận :math:`\bm{A}=\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}`.

    Xét hoán vị :math:`\sigma_1 = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix}`. Khi đó :math:`P(\sigma_1)=0`,

    .. math:: a_{11} \cdot a_{22} \cdot a_{33} \cdot (-1)^0 = 1 \cdot 5 \cdot 9 \cdot 1 = 45.

    Xét hoán vị :math:`\sigma_2 = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 2 \end{pmatrix}`. Khi đó :math:`P(\sigma_2) = 1`,

    .. math:: a_{11} \cdot a_{23} \cdot a_{32} \cdot (-1)^1 = 1 \cdot 6 \cdot 8 \cdot (-1) = -48.

    Xét hoán vị :math:`\sigma_3 = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix}`. Khi đó :math:`P(\sigma_3) = 1`,

    .. math:: a_{12} \cdot a_{21} \cdot a_{33} \cdot (-1)^1 = 2 \cdot 4 \cdot 9 \cdot (-1) = -72.

    Xét hoán vị :math:`\sigma_4 = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}`. Khi đó :math:`P(\sigma_4) = 2`,

    .. math:: a_{12} \cdot a_{23} \cdot a_{31} \cdot (-1)^2 = 2 \cdot 6 \cdot 7 \cdot 1 = 84.

    Xét hoán vị :math:`\sigma_5 = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}`. Khi đó :math:`P(\sigma_5) = 2`,

    .. math:: a_{13} \cdot a_{21} \cdot a_{32} \cdot (-1)^2 = 3 \cdot 4 \cdot 8 \cdot 1 = 96.

    Xét hoán vị :math:`\sigma_6 = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 2 & 1 \end{pmatrix}`. Khi đó :math:`P(\sigma_6) = 3`,

    .. math:: a_{13} \cdot a_{22} \cdot a_{31} \cdot (-1)^3 = 3 \cdot 5 \cdot 7 \cdot  (-1) = -105.

    Như vậy

    .. math:: \det(A)=45-48-72+84+96-105=0.

Định thức của ma trận còn được định nghĩa theo **đệ quy** như sau.

Với ma trận :math:`1 \times 1` là :math:`\bm{A} = \begin{pmatrix} a_{11} \end{pmatrix}` thì :math:`\det(\bm{A}) = a_{11}`.

Với ma trận :math:`2 \times 2` là :math:`\bm{A} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}` thì :math:`\det(\bm{A}) = a_{11} a_{22} - a_{21} a_{12}`.

Với ma trận :math:`n \times n`, gọi :math:`\bm{M}_{ij}` là ma trận có được từ ma trận :math:`\bm{A}` khi bỏ đi hàng :math:`i` và cột :math:`j` của ma trận :math:`\bm{A}` và kí hiệu :math:`A_{ij} = (-1)^{i+j} \det (\bm{M}_{ij})`.

.. prf:theorem:: Định lý Laplace
    :label: thm-laplace
    
    Định lý Laplace cho phép ta khai triển định thức của ma trận cấp :math:`n` thành tổng các ma trận cấp :math:`n-1`.

    Khai triển theo cột :math:`j`:

    .. math:: \det(\bm{A})=\displaystyle{\sum_{i=1}^na_{ij} A_{ij}} = a_{1j} A_{1j} + a_{2j} A_{2j} + \cdots + a_{nj} A_{nj},\ j = \overline{1, n}.

    Khai triển theo hàng :math:`i`: 

    .. math:: \det(\bm{A})=\displaystyle{\sum_{j=1}^n a_{ij} A_{ij}} = a_{i1} A_{i1} + a_{i2} A_{i2} + \cdots + a_{in} A_{in},\ i = \overline{1, n}.
