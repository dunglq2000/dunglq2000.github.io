=================
Không gian affine
=================

Cho :math:`\mathcal{V}` là một không gian vector trên trường :math:`\mathbb{F}` và :math:`\mathcal{A}` là một tập khác rỗng mà các phần tử của nó gọi là **điểm**.

Giả sử ta có ánh xạ :math:`\varphi` sao cho:

.. math:: \varphi: \mathcal{A} \times \mathcal{A} \to \mathcal{V}, \ (M, N) \mapsto \varphi(M, N)

thỏa hai điều kiện sau:

1. Với mọi điểm :math:`M \in \mathcal{A}` và vector :math:`\vec{v} \in \mathcal{V}`, có duy nhất một điểm :math:`N \in \mathcal{A}` sao cho :math:`\varphi(M, N) = \vec{v}`.
2. Với ba điểm :math:`M`, :math:`N`, :math:`P` bất kì ta có

.. math:: \varphi(M, N) + \varphi(N, P) = \varphi(M, P).

Khi đó, ta nói :math:`\mathcal{A}` là một **không gian affine**. Nếu ta nói đầy đủ thì :math:`\mathcal{A}` là không gian affine trên trường :math:`\mathbb{F}` liên kết với không gian vector :math:`\mathcal{V}` bởi ánh xạ liên kết :math:`\varphi`.

Khi đó, :math:`\mathcal{V}` được gọi là **không gian vector liên kết** với :math:`\mathcal{A}` (hay **không gian nền** của :math:`\mathcal{A}`) và kí hiệu là :math:`\vec{\mathcal{A}}`.

Ánh xạ :math:`\varphi` được gọi là **ánh xạ liên kết**. Ta kí hiệu :math:`\varphi(M, N) = \overrightarrow{MN}`. Khi đó hai điều kiện trên được viết lại thành:

1. Với mọi điểm :math:`M \in \mathcal{A}` và vector :math:`\vec{v} \in \vec{\mathcal{A}}` thì tồn tại duy nhất một điểm :math:`N \in \mathcal{A}` sao cho :math:`\overrightarrow{MN} = \vec{v}`.
2. Với ba điểm :math:`M`, :math:`N`, :math:`P` bất kì ta có

.. math:: \overrightarrow{MN} + \overrightarrow{NP} = \overrightarrow{MP}.

Biểu thức ở điều kiện 2 được gọi là **hệ thức Chales**. Hệ thức này đóng vai trò quan trọng trong các đại lượng có hướng (vector, góc định hướng, ...).

Nếu :math:`\mathbb{F} = \mathbb{R}` thì ta gọi là không gian affine thực.

Nếu :math:`\mathbb{F} = \mathbb{C}` thì ta gọi là không gian affine phức.

Nếu cần nhấn mạnh trường :math:`\mathbb{F}` thì ta gọi là :math:`\mathbb{F}`-không gian affine.

Kí hiệu một không gian affine là :math:`(\mathcal{A}, \vec{\mathcal{A}}, \varphi)`.

Ta có thể ghi tắt là :math:`\mathcal{A}(\mathbb{F})` hoặc :math:`\mathcal{A}`.

Nếu :math:`\vec{\mathcal{A}}` là không gian vector :math:`n` chiều thì ta nói :math:`A` là không gian affine :math:`n` chiều và kí hiệu là :math:`\mathcal{A}^n`. Khi đó

.. math:: \dim \mathcal{A} = \dim \vec{\mathcal{A}}.

.. prf:example:: 
    :label: exp-affine-space

    Hệ tọa độ trong không gian :math:`\mathbb{R}^3` mà chúng ta học ở phổ thông. Khi đó:

    1. :math:`\mathcal{A} = \mathbb{R}^3` là tập hợp tất cả điểm trong không gian.
    2. :math:`\vec{\mathcal{A}}` là tập các vector trong :math:`\mathbb{R}^3`. Về mặt hình học thì vector từ điểm :math:`A` tới điểm :math:`B` là mũi tên có hướng từ :math:`A` tới :math:`B`.

.. prf:example:: 
    :label: chinh-tac

    Gọi :math:`\mathcal{V}` là không gian vector trên trường :math:`\mathbb{F}`. Ánh xạ

    .. math:: \varphi: \mathcal{V} \times \mathcal{V} \to \mathcal{V}, \ (\vec{u}, \vec{v}) \mapsto \varphi(\vec{u}, \vec{v}) = \vec{v} - \vec{u}

    thỏa mãn định nghĩa vì:

    1. Với mọi vector :math:`\vec{u} \in \mathcal{V}` và :math:`\vec{w} \in \mathcal{V}`, tồn tại duy nhất vector :math:`\vec{v}` sao cho :math:`\varphi(\vec{u}, \vec{v}) = \vec{w}`, tương đương với :math:`\vec{v} - \vec{u} = \vec{w}`, hay :math:`\vec{v} = \vec{u} + \vec{w}`.
    2. Với ba vector :math:`\vec{u}`, :math:`\vec{v}`, :math:`\vec{w}` bất kì thuộc :math:`\mathcal{V}` ta có

    .. math:: \varphi(\vec{u}, \vec{v}) + \varphi(\vec{v}, \vec{w}) = \vec{v} - \vec{u} + \vec{w} - \vec{v} = \vec{w} - \vec{v} = \varphi(\vec{v}, \vec{w}).

Ở :prf:ref:`chinh-tac`, :math:`\mathcal{V}` là không gian vector liên kết với chính nó nên ta nói :math:`\varphi` xác định một **cấu trúc affine chính tắc** trên không gian vector :math:`\mathcal{V}`, hay :math:`\mathcal{V}` là **không gian affine với cấu trúc affine chính tắc**.

**Tính chất của không gian affine.** Với mọi điểm :math:`M`, :math:`N`, :math:`P`, :math:`Q` bất kì thuộc :math:`\mathcal{A}` ta có:

1. :math:`\overrightarrow{MN} = \vec{0}` khi và chỉ khi :math:`M \equiv N`.
2. :math:`\overrightarrow{MN} = -\overrightarrow{NM}`.
3. :math:`\overrightarrow{MN} = \overrightarrow{PQ}` khi và chỉ khi :math:`\overrightarrow{MP} = \overrightarrow{NQ}`.
4. :math:`\overrightarrow{MN} = \overrightarrow{PN} - \overrightarrow{PM}`.

Đây là các công thức cơ bản được học ở phổ thông và ở đây cũng áp dụng.

=====
Phẳng
=====

Một số khái niệm ở phổ thông dưới dạng phẳng:

1. Điểm là :math:`0`-phẳng.
2. Đường thẳng là :math:`1`-phẳng.
3. Mặt phẳng là :math:`2`-phẳng.
4. Không gian ba chiều là :math:`3`-phẳng.

Chúng ta sẽ định nghĩa **phẳng** là mở rộng cho các khái niệm trên.

Đầu tiên chúng ta cần một vài nhận xét từ hình học phổ thông.

Trong mặt phẳng :math:`\mathbb{R}^2`, mỗi đường thẳng được xác định khi biết một điểm thuộc nó và một vector chỉ phương :math:`\vec{v}`. Khi đó đường thẳng đi qua điểm :math:`M_0` và nhận :math:`\vec{v}` làm vector chỉ phương là tập các điểm :math:`M \in \mathbb{R}^2` sao cho :math:`\overrightarrow{MM_0} = \alpha \vec{v}` với :math:`\alpha \in \mathbb{R}`. Nói cách khác là vector :math:`\overrightarrow{MM_0}` cùng phương với vector :math:`\vec{v}`.

