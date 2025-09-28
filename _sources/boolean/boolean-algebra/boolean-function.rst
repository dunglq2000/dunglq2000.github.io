Hàm boolean
===========

Algebraic Normal Form
---------------------

Đặt :math:`f(\bm{x})` là hàm boolean :math:`n` biến. Với số :math:`m \leqslant n` thì

.. math:: 
    
    f(x_1, \ldots, x_n) = \bigoplus_{a_1, \ldots, a_m \in \mathbb{F}_2} & (x_1 \oplus a_1 \oplus 1) \times \cdots \times \\
    \times & (x_m \oplus a_m \oplus 1) \cdot f(a_1, \ldots, a_m, x_{m+1}, \ldots, x_n)
  

.. admonition:: Chứng minh
    :class: danger, dropdown

    Chọn bộ :math:`(b_1, \ldots, b_m)` bất kì thuộc :math:`\mathbb{F}_2^m`.

    Thay :math:`x_i` bởi :math:`b_i` với :math:`i = 1, \ldots, m` thì

    .. math:: 
        
        f(b_1, \ldots, b_m, x_{m+1}, x_m) = \bigoplus_{a_1, \ldots, a_m \in \mathbb{F}_2} (b_1 \oplus a_1 \oplus 1) \cdots (b_m \oplus a_m \oplus 1) \cdot f(a_1, \ldots, a_m, x_{m+1}, \ldots, x_n).

    Ở vế phải, tích :math:`\prod\limits_{i=1}^m (b_i \oplus a_i \oplus 1) = 1` khi và chỉ khi :math:`b_i \oplus a_i \oplus 1 = 1` với mọi :math:`i = 1, \ldots, m`.

    Nói cách khác là khi :math:`b_i \equiv a_i` thì ta còn :math:`f` ở vế phải, còn các trường hợp kia thì bằng :math:`0`. Do đó ta có điều phải chứng minh.

Khi đó, :math:`f(a_1, \ldots, a_m, x_{m+1}, \ldots, x_m)` được gọi là **hệ số khai triển của hàm** :math:`f` **theo các biến** :math:`x_1`, ..., :math:`x_m`.

.. prf:example:: 
    :label: exp-khai-trien-bool

    Xét :math:`f(x_1, x_2) = x_1 x_2 \oplus 1`. Với :math:`m = 1`, ta có

    .. math:: 
        
        a_1 = 0 & \Rightarrow (x_1 \oplus 0 \oplus 1) \cdot f(0, x_2) = (x_1 \oplus 1) \cdot 1 = x_1 \oplus 1, \\
        a_1 = 1 & \Rightarrow (x_1 \oplus 1 \oplus 1) \cdot f(1, x_2) = x_1 \oplus (x_2 \oplus 1).

    Như vậy

    .. math:: f(x_1, x_2) = (x_1 \oplus 1) \oplus \left(x_1 \cdot (x_2 \oplus 1)\right).

    Nếu khai triển vế phải ra chúng ta thấy bằng với hàm :math:`f` ban đầu.

Tương ứng với :math:`m` biến ta có :math:`2^m` hệ số khai triển.

Đặt :math:`f_1`, ..., :math:`f_{2^m}` là các hệ số khai triển hàm :math:`f` theo :math:`m` biến bất kì. Khi đó

.. math:: 
    :label: wt-decomp

    \mathrm{wt}(f) = \sum_{i=1}^{2^m} \mathrm{wt} (f_i).

.. prf:definition:: Algebraic Normal Form
    :label: def-bool-ANF

    Với hàm boolean :math:`n` biến :math:`f(x_1, x_2, \ldots, x_n)`, **algrebaric normal form** (hay **ANF**, **dạng chuẩn tắc đại số**, **алгебраическая нормальная форма**) tương ứng với hàm bool đó là cách biểu diễn đa thức đó dưới dạng tổng các tích như sau

    .. math:: 

        f(x_1, x_2, \ldots, x_n) = a_0 \oplus a_1 x_1 
        \oplus a_2 x_2 \oplus a_3 x_1 x_2 \oplus \ldots 
        \oplus a_k x_1 x_2 \ldots x_n

    với :math:`a_i \in \{ 0, 1 \}`.
    
    Ta thấy rằng có :math:`n` biến, do đó có :math:`2^n` hệ số :math:`a_i` với mỗi :math:`i = 0, 1, \ldots, 2^n-1`.

