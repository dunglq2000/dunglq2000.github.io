Dạng toàn phương
****************

Giới thiệu dạng toàn phương
===========================

.. prf:definition:: Dạng toàn phương
    :label: def-quadratic-form

    **Dạng toàn phương** (hay **quadratic form**, **квадратная форма**) là đa thức bậc hai trên trường :math:`K` với :math:`n` biến :math:`x_1`, :math:`x_2`, ..., :math:`x_n`, nghĩa là

    .. math:: 
        
        f(x_1, x_2, \ldots, x_n) & = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j \\
            & = \sum_{i=1}^n a_{ii} x_i^2 + 2 \sum_{1 \leqslant i < j \leqslant n} a_{ij} x_i x_j.

    Ở đây, :math:`a_{ij}` được gọi là **hệ số** (hay **coefficient**, **коэффициент**) với :math:`1 \leqslant i, j \leqslant n`, và :math:`a_{ij} = a_{ji}` với mọi :math:`i \neq j`.

.. prf:example:: 
    :label: exp-quadratic-form-1

    Đa thức :math:`x_1^2 + x_2^2 + 3 x_2 x_3 - x_3^2` là dạng toàn phương với ba biến.

    Đa thức :math:`x_1^2 - x_2^2 + 3 x_1 + 2 x_2` là đa thức bậc hai nhưng không phải dạng toàn phương vì có phần tuyến tính :math:`3 x_1 + 2 x_2`.

*Câu hỏi nhỏ cho bạn đọc.* Với đa thức bậc hai :math:`n` biến bất kì

.. math:: \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j + \sum_{i=1}^n b_i x_i + c

thì điều kiện nào của hệ số cho phép chúng ta biến đổi về dạng toàn phương? Ví dụ, với đa thức

.. math:: 

    x_1^2 - x_2^2 + 3 x_1 + 2 x_2 + \frac{5}{4} & = x_1^2 + 2 \cdot x_1 \cdot \frac{3}{2} + \frac{9}{4} - x_2^2 + 2 x_2 - 1 \\
        & = \left(x_1 + \frac{3}{2}\right)^2 - (x_2 - 1)^2,

nếu đặt :math:`y_1 = x_1 + \frac{3}{2}` và :math:`y_2 = x_2 - 1` thì ta có :math:`y_1^2 - y_2^2` là dạng toàn phương ứng với các biến :math:`y_1`, :math:`y_2`.

.. prf:definition:: Dạng toàn phương chính tắc
    :label: def-canonical-quadratic-form

    Dạng toàn phương được gọi là **chính tắc** (hay **canonical**) khi các hệ số :math:`a_{ij} = 0` với mọi :math:`i \neq j`.

.. prf:example:: 
    :label: exp-quadratic-form-2

    Đa thức :math:`x_1^2 + x_2^2 + 3 x_2 x_3 - x_3^2` không là dạng toàn phương chính tắc vì có đơn thức :math:`x_2 x_3`.

    Đa thức :math:`x_1^2 - x_2^2 + 4 x_3^2` là dạng toàn phương chính tắc.

Nếu đặt các biến của dạng toàn phương thành vector cột

.. math:: \bm{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}

thì dạng toàn phương có thể được viết dưới dạng phép nhân ma trận

.. math:: f(x_1, x_2, \ldots, x_n) = \bm{x}^{\top} \bm{A} \bm{x},

trong đó :math:`\bm{A}` là ma trận *đối xứng* và :math:`\bm{x}^{\top}` là chuyển vị của vector :math:`\bm{x}`.

Cụ thể hơn, dạng ma trận tương ứng với dạng toàn phương

.. math:: 
    
    f(x_1, x_2, \ldots, x_n) & = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j \\
        & = \sum_{i=1}^n a_{ii} x_i^2 + 2 \sum_{i \neq j} a_{ij} x_i x_j

ở định nghĩa là