.. prf:remark:: 
    :label: rmk-line-oxy

    Trên mặt phẳng, đường thẳng đi qua điểm :math:`M_0` và nhận :math:`\vec{v}` làm vector chỉ phương là tập hợp

    .. math:: d = \{ M \in \mathbb{R}^2 : \overrightarrow{MM_0} = \alpha \cdot \vec{v} \ \text{với} \ \alpha \in \mathbb{R} \}.

Trong không gian :math:`\mathbb{R}^3`, tương tự, một đường thẳng xác định khi biết một điểm thuộc nó và một vector chỉ phương của nó.

.. prf:remark:: 
    :label: rmk-line-oxyz

    Trong không gian :math:`\mathbb{R}^3`, đường thẳng đi qua điểm :math:`M_0` và nhận :math:`\vec{v}` làm vector chỉ phương là tập hợp

    .. math:: d = \{ M \in \mathbb{R}^2 : \overrightarrow{MM_0} = \alpha \cdot \vec{v} \ \text{với} \ \alpha \in \mathbb{R} \}.

Chúng ta đã biết ở phổ thông rằng, qua ba điểm không thẳng hàng có duy nhất một mặt phẳng đi qua. Ba điểm không thẳng hàng thì tạo thành tam giác, giả sử là :math:`M`, :math:`N` và :math:`P`. Ta lấy hai cạnh làm hai đường thẳng cho mặt phẳng. Khi đó mặt phẳng trong không gian được xác định bởi điểm :math:`M` và hai vector :math:`\overrightarrow{MN}` và :math:`\overrightarrow{MP}`.

.. prf:remark:: 
    :label: rmk-plane-oxyz

    Một mặt phẳng trong :math:`\mathbb{R}^3` xác định khi biết một điểm :math:`M_0` thuộc nó và một cặp vector :math:`\vec{u}`, :math:`\vec{v}` của nó. Khi đó mặt phẳng là tập hợp

    .. math:: p = \{ M \in \mathbb{R}^3 : \overrightarrow{MM_0} = \alpha \cdot \vec{u} + \beta \cdot \vec{v} \ \text{với} \ \alpha, \beta \in \mathbb{R} \}.

Ta định nghĩa tổng quát cho phẳng

.. prf:definition:: Phẳng
    :label: def-plane

    Cho :math:`(\mathcal{A}, \vec{\mathcal{A}}, \varphi)` là một không gian affine, :math:`M_0` là một điểm thuộc :math:`\mathcal{A}` và :math:`\vec{\alpha}` là một không gian vector con của :math:`\vec{\mathcal{A}}`. Tập hợp

    .. math:: \alpha = \{ M \in \mathcal{A} : \overrightarrow{MM_0} \in \vec{\alpha} \}

    được gọi **phẳng** (hay **plane**) đi qua :math:`M_0` với không gian chỉ phương :math:`\vec{\alpha}`, hoặc phương :math:`\vec{\alpha}`.

Nếu :math:`\dim \vec{\alpha} = m` thì ta nói :math:`\alpha` là **phẳng** :math:`m` **chiều** hay :math:`m`-**phẳng** và viết :math:`\dim \alpha = m`. Như vậy :math:`\dim \alpha = \dim \vec{\alpha}`.

Trước đây chúng ta gọi điểm, đường, mặt phẳng, nhưng khi số chiều cao hơn thì chúng ta không thể "chế" từ vựng mãi được. Khi đó chúng ta quy về khái niệm phẳng, :math:`1`-phẳng là đường thẳng, :math:`2`-phẳng là mặt phẳng.

**Siêu phẳng** (hay **hyperplane**) là tên gọi của phẳng có đối chiều là :math:`1`, tức là nếu số chiều của không gian là :math:`n` thì số chiều của siêu phẳng là :math:`n-1`.

.. prf:remark:: 
    :label: rmk-plane

    1. Nếu :math:`\alpha` là phẳng đi qua điểm :math:`M` thì :math:`M \in \alpha` và với mọi :math:`P`, :math:`Q` thuộc :math:`\alpha` ta có :math:`\overrightarrow{PQ} = \overrightarrow{MQ} - \overrightarrow{MP}` thuộc :math:`\alpha`.
    2. :math:`0`-phẳng là tập chỉ gồm một điểm. Do đó ta có thể xem một điểm là một :math:`0`-phẳng.
    3. Điểm :math:`M_0` trong định nghĩa phẳng có vai trò tổng quát, nghĩa là mọi điểm :math:`M_0` trong :math:`\alpha` có ý nghĩa như nhau trong định nghĩa phẳng.
    4. Giả sử :math:`\alpha` là phẳng đi qua :math:`M` với phương :math:`\vec{\alpha}`, :math:`\beta` là phẳng đi qua :math:`N` với phương :math:`\vec{\beta}`. Khi đó :math:`\alpha \subset \beta` khi và chỉ khi :math:`M \in \beta` và :math:`\vec{\alpha} \subset \vec{\beta}`. Suy ra :math:`\alpha \equiv \beta` khi và chỉ khi :math:`P \in \beta` (hoặc :math:`Q \in \alpha`) và :math:`\vec{\alpha} \equiv \vec{\beta}`.
    5. Nếu :math:`\alpha` là phẳng với phương :math:`\vec{\alpha}` thì :math:`\alpha` là không gian affine liên kết với :math:`\vec{\alpha}` bởi ánh xạ liên kết

    .. math:: \varphi_{\alpha \times \alpha} : \alpha \times \alpha \to \vec{\alpha}.

    Vì vậy ta có thể xem phẳng là không gian affine con.

Để xác định một không gian vector thì ta chỉ cần một cơ sở của nó. Do đó để xác định phương :math:`\vec{\alpha}` của :math:`m`-phẳng :math:`\alpha` thì ta cũng chỉ cần biết một cơ sở là đủ.

Do một không gian vector có thể có nhiều cơ sở khác nhau, một :math:`m`-phẳng chỉ có một không gian chỉ phương duy nhất nhưng có thể có nhiều cơ sở khác nhau.

==================================
Độc lập affine và phụ thuộc affine
==================================

.. prf:definition:: Độc lập và phụ thuộc affine
    :label: def-depend-independ-affine

    Hệ :math:`m+1` điểm

    .. math:: \{ A_0, A_1, \ldots, A_m \}

    với :math:`m \geqslant 1` của không gian affine :math:`\mathcal{A}` được gọi là **độc lập affine** nếu hệ :math:`m` vector

    .. math:: \{ \overrightarrow{A_0 A_1}, \overrightarrow{A_0 A_2}, \ldots, \overrightarrow{A_0 A_m} \}

    của :math:`\vec{\mathcal{A}}` là một hệ vector độc lập tuyến tính.

    Ngược lại, hệ điểm không độc lập affine được gọi là **phụ thuộc affine**.

1. Tập chỉ gồm một điểm :math:`A_0` được quy ước là luôn độc lập affine.
2. Trong định nghĩa điểm :math:`A_0` bình đẳng như các điểm khác vì hệ vector

.. math:: \{ \overrightarrow{A_0 A_1}, \overrightarrow{A_0, A_1}, \ldots, \overrightarrow{A_0 A_m} \}

độc lập affine thì hệ vector

.. math:: \{ \overrightarrow{A_i A_0}, \overrightarrow{A_i A_{i-1}}, \overrightarrow{A_i A_{i+1}}, \ldots, \overrightarrow{A_i A_m} \}

