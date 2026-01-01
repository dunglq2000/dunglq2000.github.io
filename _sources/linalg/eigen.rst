Trị riêng và vector riêng
*************************

Trị riêng và vector riêng
=========================

.. prf:definition:: Trị riêng và vector riêng
    :label: def-eigens
    
    Xét toán tử tuyến tính được biểu diễn bởi ma trận :math:`\bm{A}`. Khi đó vector :math:`\bm{v}` khác không được gọi là **vector riêng** (hay **eigenvector**) của ma trận nếu tồn tại phần tử :math:`\lambda` sao cho

    .. math:: \bm{A} \bm{v} = \lambda \bm{v}.

    Giá trị :math:`\lambda` khi đó gọi là **trị riêng** (hay **eigenvalue**) tương ứng với vector riêng :math:`\bm{v}`.

Chuyển vế đẳng thức trên ta có :math:`(\bm{A} - \lambda \bm{I}) \bm{v} = \bm{0}`. Ở đây :math:`\bm{I}` là ma trận cùng cỡ với :math:`\bm{A}` và có các phần tử ở hàng :math:`i` và cột :math:`i` bằng :math:`1` (ma trận đơn vị).

Như vậy, để phương trình có nghiệm khác không thì ma trận :math:`\bm{A} - \lambda \bm{I}` suy biến, hay :math:`\det (\bm{A} - \lambda \bm{I}) = 0`.

Mỗi nghiệm :math:`\lambda` của phương trình :math:`\det (\bm{A} - \lambda \bm{I}) = 0` là một trị riêng. Với mỗi trị riêng :math:`\lambda` ta tìm được các vector riêng :math:`\bm{v}` tương ứng.

