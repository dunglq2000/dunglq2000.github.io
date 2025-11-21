Các hàm số học quan trọng
*************************

Hàm Euler
=========

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
-------------------

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
-------------

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
------------------

.. prf:theorem:: Định lý Fermat nhỏ
    :label: thm-fermal-mini

    Cho số nguyên tố :math:`p`. Với mọi số nguyên :math:`a` thì

    .. math:: a^p \equiv a \pmod p.

    Khi :math:`(a, p) = 1` thì

    .. math:: \boxed{a^{p-1} \equiv 1 \pmod p.}

.. prf:remark:: 
    :label: rmk-euler-fermat

    Khi :math:`(a, p) = 1` thì định lý Fermat là hệ quả trực tiếp từ định lý Euler.

Hàm Möbius
==========

August Ferdinand Möbius là nhà toán học người Đức, đóng góp nổi tiếng của ông là dải Möbius. Tuy nhiên ở đây chúng ta xem xét một hàm số học mang tên ông. 

Hàm Möbius đóng vai trò quan trọng trong việc tính các đại lượng liên quan tới số học.

Hàm Möbius
----------

.. prf:definition:: Hàm Möbius
    :label: def-mobius-func

    Hàm Möbius của số nguyên dương :math:`n` được định nghĩa như sau:

    .. math:: 

        \mu (n) = \begin{cases}
            1, \quad & \text{nếu} \ n = 1 \\
            (-1)^k, \quad & \text{nếu} \ n = p_1 p_2 \ldots p_k \text{ với } p_i \ \text{là các số nguyên tố khác nhau} \\
            0, \quad & \text{trong các trường hợp còn lại}.
        \end{cases}

Điều này có nghĩa là, nếu :math:`n` là tích của các số nguyên tố bậc :math:`1` thì :math:`\mu (n) = (-1)^k` với :math:`k` là số lượng số nguyên tố trong tích. Như vậy, nếu tồn tại số nguyên tố :math:`p` sao cho :math:`p^2 \mid n` thì :math:`\mu(n) = 0`.

Tính chất hàm Möbius
--------------------

.. prf:property:: 
    :label: prop-mobius

    1. Nếu :math:`\gcd(n_1, n_2) = 1` thì :math:`\mu(n_1 \cdot n_2) = \mu(n_1) \cdot \mu(n_2)`.
    2. :math:`\sum\limits_{d \mid n} \mu(d) = 0` với :math:`n = p_1 p_2 \ldots p_k`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Với tính chất 1, ta dễ thấy rằng do :math:`n_1` và :math:`n_2` nguyên tố cùng nhau nên trong cách phân tích thừa số nguyên tố của chúng sẽ chứa các số nguyên tố khác nhau. 

    Khi đó :math:`\mu(n_1)` và :math:`\mu(n_2)` không bị phụ thuộc nhau và có thể tách thành phép nhân như trên.

    Với tính chất 2, chúng ta lần lượt chọn :math:`d` là tổ hợp của :math:`0`, :math:`1`, :math:`2`, ..., :math:`k` số nguyên tố:

    - nếu :math:`d = 1` thì :math:`\mu(d) = 1`;
    - nếu :math:`d = p_i` thì :math:`\mu(d) = (-1)^1 = -1` với :math:`i = \overline{1, k}`;
    - nếu :math:`d = p_i p_j` với :math:`i \neq j` thì :math:`\mu (d) = (-1)^2 = 1`;
    - tương tự như vậy, nếu :math:`d` là tích của :math:`t` số nguyên tố thì :math:`\mu (d) = (-1)^t`.

    Ở mỗi trường hợp trên, do :math:`d` là tổ hợp của :math:`t` số nguyên tố (:math:`0 \leqslant t \leqslant k`) nên số cách chọn số nguyên tố :math:`p_i` ở mỗi trường hợp là :math:`C^t_k`. Ta cộng tất cả chúng lại

    .. math:: \sum_{d \mid n} \mu(d) = 1 - C^1_k + C^2_k - \ldots + (-1)^k C^k_k = 0

    theo nhị thức Newton. Từ đó ta có điều phải chứng minh.

Công thức nghịch đảo Möbius
---------------------------