cũng độc lập affine.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Xét tổ hợp tuyến tính

    .. math:: I = \lambda_1 \overrightarrow{A_0 A_1} + \lambda_2 \overrightarrow{A_0 A_2} + \cdots + \lambda_m \overrightarrow{A_0 A_m} = \vec{0}.

    Do hệ vector độc lập tuyến tính nên :math:`\lambda_1 = \lambda_2 = \cdots = \lambda_m = 0`. Khi đó, biến đổi :math:`I` ta có

    .. math:: 
        
        I & = \lambda_1 (\overrightarrow{A_i A_1} - \overrightarrow{A_i A_0}) + \lambda_2 (\overrightarrow{A_i A_2} - \overrightarrow{A_i A_0}) + \cdots + \lambda_{i-1} (\overrightarrow{A_i A_{i-1}} - \overrightarrow{A_i A_0}) \\ & + \lambda_i \overrightarrow{A_0 A_i} + \lambda_{i+1} (\overrightarrow{A_i A_{i+1}} - \overrightarrow{A_i A_0}) + \cdots + \lambda_m (\overrightarrow{A_i A_m} - \overrightarrow{A_i A_0}) \\
        & = \lambda_1 \overrightarrow{A_i A_1} + \lambda_2 \overrightarrow{A_i A_2} + \cdots + \lambda_m \overrightarrow{A_i A_m} \\
        & - \underbrace{(\lambda_1 + \cdots + \lambda_m) \overrightarrow{A_i A_0}}_{\vec{0}} \\
        & = \lambda_1 \overrightarrow{A_i A_1} + \lambda_2 \overrightarrow{A_i A_2} + \cdots + \lambda_m \overrightarrow{A_i A_m} = \vec{0}
        
    với :math:`\lambda_1 = \cdots = \lambda_m = 0`. Như vậy hệ vector mới cũng độc lập tuyến tính.

3. Hệ điểm :math:`\{ A_0, \ldots, A_m \}` phụ thuộc affine khi và chỉ khi hệ vector

.. math:: \{ \overrightarrow{A_0 A_1}, \cdots, \overrightarrow{A_0 A_m} \}

phụ thuộc tuyến tính.

4. Hệ con của một hệ độc lập thì độc lập, nhưng hệ con của một hệ phụ thuộc chưa chắc phụ thuộc.

.. prf:theorem:: 
    :label: thm-n-1-dependence

    Trong không gian affine :math:`n` chiều :math:`\mathcal{A}^n`, với :math:`0 < m \leqslant n+1` thì luôn tồn tại các hệ :math:`m` điểm độc lập. Mọi hệ gồm hơn :math:`n+1` điểm đều phụ thuộc.

==============================
Giao của các phẳng. Bao affine
==============================

Cho :math:`\{ \alpha_i : i \in I \}` là một họ không rỗng các phẳng trong không gian affine :math:`\mathcal{A}`.

.. prf:theorem:: 
    :label: phuong-giao
 
    Nếu :math:`\bigcap\limits_{i \in I} \alpha_i \neq \emptyset` thì :math:`\bigcap\limits_{i \in I} \alpha_i` là một phẳng có phương là :math:`\bigcap\limits_{i \in I} \vec{\alpha}_i`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Vì :math:`\bigcap\limits_{i \in I} \alpha_i \neq \emptyset` nên tồn tại điểm :math:`M` thuộc :math:`\bigcap\limits_{i \in I} \alpha_i`, như vậy :math:`M \in \alpha_i` với mọi :math:`i \in I`.

    Nếu ta có điểm :math:`N \in \bigcap\limits_{i \in I} \alpha_i` thì :math:`N \in \alpha_i` với mọi :math:`i \in I`. Suy ra :math:`\overrightarrow{MN} \in \vec{\alpha}_i` với mọi :math:`i \in I`. Từ đó

    .. math:: \overrightarrow{MN} \in \bigcap_{i \in I} \vec{\alpha}_i \Longleftrightarrow \bigcap_{i \in I} \alpha_i = \{ N \in \mathcal{A} : \overrightarrow{MN} \in \bigcap_{i \in I} \vec{\alpha}_i \},

    nghĩa là :math:`\bigcap\limits_{i \in I} \alpha_i` là phẳng đi qua :math:`M` với không gian chỉ phương là :math:`\bigcap\limits_{i \in I} \vec{\alpha}_i`.

.. prf:definition:: Phẳng giao

    Phẳng :math:`\bigcap\limits_{i \in I} \alpha_i` trong định lí trên được gọi là **phẳng giao** của các phẳng :math:`\alpha_i`.

Từ định nghĩa ta thấy rằng :math:`\bigcap\limits_{i \in I} \alpha_i` là phẳng lớn nhất (theo nghĩa quan hệ bao hàm) chứa trong tất cả các phẳng :math:`\alpha_i` với :math:`i \in I`.

.. prf:definition:: 
    :label: def-bao-affine

    Cho :math:`X` là một tập con khác rỗng của không gian affine :math:`\mathcal{A}`. Khi đó giao của mọi phẳng chứa :math:`X` trong :math:`\mathcal{A}` sẽ là một phẳng, gọi là **bao affine** của :math:`X`. Kí hiệu là :math:`\langle X \rangle`.

Bao affine :math:`\langle X \rangle`, theo quan hệ bao hàm, của tập :math:`X` là phẳng bé nhất chứa :math:`X`.

.. prf:definition:: Phẳng tổng
    :label: def-phang-tong
    
    Cho :math:`\{ \alpha_i : i \in I \}` là một họ không rỗng các phẳng. Bao affine của tập hợp :math:`\bigcup\limits_{i \in I} \alpha_i` được gọi là **phẳng tổng** (hay **tổng**) của các phẳng :math:`\alpha_i`. Kí hiệu là :math:`\sum\limits_{i \in I} \alpha_i`.

Phẳng tổng là phẳng bé nhất (có số chiều nhỏ nhất) chứa tất cả :math:`\alpha_i` với :math:`i \in I`. Khi :math:`I` là tập hữu hạn, giả sử :math:`I = \{ 1, 2, \ldots, n \}` thì ta viết

.. math:: \alpha_1 + \alpha_2 + \cdots + \alpha_n \ \text{hay} \ \sum_{i=1}^n \alpha_i

để biểu diễn tổng của các phẳng :math:`\alpha_i`.

.. prf:remark:: 
    :label: rmk-tong-0-phang

    Nếu :math:`X` là một hệ hữu hạn điểm

    .. math:: X = \{ M_0, M_1, \ldots, M_n \}

    thì tổng :math:`M_0 + \cdots + M_n` là phẳng có số chiều nhỏ nhất đi qua các điểm này. Ở đây ta xem mỗi điểm :math:`M_i` là :math:`0`-phẳng. Hơn nữa

    .. math:: \dim (M_0 + M_1 + \cdots + M_n) = \mathrm{rank} (\overrightarrow{M_0 M_1}, \ldots, \overrightarrow{M_0 M_n}).

    Do đó nếu hệ điểm :math:`\{ M_0, \ldots, M_n \}` độc lập thì

    .. math:: \boxed{\dim(M_0 + M_1 + \cdots + M_n) = n.}

