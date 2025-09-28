Linear code
============

.. prf:definition:: Linear code
    :label: def-lincode

    Block code :math:`(n)_q` :math:`\mathcal{C}` được gọi là 
    **tuyến tính** (hay **linear**) nếu với mọi 
    :math:`a, b \in \mathbb{F}_2` và với mọi codeword 
    :math:`\bm{x}, \bm{y} \in \mathcal{C}` thì vector 
    :math:`a \cdot \bm{x} + b \cdot \bm{y}` cũng là 
    codeword thuộc :math:`\mathcal{C}`.

Ta kí hiệu linear code (mã tuyến tính) là :math:`[n]_q`. 
Có thể thấy block code :math:`[n]_q` là không gian 
vector con của :math:`V_n(q)`.

.. prf:definition::  
    :label: def-len-lincode

    Đối với code :math:`[n]_q` thì số :math:`n` được gọi là 
    **độ dài** của code.

.. prf:definition:: 
    :label: def-dim-lincode

    **Số chiều** của code :math:`[n]_q` là số :math:`k` bằng 
    với số chiều của không gian vector con :math:`\mathcal{C}` 
    của :math:`V_n(q)`.

.. prf:definition:: 
    :label: def-nk-code

    Linear code :math:`\mathcal{C}` có độ dài :math:`n` 
    và số chiều :math:`k` được gọi là :math:`[n, k]_q` code.

.. prf:definition:: 
    :label: def-speed-lincode

    **Tốc độ truyền** của :math:`[n, k]_q` code là 
    số :math:`R = \dfrac{k}{n}`.

.. prf:definition:: 
    :label: def-redudancy-lincode

    **Redundancy** (hay **избыточность**) của :math:`[n, k]_q` 
    code là số :math:`r = n - k`.

.. prf:definition:: 
    :label: def-min-dist-lincode

    **Khoảng cách nhỏ nhất** của code :math:`\mathcal{C}` là số 
    :math:`d` bằng với trọng số Hamming nhỏ nhất của các 
    codeword trong :math:`\mathcal{C}`

    .. math:: d = \min_{\bm{u} \in \mathcal{C}, \bm{u} \neq \bm{0}} \mathrm{wt}(\bm{u}).

.. prf:definition:: 
    :label: def-nkd-code

    Linear code :math:`[n, k]_q` với khoảng cách nhỏ nhất 
    :math:`d` được gọi là :math:`[n, k, d]_q` code.


Ma trận sinh
-------------

.. prf:definition::  
    :label: def-genmat-lincode

    Ma trận :math:`\bm{G}` được gọi là **ma trận sinh** 
    (hay **порождающая матрица**) của code :math:`C` 
    nếu nó chứa các vector trong cơ sở của không gian 
    vector con :math:`\mathcal{C}`.

Nếu :math:`\mathcal{C}` là :math:`[n, k]_q` code thì 
:math:`G` là ma trận kích thước :math:`k \times n`.

.. prf:remark:: 
    :label: rmk-genmat-lincode

    Nếu :math:`G` là ma trận sinh của :math:`[n, k]_q` code thì

    .. math:: \mathcal{C} = \{ \bm{a} \cdot \bm{G} : \bm{a} \in V_k(q) \}.

Ở đây ta nói ma trận :math:`\bm{G}` sinh ra code :math:`\mathcal{C}`.

Theo kiến thức đại số tuyến tính, nếu :math:`\bm{G}_1` và 
:math:`\bm{G}_2` kích thước :math:`k \times k` cùng sinh ra 
một code :math:`\mathcal{C}` thì tồn tại ma trận khả nghịch  
:math:`\bm{A}` kích thước :math:`k \times k` trên 
:math:`\mathbb{F}_q` sao cho :math:`\bm{A} \bm{G}_1 = \bm{G}_2`.


Coder
------

.. prf:definition:: 
    :label: def-coder

    **Coder** :math:`\varphi: V_k(q) \to V_n(q)` cho 
    :math:`[n, k]_q` code xác định bởi ma trận sinh 
    :math:`\bm{G}` theo nghĩa:

    .. math:: \varphi((a_1, \ldots, a_k)) = (a_1, \ldots, a_k) \cdot \bm{G}.

.. prf:definition:: 
    :label: def-systematic-mat

    Ma trận :math:`\bm{G}` kích thước :math:`k \times n` 
    được gọi là **systematic** nếu nó có dạng:

    .. math:: \bm{G} = (\bm{I}_k \Vert \bm{G}_0),

    với :math:`\bm{I}_k` là ma trận đơn vị 
    :math:`k \times k` và :math:`\bm{G}_0` là ma trận cỡ 
    :math:`k \times (n - k)` nào đó.

.. prf:definition:: 
    :label: def-systematic-code
    
    Code được gọi là **systematic** nếu nó có 
    ma trận sinh :math:`\bm{G}` là systematic.

.. prf:definition:: 
    :label: def-systematic-lincode

    Coder :math:`\varphi_{\bm{G}}` của systematic code 
    :math:`[n, k]_q`, xác định bởi ma trận sinh systematic 
    :math:`\bm{G} = (\bm{I}_k \Vert \bm{G}_0)`, được gọi là 
    **systematic**.

Khi đó với mọi thông điệp 
:math:`\bm{a} = (a_1, \ldots, a_k) \in V_k(q)` thì coder thực hiện:

.. math:: \bm{a} = (a_1, \ldots, a_n) \xrightarrow{\varphi} (a_1, \ldots, a_k, \bm{a} \cdot \bm{G}_0).

Lưu ý rằng không phải code nào cũng là systematic 
và do đó không chắc chắn tồn tại systematic coder.

