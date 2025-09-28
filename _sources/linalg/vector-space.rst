*****************
Không gian vector
*****************

=================
Không gian vector
=================

Xét tập hợp các vector :math:`\mathcal{V}` trên trường :math:`\mathbb{F}`.

Ta định nghĩa hai phép tính cộng và nhân trên các vector này.

1. Phép cộng là một ánh xạ :math:`\mathcal{V} \times \mathcal{V} \to \mathcal{V}` sao cho với mọi :math:`\bm{x}, \bm{y} \in \mathcal{V}` thì :math:`\bm{x} + \bm{y} \in \mathcal{V}`.
2. Phép nhân vô hướng là ánh xạ :math:`\mathbb{F} \times \mathcal{V} \to \mathcal{V}` sao cho với mọi :math:`\alpha \in \mathbb{F}` và :math:`\bm{x} \in \mathcal{V}` thì :math:`\alpha \bm{x} \in \mathcal{V}`.

Nói cách khác, phép cộng hai vector và phép nhân vô hướng một số với vector cho kết quả vẫn nằm trong không gian vector đó.

Đồng thời, phép cộng và phép nhân vô hướng phải thỏa mãn các tính chất sau

1. Tính giao hoán với phép cộng: với mọi :math:`\bm{x}, \bm{y} \in \mathcal{V}`, :math:`\bm{x} + \bm{y} = \bm{y} + \bm{x}`.
2. Tính kết hợp với phép cộng: với mọi :math:`\bm{x}, \bm{y}, \bm{z} \in \mathcal{V}`, :math:`\bm{x} + (\bm{y} + \bm{z}) = (\bm{x} + \bm{y}) + \bm{z}`.
3. Phần tử đơn vị của phép cộng: tồn tại vector không :math:`\bm{0} \in \mathcal{V}` sao cho với mọi :math:`\bm{x} \in \mathcal{V}`, :math:`\bm{0} + \bm{x} = \bm{x} + \bm{0} = \bm{x}`.
4. Phần tử đối của phép cộng: với mọi :math:`\bm{x} \in \mathcal{V}`, tồn tại phần tử :math:`\bm{x'} \in \mathcal{V}` sao cho :math:`\bm{x} + \bm{x'} = \bm{x} + \bm{x'} = \bm{0}`.
5. Phần tử đơn vị của phép nhân vô hướng: tồn tại phần tử :math:`1_F \in \mathbb{F}` sao cho với mọi :math:`\bm{x} \in \mathcal{V}` thì :math:`1_F \cdot \bm{x} = \bm{x}`.
6. Tính kết hợp của phép nhân vô hướng: với mọi :math:`\alpha, \beta \in \mathbb{F}`, với mọi :math:`\bm{x} \in \mathcal{V}` thì :math:`\alpha (\beta \bm{x}) = (\alpha \beta) \bm{x}`.
7. Tính phân phối giữa phép cộng và nhân: với mọi :math:`\alpha \in \mathbb{F}`, với mọi :math:`\bm{x}, \bm{y} \in \mathcal{V}` thì :math:`\alpha (\bm{x} + \bm{y}) = \alpha \bm{x} + \alpha \bm{y}`.
8. Tính phân phối giữa phép nhân vô hướng: với mọi :math:`\alpha, \beta \in \mathbb{F}`, với mọi :math:`\bm{x} \in \mathcal{V}` thì :math:`(\alpha + \beta) \bm{x} = \alpha \bm{x} + \beta \bm{x}`.

Ta thấy rằng không gian vector ở chương trình phổ thông là không gian vector xác định trên trường :math:`\mathbb{F} = \mathbb{R}`.

Khi đó :math:`\mathcal{V} = \mathbb{R}^n`. Trong chương này sẽ làm việc với không gian vector thực :math:`\mathbb{R}`.

=======================================
Cơ sở và số chiều của không gian vector
=======================================

