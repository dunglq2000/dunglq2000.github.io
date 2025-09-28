Bài toán tương đương các linear code
=======================================


Hoán vị và tác động của chúng lên tập hợp
------------------------------------------

.. prf:definition:: Hoán vị
    :label: def-perm

    Xét :math:`N` là tập hợp có :math:`n` phần tử. Khi đó một 
    **hoán vị** (hay **permutation**, **постановка**) :math:`\sigma: N \to N` 
    là một song ánh từ :math:`N` tới :math:`N`. 
    
    Tập hợp tất cả hoán vị trên tập :math:`N` được kí hiệu là 
    :math:`\mathcal{S}_N`. Nếu :math:`N = \{ 1, 2, \ldots, n \}` 
    thì ta có thể viết :math:`\mathcal{S}_N = \mathcal{S}_n`.

Đặt :math:`\sigma \in \mathcal{S}_n` là một hoán vị 
trên tập :math:`\{ 1, \ldots, n \}`. Khi đó ta định 
nghĩa tác động của hoán vị :math:`\sigma` lên vector 
:math:`\bm{x} \in V_n(q)`. Giả sử vector 
:math:`\bm{x} = (x_1, \ldots, x_n) \in V_n(q)`, ta 
định nghĩa tác động của hoán vị :math:`\sigma` lên 
vector :math:`\bm{x}` như sau:

.. math:: \bm{x}^\sigma = (x_{\sigma(1)}, x_{\sigma(2)}, \ldots, x_{\sigma(n)}).

Có thể thấy tác động của :math:`\sigma` lên :math:`V_n(q)` 
là tuyến tính, nghĩa là với mọi :math:`\alpha, \beta \in \mathbb{F}_q` 
và với mọi vector :math:`\bm{x}, \bm{y} \in V_n(q)` ta có:

.. math:: (\alpha \cdot \bm{x} + \beta \cdot \bm{y})^\sigma = \alpha \cdot \bm{x}^\sigma + \beta \cdot \bm{y}^\sigma.

Nếu :math:`U \subseteq V_n(q)` thì kí hiệu :math:`U^\sigma` 
là tác động của hoán vị :math:`\sigma` lên mỗi vector trong 
:math:`U`, nghĩa là :math:`U^\sigma = \{ \bm{x}^\sigma : \bm{x} \in U \}`.

Do tính tuyến tính của tác động từ :math:`\mathcal{S}_n` lên 
:math:`V_n(q)`, nếu :math:`\mathcal{C}` là :math:`[n, k, d]_q` 
code thì :math:`\mathcal{C}^\sigma` cũng là :math:`[n, k, d]_q` 
code.

Mỗi hoán vị :math:`\sigma \in \mathcal{S}_n` có thể được viết 
thành dạng ma trận :math:`n \times n` là :math:`\bm{P}_\sigma = (p_{ij})`. 
Khi đó phần tử :math:`p_{ij} = 1` nếu :math:`\sigma(j) = i`, 
các vị trí còn lại bằng :math:`0`.

.. prf:example:: 
    :label: exp-perm

    Với hoán vị :math:`\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 1 & 5 & 3 & 2 \end{pmatrix}` 
    thì ma trận tương ứng là:

    .. math:: 
        
        \bm{P}_\sigma = \begin{pmatrix}
            0 & 1 & 0 & 0 & 0 \\
            0 & 0 & 0 & 0 & 1 \\
            0 & 0 & 0 & 1 & 0 \\
            1 & 0 & 0 & 0 & 0 \\
            0 & 0 & 1 & 0 & 0
        \end{pmatrix}.

    Khi đó tác động của :math:`\sigma` lên vector 
    :math:`\bm{x}` là :math:`\bm{x}^\sigma = \bm{x} \cdot \bm{P}_\sigma`.

    Như vậy, với mọi vector :math:`\bm{x} = (x_1, x_2, x_3, x_4, x_5)`, 
    dưới tác động của :math:`\sigma` bên trên ta có:

    .. math:: \bm{x}^\sigma = (x_{\sigma(1)}, x_{\sigma(2)}, x_{\sigma(3)}, x_{\sigma(4)}, x_{\sigma(5)}) = (x_4, x_1, x_5, x_3, x_2).

    Ta cũng thấy phép nhân vector :math:`\bm{x}` 
    với ma trận :math:`\bm{P}_\sigma` cho kết quả:

    .. math:: \bm{x} \cdot \bm{P}_\sigma = (x_4, x_1, x_5, x_3, x_2).


Mã tương đương và nhóm các tự đẳng cấu của linear code
------------------------------------------------------