.. prf:theorem:: 
    :label: thm-giao-2-phang

    Cho :math:`\alpha` và :math:`\beta` là hai phẳng. Nếu :math:`\alpha \cap \beta \neq \emptyset` thì với mọi điểm :math:`M` thuộc :math:`\alpha` và với mọi điểm :math:`N` thuộc :math:`\beta` ta có :math:`\overrightarrow{MN} = \vec{\alpha} + \vec{\beta}`.

    Ngược lại, nếu ta có điểm :math:`M \in \alpha` và điểm :math:`N \in \beta` sao cho :math:`\overrightarrow{MN} = \vec{\alpha} + \vec{\beta}` thì :math:`\alpha \cap \beta \neq \emptyset`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử :math:`\alpha \cap \beta \neq \emptyset`. Khi đó tồn tại điểm :math:`P \in \alpha \cap \beta`. Với mọi điểm :math:`M \in \alpha` ta có :math:`\overrightarrow{MP} \in \vec{\alpha}`, tương tự với mọi điểm :math:`N \in \beta` ta có :math:`\overrightarrow{PN} \in \vec{\beta}`. Suy ra

    .. math:: \overrightarrow{MP} + \overrightarrow{PN} = \overrightarrow{MN} = \vec{\alpha} + \vec{\beta}.

    Ngược lại, giả sử có điểm :math:`M \in \alpha` và điểm :math:`N \in \beta` sao cho :math:`\overrightarrow{MN} = \vec{\alpha} + \vec{\beta}`. Khi đó :math:`\overrightarrow{MN} = \vec{u} + \vec{v}` với :math:`\vec{u} \in \vec{\alpha}` và :math:`\vec{v} \in \vec{\beta}`. Điều này xảy ra nếu tồn tại duy nhất điểm :math:`P \in \alpha` sao cho :math:`\overrightarrow{MP} = \vec{u}`, tương tự tồn tại duy nhất điểm :math:`Q \in \beta` sao cho :math:`\overrightarrow{QN} = \vec{v}`.

    Khi đó, vì

    .. math:: \overrightarrow{MN} = \vec{u} + \vec{v} = \overrightarrow{MP} + \overrightarrow{QN} = \overrightarrow{MP} - \overrightarrow{NQ}.

    Chuyển vế và đổi dấu ta có

    .. math:: \overrightarrow{MP} = \overrightarrow{MN} + \overrightarrow{NQ} = \overrightarrow{MQ}

    nên :math:`P \equiv Q`. Như vậy :math:`\alpha \cap \beta \neq \emptyset` vì có ít nhất một điểm :math:`P \equiv Q` thuộc giao của hai phẳng.

.. prf:theorem:: 
    :label: theo-dim
 
    Giả sử :math:`\alpha` và :math:`\beta` là hai phẳng với phương lần lượt là :math:`\vec{\alpha}` và :math:`\vec{\beta}`. Khi đó:

    1. Nếu :math:`\alpha \cap \beta \neq \emptyset` thì

    .. math:: \dim (\alpha + \beta) = \dim \alpha + \dim \beta = \dim (\alpha \cap \beta).

    2. Nếu :math:`\alpha \cap \beta = \emptyset` thì

    .. math:: \dim (\alpha + \beta) = \dim \alpha + \dim \beta = \dim (\vec{\alpha} + \vec{\beta}) + 1.

.. admonition:: Chứng minh công thức 1
    :class: danger, dropdown

    Nếu :math:`\alpha \cap \beta \neq \emptyset` thì theo :prf:ref:`phuong-giao` ta có :math:`\alpha \cap \beta` là một phẳng có phương :math:`\vec{\alpha} \cap \vec{\beta}`.

    Lấy điểm :math:`M \in \alpha \cap \beta` và gọi :math:`\gamma` là phẳng đi qua :math:`M` với phương :math:`\vec{\gamma} = \vec{\alpha} + \vec{\beta}`. Ta có :math:`\alpha \subset \gamma` và :math:`\beta \subset \gamma`.

    Ngoài ra nếu có phẳng :math:`\gamma'` chứa :math:`\alpha` và :math:`\beta` thì :math:`M \in \gamma'` và phương của :math:`\gamma'` phải chứa :math:`\vec{\alpha}` và :math:`\vec{\beta}`. Nói cách khác ta có :math:`\gamma \subset \gamma'`.

    Như vậy :math:`\gamma` là phẳng nhỏ nhất chứa :math:`\alpha` và :math:`\beta`, tức là :math:`\gamma = \alpha + \beta`. Do đó

    .. math::  
        
        \dim (\alpha + \beta) & = \dim \gamma = \dim \vec{\gamma} \\
        & = \dim(\vec{\alpha} + \vec{\beta}) = \dim \vec{\alpha} + \dim \vec{\beta} \\
        & = \dim \alpha + \dim \beta \stackrel{?}{=} \dim(\alpha \cap \beta).
        
.. admonition:: [TODO] Chứng minh công thức 2
    :class: danger, dropdown

    [TODO]

================
Vị trí tương đối
================

.. prf:definition:: Vị trí tương đối giữa hai phẳng
    :label: def-equiv-position

    Hai phẳng :math:`\alpha` và :math:`\beta` được gọi là **cắt nhau cấp** :math:`r` nếu :math:`\alpha \cap \beta` là một :math:`r`-phẳng.

    Hai phẳng :math:`\alpha` và :math:`\beta` được gọi là **chéo nhau cấp** :math:`r` nếu :math:`\alpha \cap \beta = \emptyset` và :math:`\dim (\vec{\alpha} \cap \vec{\beta}) = r`.

    Hai phẳng :math:`\alpha` và :math:`\beta` được gọi là **song song** (với nhau) nếu :math:`\vec{\alpha} \subset \vec{\beta}` hoặc :math:`\vec{\beta} \subset \vec{\alpha}`.

.. prf:example:: 
    :label: exp-equiv-pos-3d

    Xét không gian ba chiều :math:`\mathbb{R}^3`.

    1. Hai đường thẳng "cắt nhau" là hai :math:`1`-phẳng cắt nhau cấp :math:`0` (tại một điểm). Tổng của chúng là mặt phẳng duy nhất xác định bởi hai đường thẳng đó.
    2. Hai mặt phẳng "cắt nhau" là hai :math:`2`-phẳng cắt nhau cấp :math:`1` (đường thẳng chung). Tổng của chúng là toàn bộ :math:`\mathbb{R}^3`.

Theo :prf:ref:`theo-dim`, trong :math:`\mathbb{R}^3` không tồn tại hai mặt phẳng chéo nhau cấp :math:`0` hoặc :math:`1`.

.. prf:theorem::
    :label: parallel

    Cho hai phẳng song song :math:`\alpha` và :math:`\beta`. Nếu :math:`\alpha \cap \beta \neq \emptyset` thì :math:`\alpha \subset \beta` hoặc :math:`\beta \subset \alpha`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Do :math:`\alpha` và :math:`\beta` có điểm chung nên theo :prf:ref:`phuong-giao` :math:`\alpha \cap \beta` là một phẳng có phương :math:`\vec{\alpha} \cap \vec{\beta}`.

    Do :math:`\alpha` song song :math:`\beta` nên :math:`\vec{\alpha} \subset \vec{\beta}` hoặc :math:`\vec{\beta} \subset \vec{\alpha}`.

    Nếu :math:`\vec{\alpha} \subset \vec{\beta}` thì :math:`\vec{\alpha} \cap \vec{\beta} = \vec{\alpha}`, suy ra :math:`\alpha \cap \beta = \alpha`, hay :math:`\alpha \subset \beta`.

    Tương tự, nếu :math:`\vec{\beta} \subset \vec{\alpha}` thì :math:`\beta \subset \alpha`.

.. prf:theorem:: 
    :label: thm-phang-ss

    Qua một điểm :math:`M` có một và chỉ một :math:`m`-phẳng song song với :math:`m`-phẳng :math:`\alpha` đã cho.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Gọi :math:`\beta` là :math:`m`-phẳng đi qua điểm :math:`M` với phương :math:`\vec{\alpha}`.

    Khi đó :math:`\beta` là phẳng :math:`m` chiều song song với :math:`\alpha`. Nếu :math:`\beta'` cũng là :math:`m`-phẳng đi qua :math:`A` và song song với :math:`\alpha` thì suy ra :math:`\vec{\beta} = \vec{\beta}'` (và cũng bằng :math:`\vec{\alpha}`).

    Do :math:`\beta` và :math:`\beta'` có điểm chung nên theo :prf:ref:`parallel` ta có :math:`\beta \equiv \beta'`.