.. math:: 

    f(x_1, x_2, \ldots, x_n) = (x_1, x_2, \ldots, x_n) \begin{pmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{n1} & a_{n2} & \cdots & a_{nn}
        \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix},

với :math:`a_{ij} = a_{ji}` và điều này giải thích hệ số :math:`2` trong dạng toàn phương 

.. math:: a_{ij} x_i x_j + a_{ji} x_i x_j = 2 a_{ij} x_i x_j.

Khi dạng toàn phương là chính tắc thì :math:`a_{ij} = 0` với mọi :math:`i \neq j` nên :math:`\bm{A}` là ma trận đường chéo chính.

Hiện tại chúng ta sẽ khảo sát dạng toàn phương với hệ số thực, tức :math:`a_{ij} \in \mathbb{R}`.

Bài toán quan trọng của dạng toàn phương là làm thế nào để biến đổi dạng toàn phương tổng quát về dạng chính tắc. Để giải quyết vấn đề này ta sử dụng phương pháp chéo hóa hoặc phương pháp Lagrange.

Sơ lược về liên hợp Hermitian
=============================

Với số phức :math:`z = a + bi` với :math`a, b \in \mathbb{R}` và :math:`i` là đơn vị ảo, :math:`i^2 = -1`, ta kí hiệu :math:`\bar{z}` là liên hợp của :math:`z`, nghĩa là :math:`\bar{z} = a - bi`.

Ngoài ra ta cũng kí hiệu :math:`\lvert z \rvert` là module của số phức :math:`z`. Nếu :math:`z = a + bi` thì :math:`\lvert z \rvert = \sqrt{a^2 + b^2}`. Dễ thấy :math:`z \cdot \bar{z} = \lvert z \rvert^2`.

Với ma trận :math:`\bm{A} = (a_{ij})_{n \times m}`, ma trận **chuyển vị liên hợp** (hay **conjugate transpose**) là ma trận :math:`\bm{B} = (b_{ij})_{m \times n}` được định nghĩa bởi

.. math:: b_{ij} = \overline{a_{ji}}.

Như vậy, để thu được ma trận chuyển vị liên hợp, đầu tiên ta chuyển vị ma trận :math:`\bm{A}` (tính :math:`\bm{A}^{\top}`) và lấy liên hợp từng phần tử.

Ma trận chuyển vị liên hợp của ma trận :math:`\bm{A}` được kí hiệu là :math:`\bm{A}^*`.

Ví dụ, xét ma trận

.. math:: 

    \bm{A} = \begin{pmatrix} 2 & 3 + 4i & 7 \\ 6 & 5 & 8i \end{pmatrix}
    \Rightarrow \bm{A}^* = \begin{pmatrix} 2 & 6 \\ 3 - 4i & 5 \\ 7 & -8i \end{pmatrix}.

.. prf:property:: Tính chất của ma trận chuyển vị liên hợp
    :label: pro-trans-conj

    1. Nếu :math:`\bm{A}` và :math:`\bm{B}` là hai ma trận cùng cỡ thì :math:`\left(\bm{A} + \bm{B}\right)^* = \bm{A}^* + \bm{B}^*`.
    2. Với mọi ma trận :math:`\bm{A}` cỡ :math:`n \times m` và với mọi ma trận :math:`\bm{B}` cỡ :math:`m \times p` thì :math:`\left(\bm{A} \bm{B}\right)^* = \bm{B}^* \bm{A}^*`.
    3. Với mọi ma trận :math:`\bm{A}` thì :math:`\left(\bm{A}^*\right)^* = \bm{A}`.
    4. Nếu :math:`\bm{v} \in \mathbb{C}^{n \times 1}` là vector cột độ dài :math:`n` thì tích vô hướng :math:`\bm{v}^* \bm{v}` là số thực.

Các tính chất 1-3 có thể dễ dàng chứng minh tương tự như đối với ma trận chuyển vị, và tính chất 4 suy ra từ tính chất của module số phức bên trên.

