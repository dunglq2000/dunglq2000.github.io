Hàm Euler
*********

Đầu tiên chúng ta xem xét hệ thặng dư đầy đủ và hệ thặng dư thu gọn.

.. prf:definition:: Hệ thặng dư đầy đủ
    :label: def-full-residue

    Hệ thặng dư đầy đủ của số nguyên dương :math:`n` là tập :math:`\mathbb{Z}_n = \{ 0, 1, \ldots, n-1 \}`.

Nói cách khác, hệ thặng dư đầy đủ của :math:`n` là các số dư có thể có khi chia một số bất kì cho :math:`n`.

.. prf:definition:: Hệ thặng dư thu gọn
    :label: def-minimal-residue

    Hệ thặng dư thu gọn của số nguyên dương :math:`n` là tập các số :math:`a` mà :math:`1 \leqslant a < n` và :math:`(a, n) = 1`.

    .. math:: \mathbb{Z}_n^{\times} = \{ a : 1 \leqslant a < n \ \text{và} \ (a, n) = 1 \}.

.. prf:definition:: Phi hàm Euler
    :label: def-euler-phi

    Cho số nguyên dương :math:`n`. Số lượng các số dương nhỏ hơn :math:`n` và nguyên tố cùng nhau với :math:`n` được kí hiệu bởi :math:`\varphi(n)` và gọi là :math:`\varphi` hàm Euler.

Nói cách khác, :math:`\varphi` hàm Euler là số lượng phần tử trong tập :math:`\mathbb{Z}_n^{\times}`.

.. math:: \varphi(n) = \lvert \mathbb{Z}_n^{\times} \rvert.

.. prf:remark:: 
    :label: rmk-euler-phi
    
    Nếu :math:`n` là số nguyên tố thì :math:`\varphi(n) = n-1`.

Hàm Euler có ý nghĩa quan trọng trong lý thuyết số, công cụ giúp chúng ta giải các vấn đề về số mũ trong modulo.

Tính chất hàm Euler
===================