.. prf:definition:: 
    :label: def-equiv-codes

    Hai :math:`[n]_q` code :math:`\mathcal{C}_1` và :math:`\mathcal{C}_2` 
    được gọi là **tương đương** (hay **tương đương hoán vị**, 
    **перестановочно эквивалентные**) nếu tồn tại một hoán vị 
    :math:`\sigma \in \mathcal{S}_n` sao cho 
    :math:`\mathcal{C}_1 = \mathcal{C}_2^\sigma`.

.. prf:definition:: 
    :label: def-equiv-mat-perm

    Hai ma trận :math:`\bm{G}_1` và :math:`\bm{G}_2` kích thước 
    :math:`k \times n` gọi là **tương đương hoán vị** nếu 
    tồn tại ma trận :math:`\bm{M}` cỡ :math:`k \times k` 
    và hoán vị :math:`\sigma \in \mathcal{S}_n` sao cho 
    :math:`\bm{M} \cdot \bm{G}_1 = \bm{G}_2 \cdot \sigma`.


Nhóm các tự đẳng cấu của code
------------------------------

.. prf:definition:: 
    :label: def-aut-code

    **Tự đẳng cấu** của :math:`(n)_q` code 
    :math:`\mathcal{C}` là hoán vị :math:`\sigma` 
    sao cho :math:`\mathcal{C} = \mathcal{C}^\sigma`. 
    Tập hợp tất cả tự đẳng cấu của code :math:`\mathcal{C}` 
    được kí hiệu là nhóm :math:`\mathrm{PAut}(\mathcal{C})` 
    và được gọi là **nhóm tự đẳng cấu hoán vị** 
    hoặc đơn giản hơn là **nhóm tự đẳng cấu** của 
    code :math:`\mathcal{C}`.


Bài toán về tính tương đương giữa các linear code nhị phân
----------------------------------------------------------

.. prf:definition:: 
    :label: def-prob-equiv-bin-lincode

    **Bài toán về tính tương đương giữa các linear code** 
    là bài toán nhận dạng tính chất tương đương giữa hai 
    linear code :math:`[n]_q` :math:`\mathcal{C}_1` và 
    :math:`\mathcal{C}_2` với ma trận sinh tương ứng là 
    :math:`\bm{G}_1` và :math:`\bm{G}_2`.

    **Input:** hai ma trận :math:`\bm{G}_1` 
    và :math:`\bm{G}_2` cỡ :math:`k \times n`.

    **Output:** hai ma trận :math:`\bm{G}_1` 
    và :math:`\bm{G}_2` có tương đương 
    hoán vị hay không.

Sau đây chúng ta xem xét code nhị phân, 
tức :math:`q = 2`.


Định lí về polynomial-time reduction của bài toán đẳng cấu đồ thị đến bài toán sự tương đương của code
-------------------------------------------------------------------------------------------------------

.. prf:definition:: 
    :label: def-mat-incidence

    **Ma trận kề** (hay **матрица инцидентности**) 
    là ma trận nhị phân :math:`\bm{D} = (d_{ev})` 
    cỡ :math:`\lvert E \rvert \times \lvert V \rvert`, 
    với :math:`d_{ev} = 1` nếu :math:`e = (u, v)` 
    với :math:`v` nào đó thuộc :math:`V`, nghĩa là 
    :math:`d_{ev} = 1` khi và chỉ khi trên đồ thị có 
    cạnh :math:`e` xuất phát từ đỉnh :math:`v`.

Định nghĩa về sự đẳng cấu của hai đồ thị đã được 
giới thiệu ở :prf:ref:`def-graph-isomorphism`, ở 
đây mình giới thiệu lại.

.. important:: Đồ thị đẳng cấu

    Hai đồ thị :math:`(E_1, V_1)` và :math:`(E_2, V_2)` 
    được gọi là **đẳng cấu** (hay **isomorphism**) nếu 
    tồn tại song ánh :math:`\varphi : V_1 \to V_2` sao cho 
    với mọi cặp đỉnh :math:`(u, v) \in E_1` thì cặp 
    :math:`(\varphi(u), \varphi(v)) \in E_2`.

.. prf:definition:: 
    :label: def-prob-graph-iso

    Bài toán xác định hai đồ thị, xác định bởi 
    ma trận kề, có đẳng cấu với nhau hay không.

    **Input:** hai ma trận nhị phân :math:`\bm{D}_1` 
    và :math:`\bm{D}_2` cỡ :math:`k \times n`.

    **Output:** có tồn tại hay không các hoán vị 
    :math:`\gamma \in \mathcal{S}_k` và 
    :math:`\sigma \in \mathcal{S}_n` sao cho 
    :math:`\bm{D}_1 = \gamma \cdot \bm{D}_2 \cdot \sigma`.
