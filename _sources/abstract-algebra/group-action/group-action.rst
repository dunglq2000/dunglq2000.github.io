Tác động nhóm
=============

Tác động nhóm (Group Action) cho phép chúng ta đếm 
những cấu hình tổ hợp mà việc vét cạn rồi loại bỏ 
sẽ tốn nhiều công sức cũng như sai sót.

Cho tập hợp :math:`M` và nhóm :math:`G`. Ta nói 
:math:`G` **tác động trái** lên :math:`M` với ánh xạ:

.. math:: \alpha: G \times M \rightarrow M

thỏa mãn hai tiên đề sau:

- identity: :math:`\alpha (e, m) = m` với mọi 
  :math:`m \in M` và :math:`e` là phần tử đơn vị của :math:`G`;
- compatibility: :math:`\alpha (g, \alpha (h, m)) = \alpha (g h, x)`.

Ta thường kí hiệu :math:`\alpha (g, m)` bởi :math:`g(m)` 
hay thậm chí đơn giản hơn là :math:`gm`. Kí hiệu :math:`gm` 
sẽ được sử dụng từ đây về sau.

Khi đó hai tiên đề trên tương đương với:

- identity: :math:`e m = m` với mọi :math:`m \in M`;
- compatibility: :math:`g(hm) = (gh) m` với mọi 
  :math:`m \in M` và :math:`g, h \in G`.

.. prf:definition:: Nhóm con ổn định
    :label: def-stabilizer
    
    Với phần tử :math:`m \in M` cho trước, tập hợp các phần 
    tử :math:`g \in G` mà :math:`gm = m` được gọi là **nhóm 
    con ổn định** (hay **stabilizer**) của nhóm :math:`G`. 
    Ta kí hiệu

    .. math:: G_m = \{ g \in G : gm = m \}.

.. prf:definition:: Quỹ đạo
    :label: def-orbit
    
    **Quỹ đạo** (hay **orbit**) của phần tử :math:`m \in M` là tập hợp

    .. math:: G(m) = \{gm : g \in G\}.

.. prf:remark:: 
    :label: rmk-orbit
    
    Hai orbit của hai phần tử bất kì hoặc rời nhau, hoặc trùng nhau.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử ta có :math:`m_1, m_2 \in M` mà 
    :math:`G(m_1) \cap G(m_2) \neq \emptyset`.

    Khi đó tồn tại :math:`g_1, g_2 \in G` để 
    :math:`g_1 m_1 = g_2 m_2`, suy ra :math:`m_1 = g_1^{-1} g_2 m_2`.

    Thêm nữa, mọi phần tử trong :math:`G(m_1)` có dạng 
    :math:`g m_1` nên :math:`g m_1 = g g_1^{-1} g_2 m_2`, 
    suy ra :math:`G(m_1) \subseteq G(m_2)`.

    Chứng minh tương tự ta cũng có :math:`G(m_2) \subseteq G(m_1)` 
    nên :math:`G(m_1) \equiv G(m_2)`.

.. prf:remark:: 
    :label: rmk-union-orbits

    Tập hợp :math:`M` là giao của các orbit rời nhau. Giả sử 
    ta có :math:`t` orbit rời nhau :math:`G(m_1)`, :math:`G(m_2)`, 
    ..., :math:`G(m_t)` thì

    .. math:: M = G(m_1) \cup G(m_2) \cup \ldots \cup G(m_t).

.. prf:example:: 
    :label: exp-orbit

    Cho nhóm :math:`\mathcal{S}_3` có :math:`6` phần tử 
    :math:`(1)(2)(3)`, :math:`(1)(2,3)`, :math:`(2)(1,3)`, 
    :math:`(3)(1,2)`, :math:`(1,2,3)`, :math:`(1,3,2)`.

    Xét tập hợp :math:`M = \{1, 2, 3\}`. Khi đó, xét 
    từng hoán vị trên, ta có:

    .. math:: G_1 = \{ (1)(2)(3), (1)(2,3) \}

    và

    .. math:: G(1) = \{ 1, 2, 3 \}.

Ta nhận thấy :math:`G(1) = G(2) = G(3)`, và 
:math:`\lvert G \rvert = 6 = \lvert G_1 \rvert \cdot \lvert G(1) \rvert`.

Hay nói cách khác, :math:`\lvert G(m) \rvert = [G: G_m]` 
với :math:`G_m` là stabilizer của phần tử :math:`m` và 
:math:`[G: G_m]` là subgroup index của :math:`G_m \subset G`, 
và bằng :math:`\dfrac{\lvert G \rvert}{\lvert G_m \rvert}` 
nếu là nhóm hữu hạn.

.. prf:definition:: 
    :label: def-relate-under-action

    Hai phần tử :math:`m, n \in M` được gọi là có quan hệ 
    với nhau dưới tác động của nhóm :math:`G` nếu tồn tại 
    phần tử :math:`g \in G` sao cho :math:`m = g n`.

    Ta kí hiệu là :math:`m \tilde{G} n`.

.. prf:remark:: 
    :label: rmk-relate-under-action
    
    Quan hệ được định nghĩa như trên là quan hệ tương đương.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh một quan hệ là tương đương, ta cần chứng 
    minh tính phản xạ, đối xứng và bắc cầu.

    Đối với tính phản xạ, mọi vector đều có quan hệ với chính 
    nó qua phần tử đơn vị :math:`e \in G`.

    Đối với tính đối xứng, nếu :math:`m` có quan hệ với :math:`n` 
    thì tồn tại :math:`g \in G` sao cho :math:`m = gn`. Theo tính 
    chất nhóm thì tồn tại phần tử :math:`g^{-1}` là nghịch đảo của 
    :math:`g` trong :math:`G`. Do đó :math:`g^{-1} m = n`. Nói 
    cách khác :math:`n` cũng có quan hệ với :math:`m`. Như 
    vậy ta có tính đối xứng.

    Đối với tính bắc cầu, nếu :math:`m` có quan hệ với :math:`n` 
    thì tồn tại :math:`g_1 \in G` sao cho :math:`m = g_1 n`. 
    Tiếp theo, nếu :math:`n` có quan hệ với :math:`p` thì tồn 
    tại :math:`g_2 \in G` sao cho :math:`n = g_2 p`, suy ra
    
    .. math:: m = g_1 n = g_1 (g_2 p) = (g_1 g_2) p.
        
    Do :math:`g_1, g_2 \in G` nên :math:`g_1 g_2 \in G`. 
    Như vậy :math:`m` cũng có quan hệ với :math:`p` nên 
    quan hệ có tính bắc cầu.

    Vậy quan hệ được định nghĩa như trên là quan hệ tương đương.

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
