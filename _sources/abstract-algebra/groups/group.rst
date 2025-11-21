Nhóm
====

Nhóm và nhóm con
----------------

.. prf:definition:: Nhóm
    :label: def-group
    
    Một tập hợp :math:`G` và toán tử hai ngôi 
    :math:`\star` trên :math:`G` tạo thành một 
    **nhóm** (hay **group**, **группа**) nếu:

    1. Tồn tại phần tử :math:`e \in G` sao cho với 
       mọi :math:`g \in G` thì 
       
    .. math:: \boxed{g \star e = e \star g = g.}
        
    Khi đó :math:`e` được gọi là **phần tử đơn vị** của :math:`G`.
    
    2. Với mọi :math:`g \in G`, tồn tại :math:`g' \in G` sao cho 
    
    .. math:: \boxed{g \star g' = g' \star g = e.}
        
    Khi đó :math:`g'` được gọi là **phần tử nghịch đảo** của :math:`g`.
    
    3. Tính kết hợp: với mọi :math:`a, b, c \in G` thì 
    
    .. math:: \boxed{a \star (b \star c) = (a \star b) \star c.}

.. prf:definition:: Nhóm Abel
    :label: def-abelian-group
    
    Nếu nhóm :math:`G` có thêm tính giao hoán, tức là với 
    mọi :math:`a, b \in G` thì :math:`a \star b = b \star a` 
    thì :math:`G` gọi là **nhóm giao hoán** (**commutative group**, 
    **коммутативная группа**) hoặc **nhóm Abel** (**abelian group**, 
    **абелева группа**).

.. prf:example:: 
    :label: exp-group-Z

    Xét tập hợp số nguyên :math:`\mathbb{Z}` và phép cộng 
    hai số nguyên.
    
    1. Phần tử đơn vị là :math:`0` vì với mọi 
       :math:`a \in \mathbb{Z}` thì :math:`a + 0 = 0 + a = a`.
    2. Với mọi :math:`a \in \mathbb{Z}`, phần tử nghịch đảo 
       là :math:`-a` vì :math:`a + (-a) = (-a) + a = 0`.
    3. Phép cộng số nguyên có tính kết hợp do đó thỏa mãn điều 
       kiện về tính kết hợp.

    Như vậy :math:`(\mathbb{Z}, +)` tạo thành nhóm. Lưu ý do 
    phép cộng hai số nguyên có tính giao hoán nên đây cũng là nhóm Abel.

.. prf:example:: 
    :label: exp-group-Q

    Xét tập hợp số hữu tỉ khác :math:`0` là :math:`\mathbb{Q}^*` 
    và phép nhân hai số hữu tỉ. Do :math:`a, b \in \mathbb{Q}^*` 
    nên tích :math:`a \cdot b` cũng khác :math:`0`, do đó cũng 
    thuộc :math:`\mathbb{Q}^*`.

    1. Phần tử đơn vị là :math:`1` vì với mọi :math:`a \in \mathbb{Q}^*` 
       thì :math:`a \cdot 1 = 1 \cdot a = a`.
    2. Với mọi :math:`a \in \mathbb{Q}^*`, phần tử nghịch đảo là 
       :math:`\dfrac{1}{a}` vì :math:`a \cdot \dfrac{1}{a} = \dfrac{1}{a} \cdot a = 1`.
    3. Phép nhân hai số hữu tỉ có tính kết hợp do đó thỏa mãn 
       điều kiện về tính kết hợp.

    Tương tự như nhóm :math:`(\mathbb{Z, +})`, nhóm 
    :math:`(\mathbb{Q}^*, \cdot)` cũng là nhóm Abel.

.. prf:definition:: Order của nhóm
    :label: def-group-order
    
    **Order** (hay **порядок**) của nhóm :math:`G` là lực lượng (hay 
    số phần tử, **carninality**, **мощность**) của nhóm đó 
    và kí hiệu là :math:`\lvert G \rvert`.

Đối với nhóm có vô hạn phần tử, ta quy ước order của nhóm 
bằng :math:`0`, ví dụ như với hai nhóm :math:`(\mathbb{Z}, +)` 
và :math:`(\mathbb{Q}^*, \cdot)` ở trên.

Nhóm con
--------

