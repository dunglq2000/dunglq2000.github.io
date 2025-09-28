==============
Bổ đề Burnside
==============

Các trạng thái khác nhau của tập hợp :math:`M` là **tương đương nhau** nếu chúng nằm trong cùng lớp tương đương dưới tác động của nhóm :math:`G`.

Các ví dụ về bổ đề Burnside và định lý Polya được tham khảo tại :cite:`Tarannikov`.

.. prf:lemma:: Bổ đề Burnside
    :label: lem-burnside

    Với nhóm :math:`G` tác động lên tập hợp :math:`M`, ta có:

    .. math:: t_G = \frac{1}{\lvert G \rvert} \sum_{g \in G} \lvert M^g \rvert,

    trong đó:

    - :math:`t_G` là số lớp tương đương của tập :math:`M` dưới tác động của nhóm :math:`G`;
    - :math:`\lvert M^g \rvert` là số điểm bất động của tập :math:`M` dưới tác động của phần tử :math:`g`, nghĩa là :math:`M^g = \{ m \in M : gm = m\}`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Xét tập hợp

    .. math:: S = \{ (g, m) \in G \times M : g m = m \}.

    Ta đếm số phần tử của :math:`S` theo hai cách.

    **Cách 1: đếm theo từng phần tử $g \in G$.**

    Với mỗi phần tử :math:`g`, số phần tử :math:`m \in M` cố định dưới tác động của :math:`g` là :math:`\lvert M^g \rvert`. Khi đó lấy tổng các phần tử :math:`g` lại ta được

    .. math:: \lvert S \rvert = \sum_{g \in G} \lvert M^g \rvert.

    **Cách 2: đếm theo từng phần tử $m \in M$.**

    Với mỗi :math:`m`, stabilizer

    .. math:: G_m = \{ g \in G : g m = m \}

    có số phần tử là :math:`\lvert G_m \rvert`. Khi đó

    .. math:: \lvert S \rvert = \sum_{m \in M} \lvert G_m \rvert.

    Ở trên mình đã nói về một công thức là

    .. math:: \lvert G \rvert = \lvert G(m) \rvert \cdot \lvert G_m \rvert,

    tương đương với :math:`\lvert G_m \rvert = \dfrac{\lvert G \rvert}{\lvert G(m) \rvert}`.

    Giả sử :math:`M` có :math:`n` orbit là :math:`G(m_1)`, :math:`G(m_2)`, ..., :math:`G(m_n)`. Với mỗi orbit :math:`G(m_i)` thì mọi :math:`m \in G(m_i)` có cùng kích thước :math:`\lvert G_m \rvert`. Khi đó

    .. math:: \sum_{m \in G(m_i)} \lvert G_m \rvert = \sum_{m \in G(m_i)} \dfrac{\lvert G \rvert}{\lvert G(m_i) \rvert} = \lvert G \rvert.

    Cộng tất cả quỹ đạo lại ta có

    .. math:: \sum_{m \in M} \lvert G_m \rvert = \underbrace{\lvert G \rvert + \cdots + \lvert G \rvert}_{n \ \text{lần}} = n \cdot \lvert G \rvert.

    Kết hợp hai cách đếm suy ra

    .. math:: \sum_{g \in G} \lvert M^g \rvert = \sum_{m \in M} \lvert G_m \rvert = n \cdot \lvert G \rvert,

    tương đương với

    .. math:: n = \dfrac{1}{\lvert G \rvert} \sum_{g \in G} \lvert M^g \rvert.

    Ở đây :math:`n = t_G` và ta có điểm phải chứng minh.

--------------------------------
Bài toán tô màu bốn đỉnh tứ diện
--------------------------------

Cho hình tứ diện đều. Ta tô bốn đỉnh của nó bằng ba màu xanh, đỏ, vàng. Hỏi có bao nhiêu cách tô như vậy?

Ta cần lưu ý một điều, hai cách tô là tương đương nhau (giống nhau) nếu tồn tại một phép quay các đỉnh biến cách tô này thành cách tô kia (ví dụ như :numref:`hình %s <first_tetrahedron>` và :numref:`hình %s <second_tetrahedron>`).

.. _first_tetrahedron:

.. figure:: ../../figures/tetrahedron/tetrahedron-1.*

    Cách tô 1

.. _second_tetrahedron:

.. figure:: ../../figures/tetrahedron/tetrahedron-2.*

    Cách tô 2

Như hình trên ta thấy nếu chọn trục quay là đường thẳng nối trung điểm hai cạnh đối diện (hai điểm xanh lá) thì đỉnh trên và đỉnh dưới đổi chỗ cho nhau (xanh và vàng), đỉnh trái và đỉnh phải đổi chỗ cho nhau (xanh và đỏ).

Ta giải bài này như sau:

Đầu tiên ta đánh số các đỉnh của tứ diện như :numref:`hình %s <numbering_vertice>`.

.. _numbering_vertice:

.. figure:: ../../figures/tetrahedron/tetrahedron-3.*

    Đánh số các đỉnh tứ diện

Ta có ba trường hợp biến đổi sau:

*Trường hợp 1.* Giữ nguyên một đỉnh và trục quay là đường thẳng đi qua đỉnh đó và tâm của mặt đối diện.

.. figure:: ../../figures/tetrahedron/tetrahedron-4.*

    Trường hợp 1

Khi đó phép quay (ngược chiều đồng hồ) tương ứng hoán vị :math:`(1)(2,3,4)` (quay :math:`60` độ) và :math:`(1)(2,4,3)` (quay :math:`120` độ).

Do ta chọn một đỉnh cố định thì ta có :math:`4` cách chọn, và với mỗi cách chọn đỉnh cố định ta có thể quay hai cách nên ta có tổng là :math:`8` hoán vị.

*Trường hợp 2.* Ta chọn trung điểm hai cạnh đối nhau và nối lại thành trục quay như hình trong ví dụ. Khi đó tương ứng với hoán vị :math:`(1,4)(2,3)`.

.. figure:: ../../figures/tetrahedron/tetrahedron-5.*

    Trường hợp 2

Ta có :math:`\dfrac{C^2_4}{2!} = 3` hoán vị.

*Trường hợp 3.* Hoán vị đồng nhất :math:`(1)(2)(3)(4)`.

Tóm lại, tập hợp :math:`M` ở đây là tập hợp :math:`4` đỉnh của tứ diện, và nhóm tác động lên :math:`M` là nhóm con :math:`12` phần tử của :math:`\mathcal{S}_4`.

Như vậy, ví dụ với hoán vị :math:`(1)(2,3,4)`, nếu ta muốn sau phép quay giữ nguyên trạng thái (hay nói cách khác là tìm :math:`M^g`) thì ta tô màu đỉnh :math:`1` tùy ý, các đỉnh :math:`2-3-4` chung màu (cũng tùy ý).

Suy ra ta có :math:`3 \cdot 3` cách tô. Tương tự với các hoán vị dạng :math:`(1,4)(2,3)`.

Như vậy có tất cả

.. math:: t_G = \dfrac{1}{12}(1 \cdot 3^4 + 8 \cdot 3^2 + 3 \cdot 3^2) = 15
    
cách tô màu khác nhau.

Tổng quát, nếu có :math:`k` màu thì số lớp tương đương là

.. math:: t_G = \dfrac{1}{12}\left(1 \cdot k^4 + 8 \cdot k^2 + 3 \cdot k^2\right) = \dfrac{1}{12}(k^4 + 11 k^2).

------------------------
Tác động nhóm lên vector
------------------------

Xét nhóm :math:`G` và không gian vector :math:`\mathbb{F}_2^n`, :math:`n \in \mathbb{N}`. Khi đó hai vector :math:`\bm{x}` và :math:`\bm{y}` thuộc :math:`\mathbb{F}_2^n` được gọi là **quan hệ với nhau** nếu tồn tại :math:`g \in G` mà :math:`\bm{x} = g \bm{y}`.

Ví dụ, xét nhóm hoán vị :math:`\mathcal{S}_3`. Giả sử các vector trong :math:`\mathbb{F}_2^3` có dạng

.. math:: \bm{x} = (x_1, x_2, x_3) \in \mathbb{F}_2^3.