.. prf:theorem:: 
    :label: thm-phang-ss-x
    
    Trong không gian affine :math:`n` chiều :math:`\mathcal{A}^n` cho một siêu phẳng :math:`\alpha` và một :math:`m`-phẳng :math:`\beta` với :math:`1 \leqslant m \leqslant n-1`. Khi đó :math:`\alpha` và :math:`\beta` hoặc song song, hoặc cắt nhau theo một :math:`(m-1)`-phẳng.

=========================
Mục tiêu và tọa độ affine
=========================

.. prf:definition:: Mục tiêu affine
    :label: def-target-affine
    
    Cho :math:`\mathcal{A}^n` là một không gian affine :math:`n` chiều. Hệ

    .. math:: \{ O, \vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n \}

    gồm một điểm :math:`O \in \mathcal{A}^n` và một cơ sở :math:`\{ \vec{e}_1, \ldots, \vec{e}_n \}` của :math:`\vec{\mathcal{A}}^n` được gọi là **mục tiêu affine** (hay **mục tiêu**) của :math:`\mathcal{A}^n`.

    Điểm :math:`O` được gọi là **gốc**, các vector :math:`\vec{e}_i` được gọi là **vector cơ sở thứ** :math:`i` với :math:`i = 1, 2, \ldots, n`.

Giả sử :math:`\{ O, \vec{e}_i \}` là một mục tiêu của không gian affine :math:`\mathcal{A}^n`.

Khi đó với mọi điểm :math:`M \in \mathcal{A}^n`, vector :math:`\overrightarrow{OM} \in \mathcal{A}^n` nên ta có biểu diễn tuyến tính của :math:`\overrightarrow{OM}` qua cơ sở :math:`\{ \vec{e}_i \}`:

.. math:: \overrightarrow{OM} = \sum_{i=1}^n x_i \vec{e}_i.

Khi đó, nhắc lại kiến thức đại số tuyến tính, vector :math:`\overrightarrow{OM}` có tọa độ :math:`(x_1, \ldots, x_n)` đối với cơ sở :math:`\{ \vec{e}_i \}`, :math:`x_i` là các phần tử thuộc :math:`\mathbb{F}` với :math:`i = 1, \ldots, n`.

Bộ :math:`(x_1, \ldots, x_n)` được gọi là **tọa độ** của :math:`M` trong mục tiêu :math:`\{ O, \vec{e}_i \}`, và :math:`x_i` được gọi là **tọa độ thứ** :math:`i`. Kí hiệu là :math:`M(x_i)`.

Giả sử :math:`M` có tọa độ :math:`(x_i)` và :math:`N` có tọa độ :math:`(y_i)` thì đối với mục tiêu :math:`\{ O, \vec{e}_i \}` ta có

.. math:: \overrightarrow{MN} = \overrightarrow{ON} - \overrightarrow{OM} = (y_i - x_i).

Đây là tọa độ của :math:`\overrightarrow{MN}` trong mục tiêu :math:`\{ O, \vec{e}_i \}`.

.. prf:remark:: 
    :label: rmk-geo-to-alg

    Giả sử trên :math:`\mathcal{A}^n` đã chọn được mục tiêu cố định :math:`\{ O, \vec{e}_i \}`. Xét ánh xạ

    .. math:: \varphi : A \to \mathbb{F}^n, \ M \to (x_i)

    với :math:`(x_i)` là tọa độ của :math:`M` trong mục tiêu. Khi đó :math:`\varphi` là song ánh và mỗi điểm được đồng nhất với một phần tử của :math:`\mathbb{F}^n`. Lúc này chúng ta đã đại số hóa hình học.

.. prf:remark:: 
    :label: rmk-target-affine

    Xét mục tiêu affine :math:`\{ O, \vec{e}_i \}` của :math:`\mathcal{A}^n` và gọi :math:`E_i \in \mathcal{A}` là các điểm sao cho :math:`\overrightarrow{OE_i} = \vec{e}_i`.

    Khi đó hệ điểm :math:`\{ O, E_1, \ldots, E_n \}` độc lập affine. Ngược lại, một hệ điểm gồm :math:`n+1` độc lập :math:`\{ O, E_1, \ldots, E_n \}` độc lập affine xác định một mục tiêu affine :math:`\{ O, \vec{e}_i \}` với :math:`\vec{e}_i = \overrightarrow{OE_i}`.

    Theo định nghĩa ta có :math:`O = (0, \ldots, 0)` và :math:`E_i = (0, \ldots, 0, 1, 0, \ldots, 0)` với số :math:`1` ở vị trí :math:`i`.

.. prf:remark:: 
    :label: rmk-hyperplane-i

    Siêu phẳng đi qua :math:`n` điểm độc lập :math:`O`, :math:`E_1`, ..., :math:`E_{i-1}`, :math:`E_{i+1}`, ..., :math:`E_n` được gọi là **siêu phẳng tọa độ thứ** :math:`i`. Dễ thấy :math:`M` thuộc siêu phẳng tọa độ thứ :math:`i` khi và chỉ khi :math:`x_i = 0` với :math:`x_i` là tọa độ thứ :math:`i` của :math:`M`.

======================
Công thức đổi mục tiêu
======================

Giả sử trong không gian affine :math:`\mathcal{A}^n` có hai mục tiêu :math:`\{ O, \vec{e}_i \}` và :math:`\{ O', \vec{e}_i' \}`.

Mỗi điểm :math:`M` sẽ có tọa độ khác nhau ứng với mỗi mục tiêu :math:`(x_i)` và :math:`(x_i')`. Ta cần tìm mối liên hệ giữa chúng.

Do :math:`\vec{e}_i` là cơ sở của không gian vector nên mọi vector trong không gian vector có thể biểu diễn dưới dạng tổ hợp tuyến tính của các vector trong cơ sở, như vậy