.. prf:definition:: Nhóm con
    :label: def-subgroup
    
    Cho nhóm :math:`(G, \star)`. Tập hợp :math:`H \subset G` được gọi là **nhóm con** (hay **subgroup**, **подгруппа**) của :math:`G` nếu với mọi :math:`a, b \in H` thì :math:`a \star b \in H`.
 
Nói cách khác, toán tử :math:`\star` đóng với các phần tử trong :math:`H`.

.. prf:example:: 
    :label: exp-subgroup

    Xét nhóm :math:`(\mathbb{Z}, +)` như trên. Ta xét tập con gồm các số chẵn của nó

    .. math:: 2\mathbb{Z} = \{ \ldots, -4, -2, 0, 2, 4, \ldots \}.

    Ta thấy rằng tổng hai số chẵn vẫn là số chẵn, nghĩa là phép cộng số nguyên đóng trên :math:`2\mathbb{Z}`.

    Do đó :math:`(2\mathbb{Z}, +)` là nhóm con của :math:`(\mathbb{Z}, +)`.

    Tổng quát, mọi tập hợp có dạng :math:`n \mathbb{Z}` đều là nhóm con của :math:`(\mathbb{Z}, +)`.

.. prf:theorem:: Định lý Lagrange
    :label: thm-lagrange-group
    
    Order của nhóm luôn chia hết order của một nhóm con bất kì của nó.

Nhóm vòng
---------

.. prf:definition:: Nhóm vòng
    :label: def-cycli-group
    
    Nhóm :math:`G` được gọi là **nhóm vòng** (hay **cyclic group**, **циклическая группа**) nếu tồn tại phần tử :math:`g \in G` mà mọi phần tử trong :math:`G` đều được biểu diễn dưới dạng :math:`g^i`. Khi đó ta kí hiệu :math:`G = \langle g \rangle` hoặc :math:`G = \{ g, g^1, \ldots, g^n \}`.

Thông thường ta quy ước :math:`g^n = g^0 = e`.

Đối với nhóm :math:`(\mathbb{Z}_n, +_n)` xác định phép cộng modulo :math:`n`, ta kí hiệu

.. math:: ig = \underbrace{g + g + \ldots + g}_{i \,\text{lần}}.

Ta viết

.. math:: G = \{ 1g, 2g, 3g, \ldots, ng \}.
    
Phần tử :math:`g` được gọi là **phần tử sinh** (hay **образующий элемент**) của nhóm vòng :math:`G`.

Như vậy, số lượng phần tử sinh của :math:`\mathbb{Z}_n` là :math:`\varphi(n)` với :math:`\varphi` là hàm Euler. Lúc này điều kiện để phần tử :math:`j` là phần tử sinh tương đương với

.. math:: \langle j \rangle = \mathbb{Z}_n \Longleftrightarrow (j, n) = 1.

.. prf:definition:: Elementary abelian group
    :label: def-elem-abel-group
    
    Nhóm vòng được gọi là **elementary abelian** (hay **примарная абелева группа**) nếu bậc của nhóm là số nguyên tố.

Coset
-----

.. prf:definition:: Coset, lớp kề
    :label: def-coset
    
    Cho nhóm :math:`G` và nhóm con :math:`H` của :math:`G`.

Coset trái của :math:`H` đối với phần tử :math:`g \in G` là tập hợp

.. math:: gH = \{gh : h \in H \}.

Tương tự, coset phải là tập hợp

.. math:: Hg = \{hg : h \in H \}.

Từ đây nếu không nói gì thêm ta ngầm hiểu là coset trái.

Ví dụ với nhóm con :math:`2\mathbb{Z}` của :math:`\mathbb{Z}`, ta thấy rằng:

1. Nếu :math:`g \in \mathbb{Z}` là lẻ thì khi cộng với bất kì phần tử nào của :math:`2\mathbb{Z}` ta nhận được số lẻ.
2. Nếu :math:`g \in \mathbb{Z}` là chẵn thì khi cộng với bất kì phần tử nào của :math:`2\mathbb{Z}` ta nhận được số chẵn.

Nói cách khác, coset của :math:`2\mathbb{Z}` chia tập :math:`\mathbb{Z}` thành

.. math:: 

    0 + 2\mathbb{Z} & = \{\ldots, -4, -2, 0, 2, 4, \ldots\}, \\
    1 + 2\mathbb{Z} & = \{\ldots, -3, -1, 1, 3, 5, \ldots \}.
    
Rõ ràng hai coset trên rời nhau.