Khi đó vector :math:`(1, 0, 0)` có quan hệ với :math:`(0, 0, 1)` với hoán vị :math:`(1, 3)(2)`. Cụ thể là :math:`(x_1, x_2, x_3) \xrightarrow{(1, 3)(2)} (x_3, x_2, x_1)`.

Tương tự, vector :math:`(1, 0, 0)` cũng có quan hệ với :math:`(0, 1, 0)` với hoán vị :math:`(1, 2)(3)`.

Thêm nữa, vector :math:`(1, 0, 0)` có quan hệ với chính nó qua hoán vị đồng nhất :math:`(1)(2)(3)`.

Câu hỏi đặt ra là, có bao nhiêu lớp tương đương dưới tác động của nhóm :math:`\mathcal{S}_3`?

Để giải quyết vấn đề này ta sử dụng bổ đề Burnside.

Nhóm :math:`\mathcal{S}_3` có các hoán vị

.. math:: \mathcal{S}_3 = \{ (1)(2)(3), (1, 2)(3), (1, 3)(2), (2, 3)(1), (1, 3, 2), (1, 2, 3) \}.

Lần lượt xét từng hoán vị. Đầu tiên, với :math:`(1)(2)(3)` thì các phần tử trong vector đứng yên. Do đó dưới tác động của hoán vị này, :math:`x_1` biến thành :math:`x_1`, :math:`x_2` biến thành :math:`x_2` và :math:`x_3` biến thành :math:`x_3`. Số cách chọn cho mỗi :math:`x_i` là :math:`2` nên theo quy tắc nhân ta có :math:`2^3 = 8` cách.

Tiếp theo, với hoán vị :math:`(1, 2)(3)` thì :math:`x_1 \to x_2`, :math:`x_2 \to x_1` và :math:`x_3 \to x_3`. Do đó :math:`x_1` và :math:`x_2` có cùng giá trị (nằm cùng chu trình), thành ra có :math:`2` cách chọn, :math:`x_3` cũng có :math:`2` cách chọn nên tổng số cách là :math:`2 \cdot 2 = 4`. Hoán vị :math:`(1, 3)(2)` và :math:`(2, 3)(1)` tương tự.

Với hoán vị :math:`(1, 2, 3)` thì :math:`x_1 \to x_2`, :math:`x_2 \to x_3` và :math:`x_3 \to x_1` nên :math:`x_1 = x_2 = x_3`, có :math:`2` cách chọn trong trường hợp này. Hoán vị :math:`(1, 3, 2)` tương tự.

Như vậy, theo bổ đề Burnside, số lớp tương đương các vector trong :math:`\mathbb{F}_2^3` là

.. math:: t(\mathcal{S}_3) = \frac{1}{6} (1 \cdot 2^3 + 3 \cdot 2^2 + 2 \cdot 2) = 4.

Thật vậy, ta có thể chia các vector thành :math:`4` lớp tương đương là

.. math:: \{ 000 \}, \{ 001, 010, 011 \}, \{ 011, 101, 110 \}, \{ 111 \}.

Ngoài nhóm :math:`\mathcal{S}_3` ra còn các nhóm khác cũng tác động lên các vector. Một số nhóm hay được sử dụng là:

1. Nhóm general linear: gồm các ma trận khả nghịch :math:`n \times n` trên :math:`\mathbb{F}_2`. Tác động nhóm lúc này là phép nhân ma trận :math:`\bm{A} \in \mathrm{GL} (n, 2)` với vector :math:`\bm{x} \in \mathbb{F}_2^n`, hay :math:`\bm{A} \cdot \bm{x}`.
2. Nhóm general affine: gồm các ma trận khả nghịch :math:`n \times n` trên :math:`\mathbb{F}_2` và vector bất kì trong :math:`\mathbb{F}_2^n`. Tác động nhóm lúc này là biến đổi affine :math:`\bm{A} \cdot \bm{x} + \bm{b}` với :math:`\bm{A} \in \mathrm{GL} (n, 2)` và :math:`\bm{b} \in \mathbb{F}_2^n`.

.. prf:remark:: 
    :label: GL-n2
    
    Số lượng phần tử của nhóm :math:`\mathrm{GL} (n, 2)` là

    .. math:: (2^n - 1) \cdot (2^n - 2) \cdots (2^n - 2^{n-1}).

    Ví dụ, khi :math:`n = 3` thì
    
    .. math:: \lvert \mathrm{GL}(3, 2) \rvert = (2^3 - 1) \cdot (2^3 - 2) \cdot (2^3 - 4) = 168
        
    ma trận.