Trong các tài liệu tiếng Nga thì ANF còn được gọi là **đa thức Zhegalkin** (hay **полином Жегалкина**)

.. prf:definition:: Bậc của đa thức Zhegalkin
    :label: def-deg-ANF
    
    Tương tự như bậc của một đa thức đại số thông thường, bậc của đa thức Zhegalkin là bậc của đơn thức chứa nhiều biến :math:`x_i` nhất. Kí hiệu là :math:`\deg(f)`.

.. prf:example:: 
    :label: exp-deg-ANF

    Xét hàm boolean :math:`f(x, y, z) = 1 \oplus x \oplus yz \oplus xyz`. Khi đó :math:`\deg(f) = 3` vì đơn thức chứa nhiều biến nhất là :math:`xyz` có :math:`3` đơn thức.

    Xét hàm boolean :math:`f(x, y, z) = 1 \oplus z \oplus zy \oplus xy`. Khi đó :math:`\deg(f) = 2` vì đơn thức chứa nhiều biến nhất là :math:`zy` (cũng có thể xét :math:`xy`).

.. prf:definition:: Trọng số của hàm boolean
    :label: def-weight-bool

    **Trọng số** (hay **weight**, **вес**) của hàm boolean :math:`n` biến :math:`f(x_1, x_2, \ldots, x_n)` là số lượng giá trị khác :math:`0` của hàm :math:`f`.

    Kí hiệu là :math:`\mathrm{wt}(f)`.

.. prf:example:: 
    :label: exp-weight-bool
    
    Hàm boolean :math:`f(x, y) = (0, 1, 0, 1)` có trọng số :math:`\mathrm{wt}(f) = 2`.

    Hàm boolean :math:`f(x, y, z) = (1, 0, 1, 1, 1, 0, 0, 1)` có trọng số :math:`\mathrm{wt}(f) = 5`.

.. prf:property:: Một số tính chất của trọng số
    :label: prop-weight

    Gọi :math:`f` là hàm boolean :math:`n` biến. Khi đó:

    1. :math:`0 \leqslant \mathrm{wt}(f) \leqslant 2^n`.
    2. :math:`\mathrm{wt}(f \oplus \bm{1}) = 2^n - \mathrm{wt}(f)`.
    3. Nếu :math:`h` cũng là một hàm boolean :math:`n` biến thì

    .. math:: \mathrm{wt}(f \oplus h) = \mathrm{wt}(f) + \mathrm{wt}(h) - 2 \mathrm{wt}(fh).

    4. :math:`\mathrm{wt}(f)` nhận giá trị lẻ khi và chỉ khi :math:`\deg(f) = n`.

.. prf:definition:: Hàm boolean cân bằng
    :label: def-balanced-bool
    
    Nếu hàm boolean :math:`n` biến :math:`f` có trọng số bằng :math:`2^{n-1}` thì :math:`f` được gọi là hàm boolean **cân bằng** (hay **balanced**, **сбалансированная**).