Nếu trong không gian vector :math:`\mathcal{V}` tồn tại các vector độc lập tuyến tính :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d` mà tất cả các vector trong :math:`\mathcal{V}` có thể biểu diễn dưới dạng tổ hợp tuyến tính của các vector :math:`\bm{v}_i` trên, thì tập hợp các vector

.. math:: \{ \bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d \}

được gọi là **cơ sở** (hay **basis**, **базис**) của không gian vector :math:`\mathcal{V}`.

Khi đó

.. math:: \bm{x} = \sum_{i=1}^{d} \alpha_i \bm{v}_i \quad \text{với mọi} \ \bm{x} \in \mathcal{V}.

Số lượng phần tử của tập hợp các vector đó (ở đây là :math:`d`) gọi là **số chiều** (hay **dimension**) của không gian vector :math:`\mathcal{V}`. Ta kí hiệu :math:`\mathrm{dim} \mathcal{V} = d`.

Ta còn kí hiệu

.. math:: \mathcal{V} = \mathrm{span} \{\bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d\}

và nói là không gian vector :math:`\mathcal{V}` được span (hay được sinh) bởi các vector :math:`\bm{v_i}`.

Ta thấy rằng có thể có nhiều cơ sở cho cùng một không gian vector.

.. prf:theorem:: 
    :label: thm-dim
    
    Mọi cơ sở của không gian vector :math:`\mathcal{V}` đều có số phần tử bằng :math:`\mathrm{dim} \mathcal{V}`.

Giả sử ta có :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d` là một cơ sở của không gian vector :math:`\mathbb{R}^n`. Khi đó nếu hệ vector :math:`\bm{w}_1`, :math:`\bm{w}_2`, ..., :math:`\bm{w}_d` cũng là một hệ cơ sở khi và chỉ khi tồn tại ma trận khả nghịch :math:`\bm{A}` sao cho :math:`\bm{W} = \bm{A} \cdot \bm{V}`. Ở đây :math:`\bm{W}` là ma trận với các hàng là các vector :math:`\bm{w}_i`. Tương tự :math:`\bm{V}` là ma trận với các hàng là các vector :math:`\bm{v}_i`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta viết các vector :math:`\bm{v}_i` dưới dạng :math:`\mathbb{R}^n`.

    .. math:: 
        
        \bm{v}_1 & = (v_{11}, v_{12}, \ldots, v_{1n}), \\
        \bm{v}_2 & = (v_{21}, v_{22}, \ldots, v_{2n}), \\
        \ldots & = (\ldots, \ldots, \ldots, \ldots), \\
        \bm{v}_d & = (v_{d1}, v_{d2}, \ldots, v_{dn}).

    Tương tự là các vector :math:`\bm{w}_i`.

    .. math:: 

        \bm{w}_1 & = (w_{11}, w_{12}, \ldots, w_{1n}), \\
        \bm{w}_2 & = (w_{21}, w_{22}, \ldots, w_{2n}), \\
        \ldots & = (\ldots, \ldots, \ldots, \ldots), \\
        \bm{w}_d & = (w_{d1}, w_{d2}, \ldots, w_{dn}).

    Do :math:`\bm{v}_i` là một cơ sở của :math:`\mathbb{R}^n`, mọi vector trong :math:`\mathbb{R}^n` được biểu diễn dưới dạng tổ hợp tuyến tính của các :math:`\bm{v}_i`.

    Khi đó ta viết các :math:`\bm{w}_i` dưới dạng tổ hợp tuyến tính của :math:`\bm{v}_i`.

    .. math:: 
        
        \bm{w}_1 & = \alpha_{11} \bm{v}_1 + \alpha_{12} \bm{v}_2 + \ldots + \alpha_{1d} \bm{v}_d \\
        \bm{w}_2 & = \alpha_{21} \bm{v}_1 + \alpha_{22} \bm{v}_2 + \ldots + \alpha_{2d} \bm{v}_d \\
        \ldots & = \ldots \\
        \bm{w}_d & = \alpha_{d1} \bm{v}_1 + \alpha_{d2} \bm{v}_2 + \ldots + \alpha_{dd} \bm{v}_d.
        
    Điều này tương đương với 

    .. math:: 

        \begin{pmatrix}
            w_{11} & w_{12} & \ldots & w_{1n} \\
            w_{21} & w_{22} & \ldots & w_{2n} \\
            \ldots & \ldots & \ldots & \ldots \\
            w_{d1} & w_{d2} & \ldots & w_{dn}
        \end{pmatrix}
        = \begin{pmatrix}
            \alpha_{11} & \alpha_{12} & \ldots & \alpha_{1d} \\
            \alpha_{21} & \alpha_{22} & \ldots & \alpha_{2d} \\
            \ldots & \ldots & \ldots & \ldots \\
            \alpha_{d1} & \alpha_{d2} & \ldots & \alpha_{dd}
        \end{pmatrix}
        \times \begin{pmatrix}
            v_{11} & v_{12} & \ldots & v_{1n} \\ 
            v_{21} & v_{22} & \ldots & v_{2n} \\ 
            \ldots & \ldots & \ldots & \ldots \\ 
            v_{d1} & v_{d2} & \ldots & v_{dn}
        \end{pmatrix}

    Nếu :math:`\bm{w}_i` cũng là cơ sở của :math:`\mathcal{V}`, thì các vector :math:`\bm{v}_i` cũng phải biểu diễn được dưới dạng tổ hợp tuyến tính của :math:`\bm{w}_i`.
    
    Nói cách khác, ma trận :math:`(\alpha_{ij})` khả nghịch và ta có điều phải chứng minh.

