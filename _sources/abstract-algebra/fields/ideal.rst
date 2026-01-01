Ideal
=====

.. prf:definition:: Ideal
   :label: def-ideal

   Xét vành :math:`(R, +, \times)`. Một tập con :math:`I` của :math:`R` được gọi là **ideal trái** (hay **left ideal**, **левый идеал**) nếu:

   1. :math:`(I, +)` là nhóm con của :math:`(R, +)`.
   2. Với mọi :math:`r \in R`, với mọi :math:`x \in I` thì :math:`rx \in I`.

Ta định nghĩa tương tự với ideal phải, khi đó :math:`xr \in I`. Từ đây về sau nếu không nói gì thêm nghĩa là mình xét ideal trái.

.. prf:definition:: Principal Ideal
   :label: def-principal-ideal
   
   Nếu :math:`I = \langle a \rangle` với :math:`a` là phần tử nào đó trong :math:`R` thì :math:`I` được gọi là **principal ideal** (hay **ideal chính**, **главный идеал**).

Nói cách khác, nếu có một phần tử trong :math:`R` "sinh" ra được :math:`I` thì :math:`I` là principal.

.. prf:definition:: Maximal Ideal
   :label: def-maximal-ideal
   
   Nếu :math:`I` là một ideal của :math:`R` và không tồn tại tập con :math:`I'` mà :math:`I \subset I' \subset R` (tập con thực thụ) thì :math:`I` được gọi là **maximal ideal** (hay **максимальный идеал**).

.. prf:remark:: 
   :label: rmk-principal-ideal
   
   Xét vành số nguyên :math:`\mathbb{Z}`. Khi đó mọi ideal của :math:`\mathbb{Z}` đều là principal.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Giả sử ideal :math:`I` của :math:`\mathbb{Z}` có phần tử dương nhỏ nhất là :math:`n`.

   Theo định nghĩa của ideal thì với mọi :math:`q \in \mathbb{Z}` ta có  :math:`qn \in I`.

   Nếu phần tử :math:`a \in I`, theo phép chia Euclid ta có :math:`a = qn + r` với :math:`0 \leqslant r < n`, mà :math:`a \in I` và :math:`qn \in I` nên :math:`r = a - qn \in I`.

   Tuy nhiên phần tử dương nhỏ nhất thuộc :math:`I` là :math:`n`, do đó :math:`r = 0`.

   Nói cách khác mọi phần tử :math:`a \in I` đều có dạng :math:`qn` với :math:`q \in \mathbb{Z}`.

   Vậy mọi ideal đều là principal.

Với mọi số nguyên dương :math:`n` cố định, principal ideal có dạng

.. math:: n \mathbb{Z} = \{ \ldots, -3n, -2n, -n, 0, n, 2n, 3n, \ldots \}.

Khi đó, dễ thấy :math:`n \mathbb{Z}` là nhóm giao hoán với phần tử trung hòa :math:`0`, phần tử nghịch đảo của :math:`kn` là :math:`-kn` với :math:`k \in \mathbb{Z}`. Ngoài ra, mọi phần tử của :math:`n\mathbb{Z}` có dạng :math:`kn` với :math:`k \in \mathbb{Z}`, nên với mọi :math:`\alpha \in \mathbb{Z}` thì :math:`\alpha \cdot kn = (\alpha k) n` thuộc :math:`n \mathbb{Z}`. Do đó :math:`n\mathbb{Z}` là principal ideal với mọi số nguyên dương :math:`n` cố định.

.. prf:remark:: 
   :label: rmk-maximal-ideal
   
   Ideal :math:`I` của :math:`\mathbb{Z}` là maximal khi và chỉ khi :math:`I = n\mathbb{Z}` với :math:`n` là số nguyên tố.

