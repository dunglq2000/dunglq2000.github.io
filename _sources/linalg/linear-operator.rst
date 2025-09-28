******************
Toán tử tuyến tính
******************

.. prf:definition:: Ánh xạ tuyến tính
    :label: def-linear-map

    Toán tử tuyến tính (hay **linear operator**, **линейный оператор**) là một ánh xạ 

    .. math:: \bm{A}: \mathbb{R}^n \to \mathbb{R}^m

    thỏa hai điều kiện:

    1. Với mọi :math:`\bm{u}, \bm{v} \in \mathbb{R}^n` thì :math:`\bm{A}(\bm{u}) + \bm{A}(\bm{v}) = \bm{A}(\bm{u} + \bm{v})`.
    2. Với mọi :math:`\alpha \in \mathbb{R}` và :math:`\bm{u} \in \mathbb{R}^n` thì :math:`\bm{A} (\alpha \bm{u}) = \alpha \bm{A} (\bm{u})`.

Nếu :math:`\bm{A}` là một ma trận cỡ :math:`m \times n` thì đây là một ánh xạ tuyến tính được biểu diễn bởi phép nhân ma trận với vector :math:`\bm{A} \cdot \bm{x} = \bm{y}`.

Ở đây :math:`\bm{x} \in \mathbb{R}^n` và :math:`\bm{y} \in \mathbb{R}^m` là các vector cột.

.. prf:definition:: Hạt nhân
    :label: def-linear-kernel

    **Hạt nhân** (hay **kernel**, **ядро**) của ánh xạ tuyến tính :math:`\bm{A}` là tập hợp nghiệm của hệ thuần nhất và được kí hiệu là :math:`\ker(A)`. Nói cách khác

    .. math:: \ker(\bm{A}) = \{ \bm{x} \in \mathbb{R}^n: \, \bm{A} \cdot \bm{x} = \bm{0} \}.

.. prf:definition:: Ảnh
    :label: def-linear-image
    
    **Ảnh** (hay **image**, **образ**) của ánh xạ tuyến tính :math:`\bm{A}` là tập hợp tất cả giá trị có thể của phép nhân ma trận và được kí hiệu là :math:`\mathrm{im} (A)`. Nói cách khác

    .. math:: \mathrm{im} (\bm{A}) = \{ \bm{A} \cdot \bm{x}: \, \bm{x} \in \mathbb{R}^n \}.

.. prf:property:: 
    :label: prop-kernel-image
    
    Ánh xạ tuyến tính :math:`\bm{A} \mathbb{R}^n \to \mathbb{R}^m` có tính chất:

    1. :math:`\dim(\ker \bm{A}) + \dim(\text{im} \bm{A}) = n`.