.. math:: \overrightarrow{OO'} = \sum_{i=1}^n b_i \vec{e}_i

với :math:`b_i \in \mathbb{F}`.

Biểu diễn các vector trong cơ sở :math:`\vec{e}_i'` bởi tổ hợp tuyến tính các vector trong cơ sở :math:`\vec{e}_i`:

.. math:: 
    
    \begin{cases}
        \vec{e}_1' = c_{11} \vec{e}_1 + c_{12} \vec{e}_2 + \cdots + c_{1n} \vec{e}_n \\
        \vec{e}_2' = c_{21} \vec{e}_1 + c_{22} \vec{e}_2 + \cdots + c_{2n} \vec{e}_n \\
        \vdots \\
        \vec{e}_n' = c_{n1} \vec{e}_1 + c_{n2} \vec{e}_2 + \cdots + c_{nn} \vec{e}_n
    \end{cases}

hay viết ngắn gọn là

.. math:: \vec{e}_i' = \sum_{j=1}^n c_{ij} \vec{e}_j

với :math:`i = 1, 2, \ldots, n`.

Điểm :math:`M` có tọa độ trong hai mục tiêu trên lần lượt là :math:`(x_i)` và :math:`(x_i')`, nghĩa là

.. math:: \overrightarrow{OM} = \sum_{i=1}^n x_i \vec{e}_i, \ \overrightarrow{O'M} = \sum_{i=1}^n x_i' \vec{e}_i'.

Ta có

.. math:: 
    
    \sum_{i=1}^n x_i \vec{e}_i & = \overrightarrow{OM} = \overrightarrow{OO'} + \overrightarrow{O'M} \\
    & = \sum_{i=1}^n b_i \vec{e}_i + \sum_{i=1}^n x_i' \vec{e}_i' \\
    & = \sum_{i=1}^n b_i \vec{e}_i + \sum_{i=1}^n x_i' \sum_{j=1}^n c_{ij} \vec{e}_j \\
    & = \sum_{i=1}^n b_i \vec{e}_i + \sum_{i=1}^n x_i' \sum_{j=1}^n c_{ji} x_j' \\
    & = \sum_{i=1}^n \left(\sum_{j=1}^n c_{ji} x_j' + b_i\right) \vec{e}_i.
    
Ở đây mình biến đổi

.. math:: \sum_{i=1}^n x_i' \sum_{j=1}^n c_{ij} \vec{e}_j = \sum_{i=1}^n \sum_{j=1}^n x_i' c_{ij} \vec{e}_j = \sum_{j=1}^n \vec{e}_j \sum_{i=1}^n c_{ij} x_i',

và để đồng bộ với tổng phía trước là :math:`\sum\limits_{i=1}^n b_i \vec{e}_i` thì mình đổi :math:`j` thành :math:`i` và :math:`j` thành :math:`i` nên sẽ có

.. math:: \sum_{i=1}^n x_i' \sum_{j=1}^n c_{ij} \vec{e}_j = \sum_{i=1}^n \vec{e}_i \sum_{j=1}^n c_{ji} x_j'.

Khi đó

.. math:: x_i = \sum_{j=1}^n c_{ji} x_j' + b_i

với :math:`i = 1, 2, \ldots, n`. Điều này tương đương với

.. math::     
    
    x_1 = c_{11} x_1' + c_{21} x_2' + \cdots + c_{n1} x_n' + b_1 \\
    x_2 = c_{12} x_1' + c_{22} x_2' + \cdots + c_{n2} x_n' + b_2 \\
    \cdots \\
    x_n = c_{1n} x_1' + c_{2n} x_2' + \cdots + c_{nn} x_n' + b_n

Chúng ta có thể viết dưới dạng ma trận là

.. math:: (x_1, \ldots, x_n) = (x_1', \ldots, x_n') \cdot C + (b_1, \ldots, b_n)

với :math:`C` là ma trận

.. math:: C = \begin{pmatrix} c_{11} & c_{12} & \cdots & c_{1n} \\ c_{21} & c_{22} & \cdots & c_{2n} \\ \ddots & \ddots & \ddots & \ddots \\ c_{n1} & c_{n2} & \cdots & c_{nn} \end{pmatrix}.

Hệ phương trình tuyến tính có nghiệm khi :math:`\det C \neq 0`.

Các công thức trên được gọi là công thức đổi tọa độ (hay công thức đổi mục tiêu) và ma trận đổi tọa độ :math:`C` từ mục tiêu :math:`\{ O, \vec{e}_i \}` sang :math:`\{ O', \vec{e}_i' \}`.

================================
Phương trình của :math:`m`-phẳng
================================

--------------------
Phương trình tham số
--------------------

Cho :math:`\mathcal{A}^n` là một không gian affine :math:`n` chiều với mục tiêu :math:`\{ O, \vec{e}_i \}` cho trước, và :math:`\alpha` là một :math:`m`-phẳng đi qua điểm :math:`M` với phương :math:`\vec{\alpha}` sao cho :math:`0 < m < n`.

Giả sử

.. math:: \overrightarrow{OP} = \sum_{i=1}^n b_i \vec{e}_i

và :math:`\{ \vec{\alpha}_1, \ldots, \vec{\alpha}_m \}` là một cơ sở của :math:`\vec{\alpha}` với

.. math:: \vec{\alpha}_j = \sum_{i=1}^n a_{ij} \vec{e}_i, \quad j = 1, \ldots, m.

Điểm :math:`P` có tọa độ :math:`(x_i)` đối với mục tiêu :math:`\{ O, \vec{e}_i \}` thuộc :math:`\alpha` khi và chỉ khi :math:`\overrightarrow{MP} \in \vec{\alpha}`, tức là có các số :math:`t_j \in \mathbb{F}` sao cho

.. math:: \overrightarrow{MP} = \sum_{j=1}^m t_j \vec{\alpha}_j.

Ta có

.. math:: \overrightarrow{MP} = \overrightarrow{OP} - \overrightarrow{OM} = \sum_{i=1}^n x_i \vec{e}_i - \sum_{i=1}^n b_i \vec{e}_i = \sum_{i=1}^n (x_i - b_i) \vec{e}_i.

Ta cũng có

.. math::     
    
    \overrightarrow{MP} & = \sum_{j=1}^m t_j \vec{\alpha}_j = \sum_{j=1}^m t_j \sum_{i=1}^n a_{ij} \vec{e}_i \\
    & = \sum_{i=1}^n \left(\sum_{j=1}^m t_j a_{ij} \right) \vec{e}_i \\
    & \Rightarrow x_i = \sum_{j=1}^m t_j a_{ij} + b_i.
    
Hệ phương trình trở thành

.. math:: 
    
    \begin{cases}
        x_1 = a_{11} t_1 + a_{12} t_2 + \cdots + a_{1m} t_m + b_1 \\
        x_2 = a_{21} t_1 + a_{22} t_2 + \cdots + a_{2m} t_m + b_2 \\
        \vdots \\
        x_n = a_{n1} t_1 + a_{n2} t_2 + \cdots + a_{nm} t_m + b_n
    \end{cases}

hay dưới dạng ma trận là

.. math:: (x_1, \ldots, x_n) = A \cdot (t_1, \ldots, t_m) + (b_1, \ldots, b_n).

Khi đó ta có thể viết phương trình tham số dưới dạng vector

.. math:: \vec{x} = t_1 \vec{a}_1 + t_2 \vec{a}_2 + \cdots + t_m \vec{a}_m + \vec{b}.

Các công thức trên tương đương nhau và được gọi là phương trình tham số của :math:`m`-phẳng :math:`\alpha`, còn các phần tử :math:`t_j` với :math:`j = 1, \ldots, m` được gọi là các tham số.

-----------------------------
[TODO] Phương trình tổng quát
-----------------------------

======================
Tâm tỉ cự và tỉ số đơn
======================

Cho họ điểm

.. math:: \{ M_1, M_2, \ldots, M_n \} \subset \mathcal{A}^n

và họ hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}` với :math:`\lambda \in \mathbb{F}` thỏa điều kiện

.. math:: \lambda = \lambda_1 + \lambda_2 + \cdots + \lambda_n \neq 0.

Khi đó với điểm :math:`O` tùy ý của :math:`\mathcal{A}^n` ta có

.. math:: \dfrac{1}{\lambda} \left(\lambda_1 \overrightarrow{OM_1} + \lambda_2 \overrightarrow{OM_2} + \cdots + \lambda_n \overrightarrow{OM_n}\right)

là một vector xác định của :math:`\mathcal{A}^n`. Do đó tồn tại duy nhất một điểm :math:`G \in \mathcal{A}^n` sao cho

.. math:: \overrightarrow{OG} = \dfrac{1}{\lambda} \left(\lambda_1 \overrightarrow{OM_1} + \lambda_2 \overrightarrow{OM_2} + \cdots + \lambda_n \overrightarrow{OM_n} \right).

Khi đó điểm :math:`G` được gọi **tâm tỉ cự** của họ điểm :math:`\{ M_1, M_2, \ldots, M_ n \}` gắn với hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}`.

.. prf:theorem:: 
    :label: thm-tam-ti-cu

    Điểm :math:`G` là tâm tỉ cự của họ điểm :math:`\{ M_1, M_2, \ldots, M_ n \}` gắn với hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}` khi và chỉ khi :math:`G` thỏa mãn hệ thức

    .. math:: \lambda_1 \overrightarrow{GM_1} + \lambda_2 \overrightarrow{GM_2} + \cdots + \lambda_n \overrightarrow{GM_n} = \vec{0}.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Từ định nghĩa tâm tỉ cự ta có

    .. math:: 
        
        \overrightarrow{OG} & = \dfrac{1}{\lambda} \left( \lambda_1 \overrightarrow{OM_1} + \lambda_2 \overrightarrow{OM_2} + \cdots + \lambda_n \overrightarrow{OM_n} \right) \\
        & = \dfrac{1}{\lambda} \left[\lambda_1 \left(\overrightarrow{OG} + \overrightarrow{GM_1}\right) + \lambda_2 \left(\overrightarrow{OG} + \overrightarrow{GM_2}\right) + \cdots + \lambda_n \left(\overrightarrow{OG} + \overrightarrow{GM_n}\right)\right] \\
        & = \dfrac{\lambda_1 + \lambda_2 + \cdots + \lambda_n}{\lambda} \overrightarrow{OG} + \dfrac{1}{\lambda} \left(\lambda_1 \overrightarrow{GM_1} + \overrightarrow{GM_2} + \cdots + \overrightarrow{GM_n}\right),   

    mà :math:`\lambda_1 + \lambda_2 + \cdots + \lambda_n = \lambda` nên tối giản :math:`\overrightarrow{OG}` hai vế ta có điều phải chứng minh.

.. prf:remark:: 
    :label: rmk-property-tam-ti-cu

    Từ định lí trên ta cũng chứng minh được hai hệ quả sau:

    1. Tâm tỉ cự không phụ thuộc điểm :math:`O` được chọn mà phụ thuộc họ điểm :math:`\{ M_1, M_2, \ldots, M_n \}` và họ hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}`.
    2. Khi thay họ hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}` bởi :math:`\{ k\lambda_1, k\lambda_2, \ldots, k\lambda_n \}` với :math:`k \neq 0` thì tâm tỉ cự không thay đổi.

.. prf:definition:: 
    :label: def-trong-tam

    Tâm tỉ cự :math:`G` của hệ điểm :math:`\{ M_1, M_2, \ldots, M_n \}` gắn với họ hệ số :math:`\{ \lambda_1, \lambda_2, \ldots, \lambda_n \}` mà

    .. math:: \lambda_1 = \lambda_2 = \cdots = \lambda_n = 1

    thì :math:`G` được gọi là **trọng tâm** của hệ điểm.

Khi đó, với mọi điểm :math:`O \in \mathcal{A}^n` ta có

.. math:: \overrightarrow{OG} = \dfrac{1}{n} \sum_{i=1}^n \overrightarrow{OM_i},

hay

.. math:: \sum_{i=1}^n \overrightarrow{GM_i} = \vec{0}.

.. prf:remark:: 
    :label: rmk-trong-tam
    
    Mọi hệ :math:`m` điểm có trọng tâm khi và chỉ khi **đặc số** (**characteristic**) của trường :math:`\mathbb{F}` phải khác :math:`m`.
    
    Khi :math:`\mathbb{F} = \mathbb{R}` hoặc :math:`\mathbb{C}` thì mọi hệ hữu hạn điểm đều có trọng tâm.

.. prf:theorem:: 
    :label: thm-tam-ti-cu-coeff

    Tập hợp tất cả các tâm tỉ cự với họ các hệ số khác nhau của hệ điểm :math:`\{ M_1, \ldots, M_n \}` trong không gian affine :math:`\mathcal{A}^n` chính là phẳng

    .. math:: \alpha = M_1 + M_2 + \cdots + M_n.

=============
Ánh xạ affine
=============

.. prf:definition:: 
    :label: def-affine-map

    Cho hai không gian affine :math:`\mathcal{A}` và :math:`\mathcal{A}'` trên cùng trường :math:`\mathbb{F}` và ánh xạ :math:`\varphi: \vec{\mathcal{A}} \to \vec{\mathcal{A}'}` sao cho với mọi :math:`M, N \in \mathcal{A}` ta có

    .. math:: \overrightarrow{f(M) f(N)} = \varphi(\overrightarrow{MN})

    thì :math:`f` được gọi là **ánh xạ affine** liên kết với :math:`\varphi`.

    Ánh xạ :math:`\varphi` được gọi là **ánh xạ tuyến tính liên kết** hay **ánh xạ nền** của ánh xạ affine :math:`f`.

Theo định nghĩa, mỗi ánh xạ affine chỉ có một ánh xạ tuyến tính liên kết. Tuy nhiên một ánh xạ tuyến tính có thể liên kết với nhiều ánh xạ affine.

.. prf:example:: 
    :label: exp-affine-map-id

    Ánh xạ đồng nhất :math:`\mathrm{Id}_\mathcal{A}: \mathcal{A} \to \mathcal{A}`, :math:`f(M) = M` với mọi :math:`M \in \mathcal{A}` của không gian affine là một ánh xạ affine. Ánh xạ tuyến tính liên kết với :math:`\mathrm{Id}_\mathcal{A}` chính là ánh xạ đồng nhất :math:`\mathrm{Id}_{\vec{\mathcal{A}}}` của :math:`\vec{\mathcal{A}}`.

.. prf:example:: 
    :label: exp-affine-map-fixed

    Ánh xạ hằng :math:`f: \mathcal{A} \to \mathcal{A}'` biến mọi điểm của :math:`\mathcal{A}` thành một điểm cố định nào đó của :math:`\mathcal{A}'` là một ánh xạ affine. Ánh xạ tuyến tính liên kết :math:`\vec{f}` của :math:`f` là ánh xạ không :math:`\mathcal{O}`, biến mọi vector thành vector :math:`\vec{0}`.

.. prf:example:: 
    :label: exp-affine-map-parallel

    Phép chiếu song song: trong không gian affine :math:`n` chiều :math:`\mathcal{A}^n` cho :math:`m`-phẳng :math:`\alpha` và :math:`(n-m)`-phẳng :math:`\beta` sao cho :math:`\vec{\alpha} \cap \vec{\beta} = \{ \vec{0} \}`.
    
    Dựa vào định lí về số chiều của phẳng tổng ta chứng minh được rằng :math:`\alpha \cap \beta \neq \emptyset`. Do :math:`\vec{\alpha} \cap \vec{\beta} = \{ \vec{0} \}` ta suy ra :math:`\alpha \cap \beta` là :math:`0`-phẳng, tức là giao của :math:`\alpha` và :math:`\beta` là tập chỉ có một điểm.

    Giả sử :math:`M` là một điểm bất kì của :math:`\mathcal{A}^n`. Gọi :math:`\alpha'` là :math:`m`-phẳng đi qua :math:`M` và song song :math:`\alpha`, gọi :math:`\beta'` là :math:`(n-m)`-phẳng đi qua :math:`M` và song song với :math:`\beta`. Theo lập luận trên, :math:`\alpha'` và :math:`\beta` giao nhau tại một điểm duy nhất là :math:`M_\beta`, tương tự :math:`\beta'` cắt :math:`\alpha` tại một điểm duy nhất là :math:`M_\alpha`. Các ánh xạ

    .. math:: \rho_\alpha : \mathcal{A}^n \to \alpha, \ M \to M_\alpha

    và

    .. math:: \rho_\beta : \mathcal{A}^n \to \beta, \ M \to M_\beta

    lần lượt được gọi là **phép chiếu song song** lên phẳng :math:`\alpha` theo phương :math:`\beta` và phép chiếu song song lên phẳng :math:`\beta` theo phương :math:`\alpha`.

Ta gọi :math:`\alpha` là cơ sở và :math:`\beta` là phương chiếu của phép chiếu :math:`\rho_\alpha`.

Ta gọi :math:`\beta` là cơ sở và :math:`\alpha` là phương chiếu của phép chiếu :math:`\rho_\beta`.

Ta sẽ chứng minh :math:`\rho_\alpha` là ánh xạ affine.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Từ giả thiết :math:`\vec{\alpha} \cup \vec{\beta} = \vec{\mathcal{A}}`, gọi :math:`\rho_{\vec{\alpha}}` là phép chiếu lên thành phần thứ nhất

    .. math:: \rho_{\vec{\alpha}} : \vec{\mathcal{A}} \to \vec{\alpha}.

    Với mọi :math:`M, N \in \mathcal{A}` ta có

    .. math:: \overrightarrow{\rho_\alpha(M) \rho_\alpha(N)} = \overrightarrow{M_\alpha N_\alpha}.

    Hơn nữa

    .. math:: \rho_{\vec{\alpha}} (\overrightarrow{MN}) = \rho_{\vec{\alpha}}(\overrightarrow{MM_\alpha}) + \rho_{\vec{\alpha}} (\overrightarrow{M_\alpha N_\alpha}) + \rho_{\vec{\alpha}}(\overrightarrow{N_\alpha N}) = \overrightarrow{M_\alpha N_\alpha}.

    Từ đây suy ra :math:`\rho_\alpha` là ánh xạ liên kết với :math:`\rho_{\vec{\alpha}}`. Dễ thấy (?) :math:`\rho_\alpha` và :math:`\rho_\beta` có tính chất

    .. math:: \rho_\alpha^2 = \rho_\alpha, \ \rho_\beta^2 = \rho_\beta, \ \rho_\alpha \rho_\beta = \rho_\beta \rho_\alpha = h

    với :math:`h` là ánh xạ hẳng, biến mọi điểm thành giao điểm của :math:`\alpha` và :math:`\beta`.

.. prf:definition:: 
    :label: def-affine-homomorphism

    Nếu ánh xạ affine :math:`f` là một đơn ánh thì ta nói :math:`f` là **đơn cấu affine**. Tương tự cho **toàn cấu affine** và **đẳng cấu affine**.

Khi :math:`\mathcal{A} = \mathcal{A}'`, tức là :math:`f: \mathcal{A} \to \mathcal{A}` thì ta nói :math:`f` là một **tự đồng cấu affine** (hay **automorphism**) của :math:`\mathcal{A}`.

