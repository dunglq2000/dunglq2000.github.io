Tích chập Dirichlet
*******************

Tích chập Dirichlet
===================

Hàm số học (arithmetic function) là hàm xác định trên tập số tự nhiên và cho ảnh trong tập số phức.

.. prf:definition:: Tích chập Dirichlet
    :label: def-dirichlet-convolution

    **Tích chập Dirichlet** (hay **Dirichlet convolution**, **свёртка Дирихле**) của hai hàm số học :math:`f` và :math:`g` là một hàm số học :math:`f * g` được định nghĩa bởi

    .. math:: (f * g)(n) = \sum_{d \mid n} f(d) \ g\left(\frac{n}{d}\right) = \sum_{ab = n} f(a) \ g(b).

    Ở đây ta lấy tổng chạy theo tất cả các ước dương :math:`d` của tham số :math:`n`, hoặc tất cả cặp :math:`(a, b)` có tích bằng :math:`n`.

Dễ thấy phép cộng hai hàm số học

.. math:: (f + g)(n) = f(n) + g(n)

tạo thành một nhóm với phần tử trung hòa là hàm không :math:`\bm{0}(n) = 0` với mọi :math:`n`. Ngoài ra ta định nghĩa thêm hàm

.. math:: 

    \delta(n) = \begin{cases}
        1, & \ \text{nếu} \ n = 1, \\
        0, & \ \text{nếu} \ n \neq 1.
    \end{cases}

và hàm đồng nhất :math:`\mathsf{Id}(n) = n`.

Khi đó, tích chập Dirichlet có các tính chất sau:

- tính kết hợp: :math:`(f * g) * h = f * (g * h)`;
- tính giao hoán: :math:`f * g = g * f`;
- tính phân phối với phép cộng: :math:`f * (g + h) = f * g + f * h`;
- phần tử đơn vị là :math:`\delta(n)` vì :math:`f * \delta = \delta * f = f`.

Như vậy, nếu gọi :math:`F` là tập hợp các hàm số học với phép cộng như trên và tích chập Dirichlet thì :math:`F` là một miền nguyên. Với các điều kiện ở trên, :math:`F` là vành giao hoán với đơn vị, và khi :math:`f, g \neq 0` thì :math:`f * g \neq 0` nên :math:`F` là miền nguyên. Lúc này :math:`F` còn được gọi là **vành Dirichlet**.

.. prf:definition:: Hàm nhân tính
    :label: def-mult-func

    Hàm số học :math:`f(n)` được gọi là hàm **nhân tính** (multiplicative) nếu :math:`f(1) = 1` và với mọi :math:`a` và :math:`b` nguyên tố cùng nhau thì :math:`f(a) f(b) = f(ab)`.

.. prf:definition:: Hàm nhân tính hoàn toàn
    :label: def-completely-mult-func

    Nếu hàm số học :math:`f(n)` thỏa :math:`f(ab) = f(a) f(b)` với mọi :math:`a` và :math:`b` (không nhất thiết nguyên tố cùng nhau) thì được gọi là hàm **nhân tính hoàn toàn** (completely multiplicative).

Mặc dù :math:`F` là vành giao hoán với đơn vị nhưng :math:`F` không phải là trường vì nghịch đảo của phép nhân không nhất thiết tồn tại.

Hàm số học có nghịch đảo Dirichlet khi và chỉ khi :math:`f(1) \neq 0`. Các hàm như vậy tạo thành nhóm đơn vị của vành :math:`F`.

Ngoài ra, nghịch đảo Dirichlet của mỗi hàm số học :math:`f` là duy nhất và được xác định bởi công thức:

.. math:: 

    f^{-1} (1) & = \frac{1}{f(1)}, \\
    f^{-1} (n) & = \frac{-1}{f(1)} \sum_{d \mid n, d \neq n} f\left(\frac{n}{d}\right) \cdot f^{-1}(d), \ \text{với} \ n > 1.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đầu tiên ta chứng tỏ sự tồn tại của nghịch đảo :math:`f^{-1}` bằng quy nạp.

    Với :math:`n = 1` thì :math:`(f * f^{-1})(1) = f(1) \cdot f^{-1}(1) = 1 = \delta(1)`. Như vậy bước cơ sở đúng.

    Giả thiết quy nạp:

    .. math:: f^{-1} (k) = \frac{-1}{f(1)} \sum_{d \mid k, d \neq k} f\left(\frac{k}{d}\right) \cdot f^{-1}(d)

    đúng với mọi :math:`k < n`. Khi đó, vì

    .. math:: (f * f^{-1})(n) = \delta(n) = 0, \ n > 1,
    
    nên

    .. math:: (f * f^{-1})(n) = f(1) \cdot f^{-1}(n) + \sum_{d \mid n, d \neq n} f\left(\frac{n}{d}\right) \cdot f^{-1}(d) = 0.

    Chuyển vế và đổi dấu ta có công thức của :math:`f^{-1}(n)` là

    .. math:: f^{-1}(n) = -\frac{1}{f(1)} \sum_{d \mid n, d \neq n} f\left(\frac{n}{d}\right) \cdot f^{-1}(d).

    Ở đây, :math:`f^{-1}(d)` tồn tại theo giả thiết quy nạp (với mọi :math:`k < n`).

    Tiếp theo ta chứng minh tính duy nhất của nghịch đảo Dirichlet. Giả sử ta có hai nghịch đảo :math:`g` và :math:`h` của :math:`f`, như vậy

    .. math:: 

        f * g = g * f = \delta, \quad f * h = h * f = \delta.

    Khi đó

    .. math:: g = g * \delta = g * (f * h) = (g * f) * h = \delta * h = h.

    Như vậy :math:`g = h` và nghịch đảo Dirichlet là duy nhất.

Một số lưu ý đối với nghịch đảo Dirichlet:

1. Tích chập Dirichlet của hai hàm nhân tính thì nhân tính, và mọi hàm nhân tính khác không đều có nghịch đảo Dirichlet cũng nhân tính.
2. Tổng của hai hàm nhân tính không nhất thiết nhân tính nên tập các hàm nhân tính KHÔNG tạo thành vành con của vành :math:`F`.

Liên hệ giữa tích chập Dirichlet và hàm hằng
============================================

Ta định nghĩa hàm hằng :math:`\bm{1}(n) = 1` với mọi :math:`n`.

Khi đó tích chập Dirichlet của hàm Euler :math:`\varphi(n)` và hàm hằng :math:`\bm{1}(n)` là hàm đồng nhất :math:`\mathsf{Id}(n)` vì

.. math:: (\bm{1} * \varphi(n)) = \sum_{d \mid n} 1 \cdot \varphi(d) = \sum_{d \mid n} \varphi(d) = n = \mathsf{Id}(n).

Đối với hàm Mobius :math:`\mu(n)`, nghịch đảo Dirichlet của nó của hàm hằng :math:`\bm{1}(n)`:

.. math:: \bm{1} * \mu = \delta.

Như vậy, nếu ta có hàm số học :math:`f` và :math:`g` thỏa :math:`g = f * \bm{1}` thì bằng tích chập với :math:`\mu` ta cũng có :math:`f = g * \mu`. Việc biểu diễn :math:`f` theo :math:`g` chính là **công thức nghịch đảo Mobius**.
