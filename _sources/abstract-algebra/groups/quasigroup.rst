==========
Quasigroup
==========

.. prf:definition:: Quasigroup
    :label: def-quasigroup
    
    Tập :math:`Q` và phép toán hai ngôi :math:`\star` được gọi là **quasigroup** (hay **квазигруппа**) nếu với mọi :math:`a, b \in Q`, tồn tại duy nhất hai phần tử :math:`x, y \in Q` sao cho
    
    .. math:: a \star x = b, \quad y \star a = b.

.. prf:example:: 
    :label: exp-quasigroup-1
    
    Mọi nhóm đều là quasigroup.

.. prf:example:: 
    :label: exp-quasigroup-2
    
    :math:`(\mathbb{Z}, -)` không phải là nhóm nhưng là quasigroup.

.. admonition:: Chứng minh
    :class: dropdown, danger

    Với mọi :math:`a, b, \in \mathbb{Z}` ta tìm :math:`x`, :math:`y` sao cho :math:`a - x = b` và :math:`y - a = b`.
    
    Khi đó :math:`x = a - b` và :math:`y = a + b`, nói cách khác là tồn tại hai phần tử duy nhất :math:`x`, :math:`y`

.. prf:remark:: 
    :label: rmk-quasigroup
    
    Quasigroup không có tính kết hợp nên chúng ta không thể định nghĩa phép tính :math:`a^n` như với nhóm.

.. prf:definition:: :math:`d`-quasigroup
    :label: def-d-quasigroup
    
    Xét quasigroup :math:`(Q, g)` với :math:`g` là ánh xạ

    .. math:: g: Q^d \to Q, \quad d \geqslant 2

    được gọi là :math:`d`-**quasigroup** và :math:`g` được gọi là **toán tử quasigroup**.

Định nghĩa quasigroup ở đầu bài tương ứng với :math:`d = 2` (với :math:`g` là toán tử hai ngôi).

.. prf:definition:: Bảng Latin
    :label: def-latin-table
    
    Bảng Latin là bảng gồm :math:`k` hàng và :math:`k` cột. Ta viết các số từ :math:`0` tới :math:`k - 1` lên bảng sao cho mỗi hàng có :math:`k` phần tử khác nhau và mỗi cột cũng có :math:`k` phần tử khác nhau.

Ví dụ, với :math:`k = 2` ta có bảng

+-----------+-----------+
| :math:`0` | :math:`1` |
+-----------+-----------+
| :math:`1` | :math:`0` |
+-----------+-----------+

Ví dụ, với :math:`k = 3` ta có bảng

+-----------+-----------+-----------+
| :math:`0` | :math:`2` | :math:`1` |
+-----------+-----------+-----------+
| :math:`1` | :math:`0` | :math:`2` |
+-----------+-----------+-----------+
| :math:`2` | :math:`1` | :math:`0` |
+-----------+-----------+-----------+

Mỗi ô được biểu diễn bởi bộ ba (тройка) :math:`(i, j, t)` với

- :math:`i` là vị trí hàng;
- :math:`j` là vị trí cột;
- :math:`t` là giá trị tại ô :math:`(i, j)`.

.. prf:definition:: Homotopy
    :label: def-homotopy
    
    Giả sử :math:`(P, \star)` và :math:`(Q, *)` là hai quasigroup. Khi đó **quasigroup homotopy** từ :math:`P` tới :math:`Q` là bộ ba :math:`(\alpha, \beta, \gamma)` biểu diễn ba ánh xạ từ :math:`P` tới :math:`Q` thỏa

    .. math:: \alpha(x) * \beta(y) = \gamma(x \star y)

    với mọi :math:`x, y \in P`.

.. prf:definition:: Isotopy
    :label: def-isotopy
    
    Khi cả ba ánh xạ :math:`\alpha`, :math:`\beta` và :math:`\gamma` đều là song ánh thì ta nói homotopy là **isotopy** (hay **изотопия**).

.. prf:definition:: Autotopy
    :label: def-autotopy
    
    **Autotopy** là isotopy tới chính nó, nghĩa là :math:`P \equiv Q`.

.. prf:remark:: 
    :label: rmk-isotopy

    Isotopy là quan hệ tương đương.

    .. math:: Q_1 \sim Q_2 \Longleftrightarrow Q_1 \ \text{isotopy với} \ Q_2.

.. prf:definition:: Parastrophe
    :label: def-parastrophe

    Từ toán tử ban đầu :math:`\star` ta định nghĩa thêm năm toán tử khác là:

    1. Toán tử :math:`\circ` với :math:`x \circ y = y \star x` là toán tử đối của toán tử :math:`\star`.
    2. Toán tử :math:`\setminus` với :math:`x \setminus y = z` tương đương với :math:`y = x \star z`.
    3. Toán tử đối của :math:`\setminus`.
    4. Toán tử :math:`/`.
    5. Toán tử đối của :math:`/`.

    Như vậy có tất cả sáu toán tử quasigroup và ta gọi tập các toán tử đó là **parastrophe** (hay **conjugation**, **парастрофия**).

.. prf:definition:: Loop
    :label: def-loop

    **Loop** (hay **лупа**) là quasigroup :math:`(Q, \star)` với phần tử đơn vị :math:`e` sao cho với mọi :math:`x \in Q` thì

    .. math:: e \star x = x \star e = x.

Khi đó mỗi phần tử trong quasigroup sẽ có phần tử nghịch đảo (inverse) trái và phải tương ứng. Lưu ý rằng hai nghịch đảo không nhất thiết phải bằng nhau.

.. prf:definition:: Nhóm nhân
    :label: def-mult-group

    Ta định nghĩa phép nhân (toán tử nhân)

    .. math:: 
        
        L_x : Q \to Q, \quad L_x(y) = x \star y, \\
        R_x : Q \to Q, \quad R_x(y) = y \star x.  

    Đặt

    .. math:: \mathrm{mult}(Q) = \langle L_q, R_q : q \in Q \rangle.

    Ta nói :math:`\mathrm{mult}(Q)` là **nhóm nhân của quasigroup** (hay **группа умножений квазигруппы**).

.. prf:definition:: Chỉ số kết hợp
    :label: def-associate-index

    Ta gọi **bộ ba kết hợp** (hay **ассоциативная тройка**) là ba phần tử :math:`a, b, c \in Q` sao cho

    .. math:: a \star (b \star c) = (a \star b) \star c,

    hay tương đương với

    .. math:: R_c(L_a(b)) = L_a(R_c(b)).

    Khi đó **chỉ số kết hợp** (hay **индекс ассоциативности**) là số lượng bộ ba kết hợp trong quasigroup.

.. prf:remark:: 
    :label: rmk-purpose-quasigroup
    
    Mục tiêu của quasigroup trong mật mã học là làm yếu tính kết hợp xuống. Như vậy nếu quasigroup có càng nhiều bộ ba kết hợp thì càng dễ bị tấn công hơn.

.. prf:remark:: 
    :label: rmk-amount-associate-index
    
    Số lượng bộ ba kết hợp của quasigroup với order :math:`n` thì không nhỏ hơn :math:`n`.
    
    [TODO] Chứng minh tính chất này.
