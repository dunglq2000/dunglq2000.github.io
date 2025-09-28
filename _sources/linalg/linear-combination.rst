*****************
Tổ hợp tuyến tính
*****************

Xét tập hợp các vector :math:`\{\bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d\}` trên :math:`\mathbb{R}`.

.. prf:definition:: Tổ hợp tuyến tính
    :label: def-linear-comb
    
    Với vector :math:`\bm{x}` bất kì thuộc :math:`\mathbb{R}`, nếu tồn tại các số thực :math:`\alpha_1`, :math:`\alpha_2`, ..., :math:`\alpha_d` thuộc :math:`\mathbb{R}` sao cho

    .. math:: \bm{x} = \alpha_1 \bm{v}_1 + \alpha_2 \bm{v}_2 + \ldots + \alpha_d \bm{v}_d

    thì :math:`\bm{x}` được gọi là **tổ hợp tuyến tính** (hay **linear combination**) của các vector :math:`\bm{v}_i`, :math:`i = 1, 2, \ldots, d`.

Ta thấy rằng vector không :math:`\bm{0}` là tổ hợp tuyến tính của mọi tập các vector :math:`\bm{v}_i` khi tất cả :math:`\alpha_i = 0`.

Bây giờ ta xét tổ hợp tuyến tính

.. math:: \alpha_1 \bm{v}_1 + \alpha_2 \bm{v}_2 + \ldots + \alpha_d \bm{v}_d = \bm{0}.

.. prf:definition:: Độc lập tuyến tính
    :label: def-linear-independent
    
    Tập hợp các vector :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d` được gọi là **độc lập tuyến tính** (hay **linear independent**) nếu chỉ có duy nhất trường hợp
    
    .. math:: \alpha_1 = \alpha_2 = \ldots = \alpha_d = 0
        
    thỏa tổ hợp tuyến tính trên.

.. prf:definition:: Phụ thuộc tuyến tính
    :label: def-linear-dependent
    
    Tập các vector là **phụ thuộc tuyến tính** (hay **linear dependent**) nếu không độc lập tuyến tính. Nói cách khác tồn tại ít nhất một phần tử :math:`\alpha_i \neq 0`.
