Không gian Euclide
******************

Trên không gian vector :math:`\mathcal{V}` chúng ta bổ sung thêm một phép toán là tích vô hướng (dot product, tích chấm) của hai vector.

Giả sử với hai vector :math:`\bm{x} = (x_1, x_2, \ldots, x_n)` và :math:`\bm{y} = (y_1, y_2, \ldots, y_n)`. Khi đó tích vô hướng của :math:`\bm{x}` và :math:`\bm{y}` là

.. math:: \bm{x} \cdot \bm{y} = x_1 y_1 + x_2 y_2 + \ldots + x_n y_n.

Một số sách kí hiệu tích vô hướng của hai vector :math:`\bm{x}` và :math:`\bm{y}` là :math:`\langle \bm{x}, \bm{y} \rangle`. Trong phần này này mình sẽ dùng kí hiệu :math:`\bm{x} \cdot \bm{y}` như trên.

Không gian vector có phép toán tích vô hướng được gọi là không gian Euclide. Khi :math:`\bm{x} = \bm{y}` thì căn bậc hai của kết quả tích vô hướng được gọi là **chuẩn Euclide** (hay **Euclidean norm**) và được kí hiệu

.. math:: \lVert \bm{x} \rVert = \sqrt{\bm{x} \cdot \bm{x}} = \sqrt{x_1^2 + x_2^2 + \ldots + x_n^2}.

Như vậy ta có thể viết $\lVert \bm{x} \rVert^2 = \bm{x}^2$.

.. prf:theorem:: Bất đẳng thức Cauchy-Schwarz
    :label: thm-ineq-cauchy-schwarz

    Với hai vector :math:`\bm{x}` và :math:`\bm{y}` bất kì ta luôn có

    .. math:: \lVert \bm{x} \rVert \cdot \lVert \bm{y} \rVert \geqslant \lvert \bm{x} \cdot \bm{y} \rvert,

    nghĩa là tích độ dài của hai vector bất kì trong cùng không gian Euclide lớn hơn hoặc bằng tích vô hướng giữa chúng. Dấu bằng xảy ra khi và chỉ khi :math:`\dfrac{x_1}{y_1} = \dfrac{x_2}{y_2} = \ldots = \dfrac{x_n}{y_n}`. Nói cách khác là hai vector cùng phương.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Với mọi số thực :math:`t`, ta luôn có 

    .. math:: 0 \leqslant \lVert \bm{x} - t \bm{y} \rVert^2 = \bm{x}^2 - 2 t \bm{x} \cdot \bm{y} + t^2 \bm{y}^2 = \lVert \bm{x} \rVert^2 - 2 t \bm{x} \cdot \bm{y} + t^2 \lVert \bm{y} \rVert^2.

    Nếu xem biểu thức trên là đa thức bậc hai theo :math:`t`, để đa thức lớn hơn hoặc bằng :math:`0` với mọi :math:`t \in \mathbb{R}` thì ta phải có :math:`\Delta' \leqslant 0` và :math:`\lVert \bm{y} \rVert^2 > 0` (luôn đúng). Ta có

    .. math:: \Delta' = (\bm{x} \cdot \bm{y})^2 - \lVert \bm{x} \rVert^2 \cdot \lVert \bm{y} \rVert^2 \leqslant 0,

    tương đương với :math:`\lvert \bm{x} \cdot \bm{y} \rvert \leqslant \lVert \bm{x} \rVert \cdot \lVert \bm{y} \rVert` (điều phải chứng minh).

==================
Hệ cơ sở trực giao
==================