.. prf:definition:: 
    :label: def-info-set

    Ta đánh số tọa độ các codeword trong :math:`[n, k]_q` code 
    từ :math:`1` tới :math:`n`. 
    
    **Tập thông tin** (hay **information set**, **информационное множество**) 
    :math:`\mathcal{I}` của code :math:`[n, k]_q` là tập con 
    của tập đánh số tọa độ, nghĩa là :math:`\mathcal{I} \subseteq \{ 1, \ldots, n \}`, 
    sao cho :math:`\lvert \mathcal{I} \rvert = k` và ma trận con :math:`\bm{G}_k` 
    kích thước :math:`k \times k` của ma trận sinh :math:`\bm{G}` khả nghịch.


Ma trận kiểm tra
-----------------

.. prf:definition:: 
    :label: def-parity-mat

    Nếu :math:`\mathcal{C}` là hạt nhân của ma trận :math:`\bm{H}`, tức là

    .. math:: \mathcal{C} = \ker(\bm{H}) = \{ \bm{v} \in \mathcal{C}: \bm{H} \bm{v}^\top = \bm{0} \},

    thì ta nói :math:`\bm{H}` là **ma trận kiểm tra 
    chẵn lẻ** (hay **parity-check matrix**).

Ta có thể thấy :math:`\bm{G} \bm{H}^\top = \bm{0}`.

.. prf:definition:: 
    :label: def-syndrom

    **Syndrome** :math:`S_{\bm{H}}(\bm{y})` của vector 
    :math:`\bm{y} \in V_n(q)` tương ứng với ma trận 
    parity-check :math:`\bm{H}` của :math:`[n, k]_q` code 
    :math:`\mathcal{C}` là vector cột 
    :math:`S_{\bm{H}}(\bm{y}) = \bm{H} \cdot \bm{y}^\top`. 
    
    Khi đó :math:`S_{\bm{H}}(\bm{y})` có độ dài 
    :math:`r = n - k` -- chính là redundancy ở trên.

.. prf:remark:: 
    :label: rmk-parity-mat

    Nếu :math:`\bm{H}_1` và :math:`\bm{H}_2` là hai ma trận 
    parity-check của code :math:`\mathcal{C}` thì 
    :math:`S_{\bm{H}_1}(\bm{y}) = \bm{A} \cdot S_{\bm{H}_2}(\bm{y})` 
    với :math:`\bm{A}` là ma trận khả nghịch thỏa mãn 
    :math:`\bm{H}_2 = \bm{A} \cdot \bm{H}_1`.


Linear code
-----------

Do :math:`[n]_q` code cũng là :math:`(n)_q` code nên 
ta cũng có định nghĩa phổ trọng số như :math:`(n)_q`:

.. prf:definition:: 
    :label: def-spec-lincode

    **Спектр весов** của :math:`[n]_q` code 
    :math:`\mathcal{C}` là vector :math:`(A_0, A_1, \ldots, A_n) \in \mathbb{Z}^{n+1}_{\geqslant 0}` 
    với :math:`A_i \geqslant 0` là số lượng vector có 
    trọng số bằng :math:`i` trong code.


Dual code (mã đối ngẫu) và kiểm tra chẵn lẻ (check-parity)
----------------------------------------------------------

.. prf:definition:: Dual code
    :label: def-dual-code

    **Dual code** (hay **mã đối ngẫu**, **дуальный код**) 
    của linear code :math:`\mathcal{C}` là code :math:`\mathcal{C}^\top` 
    được sinh bởi parity-check matrix :math:`\bm{H}` của code :math:`\mathcal{C}`.

.. prf:remark:: 
    :label: rmk-dual-code

    Dual code với :math:`[n, k]_q` code là :math:`[n, n-k]_q` code.

.. prf:remark:: 
    :label: rmk-code-T

    Với mọi code :math:`\mathcal{C}` ta có 
    :math:`(\mathcal{C}^\top)^\top = C`.

.. prf:remark:: 
    :label: rmk-sum-code

    Với mọi :math:`[n]_q` code :math:`\mathcal{C}` 
    và :math:`\mathcal{B}` thì ta có đẳng thức:

    .. math:: (\mathcal{C} + \mathcal{B})^\top = \mathcal{C}^\top \cap \mathcal{B}^\top.

    Trong đó :math:`\mathcal{C} + \mathcal{B} = \{ \bm{u} + \bm{v} : \bm{u} \in \mathcal{C}, \bm{v} \in \mathcal{B} \}` 
    là tổng của hai code :math:`\mathcal{C}` và :math:`\mathcal{B}`.

.. prf:definition:: 
    :label: def-inner-prod-code

    Với các vector :math:`\bm{x} = (x_1, \ldots, x_n)` và 
    :math:`\bm{y} = (y_1, \ldots, y_n)` trong :math:`V_n(q)` 
    ta định nghĩa **tích vô hướng** (hay **inner product**, 
    **dot product**, **скалярное произведение**) của hai vector là:

    .. math:: \langle \bm{x}, \bm{y} \rangle = x_1 y_1 + \ldots + x_n y_n \in \mathbb{F}_q.

.. prf:definition:: 
    :label: def-parity-vec

    Vector :math:`\bm{h} \in V_n(q)` được gọi là **parity-check** 
    (hay **проверка на чётность**) của :math:`[n]_q` code nếu 
    với mọi :math:`\bm{c} \in \mathcal{C}` ta có 
    :math:`\langle \bm{c}, \bm{h} \rangle = 0`, nói cách khác 
    vector :math:`\bm{h}` trực giao với mọi vector :math:`\bm{c} \in \mathcal{C}`.

.. prf:remark:: 
    :label: rmk-parity-matvec

    Dual code :math:`\mathcal{C}^\top` trùng với tập tất cả 
    parity-check vector của code :math:`\mathcal{C}`.
