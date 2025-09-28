Introduction
============

.. prf:definition:: Block code
    :label: def-block-code

    **Block code** :math:`(n)_q` là tập hợp 
    :math:`\mathcal{C}` bất kì chứa các vector độ dài 
    :math:`n` trên trường :math:`\mathbb{F}_q`.

.. prf:definition:: Codeword
    :label: def-codeword

    **Codeword** (hay **từ mã**) là bất kì vector nào trong block code 
    :math:`\mathcal{C}`.

.. prf:definition:: Lực lượng của code
    :label: def-card-code
    
    **Lực lượng** (hay **cardinality**, **мощность**) :math:`M` của block code 
    :math:`\mathcal{C}` là số lượng codeword trong :math:`\mathcal{C}`. 
    
    Kí hiệu :math:`M = \lvert C \rvert`.

.. prf:definition:: 
    :label: def-nm-code
    
    Block code :math:`\mathcal{C}` trên trường :math:`\mathbb{F}_q` 
    có độ dài :math:`n` và có lực lượng :math:`M` được gọi là 
    :math:`(n, M)_q` code.

.. prf:definition:: Độ dài của code
    :label: def-len-code
    
    Độ dài của :math:`(n)_q` code :math:`\mathcal{C}` là số :math:`n` 
    chỉ độ dài mỗi codeword (độ dài mỗi vector).

.. prf:definition:: Khoảng cách tối thiểu
    :label: def-min-dist

    **Khoảng cách tối thiểu** (hay **minimum distance**) 
    của code :math:`\mathcal{C}` là số :math:`d` chỉ 
    khoảng cách Hamming nhỏ nhất giữa hai codeword trong 
    code :math:`\mathcal{C}`:

    .. math:: 
        
        d = \min_{\bm{u}, \bm{v} \in \mathcal{C}, \bm{u} \neq \bm{v}} \rho(\bm{u}, \bm{v}) 
        = \min_{\bm{u}, \bm{v} \in \mathcal{C}, \bm{u} \neq \bm{v}} \mathrm{wt}(\bm{u} - \bm{v}).

Nhắc lại, khoảng cách Hamming của một vector là số phần tử khác :math:`0` trong vector đó:

.. math:: \mathrm{wt}(x_1, x_2, \ldots, x_n) = \lvert \{ x_i : x_i \neq 0 \} \rvert.

.. prf:definition:: 
    :label: def-nmd-code
    
    Block code :math:`\mathcal{C}` trên trường :math:`\mathbb{F}_q` 
    với độ dài :math:`n`, lực lượng :math:`M` và có khoảng cách 
    tối thiểu :math:`d` được gọi là :math:`(n, M, d)_q` code.

Thông tin ban đầu có thể được chia thành các đoạn 
độ dài :math:`k` và mỗi đoạn như vậy được encode 
thành một đoạn độ dài :math:`n`. 

Cụ thể hơn, **hàm encode** biến đổi một thông điệp là vector 
:math:`\bm{a}` độ dài :math:`k` thành codeword 
:math:`\bm{c} \in \mathcal{C}` với độ dài :math:`n`:

.. math:: \varphi: V_k(q) \to \mathcal{C}, \quad \varphi(\bm{a}) = \bm{c}.

Ánh xạ :math:`\varphi` cần là đơn ánh (one-to-one) vì chúng ta 
không muốn hai thông điệp độ dài :math:`k` cùng encode ra một 
codeword độ dài :math:`n` (khi decode chúng ta không biết sẽ 
ra thông điệp nào).

.. prf:lemma:: 
    :label: lem-nm-code
    
    Để :math:`(n, M)_q` code có thể encode được các thông điệp 
    độ dài :math:`k` thì điều kiện cần và đủ để tồn tại ánh xạ 
    :math:`\varphi` như trên là :math:`k \leqslant \lfloor \log_q M \rfloor`.

.. prf:definition:: Спектр весов
    :label: def-spec-code

    **Phổ trọng số** (hay **спектр весов**) của :math:`(n)_q` code 
    :math:`\mathcal{C}` là một vector các số nguyên không âm 
    :math:`(A_0, A_1, \ldots, A_n) \in \mathbb{Z}^{n+1}_{\geqslant 0}` 
    với :math:`A_i` là số lượng vector có trọng số Hamming bằng 
    :math:`i` trong code.