.. prf:example:: 
    :label: exp-eigens

    Trị riêng của ma trận :math:`\begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}` là :math:`\pm 5`, trong đó:
    
    - tương ứng với trị riêng :math:`\lambda_1 = 5` là vector riêng :math:`\bm{v}_1 = (2, 1)`;
    - tương ứng với trị riêng :math:`\lambda_2 = -5` là vector riêng :math:`\bm{v}_2 = (1, -2)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta có

    .. math:: \bm{A} - \lambda \bm{I} = \begin{pmatrix} 3 - \lambda & 4 \\ 4 & -3 - \lambda \end{pmatrix}

    nên 
        
    .. math:: 

        \det(\bm{A} - \lambda \bm{I}) = \lambda^2 - 25 = 0 \Rightarrow \lambda = \pm 5.

    Khi :math:`\lambda = 5` thì

    .. math:: \bm{A} - 5 \bm{I} = \begin{pmatrix} -2 & 4 \\ 4 & -8 \end{pmatrix} \sim \begin{pmatrix} 1 & -2 \\ 0 & 0 \end{pmatrix},

    do đó :math:`x_1 - 2 x_2 = 0`, tương đương :math:`x_1 = 2 x_2`. Khi đó mọi vector :math:`(x_1, x_2)` có dạng

    .. math:: (x_1, x_2) = (2 x_2, x_2) = x_2 (2, 1), \quad x_2 \in \mathbb{R},

    nên vector riêng ứng với trị riêng :math:`\lambda = 5` là :math:`(2, 1)`.

    Khi :math:`\lambda = -5` thì

    .. math:: \bm{A} - (-5) \bm{I} = \begin{pmatrix} 8 & 4 \\ 4 & 2 \end{pmatrix} \sim \begin{pmatrix} 2 & 1 \\ 0 & 0 \end{pmatrix},

    do đó :math:`2 x_1 + x_2 = 0`, tương đương :math:`x_2 = -2 x_1`. Khi đó mọi vector :math:`(x_1, x_2)` có dạng

    .. math:: (x_1, x_2) = (x_1, -2 x_1) = x_1 (1, -2), \quad x_1 \in \mathbb{R},

    nên vector riêng ứng với trị riêng :math:`\lambda = -5` là :math:`(1, -2)`.

.. prf:property:: Một số tính chất của trị riêng và vector riêng
    :label: prop-eigens
    
    Giả sử đối với ma trận :math:`\bm{A}` cỡ :math:`n \times n` thì phương trình đặc trưng có đầy đủ :math:`n` nghiệm thực, ta có các tính chất sau:

    1. :math:`\mathrm{tr} \bm{A} = \lambda_1 + \lambda_2 + \ldots + \lambda_n`.
    2. :math:`\det \bm{A} = \lambda_1 \cdot \lambda_2 \cdots \lambda_n`.

.. prf:property:: Tính chất liên quan đến rank và trace
    :label: prop-eigens-rank-trace

    1. :math:`\mathrm{tr} (\bm{A} \bm{B}) = \mathrm{tr} (\bm{B} \bm{A})`.
    2. :math:`\mathrm{rank} (\bm{A} \bm{B}) \leqslant \min(\mathrm{rank}(\bm{A}), \mathrm{rank}(\bm{B}))`.

Bài tập
=======

**Bài 1.** Cho vector cột :math:`\bm{v} \in \mathbb{R}^n`. Đặt :math:`\bm{A} = \bm{v} \cdot \bm{v}^\top`. Tìm :math:`\mathrm{spa} \bm{A}`.

Các cột của :math:`A` có dạng :math:`\bm{v} \cdot \bm{v}_1`, :math:`\bm{v} \cdot \bm{v}_2`, ..., :math:`\bm{v} \cdot \bm{v}_n`. Như vậy các cột đều tỉ lệ với cột đầu nên :math:`\mathrm{rank} \bm{A} = 1`.

Suy ra :math:`\dim \ker \bm{A} = n-1` và do đó :math:`\lambda = 0` là nghiệm bậc :math:`n-1` trong phương trình đặc trưng.

Như vậy phương trình đặc trưng còn một nghiệm :math:`\lambda \neq 0`.

Do

.. math:: (\bm{v} \cdot \bm{v}^\top) \bm{x} = \lambda \bm{x} \Leftrightarrow \bm{v} (\bm{v}^\top \cdot \bm{x}) = \lambda \bm{x}.

Đặt :math:`\bm{v}^\top \cdot \bm{x} = \alpha` thì :math:`\alpha \bm{v} = \lambda \bm{x}`. Suy ra :math:`\bm{x} = \bm{v}` và do đó :math:`\alpha = \lambda = \lVert \bm{v} \rVert^2`.

Vậy :math:`\mathrm{spa} \bm{A} = \{ \lVert \bm{v} \rVert^2, 0, 0, \ldots, 0\}`.

----

**Bài 3.** Cho ma trận :math:`\bm{A}_{3 \times 3}`. Biết rằng :math:`\mathrm{tr} \bm{A} = \mathrm{tr} \bm{A}^{-1} = 0` và :math:`\det \bm{A} = 1`. Chứng minh rằng :math:`\bm{A}^3 = \bm{I}`.

Phương trình đặc trưng có dạng :math:`P_3(\lambda) = -\lambda^3 + a_2 \lambda^2 + a_1 \lambda + a_0`.

Theo tính chất trên thì :math:`a_2 = \sum \lambda = \mathrm{tr} \bm{A} = 0`.

Do :math:`\lambda` là trị riêng nên :math:`\bm{A} \bm{x} = \lambda \bm{x}`. Do :math:`\bm{A}` khả nghịch nên :math:`\dfrac{1}{\lambda} \bm{x} = \bm{A}^{-1} \bm{x}`.

Nghĩa là :math:`\dfrac{1}{\lambda}` là trị riêng của ma trận :math:`\bm{A}^{-1}`. Suy ra :math:`\dfrac{1}{\lambda_1} + \dfrac{1}{\lambda_2} + \dfrac{1}{\lambda_3} = \mathrm{tr} A^{-1} = 0`.

Từ đó suy ra :math:`\lambda_1 \lambda_2 + \lambda_2 \lambda_3 + \lambda_3 \lambda_1 = 0`.

Cuối cùng :math:`\det \bm{A} = \lambda_1 \cdot \lambda_2 \cdot \lambda_3 = 1`.

Vậy phương trình đặc trưng là :math:`P_3(\lambda) = -\lambda^3 + 1`. Theo định lý Cayley-Hamilton thì :math:`P_3(\bm{A}) = -\bm{A}^3 + \bm{I} = \bm{0}`, hay :math:`\bm{A}^3 = \bm{I}`.

----

**Bài 4.** Cho ma trận :math:`\bm{A}_{n \times n}`, :math:`\bm{A}_{ij} \geqslant 0`. Giả sử ma trận có đủ :math:`n` trị riêng thực. Chứng minh rằng :math:`\lambda_1^k + \lambda_2^k + \ldots + \lambda_n^k \geqslant 0` với mọi :math:`k \in \mathbb{N}`.

Ta thấy rằng với :math:`k = 1` thì :math:`\lambda_1 + \ldots + \lambda_n = \mathrm{tr}(\bm{A}) \geqslant 0`.

Vì :math:`\lambda_i` là thỏa phương trình :math:`\bm{A} \bm{x} = \lambda_i \bm{x}` nên nhân hai vế cho :math:`\bm{A}` ta có :math:`\bm{A} \cdot \bm{A} \bm{x} = \bm{A} \cdot \lambda_i \bm{x}`. Tương đương với :math:`\bm{A}^2 \bm{x} = \lambda_i (\bm{A} \bm{x}) = \lambda_i^2 \bm{x}`.

Nói cách khác, :math:`\lambda_i^2` là trị riêng của ma trận :math:`\bm{A}^2`. Thực hiện tương tự ta có :math:`\lambda_i^k` là trị riêng của ma trận :math:`\bm{A}^k`.

Do đó :math:`\lambda_1^k + \ldots + \lambda_n^k = \mathrm{tr}(\bm{A}^k) \geqslant 0`.

----

**Bài 5.** Cho ma trận :math:`\bm{A}` khả nghịch. :math:`\bm{X}` là ma trận sao cho :math:`\bm{A} \bm{X} + \bm{X} \bm{A} = \bm{0}`. Chứng minh rằng :math:`\mathrm{tr} \ \bm{X} = 0`.

Nhân bên trái hai vế cho :math:`\bm{A}^{-1}` ta có :math:`\bm{X} + \bm{A}^{-1} \bm{X} \bm{A} = \bm{0}`. Ta biết rằng :math:`\bm{A}^{-1} \bm{X} \bm{A}` là ma trận tương đương ma trận :math:`\bm{X}` nên :math:`\mathrm{tr} (\bm{A}^{-1} \bm{X} \bm{A}) = \mathrm{tr} \ \bm{X}`.

Suy ra :math:`\mathrm{tr} \bm{X} + \mathrm{tr} \bm{X} = \mathrm{tr} \ \bm{0} = 0`. Từ đây có :math:`\mathrm{tr} \ \bm{X} = 0`.