Phương pháp trực giao
=====================

Ta sử dụng tính chất sau của ma trận đối xứng.

.. prf:property:: Số lượng trị riêng của ma trận đối xứng
    :label: pro-eigen-num-symmetric-matrix

    Ma trận đối xứng kích thước :math:`n \times n` trên :math:`\mathbb{R}` có đúng :math:`n` trị riêng thực.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Theo định lí cơ bản của đại số thì mọi đa thức bậc :math:`n` trên :math:`\mathbb{R}` có đầy đủ :math:`n` nghiệm trên :math:`\mathbb{C}`. Do đó nếu gọi :math:`\lambda` là trị riêng của ma trận vuống đối xứng :math:`\bm{A}` thì ta cần chứng minh :math:`\lambda = \overline{\lambda}`, tức :math:`\lambda` là số thực.

    Vì :math:`\lambda` là trị riêng của ma trận :math:`\bm{A}` cỡ :math:`n \times n` nên tồn tại vector :math:`\bm{v} \in \mathbb{C}^{n \times 1}` khác không sao cho 

    .. math:: 

        \begin{array}{cccc}
            & \bm{A} \bm{v} & = & \lambda \bm{v} \\
            \Rightarrow & \bm{v}^* \bm{A} \bm{v} & = & \lambda \bm{v}^* \bm{v},
        \end{array}
    
    với :math:`\bm{v}^*` là chuyển vị liên hợp của vector :math:`\bm{v}`.

    Lúc này, lấy chuyển vị liên hợp hai vế và sử dụng tính chất 3 của tích các ma trận ta có

    .. math:: 

        \begin{array}{cccc}
            & \bm{v}^* \bm{A} \bm{v} & = & \lambda \bm{v}^* \bm{v} \\
            \Rightarrow & \left(\bm{v}^* \bm{A} \bm{v}\right)^* & = & \left(\lambda \bm{v}^* \bm{v}\right)^* \\
            \Rightarrow & \bm{v}^* \left(\bm{A}^*\right) \left(\bm{v}^*\right)^* & = & \overline{\lambda} \bm{v}^* \bm{v} \\
            \Rightarrow & \bm{v}^* \left(\bm{A}^*\right) \bm{v} & = & \overline{\lambda} \bm{v}^* \bm{v}.
        \end{array}

    Vì :math:`\bm{A}` là ma trận đối xứng thực nên :math:`\bm{A}^* = \bm{A}`, do đó

    .. math:: \bm{v}^* \left(\bm{A}^*\right) \bm{v} = \bm{v}^* \bm{A} \bm{v} \Rightarrow \overline{\lambda} \bm{v}^* \bm{v} = \lambda \bm{v}^* \bm{v},

    và theo tính chất 4 ở trên, do :math:`\bm{v}` là vector khác không nên :math:`\bm{v}^* \bm{v} \neq 0`, suy ra :math:`\overline{\lambda} = \lambda`. Như vậy :math:`\lambda` là số thực.

Lúc này, với dạng toàn phương cho bởi :math:`\bm{x}^{\top} \bm{A} \bm{x}` và :math:`\bm{A}` là ma trận đối xứng thì ma trận :math:`\bm{A}` có đầy đủ :math:`n` trị riêng thực và có thể chéo hóa thành :math:`\bm{A} = \bm{P} \cdot \bm{D} \cdot \bm{P}^{-1}`, trong đó

- :math:`\bm{D}` là ma trận chéo với các phần tử trên đường chéo chính là các trị riêng;
- :math:`\bm{P}` là ma trận với các cột là các vector riêng ứng với các trị riêng (theo thứ tự) trong ma trận :math:`\bm{D}`.

Tiếp theo ta cần hai tính chất của các vector riêng của ma trận đối xứng thực: 

