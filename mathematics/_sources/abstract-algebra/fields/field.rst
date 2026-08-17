Trường
======

.. prf:definition:: Trường
   :label: def-field
   
   Cho tập hợp :math:`F` và hai toán tử hai ngôi trên :math:`F` là phép cộng :math:`+` và phép nhân :math:`\times`. Khi đó :math:`(F, +, \times)` là **trường** (hay **field**, **поля**) nếu

   1. :math:`(F, +, \times)` là vành giao hoán với đơn vị.
   2. Với mọi phần tử :math:`f \neq 0_F`, tồn tại nghịch đảo :math:`f^{-1}` của :math:`f` đối với phép nhân, nghĩa là
   
   .. math:: f \times f^{-1} = f^{-1} \times f = 1_F.

Nói cách khác, :math:`(F, \times)` là nhóm Abel. Trên trường ta thực hiện được bốn phép tính cộng, trừ, nhân, chia.

.. prf:example:: 
   :label: exp-field

   Các tập hợp sau với phép cộng và nhân là trường.

   1. Tập hợp số thực :math:`\mathbb{R}`.
   2. Tập hợp các số phức :math:`\mathbb{C}`.
   3. Tập hợp các số dạng :math:`a + b \sqrt{2}` với :math:`a, b \in \mathbb{Q}`.

Những trường trên được gọi là **trường vô hạn** vì có vô số phần tử.

Ngược lại, chúng ta cũng có các **trường hữu hạn**.

Trường hữu hạn
--------------

Trường hữu hạn modulo nguyên tố
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cho :math:`p` là số nguyên tố. Khi đó tập hợp các số dư khi chia cho :math:`p` cùng với phép cộng và nhân modulo :math:`p` tạo thành trường.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Xét tập hợp các số dư khi chia cho :math:`p` là
   
   .. math:: S = \{0, 1, \ldots, p-2, p-1\}.

   Ta thấy rằng với mọi :math:`a, b \in S` thì :math:`a + b \pmod p` và :math:`a \cdot b \pmod p` đều thuộc :math:`S`.

   1. Vì :math:`0 + a = a + 0 = a \pmod p` với mọi :math:`a \in S` nên :math:`0` là phần tử đơn vị của phép cộng.
   2. Với mọi :math:`a \in S`, ta có :math:`(p-a) + a = a + (p-a) \equiv 0 \pmod p` nên phần tử nghịch đảo của :math:`a` đối với phép cộng là :math:`p-a \in S`.
   3. Phép cộng modulo có tính kết hợp.
   4. Phép cộng modulo có tính giao hoán.

   Như vậy :math:`(S, +)` là nhóm Abel.

   Tiếp theo, ta thấy rằng phép cộng và nhân có tính phân phối trên modulo.

   Đồng thời phép nhân modulo cũng có tính kết hợp. Do đó :math:`(S, +, \cdot)` là vành.

   1. Phần tử đơn vị của phép nhân là :math:`1`.
   2. Phép nhân modulo có tính giao hoán.
   3. Do mọi phần tử thuộc :math:`S` đều nguyên tố cùng nhau với :math:`p` nên luôn tồn tại nghịch đảo của phần tử khác :math:`0` trong :math:`S`.

   Kết luận: :math:`(S, +, \cdot)` là trường.

Ta thường kí hiệu trường này là :math:`\mathrm{GF}(p)` (GF là viết tắt của Galois Field để tưởng nhớ người có đóng góp quan trọng trong lý thuyết nhóm).

Trường hữu hạn modulo đa thức
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Xét các đa thức với hệ số nguyên