-----------------------------
Tác động nhóm lên hàm boolean
-----------------------------

Ta tiếp tục xét nhóm :math:`G` và không gian vector :math:`\mathbb{F}_2^n`, :math:`n \in \mathbb{N}`. Khi đó hai hàm boolean :math:`n` biến :math:`f(x_1, \ldots, x_n)` và :math:`g(x_1, \ldots, x_n)` được gọi là **quan hệ với nhau** nếu tồn tại :math:`\tilde{g} \in G` mà :math:`g(\bm{x}) = f(\tilde{g} \bm{x})` với mọi :math:`\bm{x} \in \mathbb{F}_2^n`.

Ta cũng xét hoán vị :math:`\mathcal{S}_3` làm ví dụ. Ta cũng lần lượt xét các phần tử của nhóm.

Đặt :math:`f_0`, :math:`f_1`, ..., :math:`f_7` lần lượt là các giá trị hàm :math:`f` với các vector :math:`\bm{x} \in \mathbb{F}_2^3`.

Đầu tiên, với :math:`(1)(2)(3)`, ta có bảng chuyển vector như :numref:`hình %s <burnside-first>`.

.. _burnside-first:

.. figure:: ../../figures/burnside/burnside-1.*

    Hoán vị :math:`(1)(2)(3)`

Ta thấy rằng :math:`f_0 \to f_0`, :math:`f_1 \to f_1`, ..., :math:`f_7 \to f_7` nên có :math:`8` chu trình. Vậy số lượng cách chọn là :math:`2^8`.

Tiếp theo, xét các hoán vị dạng :math:`(1)(2, 3)`, ta có bảng chuyển vector như :numref:`hình %s <burnside-second>`.

.. _burnside-second:

.. figure:: ../../figures/burnside/burnside-2.*

    Hoán vị :math:`(1)(2, 3)`

Ta thấy rằng :math:`f_0 \to f_0`, :math:`f_1 \to f_2 \to f_1`, :math:`f_3 \to f_3`, :math:`f_4 \to f_4`, :math:`f_5 \to f_6 \to f_5`, :math:`f_7 \to f_7`. Ở đây có :math:`6` chu trình nên số cách chọn là :math:`2^6`.

Tiếp theo ta xét các hoán vị dạng :math:`(1, 2, 3)` (:numref:`burnside-third`).

.. _burnside-third:

.. figure:: ../../figures/burnside/burnside-3.*

    Hoán vị :math:`(1, 2, 3)`

Ta thấy rằng :math:`f_0 \to f_0`, :math:`f_1 \to f_2 \to f_4 \to f_1`, :math:`f_3 \to f_6 \to f_5 \to f_3`, :math:`f_7 \to f_7` nên ở đây có :math:`4` chu trình. Số cách chọn là :math:`2^4`.

Như vậy theo bổ đề Burnside, số lớp hàm bool tương đương dưới tác động của nhóm :math:`\mathcal{S}_3` là

.. math:: t (\mathcal{S}_3) = \dfrac{1}{6}(2^8 + 3 \cdot 2^6 + 2 \cdot 2^4) = 80.

-------------
Định lý Polya
-------------

Với mỗi hoán vị trong tập :math:`G`, ta viết dưới dạng các chu trình độc lập

.. math:: \underbrace{(g_1) (g_2) \ldots (g_{t_{1}})}_{t_1} \underbrace{(g_{j_1} g_{j_2}) (g_{j_3} g_{j_4})}_{t_2} \ldots

Nếu ta viết hoán vị dưới dạng các chu trình rời nhau, ta gọi

+-------------+----------------------------------+
| Kí hiệu     | Ý nghĩa                          |
+=============+==================================+
| :math:`t_1` | số chu trình có độ dài :math:`1` |
+-------------+----------------------------------+
| :math:`t_2` | số chu trình có độ dài :math:`2` |
+-------------+----------------------------------+
| ...         | tương tự                         |
+-------------+----------------------------------+
| :math:`t_n` | số chu trình có độ dài :math:`n` |
+-------------+----------------------------------+