1. Hai vector riêng ứng với hai trị riêng khác nhau luôn trực giao với nhau.
2. Hai vector riêng ứng với cùng trị riêng có thể được chọn sao cho trực giao với nhau.

Đối với tính chất 2, hai vector riêng cùng trị riêng sinh ra một không gian vector với cơ sở là hai vector riêng đó. Từ đây áp dụng phương pháp trực giao hóa Gram-Schmidt ta có thể xây dựng hai vector mới trực giao với nhau từ hai vector riêng ban đầu. Sau đây ta sẽ chứng minh tính chất 1.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử :math:`\lambda_1` và :math:`\lambda_2` là hai trị riêng khác nhau của ma trận đối xứng thực :math:`\bm{A}`, tương ứng là hai vector riêng :math:`\bm{v}_1` và :math:`\bm{v}_2`.
    
    Vì :math:`\bm{A}` là ma trận đối xứng thực nên :math:`\bm{A} = \bm{A}^{\top}` và ta có

    .. math:: 
        
        \bm{A} \bm{v}_1 = \lambda_1 \bm{v}_1 \Rightarrow \bm{v}_1^{\top} \bm{A}^{\top} = \bm{v}_1^{\top} \bm{A} = \lambda_1 \bm{v}_1^{\top}, \\
        \bm{A} \bm{v}_2 = \lambda_2 \bm{v}_2 \Rightarrow \bm{v}_2^{\top} \bm{A}^{\top} = \bm{v}_2^{\top} \bm{A} = \lambda_2 \bm{v}_2^{\top}.

    Bây giờ xét :math:`\bm{v}_1^{\top} \bm{A}^{\top} \bm{v}_2` thì với :math:`\bm{A}`

    .. math:: 

        \bm{v}_1^{\top} \bm{A} \bm{v}_2 & = \left(\bm{v}_1^{\top} \bm{A}\right) \bm{v}_2 = \lambda_1 \bm{v}_1^{\top} \bm{v}_2, \\
        \bm{v}_1^{\top} \bm{A} \bm{v}_2 & = \bm{v}_1^{\top} \left(\bm{A} \bm{v}_2\right) = \bm{v}_1^{\top} (\lambda_2 \bm{v}_2).

    Như vậy

    .. math:: 
        
        \lambda_1 \bm{v}_1^{\top} \bm{v}_2 = \bm{v}_1^{\top} (\lambda_2 \bm{v}_2) = \lambda_2 \bm{v}_1^{\top} \bm{v}_2 
        \Rightarrow (\lambda_1 - \lambda_2) \bm{v}_1^{\top} \bm{v}_2 = \bm{0},

    mà :math:`\lambda_1 \neq \lambda_2` nên :math:`\bm{v}_1^{\top} \bm{v}_2 = \bm{0}`. Kết luận: :math:`\bm{v}_1` và :math:`\bm{v}_2` trực giao.

Khi ta chuẩn hóa các vector riêng thì ta thu được các vector riêng trực chuẩn nhau đôi một từ hai tính chất trên. Khi đó ta có thể chứng minh được tính chất của ma trận :math:`\bm{P}` là :math:`\bm{P}^{\top} \bm{P} = \bm{I}`, hay :math:`\bm{P}^{-1} = \bm{P}^{\top}`.

Vì :math:`\bm{A}` là ma trận đối xứng nên

.. math:: \bm{A}^{\top} = \bm{A} = \bm{P} \cdot \bm{D} \cdot \bm{P}^{-1} = \bm{P} \cdot \bm{D} \cdot \bm{P}^{\top} \Rightarrow (\bm{P}^{\top})^{\top} \cdot \bm{D}^{\top} \cdot \bm{P}^{\top} = \bm{A},

mà :math:`\bm{D}` là ma trận đường chéo chính nên :math:`\bm{D}^{\top} = \bm{D}` và ta thu được

.. math:: \bm{P} \cdot D \cdot \bm{P}^{\top} = \bm{A}.