.. prf:remark:: 
    :label: rmk-property-euler-phi

    Với :math:`(m, n) = 1` thì :math:`\varphi(m n) = \varphi(m) \varphi(n)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta viết các số từ :math:`1` tới :math:`mn` thành bảng như sau

    .. only:: html

    .. table:: 
        :class: centered-table

        .. include:: table-euler.rst.inc

    .. only:: latex

        .. tabularcolumns:: |c|c|c|c|

        .. include:: table-euler.rst.inc

    Hàng :math:`r` gồm các phần tử dạng :math:`r m + k` với :math:`0 \leqslant r \leqslant n-1` và :math:`1 \leqslant k \leqslant m`. Ta thấy rằng nếu :math:`(rm + k, m) = 1` thì :math:`(k, m) = 1`.

    Do đó trên mỗi hàng có :math:`\varphi(m)` phần tử nguyên tố cùng nhau với :math:`m`.

    Tiếp theo, trên các hàng vừa tìm được, do :math:`(m, n) = 1` nên để :math:`(rm + k, n) = 1` thì :math:`(r, n) = 1`, nghĩa là có :math:`\varphi(n)` hàng như vậy.

    Tổng kết lại, ta có :math:`\varphi(m) \varphi(n)` phần tử trong bảng nguyên tố cùng nhau với :math:`mn`. Do đó có điều phải chứng minh.

Do tính chất này nên hàm Euler là hàm nhân tính.

.. prf:remark:: 
    :label: rmk-property-euler-phi-2
    
    Cho số nguyên dương :math:`n`. Khi đó
    
    .. math:: \sum_{d \mid n} \varphi(d) = n.

Để chứng minh tính chất trên ta cần công thức khai triển

.. math:: \prod_{i=1}^n (1 + x_i) = \sum_{\{ i_1, \ldots, i_k \} \subset I} x_{i_1} \cdots x_{i_k}

với :math:`I = \{ 1, \ldots, n \}`.

Khi :math:`n = 2` ta có biểu thức đơn giản là

.. math:: (1+x)(1+y) = 1+x+y+xy,

hoặc với :math:`n = 3` biến là

.. math:: (1+x)(1+y)(1+y) = 1 + x + y + z + xy + yz + yz + xyz.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử phân tích thừa số nguyên tố của :math:`n` là 

    .. math:: n = p_1^{e_1} p_2^{e_2} \ldots p_k^{e_k}.

    Khi đó mỗi ước :math:`d` của :math:`n` đều có dạng :math:`p_1^{f_1} p_2^{f_2} \cdots p_k^{f_k}` với :math:`0 \leqslant f_i \leqslant e_i`, :math:`i = 1, 2, \ldots, k`.

    Như vậy

    .. math:: 
    
        \sum_{d | n} \varphi(d) = \sum_{0 \leqslant f_i \leqslant e_i} \varphi\Big(p_1^{f_1} p_2^{f_2} \ldots p_k^{f_k}\Big)
                            = \varphi\Big(p_1^{f_1}\Big) \varphi\Big(p_2^{f_2}\Big) \ldots \varphi\Big(p_k^{f_k}\Big)

    Sử dụng công thức khai triển trên cho :math:`k` biến ở trên thì biểu thức tương đương với

    .. math::  
        
        \sum_{0 \leqslant f_i \leqslant e_i} \varphi\left(p_1^{f_1}\right) \varphi\left(p_2^{f_2}\right) \ldots
        \varphi\left(p_k^{f_k}\right) = & (1 + \varphi(p_1) + \varphi(p_1^2) + \ldots + \varphi(p_1^{e_1})) \\
        \times & (1 + \varphi(p_2) + \varphi(p_2^2) + \ldots + \varphi(p_2^{e_2})) \\
        \times & \ldots \\
        \times & (1 + \varphi(p_k) + \varphi(p_k^2) + \ldots + \varphi(p_k^{e_k})).

    Ở đây ta rút gọn dễ dàng với :math:`i = 1, 2, \ldots, k`:

    .. math:: 
    
        & 1 + \varphi(p_i) + \varphi(p_i^2) + \ldots + \varphi(p_i^{e_i}) \\
        = & 1 + p_i - 1 + p_i^2 - p_i + \ldots + p_i^{e_i} - p_i^{e_i-1} \\
        = & p_i^{e_i}.
        
    Như vậy mỗi tổng :math:`1 + \varphi(p_i) + \cdots` bằng chính :math:`p_i^{e_i}`. Nhân chúng lại với nhau ta có lại :math:`n`.

Định lý Euler
=============

.. prf:theorem:: Định lý Euler
    :label: thm-euler

    Cho số nguyên dương :math:`n`. Với mọi số nguyên :math:`a` mà :math:`(a, n) = 1` thì

    .. math:: \boxed{a^{\varphi(n)} \equiv 1 \pmod n.}

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử :math:`S = \{ a_1, a_2, \ldots, a_{\varphi(n)} \}` là hệ thặng dư thu gọn của :math:`n`. Ta sẽ chứng minh rằng nếu :math:`a` là số sao cho :math:`(a, n) = 1` thì tập hợp

    .. math:: \{ a a_1 \pmod n, a a_2 \pmod n, \ldots, a a_{\varphi(n)} \pmod n \}

    là hoán vị của tập :math:`S`.

    Thật vậy, giả sử :math:`a a_i \equiv a a_j \pmod n` với :math:`1 \leqslant i, j \leqslant \varphi(n)` và :math:`i \neq j`.

    Do :math:`(a, n) = 1` nên tồn tại nghịch đảo :math:`a' \pmod n` của :math:`a`. Nhân :math:`a'` cho hai vế ta còn :math:`a_i \equiv a_j \pmod n`.

    Nói cách khác, nếu :math:`a_i \not\equiv a_j \pmod n` thì :math:`a a_i \not\equiv a a_j \pmod n`, suy ra tập

    .. math:: \{ a a_1, a a_2, \ldots, a a_{\varphi(n)} \}

    là hoán vị của :math:`S`.

    Ta nhân tất cả phần tử của :math:`S` thì sẽ bằng tích phần tử của tập trên

    .. math:: a a_1 \cdot a a_2 \ldots a a_{\varphi(n)} \equiv a_1 \cdot a_2 \ldots a_{\varphi(n)} \pmod n.

    Đặt :math:`I = a_1 \cdot a_2 \cdots a_{\varphi(n)}` thì phương trình trên tương đương với

    .. math:: a^{\varphi(n)} \cdot I \equiv I \pmod n,

    mà :math:`(I, n) = 1` do là tích các số nguyên tố cùng nhau với :math:`n` nên rút gọn hai vế ta được

    .. math:: a^{\varphi(n)} \equiv 1 \pmod n.

    Ta có điều phải chứng minh.

Định lý Fermat nhỏ
==================

.. prf:theorem:: Định lý Fermat nhỏ
    :label: thm-fermal-mini

    Cho số nguyên tố :math:`p`. Với mọi số nguyên :math:`a` thì

    .. math:: a^p \equiv a \pmod p.

    Khi :math:`(a, p) = 1` thì

    .. math:: \boxed{a^{p-1} \equiv 1 \pmod p.}

.. prf:remark:: 
    :label: rmk-euler-fermat

    Khi :math:`(a, p) = 1` thì định lý Fermat là hệ quả trực tiếp từ định lý Euler.