Khi đó, **cycle index** (hay **chỉ số chu trình**) của hoán vị ứng các biến :math:`z_1`, :math:`z_2`, ..., :math:`z_n` là

.. math:: I_g (z_1, z_2, ,\ldots, z_n) = z_1^{t_1} z_2^{t_2} \cdots z_n^{t_n}.

.. prf:example:: 
    :label: exp-independent-cycles
    
    Xét hoán vị :math:`(1,2,3)(4)(5)(6,7) \in \mathcal{S}_7`.

    Ta có hai chu trình độ dài :math:`1`, một chu trình độ dài :math:`2` và một chu trình độ dài :math:`3` và không có chu trình độ dài :math:`4`, :math:`5`, :math:`6`, :math:`7`.

    Do đó chỉ số chu trình là
    
    .. math:: I_g (z_1, z_2, z_3) = z_1^2 z_2^1 z_3^1.

.. prf:remark:: 
    :label: rmk-independent-cycles
    
    Bất kì hoán vị nào thuộc :math:`\mathcal{S}_n` đều thỏa
    
    .. math:: 1 \cdot t_1 + 2 \cdot t_2 + \ldots + n \cdot t_n = n.

.. prf:definition:: Cyclic index, chỉ số chu trình
    :label: def-cyclic-index

    **Chỉ số chu trình** của nhóm :math:`G` là:

    .. math:: P_G (z_1, z_2, \ldots, z_n) = \frac{1}{G}\sum_{g \in G} I_g (z_1, z_2, \ldots, z_n).

Nhìn lại ví dụ về tứ diện bên trên, các đỉnh nằm trong cùng chu trình cần được tô cùng màu. Từ đó ta có chỉ số chu trình

.. math:: P_G(z_1, z_2, z_3) = \frac{1}{12}\left(z_1^4 + 8 z_1 z_3 + 3 z_2^2\right).

Cho mỗi :math:`z_i = 3` ta có kết quả phép tính theo bổ đề Burnside.

Định lý Polya là một mở rộng cho bổ đề Burnside, cho phép chúng ta đếm số lớp tương đương thỏa mãn điều kiện nhất định (về số lượng phần tử).

Ví dụ với hình tứ diện như trên nhưng ta thêm điều kiện tô hai đỉnh màu vàng, một đỉnh màu đỏ và một đỉnh màu xanh.

Ta kí hiệu tập :math:`R` là tập hợp các trạng thái có thể nhận của mỗi phần tử :math:`m \in M`.

.. math:: R = \{r_1, r_2, \ldots, r_c \}.

Ở ví dụ trên thì :math:`R = \{\text{đỏ}, \text{xanh}, \text{vàng}\}`.

Ta thay mỗi :math:`z_i` trong chỉ số chu trình bằng tổng :math:`\sum\limits_{r \in R} r^i`.