Giả sử ta có hai hàm :math:`f` và :math:`g` từ :math:`\mathbb{N}` tới :math:`\mathbb{Z}`. Khi đó hai cách biểu diễn sau là tương đương.

.. math:: 

    f(n) = \sum_{d \mid n} g(d) \Longleftrightarrow g(n) 
    = \sum_{d \mid n} f(d) \mu\left(\frac{n}{d}\right).

Nghĩa là nếu chúng ta có hai hàm số :math:`f` và :math:`g` thỏa phương trình đầu (biểu diễn :math:`f` theo :math:`g`) thì chúng ta cũng sẽ tìm được cách biểu diễn :math:`g` theo :math:`f`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Với :math:`d \mid n`, đặt :math:`d' = \dfrac{n}{d}`, suy ra :math:`d = \dfrac{n}{d'}`.

    Như vậy :math:`f(d) \cdot \mu\left(\dfrac{n}{d}\right) = f \left(\dfrac{n}{d'}\right) \cdot \mu(d')`.

    Ta lấy tổng lại thì

    .. math:: \sum_{d \mid n} f(d) \cdot \mu \left(\frac{n}{d}\right) = \sum_{d \mid n} f\left(\frac{n}{d'}\right) \cdot \mu(d') = \sum_{d \mid n} f\left(\frac{n}{d}\right) \cdot \mu(d).

    Ở đây lưu ý rằng nếu :math:`d` là ước của :math:`n` thì :math:`d' = \dfrac{n}{d}` cũng là ước của :math:`n`. Do đó ta hoàn toàn có thể thay thế :math:`d'` bởi :math:`d` trong tổng trên.

    Vì :math:`f(n) = \displaystyle{\sum_{d \mid n} g(d)}` nên

    .. math:: 
        :label: eq:mebius1

        \sum_{d \mid n} f\left(\frac{n}{d}\right) \cdot \mu(d) = \sum_{d \mid n} \mu(d) \sum_{d' \mid \frac{n}{d}} g(d').

    Dễ thấy rằng do :math:`d \mid n` và :math:`d' \mid \dfrac{n}{d}` nên tồn tại :math:`k`, :math:`l` sao cho :math:`kd = n` và :math:`ld' = \dfrac{n}{d}`. Khi đó :math:`n = ldd'` và :math:`kd = n`, suy ra :math:`d' \mid n` và :math:`d \mid \dfrac{n}{d'}`.

    Tương tự như trên, ta có thể thay thế :math:`d` bởi :math:`d'` và ngược lại, phương trình :eq:`eq:mebius1` tương đương:

    .. math:: \sum_{d' \mid n} g(d') \sum_{d \mid \frac{n}{d'}} \mu(d),

    mà :math:`\sum\limits_{a \mid p} \mu(a) = 0` nếu :math:`p \neq 1` và bằng :math:`1` với :math:`p = 1` (đã chứng minh ở trên) nên từ đây suy ra

    .. math:: 

        \sum_{d' \mid n} g(d') \sum_{d \mid \frac{n}{d'}} \mu(d)
        = \sum_{d' \mid n} g(d') \cdot 1 \,(\text{khi } n = d') = g(n).

Tương tự ta cũng có công thức nghịch đảo Möbius đối với phép nhân

.. math:: 
    
    f(n) = \prod_{d \mid n} g(d) \Longleftrightarrow 
    g(n) = \prod_{d \mid n} f(d)^{\mu\left(\frac{n}{d}\right)}.

Liên hệ với hàm Euler
---------------------

Nếu ta chọn :math:`f(n) = n` và :math:`g(n) = \varphi(n)` thì theo công thức nghịch đảo Möbius ta có

.. math:: \varphi(n) = \sum_{d \mid n} d \cdot \mu\left(\frac{n}{d}\right)
    
do ta đã biết :math:`\sum\limits_{d \mid n} \varphi(d) = n`.

.. raw:: html

   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2343650775986433"
     crossorigin="anonymous"></script>
   <!-- First Ads -->
   <ins class="adsbygoogle"
      style="display:block"
      data-ad-client="ca-pub-2343650775986433"
      data-ad-slot="4417625951"
      data-ad-format="auto"
      data-full-width-responsive="true"></ins>
   <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
   </script>