Khi đó dạng toàn phương trở thành

.. math:: f(x_1, x_2, \ldots, x_n) = \bm{x}^{\top} \bm{A} \bm{x} = \bm{x}^{\top} \bm{P} \cdot \bm{D} \cdot \bm{P}^{\top} \bm{x} = (\bm{P}^{\top} \bm{x})^{\top} \cdot \bm{D} \cdot (\bm{P}^{\top} \bm{x}).

Đặt :math:`\bm{y} = \bm{P}^{\top} \bm{x}` thì ta được dạng toàn phương mới theo các biến :math:`y_1`, :math:`y_2`, ..., :math:`y_n`

.. math:: f(y_1, y_2, \ldots, y_n) = \bm{y}^{\top} \cdot \bm{D} \cdot \bm{y},

và do :math:`\bm{D}` là ma trận đường chéo nên đây là dạng toàn phương chính tắc.

Chúng ta hãy thử một ví dụ nhỏ.

.. prf:example:: 
    :label: exp-quadratic-form-3

    Chuyển đa thức :math:`3 x^2 + 8 x y - 3 y^2` thành dạng toàn phương chính tắc.

    Dạng toàn phương trên tương đương phép nhân ma trận

    .. math:: \begin{pmatrix} x & y \end{pmatrix} \cdot \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.

    Đầu tiên ta tính các trị riêng của ma trận :math:`\bm{A} = \begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix}`.

    Ta có

    .. math:: \bm{A} - \lambda \bm{I} = \begin{pmatrix} 3 - \lambda & 4 \\ 4 & -3 - \lambda \end{pmatrix}

    nên 
        
    .. math:: 

        f(\lambda) = \lambda^2 - 25 = 0 \Rightarrow \lambda = \pm 5.

    Khi :math:`\lambda = 5` thì

    .. math:: \bm{A} - 5 \bm{I} = \begin{pmatrix} -2 & 4 \\ 4 & -8 \end{pmatrix} \sim \begin{pmatrix} 1 & -2 \\ 0 & 0 \end{pmatrix},

    do đó :math:`x_1 - 2 x_2 = 0`, tương đương :math:`x_1 = 2 x_2`. Khi đó mọi vector :math:`(x_1, x_2)` có dạng

    .. math:: (x_1, x_2) = (2 x_2, x_2) = x_2 (2, 1), \quad x_2 \in \mathbb{R},

    nên vector riêng ứng với trị riêng :math:`\lambda = 5` là :math:`(2, 1)` và ta chuẩn hóa thành :math:`(2/\sqrt{5}, 1/\sqrt{5})`.

    Khi :math:`\lambda = -5` thì

    .. math:: \bm{A} - (-5) \bm{I} = \begin{pmatrix} 8 & 4 \\ 4 & 2 \end{pmatrix} \sim \begin{pmatrix} 2 & 1 \\ 0 & 0 \end{pmatrix},

    do đó :math:`2 x_1 + x_2 = 0`, tương đương :math:`x_2 = -2 x_1`. Khi đó mọi vector :math:`(x_1, x_2)` có dạng

    .. math:: (x_1, x_2) = (x_1, -2 x_1) = x_1 (1, -2), \quad x_1 \in \mathbb{R},

    nên vector riêng ứng với trị riêng :math:`\lambda = -5` là :math:`(1, -2)` và ta chuẩn hóa thành :math:`(1/\sqrt{5}, -2/\sqrt{5})`.

    Như vậy ma trận :math:`\bm{A}` được chéo hóa thành

    .. math:: \bm{A} = \bm{P} \bm{D} \bm{P}^{-1}, \quad \bm{D} = \begin{pmatrix} 5 & 0 \\ 0 & -5 \end{pmatrix}, \quad \bm{P} = \begin{pmatrix} 2/\sqrt{5} & -1/\sqrt{5} \\ 1/\sqrt{5} & 2/\sqrt{5} \end{pmatrix}.

    Cuối cùng, để chuyển đa thức về dạng toàn phương chính tắc ta đổi biến

    .. math:: 
        
        \begin{pmatrix} u \\ v \end{pmatrix} = \bm{P}^{\top} \begin{pmatrix} x \\ y \end{pmatrix} 
        = \begin{pmatrix} 2/\sqrt{5} & 1/\sqrt{5} \\ -1/\sqrt{5} & 2/\sqrt{5} \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
        = \begin{pmatrix} 2x/\sqrt{5} + y/\sqrt{5} \\ -x/\sqrt{5} + 2y/\sqrt{5} \end{pmatrix}

    thì ta có dạng toàn phương chính tắc :math:`5 u^2 - 5 v^2`.