.. prf:example:: 
    :label: exp-cyclic-index

    Giả sử ta tô màu bốn đỉnh tứ diện với hai màu :math:`R = \{r_1, r_2\}`.

    Với :math:`z_1` ta thay bằng :math:`r_1 + r_2`.

    Với :math:`z_2` ta thay bằng :math:`r_1^2 + r_2^2`.

    Với :math:`z_3` ta thay bằng :math:`r_1^3 + r_2^3`.

    Khi đó :math:`P_G` tương đương với

    .. math:: \frac{1}{12}\left[ (r_1 + r_2)^4 + 8 \cdot (r_1 + r_2)(r_1^3 + r_2^3) + 3 \cdot (r_1^2 + r_2^2)^2 \right].

    Ta khai triển :math:`P_G` (lưu ý là ở đây không có tính giao hoán phép nhân).

    .. math:: 
        
        (r_1 + r_2)^4 = & r_1 r_1 r_1 r_1 + r_1 r_1 r_1 r_2 + r_1 r_1 r_2 r_1 + r_1 r_1 r_2 r_2 \\
        + & r_1 r_2 r_1 r_1 + r_1 r_2 r_1 r_2 + r_1 r_2 r_2 r_1 + r_1 r_2 r_2 r_2 \\
        + & r_2 r_1 r_1 r_1 + r_2 r_1 r_1 r_2 + r_2 r_1 r_2 r_1 + r_2 r_1 r_2 r_2 \\
        + & r_2 r_2 r_1 r_1 + r_2 r_2 r_1 r_2 + r_2 r_2 r_2 r_1 + r_2 r_2 r_2 r_2. 

    Mình thấy rằng có :math:`16` cấu hình khác nhau tương ứng :math:`16` cách tô hai màu cho bốn đỉnh. Tương tự

    .. math:: 
        
        (r_1 + r_2) (r_1^3 + r_2^3) & = r_1^4 + r_1 r_2^3 + r_2 r_1^3 + r_2^4 \\
        & = r_1 r_1 r_1 r_1 + r_1 r_2 r_2 r_2 + r_2 r_1 r_1 r_1 + r_2 r_2 r_2 r_2.

    Cuối cùng là

    .. math:: 
    
        (r_1^2 + r_2^2)^2 & = r_1^4 + r_1^2 r_2^2 + r_2^2 r_1^2 + r_2^4 \\
        & = r_1 r_1 r_1 r_1 + r_1 r_1 r_2 r_2 + r_2 r_2 r_1 r_1 + r_2 r_2 r_2 r_2.      

    Việc không có tính giao hoán với phép nhân làm biểu thức cồng kềnh và phức tạp.

    Do đó mình thêm một tập hợp :math:`W` là vành giao hoán, và xét ánh xạ :math:`w: R \mapsto W` với:math:`w(r_i) = w_i`.

    Khi đó nếu thay :math:`r_i` bởi :math:`w_i` vào bên trên biểu thức sẽ rất đẹp:

    .. math:: P_G(w_1, w_2) = \frac{1}{12} \left[(w_1 + w_2)^4 + 8 (w_1 + w_2) (w_1^3 + w_2^3) + 3 (w_1^2 + w_2^2)^2\right].

    Khai triển và thu gọn ta có

    .. math::  
        
        P_G(w_1, w_2) & = \frac{1}{12} \left[12 w_1^4 + 12 w_1^3 w_2 + 12 w_1^2 w_2^2 + 12 w_1 w_2^3 + 12 w_2^4\right] \\
        & = w_1^4 + w_1^3 w_2 + w_1^2 w_2^2 + w_1 w_2^3 + w_2^4.
        
    Ở đây, định lý Polya nói rằng, số mũ của :math:`w_i` thể hiện số lượng phần tử của tập :math:`M` nhận giá trị :math:`r_i`, và hệ số trước mỗi toán hạng là số lớp tương đương tương ứng với số lượng phần tử của tập :math:`M` nhận các giá trị :math:`r_i`.

    Nói cách khác:

    - có :math:`1` lớp tương đương mà :math:`4` đỉnh nhận màu :math:`r_1`;
    - có :math:`1` lớp tương đương mà :math:`3` đỉnh nhận màu :math:`r_1` và :math:`1` đỉnh nhận màu :math:`r_2`;
    - có :math:`1` lớp tương đương mà :math:`2` đỉnh nhận màu :math:`r_1` và :math:`2` đỉnh nhận màu :math:`r_2`;
    - có :math:`1` lớp tương đương mà :math:`1` đỉnh nhận màu :math:`r_1` và :math:`3` đỉnh nhận màu :math:`r_2`;
    - có :math:`1` lớp tương đương mà :math:`4` đỉnh nhận màu :math:`r_2`.

Quay lại vấn đề tô bốn đỉnh tứ diện với ba màu xanh, đỏ, vàng. Tìm số cách tô hai đỉnh màu vàng, một đỉnh màu đỏ và một đỉnh màu xanh.

Đặt

.. math:: w(\text{vàng}) = x, w(\text{đỏ}) = y, w(\text{xanh}) = z.

Ta có:

.. math:: P_G = \frac{1}{12} \left[(x + y + z)^4 + 8 \cdot (x + y + z) (x^3 + y^3 + z^3) + 3 \cdot (x^2 + y^2 + z^2)^2\right].

Như vậy đề bài tương ứng việc tìm hệ số của hạng tử :math:`x^2 yz` trong biểu thức trên. Kết quả là :math:`1`.