Cho không gian Euclide :math:`\mathcal{V}` và một cơ sở của nó là :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d`. Thuật toán trực giao Gram-Schmidt là thuật toán biến đổi cơ sở trên thành một cơ sở mới, trong đó các vector đều trực giao nhau.

.. prf:algorithm:: Thuật toán trực giao Gram-Schmidt
    :label: algo-gram-schmidt

    **Input:** :math:`\bm{v}_1`, ..., :math:`\bm{v}_d` trong :math:`\mathbb{R}^n`.

    **Output:** :math:`\bm{u}_1`, ..., :math:`\bm{u}_d` trong :math:`\mathbb{R}^n` mà :math:`\bm{u}_i \cdot \bm{u}_j = 0` với mọi :math:`i \neq j`.

    1. :math:`\bm{u}_1 \gets \bm{v}_1`
    2. for :math:`i = 2` to :math:`d`

       1. :math:`\bm{w} = \bm{v}_i`
       2. for :math:`j = i-1` to :math:`1`
        
          1. :math:`\mu_{i,j} = (\bm{v}_i \cdot \bm{u}_j) / (\bm{u}_i \cdot \bm{u}_j)`
          2. :math:`\bm{w} \gets \bm{w} - \mu_{i, j} \bm{u}_j`
        
       3. :math:`\bm{u}_i \gets \bm{w}`

    3. Trả về cơ sở trực giao :math:`\bm{u}_1`, ..., :math:`\bm{u}_d`

Nói cách khác, với :math:`\bm{u}_1 = \bm{v}_1`, với mỗi :math:`i = 2, 3, \ldots, d` ta tính vector :math:`\bm{u}_i` với công thức

.. math:: \bm{u}_i = \bm{v}_i - \sum_{j=1}^{i-1} \mu_{i,j} \bm{u}_j.

Ở đây :math:`\mu_{i,j} = \dfrac{\bm{v}_i \cdot \bm{u}_j}{\bm{u}_i \cdot \bm{u}_j}` là hệ số trước :math:`\bm{u}_j`.

.. prf:example:: 
    :label: exp-gram-schmidt

    Xét cơ sở :math:`\bm{v}_1 = (2, -2, 4)`, :math:`\bm{v}_2 = (1, -1, 0)` và :math:`\bm{v}_3 = (5, -3, 3)` của :math:`\mathbb{R}^3`.

    Đặt :math:`\bm{u}_1 = \bm{v}_1 = (2, -2, 4)`.

    Ta có

    .. math:: \mu_{2,1} = \dfrac{\bm{v}_2 \cdot \bm{u}_1}{\bm{u}_1 \cdot \bm{u}_1} = \dfrac{1 \cdot 2 + (-1) \cdot (-2) + 0 \cdot 4}{2^2 + (-2)^2 + 4^2} = \dfrac{4}{24} = \dfrac{1}{6}.

    Suy ra

    .. math:: \bm{u}_2 = \bm{v_2} - \mu_{2, 1} \bm{u}_1 = (1, -1, 0) - \dfrac{1}{6} \cdot (2, -2, 4) = \left(\dfrac{2}{3}, \dfrac{-2}{3}, \dfrac{-2}{3}\right).

    Tương tự

    .. math:: \mu_{3, 1} = \dfrac{\bm{v}_3 \cdot \bm{u}_1}{\bm{u}_1 \cdot \bm{u}_1} = \dfrac{5 \cdot 2 + (-3) \cdot (-2) + 3 \cdot 4}{2^2 + (-2)^2 + 4^2} = \dfrac{28}{24} = \dfrac{7}{6}.

    Tiếp theo

    .. math:: \mu_{3,2} = \dfrac{\bm{v}_3 \cdot \bm{u}_2}{\bm{u}_2 \cdot \bm{u}_2} = \dfrac{5 \cdot \dfrac{2}{3} + (-3) \cdot \dfrac{-2}{3} + 3 \cdot \dfrac{-2}{3}}{ \left(\dfrac{2}{3}\right)^2 + \left(\dfrac{-2}{3}\right)^2 + \left(\dfrac{-2}{3}\right)^2 } = \dfrac{5}{2}.

    .. math:: 
        
        \Rightarrow \quad \bm{u}_3 = & \bm{v}_3 - \mu_{3,1} \bm{u}_1 - \mu_{3,2} \bm{u}_2 \\ 
        = & (5, -3, 3) - \dfrac{7}{6} \cdot (2, -2, 4) - \dfrac{5}{2} \cdot \left(\dfrac{2}{3}, \dfrac{-2}{3}, \dfrac{-2}{3}\right) \\ = & (1, 1, 0).
        
    Ta có thể kiếm chứng rằng

    .. math:: \bm{u}_1 \cdot \bm{u}_2 = 2 \cdot \dfrac{2}{3} + (-2) \cdot \dfrac{-2}{3} + 4 \cdot \dfrac{-2}{3} = 0.

    Tương tự với :math:`\bm{u}_1 \cdot \bm{u}_3 = 0` và :math:`\bm{u}_2 \cdot \bm{u}_3 = 0`. Thêm nữa các vector này cũng độc lập tuyến tính nên cũng là một hệ cơ sở của :math:`\mathbb{R}^3`.

    Như vậy các vector :math:`\bm{u}_1`, :math:`\bm{u}_2`, :math:`\bm{u}_3` là một cơ sở trực giao của :math:`\mathbb{R}^3`.

.. prf:remark:: 
    :label: rmk-ortho
    
    Cơ sở trực giao cho phép ta tính độ dài của tất cả các vector khác trong không gian vector dễ dàng hơn.

Thật vậy, giả sử :math:`\bm{u}_1`, :math:`\bm{u}_2`, ..., :math:`\bm{u}_d` là các vector trong cơ sở trực giao. Mọi vector :math:`\bm{x}` trong không gian vector đều có dạng

.. math:: \bm{x} = \alpha_1 \bm{u}_1 + \alpha_2 \bm{u}_2 + \ldots + \alpha_d \bm{u}_d.

Khi đó

.. math:: \lVert \bm{x} \rVert^2 = \bm{x}^2 = (\alpha_1 \bm{u}_1 + \alpha_2 \bm{u}_2 + \ldots + \alpha_d \bm{u}_d)^2 = \sum_{i=1}^d \alpha_i^2 \bm{u}_i^2 + 2 \sum_{i \neq j} \bm{u}_i \bm{u}_j.
    
Do các vector trong cơ sở đều trực giao với nhau nên :math:`\bm{u}_i \cdot \bm{u}_j = 0` với :math:`i \neq j`, :math:`1 \leqslant i, j \leqslant d`. Từ đó ta có được

.. math:: \lVert \bm{x} \rVert^2 = \sum_{i=1}^d \alpha_i^2 \bm{u}_i^2 = \sum_{i=1}^d \alpha_i^2 \lVert \bm{u}_i \rVert^2,

hay

.. math:: \lVert \bm{x} \rVert = \sqrt{\alpha_1^2 \bm{u}_1^2 + \ldots + \alpha_d^2 \bm{u}_d^2}.

Kết quả rất đơn giản, độ dài của các vector bất kì là căn bậc hai của tổ hợp độ dài các vector trong cơ sở và hệ số tương ứng.

==================================
Chứng minh thuật toán Gram-Schmidt
==================================

Cho không gian vector :math:`\mathcal{V}` với cơ sở là các vector :math:`\bm{v}_1`, ..., :math:`\bm{v}_d`. Thuật toán Gram-Schmidt biến đổi và cho kết quả là cơ sở mới :math:`\bm{u}_1`, ..., :math:`\bm{u}_d` sao cho các vector trong cơ sở mới này trực giao nhau đôi một.

Đặt :math:`\bm{u}_1 = \bm{v}_1`.

**Bước 1.** Ta chứng minh với mọi :math:`k \geqslant 2` thì :math:`\bm{u}_k \cdot \bm{u}_1 = 0`.

Ta có

.. math:: \bm{u}_2 = \bm{v}_1 - \mu_{2, 1} \bm{u_1} = \bm{v}_2 - \dfrac{\bm{v}_2 \cdot \bm{u}_1}{\bm{u}_1 \cdot \bm{u}_1} \cdot \bm{u}_1.

Suy ra

.. math:: 
    
    \bm{u}_2 \cdot \bm{u}_1 & = \bm{v}_2 \cdot \bm{u}_1 - \dfrac{\bm{v}_2 \cdot \bm{u}_1}{\bm{u}_1 \cdot \bm{u}_1} \cdot (\bm{u}_1 \cdot \bm{u}_1) \\ 
    & = \bm{v}_2 \cdot \bm{u}_1 - \bm{v}_2 \cdot \bm{u}_1 = 0.
    
Như vậy với :math:`k = 2` thì đẳng thức đúng. Giả sử đẳng thức :math:`\bm{u}_k \cdot \bm{u}_1 = 0` đúng tới :math:`k \geqslant 2`. Xét :math:`k+1` ta có

.. math:: \bm{u}_{k+1} = \bm{v}_{k+1} - \sum_{j=1}^{k} \mu_{k+1, j} \bm{u}_j,

suy ra

.. math:: \bm{u}_{k+1} \cdot \bm{u}_1 = \bm{v}_{k+1} \cdot \bm{u}_1 - \sum_{j=1}^{k} \dfrac{\bm{v}_{k+1} \cdot \bm{u}_j}{\bm{u}_j \cdot \bm{u}_j} \cdot (\bm{u}_j \cdot \bm{u}_1).

Ta thấy rằng với :math:`j = 2, \ldots, k` thì :math:`\bm{u}_j \cdot \bm{u}_1 = 0` theo giả thiết quy nạp. Như vậy chỉ còn lại :math:`j = 1` và kết quả là

.. math:: \bm{u}_{k+1} \cdot \bm{u}_1 = \bm{v}_{k+1} \cdot \bm{u}_1 - \dfrac{\bm{v}_{k+1} \cdot \bm{u}_1}{\bm{u}_1 \cdot \bm{u}_1} \cdot (\bm{u}_1 \cdot \bm{u}_1) = 0.

**Bước 2.** Ta chứng minh với mọi :math:`k \geqslant 3` thì :math:`\bm{u}_k \cdot \bm{u}_2 = 0`.

Tương tự ta sử dụng quy nạp. Ta có

.. math:: \bm{u}_3 = \bm{v}_3 - \mu_{3,2} \bm{u}_2 - \mu_{3,1} \bm{u}_1,

suy ra

.. math:: \bm{u}_3 \cdot \bm{u}_2 = \bm{v}_3 \cdot \bm{u}_2 - \mu_{3,2} \bm{u}_2 \cdot \bm{u}_2 - \mu_{3,1} \cdot \bm{u}_1 \cdot \bm{u}_2.

Ta đã chứng minh được :math:`\bm{u}_2 \cdot \bm{u}_1 = 0`. Như vậy kết quả sẽ là

.. math:: \bm{u}_3 \cdot \bm{u}_2 = \bm{v}_3 \cdot \bm{u}_2 - \dfrac{\bm{v}_3 \cdot \bm{u}_2}{\bm{u}_2 \cdot \bm{u}_2} \cdot (\cdot \bm{u}_2 \cdot \bm{u}_2) = 0.

Với giả thiết quy nạp :math:`\bm{u}_k \cdot \bm{u}_2 = 0` đúng tới :math:`k \geqslant 3`, ta xét :math:`k+1`. Khi đó

.. math:: \bm{u}_{k+1} = \bm{v}_{k+1} - \sum_{j=1}^k \mu_{k+1,j} \bm{u}_j,

suy ra

.. math:: \bm{u}_{k+1} \cdot \bm{u}_2 = \bm{v}_{k+1} \cdot \bm{u}_2 - \sum_{j=1}^k \mu_{k+1,j} \bm{u}_j \cdot \bm{u}_2.

Theo giả thiết quy nạp thì mọi :math:`j \geqslant 3` đều cho kết quả :math:`\bm{u}_j \cdot \bm{u}_2 = 0`, thêm nữa là :math:`\bm{u}_1 \cdot \bm{u}_2 = 0` do chứng minh trên. Như vậy trong tổng chỉ còn lại :math:`j = 2` và kết quả sẽ là

.. math:: \bm{u}_{k+1} \cdot \bm{u}_2 = \bm{v}_{k+1} \cdot \bm{u}_2 - \dfrac{\bm{v}_{k+1} \cdot \bm{u}_2}{\bm{u}_2 \cdot \bm{u}_2} \cdot (\bm{u}_2 \cdot \bm{u}_2) = 0.

Từ đây có thể thấy, sử dụng phương pháp quy nạp ta có thể chứng minh được rằng với mỗi số :math:`n \geqslant 2`, thì mọi :math:`k \geqslant n+1` ta đều có :math:`\bm{u}_k \cdot \bm{u}_n = 0`, hay nói cách khác là khi thuật toán tính :math:`\bm{u}_k` thì nó sẽ trực giao với tất cả :math:`\bm{u}_1`, :math:`\bm{u}_2`, ..., :math:`\bm{u}_{k-1}`.