Nếu có một đẳng cấu affine từ :math:`\mathcal{A}` vào :math:`\mathcal{A}'` thì ta nói :math:`\mathcal{A}` và :math:`\mathcal{A}'` đẳng cấu affine với nhau và kí hiệu là :math:`\mathcal{A} \cong \mathcal{A}'`.

Quan hệ đẳng cấu giữa các không gian affine là quan hệ tương đương và hai không gian affine đẳng cấu khi và chỉ khi chúng có cùng số chiều.

.. prf:theorem:: 
    :label: thm-affine-homomorphism

    Cho :math:`f: \mathcal{A} \to \mathcal{A}'` là ánh xạ affine. Khi đó

    1. Nếu :math:`f` là đơn cấu, toàn cấu hoặc đẳng cấu affine thì ánh xạ liên kết:math:`\vec{f}` theo thứ tự là đơn cấu, toàn cấu và dẳng cấu tuyến tính.
    2. Nếu :math:`f` là đẳng cấu affine thì ánh xạ ngược :math:`f^{-1} : \mathcal{A}' \to \mathcal{A}` cũng là đẳng cấu affine và :math:`\overrightarrow{f^{-1}} = (\vec{f})^{-1}`.

.. prf:theorem:: 
    :label: thm-affine-map-comb

    Nếu :math:`f: \mathcal{A} \to \mathcal{A}'` và :math:`g: \mathcal{A}' \to \mathcal{A}''` là các ánh xạ affine lần lượt liên kết với các ánh xạ tuyến tính :math:`\vec{f}` và :math:`\vec{g}` thì :math:`g \circ f` là ánh xạ affine liên kết với :math:`\vec{g} \circ \vec{f}`, tức là

    .. math:: \overrightarrow{g \circ f} = \vec{g} \circ \vec{f}.