Để kiểm tra ví dụ trên ta biểu diễn :math:`(x, y)` theo :math:`(u, v)` với lưu ý :math:`\bm{P}^{\top} = \bm{P}^{-1}`

.. math:: 
    
    \begin{pmatrix} u \\ v \end{pmatrix} = \bm{P}^{-1} \begin{pmatrix} x \\ y \end{pmatrix} \Rightarrow \begin{pmatrix} x \\ y \end{pmatrix} = \bm{P} \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} 2u/\sqrt{5} - v/\sqrt{5} \\ u/\sqrt{5} + 2v/\sqrt{5} \end{pmatrix}.

Ta thay vào đa thức ban đầu

.. math:: 
    
    3 x_1^2 + 8 x_1 x_2 - 3 x_2^2 & = 3 \cdot \left(\frac{2u - v}{\sqrt{5}}\right)^2 + 8 \cdot \frac{2u - v}{\sqrt{5}} \cdot \frac{u + 2v}{\sqrt{5}} - 3 \cdot \left(\frac{u + 2v}{\sqrt{5}}\right)^2 \\
    & = 3 \cdot \frac{4u^2 - 4uv + v^2}{5} + 8 \cdot \frac{2u^2 + 3uv - 2v^2}{5} - 3 \cdot \frac{u^2 + 4uv + 4v^2}{5} \\
    & = \frac{25u^2 - 25v^2}{5} = 5u^2 - 5v^2.

.. note:: 

    Nhược điểm của phương pháp trực giao là phải tìm tất cả 
    nghiệm của phương trình đặc trưng. Trong trường hợp tổng 
    quát điều này không dễ thực hiện, thậm chí bất khả thi 
    trong trường hợp tổng quát với kích thước lớn vì không 
    tồn tại công thức nghiệm tổng quát cho phương trình bậc 
    :math:`5` trở lên. Do đó chúng ta sẽ tìm hiểu phương pháp 
    thứ hai là *phương pháp Lagrange*.

Phương pháp Lagrange
====================

Ý tưởng chính của phương pháp Lagrange dựa trên khai triển bình phương

.. math:: (z_1 + z_2 + \cdots + z_n)^2 = \sum_{i=1}^n z_i^2 + 2 \sum_{i \neq j} z_i z_j.

Khi đó ta cố gắng đưa dạng toàn phương

.. math:: f(x_1, x_2, \ldots, x_n) = b_1 y_1^2 + f_1(x_2, x_3, \ldots, x_n)

với :math:`y_1` là một tổ hợp của các biến :math:`x_1`, :math:`x_2`, ..., :math:`x_n`.

Giả sử ta có dạng toàn phương

.. math:: f(x_1, x_2, \ldots, x_n) = \sum_{i=1}^n a_{ii} x_i^2 + 2 \sum_{i \neq j} a_{ij} x_i x_j.

Không mất tính tổng quát, giả sử :math:`a_{11} \neq 0` và xét biến :math:`x_1` (nếu bằng :math:`0` thì ta chuyển sang xét :math:`a_{22}` với biến :math:`x_2`, vân vân). Khi đó ta biến đổi

