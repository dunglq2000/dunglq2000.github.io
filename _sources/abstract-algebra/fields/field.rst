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

        .. include:: gf9-add.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|

    .. include:: gf9-add.rst.inc

Tương tự, sau đây là bảng phép nhân hai đa thức bậc nhỏ hơn :math:`2` trong modulo :math:`m(x)`.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: gf9-mult.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|

    .. include:: gf9-mult.rst.inc

Ta thấy rằng bảng phép nhân đối xứng qua đường chéo chính. Điều này chứng tỏ phép nhân có tính giao hoán. Thêm nữa ở mỗi hàng hoặc cột khác :math:`0` đều có :math:`9` phần tử khác nhau.

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