.. admonition:: Chứng minh
   :class: danger, dropdown

   **Điều kiện cần.** Khi :math:`n` là số nguyên tố, ta cần chứng minh :math:`n\mathbb{Z}` là maximal ideal. Sử dụng phản chứng, ta giả sử :math:`n\mathbb{Z}` không là maximal ideal. Lúc này tồn tại tập :math:`n_1 \mathbb{Z}` sao cho :math:`n\mathbb{Z} \subset n_1 \mathbb{Z} \subset \mathbb{Z}` với :math:`1 < n_1 < n`.

   Vì :math:`n_1 < n` nên tồn tại phép chia Euclid :math:`n = q n_1 + r` với :math:`0 \leqslant r < n_1`, do đó phần tử của :math:`n\mathbb{Z}` sẽ có dạng :math:`kn = k q n_1 + k r` với :math:`k \in \mathbb{Z}`.

   Tuy nhiên, vì :math:`n\mathbb{Z} \subset n_1\mathbb{Z}`, mà mọi phần tử của :math:`n_1\mathbb{Z}` đều chia hết cho :math:`n_1`, nên suy ra :math:`kn \in n\mathbb{Z}` cũng phải chia hết cho :math:`n_1` với mọi :math:`k \in \mathbb{Z}`. Điều này chỉ xảy ra khi và chỉ khi :math:`n` chia hết cho :math:`n_1` và do đó :math:`n` là hợp số, mâu thuẫn với giả thiết.

   **Điều kiện đủ.** Với :math:`I` là maximal ideal của :math:`\mathbb{Z}`, ta cần chứng minh :math:`n` là số nguyên tố. Sử dụng phản chứng, ta giả sử :math:`n` là hợp số. Khi đó :math:`n = n_1 n_2` với :math:`n_1 \geqslant n_2 > 1`.

   Khi đó :math:`n \mathbb{Z} \subset n_1 \mathbb{Z} \subset \mathbb{Z}`, suy ra ideal không phải maximal. Ta có điều phải chứng minh.
    
.. prf:theorem:: 
   :label: thm-max-ideal-field

   Gọi :math:`R` là vành giao hoán với đơn vị. Khi đó, nếu :math:`I` là ideal của :math:`R` thì :math:`R / I` là trường khi và chỉ khi :math:`I` là maximal ideal.

.. admonition:: Chứng minh
   :class: danger, dropdown

   **Điều kiện cần.** Ta có :math:`I` là maximal ideal. Ta thấy rằng :math:`a + I \neq 0` khi và chỉ khi :math:`a \not\in I`, vì nếu :math:`a \in I` thì tồn tại :math:`-a \in I` và kéo theo :math:`a + I = 0`. Theo định nghĩa vành thì :math:`a R` cũng là ideal nên :math:`I + a R` là ideal, mà :math:`a \not\in I` và :math:`a \in I + a R` nên suy ra :math:`I \subset I + a R`.
   
   Ta lại có :math:`I` là maximal nên :math:`I + aR = R`, do đó tồn tại :math:`n \in I` và :math:`b \in R` sao cho :math:`n + ab = 1`. Tóm lại là tồn tại nghịch đảo của phép nhân, do đó :math:`R / I` là trường.

   **Điều kiện đủ.** Với :math:`R / I` là trường. Ta giả sử :math:`I` không là maximal ideal. Khi đó tồn tại :math:`I'` sao cho :math:`I \subset I' \subset R`.

   Khi đó tồn tại phần tử :math:`a \in I'` và :math:`a \not\in I` mà :math:`a + I \neq 0`. Do đó :math:`(a + I) (b + I) = 1 + I`, suy ra tồn tại :math:`n \in I \subset I'` sao cho :math:`a b = 1 + n`. Vì :math:`a, b \in I'` nên :math:`1 \in I'`, từ đó :math:`1 \in R` nên :math:`I'` không phải maximal.

.. prf:example:: 
   :label: exp-max-ideal-field
   
   Xét tập hợp :math:`\mathbb{Z}` là vành giao hoán với đơn vị. Nếu :math:`n` là số nguyên tố thì :math:`n \mathbb{Z}` là maximal ideal (đã chứng minh ở trên).
   
   Khi đó tập :math:`\mathbb{Z} / n\mathbb{Z}` là trường hữu hạn modulo nguyên tố gồm các phần tử :math:`0`, :math:`1`, ..., :math:`p-1`.

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
