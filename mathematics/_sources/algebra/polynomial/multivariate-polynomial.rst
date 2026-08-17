Đa thức nhiều biến
==================

Ta xét hàm số trên :math:`n` biến là :math:`x_1`, :math:`x_2`, ..., :math:`x_n`.

**Đơn thức** (hay **monomial**) là tích các lũy thừa của :math:`n` biến, có dạng :math:`x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}`, 
trong đó :math:`i_k \in \ZZ_{\geqslant 0}` với mọi :math:`k = \overline{1, n}`. Quy ước :math:`x_k^{0} = 1`.

Trên vành :math:`\KK` nào đó, một **hạng tử** (hay **term**) có dạng :math:`a x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}` với :math:`a \in \KK` và :math:`a \neq 0`. Khi đó :math:`a` được gọi là **hệ số** (hay **coefficient**).

Khi đó, **đa thức nhiều biến** (hay **multivariate polynomial**) của :math:`n` biến sẽ là tổng các hạng tử :math:`a x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}`.

Kí hiệu vành các đa thức :math:`n` biến với hệ số trong vành :math:`\KK` là :math:`\KK[x_1, x_2, \ldots, x_n]`.

Thứ tự đơn thức
---------------

Khi làm việc với các đa thức nhiều biến, ta quan tâm cách so sánh hai đơn thức bất kì.

Xét đơn thức :math:`x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}`. Đặt :math:`\bm{i} = (i_1, i_2, \ldots, i_n) \in \ZZ_{\geqslant 0}^n` là vector biểu diễn số mũ của đơn thức.

.. prf:definition:: Thứ tự từ điển
   :label: def-lex-order

   Vector :math:`\bm{i} = (i_1, i_2, \ldots, i_n)` được gọi là **lớn hơn** so với :math:`\bm{j} = (j_1, j_2, \ldots, j_n)` **theo thứ tự từ điển** (lexicographic) nếu tồn tại :math:`k`, :math:`1 \leqslant k \leqslant n`, sao cho

   .. math:: i_1 = j_1, \ldots, i_{k-1} = j_{k-1}, i_k > j_k.

Ta kí hiệu vector :math:`\bm{i}` lớn hơn vector :math:`\bm{j}` theo thứ tự từ điển là :math:`\bm{i} \succ_{\lex} \bm{j}`.

Các bạn hoàn toàn có thể sử dụng kí hiệu bé hơn :math:`\prec` để chỉ :math:`\bm{j} \prec_{\lex} \bm{i}`. Tuy nhiên chúng ta quan tâm tới vector lớn nhất trong một tập các vector và do đó, việc sử dụng dấu lớn hơn :math:`\succ` sẽ thuận tiện cho việc quan sát.

.. prf:definition:: Thứ tự bậc - từ điển
   :label: def-grlex-order

   Vector :math:`\bm{i} = (i_1, i_2, \ldots, i_n)` được gọi là **lớn hơn** so với :math:`\bm{j} = (j_1, j_2, \ldots, j_n)` **theo thứ tự bậc - từ điển** (graded-lexicographic) nếu:

   .. math:: \left(\sum_{k=1}^{n} i_k > \sum_{k=1}^{n} j_k\right), \text{hoặc} \ \left(\sum_{k=1}^{n} i_k = \sum_{k=1}^{n} j_k \ \text{và} \ \bm{i} \succ_{\lex} \bm{j}\right).

Ta kí hiệu vector :math:`\bm{i}` lớn hơn vector :math:`\bm{j}` theo thứ tự bậc - từ điển là :math:`\bm{i} \succ_{\grlex} \bm{j}`.

.. prf:remark:: 
   :label: rmk-mon-order

   Thứ tự từ điển, bậc - từ điển là quan hệ thứ tự toàn phần.

Ví dụ, xét các đơn thức ba biến là :math:`x^2 z` và :math:`y^2 z^2`. Ta chọn thứ tự của biến là :math:`x > y > z` nên khi viết đơn thức thì ta cần viết theo thứ tự đó.

Lúc này, vector biểu diễn số mũ của hai đơn thức lần lượt là :math:`(2, 0, 1)` và :math:`(0, 2, 2)`. Do đó nếu xét theo thứ tự từ điển thì :math:`x^2 z \succ_{\lex} y^2 z^2`, nhưng nếu xét theo thứ tự bậc - từ điển thì :math:`y^2 z^2 \succ_{\grlex} x^2 z`.

Hạng tử, hệ số, đơn thức dẫn đầu
--------------------------------

Đặt :math:`\bm{x} = (x_1, x_2, \ldots, x_n)` là vector biểu diễn :math:`n` biến, và :math:`\bm{i} = (i_1, i_2, \ldots, i_n)` là vector biểu diễn số mũ. Đặt :math:`\bm{x}^{\bm{i}} = x_1^{i_1} x_2^{i_2} \cdots x_n^{i_n}`.

Xét đa thức :math:`f` trên :math:`n` biến. Khi đó :math:`f` có dạng

.. math:: f(x_1, x_2, \ldots, x_n) = \sum c_{\bm{i}} \bm{x}^{\bm{i}},

với $c_{\bm{i}}$ là hệ số thuộc trường $\KK$.

Đặt :math:`\text{T}(f)` là tập tất cả hạng tử của đa thức $f$.