.. prf:theorem:: 
    :label: thm-linear-map

    Cho :math:`f: \mathcal{A} \to \mathcal{A}'` là ánh xạ affine liên kết với ánh xạ tuyến tính :math:`\vec{f}`. Khi đó

    1. Nếu :math:`\alpha` là một phẳng trong :math:`\mathcal{A}` với phương :math:`\vec{\alpha}` thì :math:`f(\alpha)` là một phẳng trong :math:`\mathcal{A}'` với phương :math:`\vec{f}(\vec{\alpha})` và :math:`\dim f(\alpha) \geqslant \dim\alpha`. Trong trường hợp :math:`f` là đơn cấu thì :math:`\dim f(\alpha) = \dim \alpha`.
    2. Giả sử :math:`\alpha'` là một phẳng trong :math:`\mathcal{A}'` với phương :math:`\vec{\alpha}'`. Nếu :math:`f^{-1}(\alpha')` khác rỗng thì :math:`f^{-1}(\alpha')` là một phương trong :math:`\mathcal{A}` với phương :math:`\overrightarrow{f^{-1}}(\vec{\alpha}')`.

=========================
Sự xác định ánh xạ affine
=========================

Ánh xạ tuyến tính hoàn toàn xác định nếu biết được ảnh của một cơ sở. Ánh xạ affine cũng vậy, nó hoàn toàn xác định nếu biết được ảnh của một mục tiêu.

.. prf:theorem:: 
    :label: thm-define-affine

    Cho :math:`\mathcal{A}` và :math:`\mathcal{A}'` là các :math:`\mathbb{F}`-không gian affine, :math:`\varphi: \vec{\mathcal{A}} \to \vec{\mathcal{A}'}` là ánh xạ tuyến tính, :math:`M \in \mathcal{A}` và :math:`M' \in \mathcal{A}'`. Khi đó tồn tại duy nhất một ánh xạ affine :math:`f: \mathcal{A} \to \mathcal{A}'` sao cho :math:`f(M) = M'` và :math:`\vec{f} = \varphi`.

Nói cách khác, ánh xạ affine hoàn toàn xác định khi biết ánh xạ tuyến tính liên kết và một cặp điểm tương ứng.

.. prf:remark:: 
    :label: rmk-isomorphism

    Nếu :math:`\dim \mathcal{A} = \dim \mathcal{A}'` và :math:`\varphi` là đẳng cấu tuyến tính thì :math:`f` là một đẳng cấu affine.

.. prf:corollary:: 
    :label: cor-exist-map

    Cho :math:`\mathcal{A}` và :math:`\mathcal{A}'` là hai :math:`\mathbb{F}`-không gian affine, :math:`\{ O, \vec{e}_1, \ldots, \vec{e}_n \}` là mục tiêu của :math:`\mathcal{A}`, :math:`O' \in \mathcal{A}'` và :math:`\{ \vec{e}_1', \ldots, \vec{e}_n' \}` là một hệ vector trong :math:`\vec{\mathcal{A}'}`. Khi đó tồn tại duy nhất một ánh xạ affine :math:`f: \mathcal{A} \to \mathcal{A}'` sao cho

    .. math:: f(O) = O', \ \text{và} \ \vec{f}(\vec{e}_i) = \vec{e}_i'

    với mọi :math:`i = 1, \ldots, n`.

Nói cách khác, ánh xạ affine hoàn toàn được xác định bởi ảnh của một mục tiêu.

Hơn nữa, nếu :math:`\dim\mathcal{A} = \dim \mathcal{A}'` và :math:`\{ \vec{e}_1', \ldots, \vec{e}_n' \}` là một cơ sở của :math:`\mathcal{A}'` thì :math:`f` là một đẳng cấu affine.