.. math:: f(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_2 x^2 + a_1 x + a_0.

Ta thấy rằng phép cộng và nhân hai đa thức tạo thành một vành giao hoán với đơn vị là đa thức :math:`f(x) \equiv 1`.

Thêm nữa vành này có vô số phần tử. Ta cần một phương án để số phần tử là hữu hạn, và đồng thời là trường.

Với :math:`p` là số nguyên tố và :math:`n` là số nguyên dương. Mình xét các đa thức có bậc tối đa là :math:`n-1` với hệ số nằm trong tập hợp các số dư khi chia cho :math:`p`. Như vậy mình có :math:`p^n` đa thức như vậy.

.. prf:example:: 
   :label: exp-field-poly

   Với :math:`p = 3` và :math:`n = 2`. Khi đó các đa thức có thể có là

   .. math:: \{ 0, 1, 2, x, x+1, x+2, 2x, 2x+1, 2x+2 \}.

Tương tự với việc modulo cho một số nguyên tố, ở đây mình xét phép cộng và nhân trên modulo một đa thức tối giản (irreducible polynomial) có bậc :math:`n` (vì khi modulo một đa thức bậc bất kì cho đa thức bậc :math:`n` ta có đa thức bậc nhỏ hơn :math:`n`). 

Đồng thời hệ số của đa thức từ phép cộng và nhân cũng được modulo :math:`p` (nằm trong :math:`\mathrm{GF}(p)`).

Với trường hợp :math:`p = 3` và :math:`n = 2` ở trên mình có thể chọn đa thức modulo là :math:`m(x) = x^2 + 2x + 2`.

Sau đây là bảng phép cộng hai đa thức bậc nhỏ hơn :math:`2` trong modulo :math:`m(x)`.

.. only:: html

   .. table:: 
      :class: centered-table

      .. include:: tables/gf9-add.rst.inc

.. only:: latex

   .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|

   .. include:: tables/gf9-add.rst.inc

Tương tự, sau đây là bảng phép nhân hai đa thức bậc nhỏ hơn :math:`2` trong modulo :math:`m(x)`.

.. only:: html

   .. table:: 
      :class: centered-table

      .. include:: tables/gf9-mult.rst.inc

.. only:: latex

   .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|

   .. include:: tables/gf9-mult.rst.inc

Ta thấy rằng bảng phép nhân đối xứng qua đường chéo chính. Điều này chứng tỏ phép nhân có tính giao hoán. Thêm nữa ở mỗi hàng hoặc cột khác :math:`0` đều có :math:`9` phần tử khác nhau.

Phân tích :math:`x^p - x` và :math:`x^{p^n} - x` thành nhân tử
--------------------------------------------------------------

Tiếp theo chúng ta sẽ phân tích các đa thức :math:`x^p - x` và :math:`x^{p^n} - x` thành nhân tử với :math:`p` là số nguyên tố.

.. prf:theorem:: Phân tích :math:`x^p - x`
   :label: thm-xp-x

   Với :math:`p` là số nguyên tố, đa thức :math:`q(x) = x^p - x` trên :math:`\mathbb{F}_p` có phân tích là

   .. math:: q(x) = x^p - x = x (x - 1) (x - 2) \cdots (x - (p - 1)).

.. admonition:: Chứng minh
   :class: danger, dropdown

   Theo định lí Fermat nhỏ, :math:`a^p \equiv a \pmod{p}` với mọi :math:`a \in \mathbb{F}_p`. Nói cách khác với mọi :math:`a \in \mathbb{F}_p` ta có :math:`q(a) = a^p - a = 0` trên :math:`\mathbb{F}_p`, hay :math:`a` là nghiệm của :math:`q(x)`.

   Đa thức :math:`q(x)` có bậc là :math:`p` nên có tối đa :math:`p` nghiệm, và mọi phần tử :math:`a \in \mathbb{F}_p` đều là nghiệm, nên ta có điều phải chứng minh khi đồng nhất hệ số :math:`x^p` ở hai vế.

.. prf:theorem:: Phân tích :math:`x^{p^n} - x`
   :label: thm-xpn-x

   Với :math:`p` là số nguyên tố và :math:`n` là số nguyên dương bất kì, đa thức :math:`q(x) = x^{p^n} - x` trên :math:`\mathbb{F}_p` là tích của tất cả đa thức tối giản có bậc là ước của :math:`n`.

Để chứng minh định lí trên ta cần ba bổ đề:

#. Hàm số :math:`x^{p^n} - x` không có nhân tử bội (:prf:ref:`lem-coprime-derivative`).
#. Nếu một đa thức tối giản có bậc là ước của :math:`n` thì đa thức đó là ước của :math:`q(x)` (:prf:ref:`lem-deg-div-n`.
#. Ngoài ra, không có đa thức tối giản nào khác là ước của :math:`q(x)`.

.. prf:lemma:: 
   :label: lem-coprime-derivative

   Hàm số :math:`f(x)` không có nhân tử bội khi và chỉ khi nó nguyên tố cùng nhau với đạo hàm của nó.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Ta chứng minh mệnh đề đối: hàm số :math:`f(x)` có nhân tử bội khi và chỉ khi nó không nguyên tố cùng nhau với đạo hàm của nó.

   **Điều kiện đủ.** Với :math:`f(x)` có nhân tử bội, ta cần chứng minh :math:`\gcd(f(x), f'(x)) \neq 1`.

   Giả sử :math:`f(x) = [d(x)]^k \cdot g(x)` với :math:`d(x)` là đa thức tối giản có bậc thấp hơn :math:`f(x)` và :math:`k \geqslant 2`. Khi đó

   .. math:: 

      f'(x) = k \cdot [d(x)]^{k-1} \cdot d'(x) \cdot g(x) + [d(x)]^k \cdot g'(x) \\
      = [d(x)]^{k-1}[k \cdot d'(x) \cdot g(x) + d(x) \cdot g'(x)],

   nên suy ra :math:`[d(x)]^{k-1}` chia hết :math:`f'(x)`, mà :math:`k \geqslant 2` nên :math:`[d(x)]^{k-1} \neq 1`, hay :math:`\gcd(f(x), f'(x)) \neq 1`.

   **Điều kiện cần.** Giả sử :math:`\gcd(f(x), f'(x)) = d(x) \neq 1`, ta cần chứng minh :math:`f(x)` có nhân tử bội.

   Vì :math:`d(x)` chia hết :math:`f(x)` nên tồn tại :math:`g(x)` sao cho :math:`f(x) = d(x) \cdot g(x)`. Khi đó

   .. math:: f'(x) = d'(x) \cdot g(x) + d(x) \cdot g'(x),

   mà :math:`d(x)` cũng chia hết :math:`f'(x)` nên :math:`d(x)` chia hết :math:`d'(x) \cdot g(x)`. Ở đây :math:`d'(x)` có bậc thấp hơn :math:`d(x)` nên :math:`d(x)` không thể chia hết :math:`d'(x)`, suy ra :math:`d(x)` phải chia hết :math:`g(x)`.

   Như vậy :math:`g(x) = d(x) \cdot h(x)`, thay vào :math:`f(x)` ta có nhân tử bội :math:`[d(x)]^2`. Ta có điều phải chứng minh.

.. prf:lemma:: 
   :label: lem-deg-div-n

   Xét đa thức :math:`q(x) = x^{q^n} - x` trên :math:`\mathbb{F}_p`. Khi đó mọi đa thức tối giản có bậc là ước của :math:`n` thì chia hết cho :math:`q(x)`.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Giả sử :math:`s(x)` là đa thức tối giản bậc :math:`d` trên :math:`\mathbb{F}_p` sao cho :math:`n = ad` với :math:`a \in \mathbb{Z}`.

   Vì :math:`s(x)` là đa thức tối giản trên :math:`\mathbb{F}_p` nên nó xác định trường hữu hạn :math:`\mathbb{F}_{p^d}` có :math:`p^d` phần tử. Khi đó :math:`\mathbb{F}_{p^d}^*` là nhóm đối với phép nhân nên

   .. math:: x^{p^d - 1} \equiv 1 \bmod{s(x)} \Longleftrightarrow (x^{p^d - 1} - 1) \ \vdots \ s(x).

   Ta sử dụng bổ đề về tính chất của ước chung lớn nhất sau: với mọi :math:`a`, :math:`m`, :math:`n` ta đều có

   .. math:: \gcd(a^m - 1, a^n - 1) = a^{\gcd(m, n)} - 1.

   Thay :math:`a` thành :math:`x`, :math:`m` thành :math:`p^d - 1` và :math:`p^n - 1` ta có

   .. math:: 
      :label: eq-xpn-xpd-1

      \gcd(x^{p^d - 1} - 1, x^{p^n - 1} - 1) = x^{\gcd(p^d - 1, p^n - 1)} - 1.

   Vì :math:`n = ad` nên

   .. math:: p^n - 1 = \left(p^d\right)^a - 1 = (p^d - 1)[(p^d)^{a-1} + (p^d)^{a-2} + \cdots + (p^d) + 1],

   hay :math:`p^d - 1` là ước của :math:`p^n - 1`, suy ra :math:`\gcd(p^d - 1, p^n - 1) = p^d - 1`. Do đó từ :eq:`eq-xpn-xpd-1` suy ra

   .. math:: \gcd(x^{p^d - 1} - 1, x^{p^n - 1} - 1) = x^{p^d - 1} - 1,

   nói cách khác :math:`x^{p^d - 1} - 1` là ước của :math:`x^{p^n - 1} - 1`, và :math:`s(x)` là ước của :math:`x^{p^d - 1} - 1` từ chứng minh trên, nên suy ra :math:`s(x)` là ước của :math:`x^{p^n - 1} - 1` và

   .. math:: x^{p^n - 1} - 1 \equiv 0 \bmod{s(x)} \Longrightarrow x^{p^n} - x \equiv 0 \bmod{s(x)} \Longleftrightarrow (x^{p^n} - x) \ \vdots \ s(x).

   Ta có điều phải chứng minh.

.. prf:lemma:: 
   :label: lem-no-deg-div-n

   Xét đa thức :math:`q(x) = x^{q^n} - x` trên :math:`\mathbb{F}_p`. Khi đó mọi đa thức tối giản có bậc là không là ước của :math:`n` thì cũng không là ước của :math:`q(x)`.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Giả sử tồn tại đa thức :math:`s(x)` là ước của :math:`q(x)` nhưng có bậc không là ước của :math:`n` gọi là :math:`d`. Rõ ràng :math:`s(x) \neq x` vì đây là đa thức tối giản bậc :math:`1`, mà :math:`1` là ước của mọi số nguyên. Như vậy suy ra :math:`s(x)` là ước của :math:`x^{p^n - 1} - 1`.

   Tương tự bên trên, :math:`s(x)` xác định trường hữu hạn có :math:`p^d` phần tử, do đó với mọi phần tử :math:`a \in \mathbb{F}_{p^d}` ta có

   .. math:: a^{p^d - 1} \equiv 1 \bmod{s(x)}.

   Vì

   .. math:: s(x) \mid (x^{p^n - 1} - 1) \Longrightarrow a^{p^n - 1} \equiv 1 \bmod{s(x)} \ \text{với mọi} \ a \in \mathbb{F}_{p^d}.
   
   Như vậy, theo định lí Lagrange, order đối với phép nhân của bất kì phần tử nào trong :math:`\mathbb{F}_{p^d}` phải là ước của :math:`p^d - 1` và :math:`p^n - 1`, hay

   .. math:: a^{p^{\gcd(d, n)} - 1} \equiv 1 \bmod{s(x)} \ \text{với mọi} \ a \in \mathbb{F}_{p^d}.

   Điều này là bất khả thi vì đa thức :math:`q(t) = t^{p^{\gcd(d, n)} - 1} - 1` là đa thức bậc :math:`p^{\gcd(d, n) - 1}`, mà :math:`d` không là ước của :math:`n` nên :math:`\gcd(d, n) < d`, suy ra :math:`p^{\gcd(d, n) - 1} < p^d - 1` và :math:`q(t)` không thể có :math:`p^d - 1` nghiệm.

.. admonition:: Chứng minh (:prf:ref:`thm-xpn-x`)
   :class: danger, dropdown

   Với :math:`q(x) = x^{p^n} - x` ta có

   .. math:: q'(x) = p^n x^{p^n - 1} - 1,

   mà :math:`\mathbb{F}_p` có đặc số là :math:`p` nên ta rút gọn được :math:`p^n x^{p^n - 1}`, suy ra :math:`q(x)` và :math:`q'(x)` là hai đa thức nguyên tố cùng nhau. Như vậy :math:`q(x)` không có nhân tử bội.

   Ngoài ra, từ :prf:ref:`lem-deg-div-n` và :prf:ref:`lem-no-deg-div-n` ta có điều phải chứng minh.

Từ đây chúng ta có thể tính được số lượng đa thức tối giản bậc :math:`n` trên trường :math:`\mathbb{F}_p` bất kì.

.. prf:theorem:: 
   :label: thm-irr-poly-on-fp

   Số lượng đa thức tối giản bậc :math:`n` trên trường hữu hạn :math:`\mathbb{F}_p` với :math:`p` nguyên tố là

   .. math:: f_q(n) = \dfrac{1}{n} \sum_{d \mid n} \mu(n / d) p^{d},

   trong đó :math:`\mu(d)` là hàm Mobius của số nguyên :math:`d`.

.. admonition:: Chứng minh
   :class: danger, dropdown

   Ở trên ta đã chứng minh được tích tất cả đa thức tối giản có bậc là ước của :math:`n` trên :math:`\mathbb{F}_p` là :math:`x^{p^n} - x` (:prf:ref:`thm-xpn-x`). Xét hạng tử bậc cao nhất trong mỗi đa thức tối giản ta có

   .. math:: x^{p^n} = \prod_{d \mid n} \left(x^d\right)^{f_q(d)} = \prod_{d \mid n} x^{d f_q(d)}

   vì ta có :math:`f_q(d)` đa thức tối giản bậc :math:`d` với mọi :math:`d \mid n`. So sánh số mũ hai vế ta được

   .. math:: p^n = \sum_{d \mid n} d f_q(d).

   Theo công thức nghịch đảo Mobius (bài viết :ref:`sec_mobius_fucntion`) ta chọn :math:`f(n) = p^n` và :math:`g(n) = n f_q(n)` suy ra

   .. math:: f_q(n) = \dfrac{1}{n} \sum_{d \mid n} \mu(n / d) p^d.