.. prf:remark:: 
    :label: rmk-coset
    
    Hai coset bất kì hoặc rời nhau, hoặc trùng nhau.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Nếu hai coset rời nhau thì không có gì phải nói. Ta chứng minh trường hợp còn lại.

    Giả sử :math:`g_1 H \cap g_2 H \neq \emptyset`. Như vậy tồn tại :math:`h_1, h_2 \in H` mà :math:`g_1 h_1 = g_2 h_2`.

    Do :math:`h_1^{-1} \in H`, ta có :math:`g_1 = g_2 h_2 h_1^{-1}`, nghĩa là :math:`g_1 \in g_2 H`.

    Mà mọi phần tử trong :math:`g_1 H` có dạng :math:`g_1 h` nên :math:`g_1 h = g_2 h_2 h_1^{-1} h`. Do :math:`H` là nhóm con của :math:`G` nên :math:`h_2 h_1^{-1} h \in H`.

    Từ đó :math:`g_1 H \subseteq g_2 H`. Tương tự ta cũng có :math:`g_2 H \subseteq g_1 H`. Vậy :math:`g_1 H = g_2 H`.

Normal Subgroup
---------------

.. prf:definition:: Normal Subgroup
    :label: def-normal-subgroup

    Nhóm con :math:`H` của :math:`G` được gọi là **normal subgroup** (hay **нормальная подгруппа**, **nhóm con chuẩn tắc**) nếu với mọi :math:`g \in G` ta có coset trái trùng với coset phải.

    .. math:: gH = Hg \quad \text{ với mọi } g \in G.

Nếu :math:`H` là normal subgroup của :math:`G` ta kí hiệu :math:`H \triangleleft G`. Khi đó, với mọi :math:`a, b \in G` thì :math:`(a H) (b H) = (ab) H`.

.. prf:definition:: Quotient Group
    :label: def-quot-group
    
    Với nhóm :math:`G` và normal subgroup của nó là :math:`H`.

    **Quotient Group** (hay **nhóm thương**) được kí hiệu là :math:`G / H` và được định nghĩa là tập hợp các coset tương ứng với normal subgroup :math:`H`.

    .. math:: G / H = \{gH : g \in H \}.

    Ta thấy rằng điều này chỉ xảy ra nếu :math:`H` là normal subgroup.

Quotient Group còn được gọi là **Factor Group** (hay **nhóm nhân tử**).

.. prf:example:: 
    :label: exp-quot-group

    Với nhóm :math:`\mathbb{Z}` và normal subgroup của nó là :math:`2\mathbb{Z}`.

    Ta thấy
    
    .. math:: \mathbb{Z} / 2 \mathbb{Z} = \{0 + 2 \mathbb{Z}, 1 + 2 \mathbb{Z} \}.

Direct sum of modules
---------------------

Có hai dạng tổng là external và internal.

.. prf:definition:: External direct sum
    :label: def-ext-sum
    
    Giả sử ta có các nhóm :math:`(G_1, *)`, :math:`(G_2, \star)`, ..., :math:`(G_t, \circ)`. Khi đó externel direct sum của các nhóm :math:`G_1`, ..., :math:`G_t` là:

    .. math::

        G = G_1 \times G_2 \times G_t, \quad (G, \square).

Giả sử :math:`g = (g_1, g_2, \ldots, g_t) \in G` với :math:`g_i \in G_i`, và :math:`g' = (g'_1, g'_2, \ldots, g'_t) \in G` với :math:`g_i' \in G_i`. Khi đó:

.. math:: g \square g' = (g_1 * g'_1, g_2 \star g'_2, \ldots, g_t \circ g'_t).

.. prf:definition:: Internal direct sum
    :label: def-int-sum

    Giả sử ta có nhóm :math:`(G, \circ)` và các nhóm con :math:`G_1`, :math:`G_2`, ..., :math:`G_t` của :math:`G`. Khi đó internal direct sum là:

    1. Với mọi :math:`g \in G` thì :math:`g = g_1 \circ g_2 \circ \ldots \circ g_t` với :math:`g_i \in G_i`.
    2. Với mọi :math:`i, j` mà :math:`i \neq j`, :math:`1 \leqslant i, j \leqslant t` ta có

    .. math:: g_i \circ g_j = g_j \circ g_i

    với mọi :math:`g_i \in G_i` và :math:`g_j \in G_j`.

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