.. prf:remark:: 
    :label: rmk-depend

    Ta nói hàm boolean :math:`g` *giả phụ thuộc* vào biến :math:`y` nếu :math:`g(x_1, \ldots, x_n, y) = f(x_1, \ldots x_n)`. Khi đó :math:`\mathrm{wt} (g) = 2 \mathrm{wt} (f)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Do 

    .. math:: g(x_1, \ldots, x_n, 0) = g(x_1, \ldots, x_n, 1) = f(x_1, \ldots, x_n)

    nên ta có điều phải chứng minh.

.. prf:remark:: 
    :label: rmk-depend-balanced

    Đặt :math:`f(x_1, \ldots, x_n)` và :math:`g(y_1, \ldots, y_m)` là các hàm boolean phụ thuộc vào tập các biến không giao nhau. Khi đó:

    1. Nếu :math:`f` và :math:`g` là các hàm số khác hằng :math:`1` thì :math:`f \cdot g` không là hàm cân bằng.

    2. :math:`f` hoặc :math:`g` cân bằng khi và chỉ khi :math:`f \oplus g` cân bằng.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`\bm{x} = (x_1, \ldots, x_n)` và :math:`\bm{y} = (y_1, \ldots, y_m)`.

    1. Đặt :math:`\mathrm{wt}(f) = r < 2^n` và :math:`\mathrm{wt}(g) = s < 2^m`. Vì :math:`f(\bm{x}) \cdot g(\bm{y}) = 1` khi và chỉ khi :math:`f(\bm{x}) = g(\bm{y}) = 1` nên :math:`\mathrm{wt}(f \cdot g) = r \cdot s`.

    Do đó nếu :math:`f \cdot g` cân bằng thì :math:`2^{n+m-1} = \mathrm{wt}(f \cdot g) = r \cdot s`.

    Như vậy :math:`r = 2^k` và :math:`s = 2^l` với :math:`k \leqslant n-1` và :math:`l \leqslant m-1`.

    Suy ra :math:`r \cdot s \leqslant 2^{n+m-2}`. Điều này vô lý vì :math:`r \cdot s = 2^{n + m - 1} > 2^{n+m-2}`. Như vậy giả sử ban đầu :math:`r < 2^n` là sai, tương tự với :math:`s` và ta có điều phải chứng minh.

    2. Chú ý rằng :math:`f(\bm{x}) \oplus g(\bm{y}) = 1` khi và chỉ khi :math:`f(\bm{x}) \neq g(\bm{y})`, suy ra 

    .. math:: \mathrm{wt}(f \oplus g) = \mathrm{wt}(f) \cdot \mathrm{wt}(\bar{g}) + \mathrm{wt}(\bar{f}) \cdot \mathrm{wt}(g).

    *Điều kiện đủ.* Giả sử hàm :math:`f` cân bằng, suy ra

    .. math:: \mathrm{wt}(f) = \mathrm{wt}(\bar{f}) = 2^{n-1}.

    Như vậy

    .. math:: \mathrm{wt}(f \oplus g) = 2^{n-1} \cdot \mathrm{wt}(g) + 2^{n-1} \cdot \mathrm{wt}(\bar{g}) = 2^{n-1} \cdot 2^m.

    Vậy :math:`f \oplus g` là hàm cân bằng.

    *Điều kiện cần.* Giả sử :math:`\mathrm{wt}(f) = r \neq 2^{n-1}` và :math:`\mathrm{wt}(g) = s`. Như vậy

    .. math:: \mathrm{wt}(f \oplus g) = r (2^m - s) + s (2^n - r) = 2^{n+m-1}

    do :math:`f \oplus g` là hàm cân bằng. Tiếp theo

    .. math:: s = \dfrac{2^{n+m-1} - 2^m \cdot r}{2^n - 2r} = 2^{m-1}.

    Vậy :math:`g` là hàm cân bằng.

Đặt

.. math:: 
    :label: g

    f(x_1, \ldots, x_n) = \bigoplus_{a_1, \ldots, a_n \in \mathbb{F}_2} g(a_1, \ldots, a_n) \cdot x_1^{a_1} \cdots x_n^{a_n}.

Hàm :math:`g` khi đó được gọi là **hệ số ANF** của hàm :math:`f`.

Ánh xạ :math:`\mu(f) = g` được gọi là **biến đổi Mobius** (hay **преобразование Мёбиуса**).

.. prf:example:: 
    :label: exp-mobius

    Cho hàm bool :math:`f(x, y) = x \vee y`. Ta có bảng chân trị sau.

    +-----------+-----------+-----------------+
    | :math:`x` | :math:`y` | :math:`f(x, y)` |
    +===========+===========+=================+
    | :math:`0` | :math:`0` |    :math:`0`    |
    +-----------+-----------+-----------------+
    | :math:`0` | :math:`1` |    :math:`1`    |
    +-----------+-----------+-----------------+
    | :math:`1` | :math:`0` |    :math:`1`    |
    +-----------+-----------+-----------------+
    | :math:`1` | :math:`1` |    :math:`1`    |
    +-----------+-----------+-----------------+

    Bảng chân trị này tương đương với đa thức Zhegalkin

    .. math:: f(x, y) = x \oplus y \oplus xy.

ANF ở ví dụ trên có thể được viết lại

.. math:: f(x, y) = 0 \cdot x^0 y^0 \oplus 1 \cdot x^0 y^1 \oplus 1 \cdot x^1 y^0 \oplus 1 \cdot x^1 y^1.

Như vậy biến đổi Mobius của hàm :math:`f` là

+-----------+-----------+-----------------+--------------------+
| :math:`x` | :math:`y` | :math:`f(x, y)` | :math:`g = \mu(f)` |
+===========+===========+=================+====================+
| :math:`0` | :math:`0` | :math:`0`       | :math:`0`          |
+-----------+-----------+-----------------+--------------------+
| :math:`0` | :math:`1` | :math:`1`       | :math:`1`          |
+-----------+-----------+-----------------+--------------------+
| :math:`1` | :math:`0` | :math:`1`       | :math:`1`          |
+-----------+-----------+-----------------+--------------------+
| :math:`1` | :math:`1` | :math:`1`       | :math:`1`          |
+-----------+-----------+-----------------+--------------------+

Ta kí hiệu :math:`\bm{x}^{\bm{a}} = x_1^{a_1} \cdots x_n^{a_n}` với

- :math:`\bm{x} = (x_1, \ldots, x_n)`;
- :math:`\bm{a} = (a_1, \ldots, a_n)`.

Do :math:`x_i^{a_i} = 1` khi và chỉ khi :math:`a_i \leqslant x_i`, ta có :math:`\bm{x}^{\bm{a}} = 1` khi và chỉ khi :math:`\bm{a} \preccurlyeq \bm{x}` theo nghĩa :math:`a_i \leqslant x_i` với math:`i = 1, \ldots, n`.

Ta có thể viết lại :eq:`g` là

.. math:: f(\bm{x}) = \bigoplus_{\bm{a} \in \mathbb{F}_2^n} g(\bm{a}) \cdot \bm{x}^{\bm{a}} = \bigoplus_{\bm{a} \in \mathbb{F}_2^n} g(\bm{a}).

.. prf:remark:: Biến đổi Mobius
    :label: rmk-mobius-trans

    Đặt :math:`f \in \mathcal{F}_n` và :math:`g = \mu(f)`. Khi đó với mọi :math:`\bm{a} \in \mathbb{F}_2^n` ta có

    .. math:: g(\bm{a}) = \bigoplus_{\bm{x} \preccurlyeq \bm{a}} f(\bm{x}).

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta chứng minh bằng quy nạp theo trọng số của :math:`\bm{a}`.

    Ở bước cơ sở khi trọng số bằng không, :math:`g(\bm{0}) = f(\bm{0})` với :math:`\bm{0}` là vector chứa :math:`n` số :math:`0`.

    Giả thiết quy nạp: giả sử mệnh đề đúng với mọi vector :math:`\bm{a}` có trọng số nhỏ hơn :math:`p`.

    Khi :math:`\bm{a}` có trọng số bằng :math:`p`, ta có

    .. math:: 
        
        f(\bm{a}) = \bigoplus_{\bm{x} \preccurlyeq \bm{a}} g(\bm{x}) & = \left( \bigoplus_{\bm{x} \prec \bm{a}} g(\bm{x}) \right) \oplus g(\bm{a}) \quad (\text{tách thành phần nhỏ hơn và bằng} \, \bm{a}) \\
        & = \left(\bigoplus_{\bm{x} \prec \bm{a}} \bigoplus_{\bm{y} \preccurlyeq \bm{x}} f(\bm{y})\right) \oplus g(\bm{a}) \quad (\text{sử dụng giả thiết quy nạp thay} \, g(\bm{x})).

    Đặt 

    .. math:: S = \bigoplus_{\bm{x} \prec \bm{a}} \bigoplus_{\bm{y} \preccurlyeq \bm{x}} f(\bm{y}) = \bigoplus_{\bm{y} \prec \bm{a}} f(\bm{y}) \bigoplus_{\bm{y} \preccurlyeq \bm{x} \prec \bm{a}} 1 = \bigoplus_{\bm{y} \prec \bm{a}} f(\bm{y}).

    Đẳng thức thứ hai đúng là do :math:`\bm{y}` nhận tất cả vector từ :math:`\bm{0}` tới :math:`\bm{x}` mà :math:`\bm{x} \prec \bm{a}` nên thực chất có thể thay :math:`\bm{x}` thành :math:`\bm{y}`.

    Đẳng thức cuối đúng là do :math:`2^{\mathrm{wt}(\bm{a}) - \mathrm{wt}(\bm{y})} - 1` là số lẻ nào đó mà :math:`\bm{y} \preccurlyeq \bm{x} \prec \bm{a}`, suy ra :math:`g(\bm{a}) = S \oplus f(\bm{a}) = \bigoplus\limits_{\bm{y} \preccurlyeq \bm{a}} f(\bm{y})`.

.. prf:corollary::
    :label: cor-mobius

    .. math:: \mu(\mu(f)) = f.

.. prf:remark::
    :label: rmk-mobius

    .. math:: g(\bm{1}) = \bigoplus_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x})

    với :math:`\bm{1}` là vector có :math:`n` số :math:`1`.

.. prf:remark:: 
    :label: rmk-weight

    Nếu :math:`f \in \mathcal{F}_n` và :math:`\deg f = d \geqslant 1` thì

    .. math:: 2^{n - d} \leqslant \mathrm{wt} (f) \leqslant 2^n - 2^{n-d}.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`x_{i_1} \cdots x_{i_d}` là đơn thức có bậc cao nhất ở ANF. Khai triển :math:`f` thành :math:`n-d` biến và đặt :math:`f_1`, ..., :math:`f_{2^{n-d}}` là các hệ số khai triển.

    Ở ANF, mỗi hệ số đều có :math:`x_{i_1}`, ..., :math:`x_{i_d}` nên mọi hệ số đều khác hằng, suy ra

    .. math:: 1 \leqslant \mathrm{wt} (f_i) \leqslant 2^d - 1

    với :math:`i = 1, \ldots, 2^{n-d}`. Ta có điều phải chứng minh.

Nói riêng, nếu :math:`\deg f = 1` thì :math:`f` là hàm cân bằng.

Phụ thuộc tuyến tính
--------------------

.. prf:definition:: 
    :label: def-linear-depend

    Hàm :math:`f(x_1, \ldots, x_n)` được gọi là **linear dependent** (hay **линейно зависить**) vào biến :math:`x_i` nếu :math:`f` có thể biểu diễn ở dạng

    .. math:: f(x_1, \ldots, x_n) = g(x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n) \oplus x_i

    với :math:`g \in \mathcal{F}_{n-1}`.

Theo trường hợp riêng ở trên thì nếu :math:`f` linear dependent vào một biến bất kì thì :math:`f` là hàm cân bằng.

Ta có thể diễn đạt định nghĩa trên theo cách khác:

.. math:: f(x_1, \ldots, x_{i-1}, 0, x_{i+1}, \ldots, x_n) \neq f(x_1, \ldots, x_{i-1}, 1, x_{i+1}, \ldots, x_n).

.. prf:definition:: 
    :label: def-quasi-linear-depend

    Hàm :math:`f(x_1, \ldots, x_n)` được gọi là **quasi-linear dependent** (hay **квазилинейно зависить**) trên cặp biến :math:`x_i` và :math:`x_j` nếu :math:`f` đổi giá trị khi ta đảo giá trị ở vị trí :math:`i` và :math:`j`.

    Nói cách khác, ta có

    .. math:: f(x_1, \ldots, x_i, \ldots, x_j, \ldots, x_n) = \bar{f}(x_1, \ldots, \bar{x}_i, \ldots, \bar{x}_j, \ldots, x_n)

    với :math:`x_i, x_j \in \mathbb{F}_2`.

.. prf:remark:: 
    :label: quasi-fg

    Hàm :math:`f(x_1, \ldots, x_n, y, z)` là hàm quasi-linear dependent trên biến :math:`y` và :math:`z` khi và chỉ khi :math:`f` có dạng

    .. math:: f(x_1, \ldots, x_n, y, z) = g(x_1, \ldots, x_n, y \oplus z) \oplus y.

.. admonition:: Chứng minh
    :class: danger, dropdown

    **Điều kiện cần.** Đặt :math:`\bm{x} = \mathbb{F}_2^n`. Khi đó

    .. math:: 
        
        f(\bm{x}, 0, 0) = g(\bm{x}, 0), \quad f(\bm{x}, 1, 1) = g(\bm{x}, 0) \oplus 1 = \bar{f}(\bm{x}, 0, 0) \\
        f(\bm{x}, 0, 1) = g(\bm{x}, 1), \quad f(\bm{x}, 1, 0) = g(\bm{x}, 1) \oplus 1  = \bar{f}(\bm{x}, 1, 0).

    Như vậy :math:`f` là quasi-linear dependent.

    **Điều kiện đủ.** Khai triển :math:`f` theo :math:`y` và :math:`z`, sau đó thay $:math:`(\bm{x}, 0, 0)` bởi :math:`f(\bm{x}, 0, 0) \oplus 1`, tương tự :math:`f(\bm{x}, 0, 1)` thành :math:`f(\bm{x}, 0, 1) \oplus 1`. Nói cách khác là

    .. math:: 
        :label: fyz
        
        f(\bm{x}, y, z) & = (y \oplus 1) \cdot (z \oplus 1) \cdot f(\bm{x}, 0, 0) \\
        & \oplus (y \oplus 1) \cdot z \cdot f(\bm{x}, 0, 1) \\
        & \oplus y \cdot (z \oplus 1) \cdot f(\bm{x}, 1, 0) \\
        & \oplus y \cdot z \cdot f(\bm{x}, 1, 1).

    Ta gom hai nhóm:

    .. math:: 
        
        & (y \oplus 1) \cdot (z \oplus 1) \cdot f(\bm{x}, 0, 0) \oplus y \cdot z \cdot f(\bm{x}, 1, 1) \\
        = & (yz \oplus y \oplus z \oplus 1) \cdot f(\bm{x}, 0, 0) \oplus y z \cdot (f(\bm{x}, 0, 0) \oplus 1) \\
        = & (y \oplus z \oplus 1) \cdot f(\bm{x}, 0, 0) \oplus yz,
        
    và

    .. math:: 
    
        & (y \oplus 1) \cdot z \cdot f(\bm{x}, 0, 1) \oplus y \cdot (z \oplus 1) \cdot f(\bm{x}, 1, 0) \\
        = & (y \oplus 1) \cdot z \cdot f(\bm{x}, 0, 1) \oplus y \cdot (z \oplus 1) \cdot (f(\bm{x}, 0, 1) \oplus 1) \\
        = & (y \oplus z) \cdot f(\bm{x}, 0, 1) \oplus yz \oplus y.
        
    Tóm lại, phương trình khai triển ở :eq:`fyz` sẽ tương đương với

    .. math:: f(\bm{x}, y, z) = \underbrace{(y \oplus z \oplus 1) \cdot f(\bm{x}, 0, 0) \oplus (y \oplus z) \cdot f(\bm{x}, 0, 1)}_{g(\bm{x}, y \oplus z)} \oplus y.

.. prf:remark:: 
    :label: rmk-quasi-linear-balanced
    
    Nếu hàm boolean quasi-linear dependent trên hai biến bất kì thì hàm boolean đó cân bằng.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`\bm{x} \in \mathbb{F}_2^n`. Do :math:`f(\bm{x}, y, z) \in \mathcal{F}_{n+2}` và :math:`f` quasi-linear dependent trên hai biến :math:`y` và :math:`z` nên theo :prf:ref:`quasi-fg` thì :math:`f` có dạng

    .. math:: f(\bm{x}, y, z) = g(\bm{x}, y \oplus z) \oplus y.

    Do tổng (XOR) của :math:`f` có phần tuyến tính nên :math:`f` cân bằng.

    Chúng ta cũng có thể chứng minh theo cách khác bằng khai triển :math:`f` theo :math:`y` và :math:`z`

    .. math:: 
    
        f(\bm{x}, y, z) & = y \cdot z \cdot (g(\bm{x}, 0) \oplus 1) \oplus y \cdot (z \oplus 1) \cdot (g(\bm{x}, 1) \oplus 1) \\
        & \oplus (y \oplus 1) \cdot z \cdot g(\bm{x}, 1) \oplus (y \oplus 1) \cdot (z \oplus 1) \cdot g(\bm{x}, 0).

    Theo đẳng thức :eq:`wt-decomp` thì

    .. math:: \mathrm{wt}(f) = \mathrm{wt}(\bar{g}(\bm{x}, 0)) + \mathrm{wt}(\bar{g}(\bm{x}, 1)) + \mathrm{wt}(g(\bm{x}, 1)) + \mathrm{wt}(g(\bm{x}, 0)) = 2^{n+1}.

.. prf:example:: hàm quasi-linear dependent
    :label: exp-quasi-linear

    Hàm boolean

    .. math:: f(x, y, z) = y \oplus xz \oplus xy

    quasi-linear dependent trên hai biến :math:`y` và :math:`z`.

Cách tìm đa thức Zhegalkin từ bảng chân trị
-------------------------------------------

Ta có nhiều phương pháp để tìm đa thức Zhegalkin của một hàm boolean từ bảng chân trị. 

Phương pháp tam giác
^^^^^^^^^^^^^^^^^^^^

Ở hàng đầu ta viết các phần tử bảng chân trị từ trái sang phải. Với :math:`n` biến sẽ có :math:`2^n` ô.

Hàng thứ hai có :math:`2^n-1` ô. Phần tử dưới sẽ bằng XOR của :math:`2` phần tử ngay trên nó (tạo thành tam giác). Tiếp tục như vậy tới khi ta có hàng cuối chỉ có :math:`1` ô.

.. figure:: ../../figures/boolean/zhegalkin-1.*

    Phương pháp tam giác

Khi đó, tương ứng với các biến, nếu biến đó là :math:`1` thì đơn thức sẽ chứa biến đó, :math:`0` thì không ghi. Ở ví dụ trên, nếu :math:`(x, y) = (0, 0)`  thì không có gì (phần tử :math:`1`), :math:`(x, y) = (0, 1)` tương ứng với đơn thức :math:`y` trong đa thức Zhegalkin, :math:`(x, y) = (1, 0)` tương ứng đơn thức :math:`x`. Cuối cùng :math:`(x, y) = (1, 1)` tương ứng đơn thức :math:`xy`.

Hệ số trước mỗi đơn thức là phần tử đầu tiên bên trái theo bảng kim tự tháp. Như vậy đa thức Zhegalkin là:

.. math:: 

    f(x, y) = 0 \cdot 1 \oplus 1 \cdot y \oplus 1 \cdot x \oplus 
        1 \cdot xy = x \oplus y \oplus xy.

Đa thức Zhegalkin đóng vai trò quan trọng trong nhiều lĩnh vực, bao gồm cả toán học, vật lý, khoa học máy tính, vì AND và XOR là hai toán tử đại số cơ bản, do đó biểu diễn đa thức Zhegalkin được gọi là dạng chuẩn tắc đại số như ở trên đề cập.

Một ví dụ khác của đa thức Zhegalkin với hàm :math:`3` biến :math:`x`, :math:`y` và :math:`z` như hình sau:

.. figure:: ../../figures/boolean/zhegalkin-2.*

Như vậy ứng với hàm boolean :math:`f` thì đa thức Zhegalkin là:

.. math:: f(x, y, z) = z \oplus yz \oplus x \oplus xz \oplus xyz.

Phương pháp Möbius
^^^^^^^^^^^^^^^^^^

Phương pháp này cho phép chúng ta tính hệ số đa thức Zhegalkin như phương pháp tam giác nhưng nhanh hơn và đỡ sai sót hơn.

Đầu tiên chúng ta chia đôi bảng chân trị thành hai nửa trái phải. Nửa trái giữa nguyên, mỗi phần tử ở nửa phải được XOR (cộng modulo :math:`2`) với phần tử tương ứng ở nửa trái.

Ví dụ với hàm :math:`f(x, y) = (0, 1, 1, 1)` như trên.

Bước 1, ta giữ nguyên hai phần tử đầu :math:`0` và :math:`1`. Phần tử thứ ba (mới) bằng phần tử thứ ba (cũ) XOR với phần tử đầu, nghĩa là :math:`0 \oplus 1 = 1`. Phần tử thứ tư (mới) bằng phần tử thứ tư (cũ) XOR với phần tử thứ hai, nghĩa là :math:`1 \oplus 1 = 0`.

Tiếp theo, chúng ta xử lý như trên cho hai phần tử bên nửa trái (hai phần tử bên nửa phải xử lý tương tự).

.. figure:: ../../figures/boolean/zhegalkin-3.*

    Bước 1

.. figure:: ../../figures/boolean/zhegalkin-4.*

    Bước 2

Như vậy ta có kết quả là :math:`(0, 1, 1, 1)`, tương ứng với các đơn thức :math:`1`, :math:`y`, :math:`x`, :math:`xy` (như trên). Vậy đa thức Zhegalkin là :math:`f(x, y) = x \oplus y \oplus xy`.