.. math:: 

    f(x_1, x_2, \ldots, x_n) & = a_{11} x_1^2 + 2 \sum_{j=2}^n a_{1j} x_1 x_j + \sum_{i=2}^n a_{ii} x_i^2 + \sum_{2 \leqslant i < j \leqslant n} a_{ij} x_i x_j \\
        & = a_{11} \left( x_1^2 + 2 x_1 \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right) + \sum_{i=2}^n a_{ii} x_i^2 + \sum_{2 \leqslant i < j \leqslant n} a_{ij} x_i x_j \\
        & = a_{11} \left( x_1^2 + 2 x_1 \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j + \left( \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 - \left( \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 \right) \\
        & + \sum_{i=2}^n a_{ii} x_i^2 + \sum_{2 \leqslant i < j \leqslant n} a_{ij} x_i x_j \\
        & = a_{11} \left( x_1 + \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 + \sum_{i=2}^n a_{ii} x_i^2 - a_{11} \left( \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 + \sum_{2 \leqslant i < j \leqslant n} a_{ij} x_i x_j.

Lúc này, thực hiện đổi biến

.. math:: y_1 = x_1 + \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j

và đặt

.. math:: f_1(x_2, x_3, \ldots, x_n) = \sum_{i=2}^n a_{ii} x_i^2 - a_{11} \left( \sum_{j=2}^n \frac{a_{1j}}{a_{11}} x_j \right)^2 + \sum_{2 \leqslant i < j \leqslant n} a_{ij} x_i x_j

thì ta thu được dạng toàn phương mới

.. math:: a_{11} y_1^2 + f_1(x_2, x_3, \ldots, x_n)

không còn các đơn thức dạng :math:`x_1 x_j`.

Tiếp tục thực hiện như vậy cho từng biến và ta thu được dạng toàn phương chính tắc.

Mình sẽ thử nghiệm với ví dụ bên trên: :math:`3 x^2 + 8 x y - 3 y^2`.

Mình biến đổi

.. math:: 

    3 x^2 + 8 x y - 3 y^2 & = 3 \left(x^2 + \frac{8}{3} x y\right) - 3 y^2 \\
        & = 3 \left(x^2 + 2 \cdot x \cdot \frac{4y}{3} + \frac{16y^2}{9} - \frac{16y^2}{9}\right) - 3y^2 \\
        & = 3 \left(x + \frac{4y}{3}\right)^2 - \frac{16y^2}{3} - 3y^2 \\
        & = 3 \left(x + \frac{4y}{3}\right)^2 - \frac{25y^2}{3}.

Thực hiện đổi biến :math:`u = x + 4y/3` thì ta có dạng toàn phương chính tắc

.. math:: 3 u^2 - \frac{25}{3} y^2

theo hai biến :math:`u` và :math:`y`.

.. prf:remark:: 
    :label: rmk-quadratic-form-lagrange

    1. Dạng toàn phương không là duy nhất tùy vào phương pháp biến đổi. Hơn nữa, ở ví dụ trên, nếu ta lấy :math:`y` làm mốc thay vì :math:`x` thì ta có dạng toàn phương 

    .. math:: -\frac{7}{3} x^2 - 3 v^2, \quad \text{với} \ v = 4x/3 - y.

    2. Phương pháp Lagrange khắc phục được nhược điểm của phương pháp trực giao vì không phải tìm nghiệm đa thức bậc cao mà chỉ cần rút gọn từng biến đến khi các đơn thức :math:`x_i x_j` với :math:`i \neq j` không còn nữa.
    3. Phương pháp Lagrange có nhược điểm khi số biến lớn vì việc khai triển tổng bậc hai ra để thu gọn hệ số với :math:`n-1` biến còn lại rất phức tạp. Tuy nhiên điều này có thể được khắc phục khi cài đặt trên máy tính.