=====================
Không gian vector con
=====================

Cho không gian vector :math:`\mathcal{V} \subset \mathbb{R}^n` với phép cộng hai vector và phép nhân vô hướng. Một tập con :math:`L` của :math:`\mathcal{V}` được gọi là không gian vector con nếu:

1. Với mọi :math:`\bm{x}`, :math:`\bm{y}` thuộc :math:`L`, :math:`\bm{x} + \bm{y} \in L`.
2. Với mọi :math:`\alpha \in \mathbb{R}`, với mọi :math:`\bm{x} \in L`, :math:`\alpha \bm{x} \in L`.

Nói cách khác, phép cộng và phép nhân vô hướng **đóng** (hay **closure**) trên không gian vector con.

.. prf:remark:: 
    :label: rmk-sys-eqs
    
    Trên :math:`\mathbb{R}^n`, hệ phương trình tuyến tính thuần nhất có thể sinh ra một không gian vector con của :math:`\mathbb{R}^n`.

.. prf:example:: 
    :label: exp-sys-eqs

    Xét hệ phương trình tuyến tính sau:

    .. math:: 

        \begin{array}{cccccccc}
            x_1 & + & 3x_2 & + & 5x_3 & + & 7x_4 & = 0 \\
            2x_1 & & & + & 4x_3 & + & 2x_4 & = 0 \\
            3x_1 & + & 2x_2 & + & 8x_3 & + & 7x_4 & = 0
        \end{array}

    Biến đổi ma trận

    .. math:: 

        \begin{pmatrix}
            1 & 3 & 5 & 7 \\
            2 & 0 & 4 & 2 \\
            3 & 2 & 8 & 7
        \end{pmatrix} \sim \begin{pmatrix}
            1 & 3 & 5 & 7 \\
            0 & -6 & -6 & -12 \\
            0 & -7 & -7 & -14
        \end{pmatrix} \sim \begin{pmatrix}
            1 & 3 & 5 & 7 \\
            0 & 1 & 1 & 2 \\
            0 & 0 & 0 & 0
        \end{pmatrix}.


    Như vậy hệ tương đương với

    .. math:: x_1 + 3x_2 + 5x_3 + 7x_4 = 0, \quad x_2 + x_3 + 2x_4 = 0.

    Ta chọn :math:`x_3, x_4 \in \mathbb{R}` tự do, khi đó :math:`x_1` và :math:`x_2` được biểu diễn theo :math:`x_3` và :math:`x_4`

    .. math:: x_1 = -2 x_3 - x_4, \quad x_2 = -x_3 - 2 x_4.


    Mọi vector trong không gian tuyến tính khi đó có dạng

    .. math:: 
        
        (x_1, x_2, x_3, x_4) & = (-2x_3 - x_4, -x_3 - 2x_4, x_3, x_4)
        \\ & = x_3 \cdot (-2, -1, 1, 0) + x_4 \cdot (-1, -2, 0, 1) 
        
    Ở đây ta thấy :math:`x_3`, :math:`x_4` nhận giá trị tùy ý trong :math:`\mathbb{R}`, và mọi vector trong không gian nghiệm là tổ hợp tuyến tính của hai vector :math:`(-2, -1, 1, 0)` và :math:`(-1, -2, 0, 1)`. Suy ra hai vector này là cơ sở của không gian nghiệm, và :math:`\dim \mathcal{V} = 2`.
