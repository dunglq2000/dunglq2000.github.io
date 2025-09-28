Hàm Möbius
**********

August Ferdinand Möbius là nhà toán học người Đức, đóng góp nổi tiếng của ông là dải Möbius. Tuy nhiên ở đây chúng ta xem xét một hàm số học mang tên ông. 

Hàm Möbius đóng vai trò quan trọng trong việc tính các đại lượng liên quan tới số học.

Hàm Möbius
==========

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
====================

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
===========================

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
=====================

Nếu ta chọn :math:`f(n) = n` và :math:`g(n) = \varphi(n)` thì theo công thức nghịch đảo Möbius ta có

.. math:: \varphi(n) = \sum_{d \mid n} d \cdot \mu\left(\frac{n}{d}\right)
    
do ta đã biết :math:`\sum\limits_{d \mid n} \varphi(d) = n`.
