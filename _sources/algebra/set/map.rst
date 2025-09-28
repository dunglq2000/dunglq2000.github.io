Ánh xạ
======

[TODO] Viết lại ánh xạ dựa trên một giáo trình chuẩn.


Ánh xạ
------

Cho hai tập hợp :math:`X` và :math:`Y`.

Nói đơn giản, ánh xạ :math:`f` biến một phần tử :math:`x \in X` thành một và chỉ một phần tử :math:`y \in Y`.

.. prf:definition:: Ánh xạ

    Một ánh xạ :math:`f` từ tập :math:`X` đến tập :math:`Y` là một 
    quy tắc đặt tương ứng mỗi phần tử :math:`x` của :math:`X` với
    một (và chỉ một) phần tử của :math:`Y`. Phần tử này được gọi 
    là **ảnh** của :math:`x` qua ánh xạ :math:`f` và được kí hiệu 
    là :math:`f(x)`.

Tập hợp :math:`X` được gọi là **tập xác định** của :math:`f`. 
Tập hợp :math:`Y` được gọi là **tập giá trị** của :math:`f`.

Ánh xạ :math:`f` từ :math:`X` đến :math:`Y` được kí hiệu là
:math:`f: X \to Y` hoặc :math:`f(x) = y`.

Cho :math:`a \in X` và :math:`y \in Y`. Nếu :math:`f(a) = y` 
thì ta nói :math:`y` là **ảnh** của :math:`a` và :math:`a` là 
**nghịch ảnh** của :math:`y` qua ánh xạ :math:`f`.

.. admonition:: Chú ý
    :class: important

    1. Mỗi phần tử :math:`a` của :math:`X` chỉ có một 
       ảnh duy nhất (là phần tử :math:`f(a)`).
    2. Mỗi phần tử :math:`y` của :math:`Y` có thể có 
       nhiều nghịch ảnh hoặc không có nghịch ảnh nào.

Tập

.. math:: f(X) = \{ y \in Y : \exists x \in X, y = f(x) \}

được gọi là **tập ảnh** của :math:`f`.

Như vậy, tập ảnh :math:`f(X)` là tập tất cả phần tử của 
:math:`Y` có nghịch ảnh.

Ánh xạ có ba loại:

1. **Đơn ánh** (hay **Injection**): Hai phần tử khác nhau của tập 
   nguồn cho hai ảnh khác nhau, tức là với mọi :math:`x_1, x_2 \in X` 
   mà :math:`x_1 \neq x_2`, thì :math:`f(x_1) \neq f(x_2)`.
2. **Toàn ánh** (hay **Surjection**): Mọi phần tử :math:`y \in Y` 
   đều có ít nhất một phần tử :math:`x \in X` mà :math:`f(x) = y`. 
   Nói cách khác với mỗi phần tử trong :math:`Y` ta đều tìm được 
   phần tử thuộc :math:`X` biến thành nó.
3. **Song ánh** (hay **Bijection**): Nếu ánh xạ đó vừa là đơn ánh, 
   vừa là toàn ánh.

Dựa vào định nghĩa và hình vẽ, ta có thể rút ra kết luận như sau

1. Đối với đơn ánh, do mọi phần tử của :math:`X` đều có ảnh ở :math:`Y`, 
   tuy nhiên có thể có phần tử ở :math:`Y` không do phần tử nào của 
   :math:`X` biến thành (trong hình là :math:`5`). Do đó 
   :math:`\lvert X \rvert \leqslant \lvert Y \rvert`.
2. Đối với toàn ánh, mọi phần tử của :math:`Y` đều có nguồn gốc xuất xứ, 
   tuy nhiên có thể có phần tử của :math:`X` không biến thành :math:`y` 
   nào của :math:`Y` (trong hình là :math:`e`). Do đó 
   :math:`\lvert X \rvert \geqslant \lvert Y \rvert`.
3. Đối với song ánh, do là kết hợp giữa đơn ánh và toàn ánh, khi đó dấu 
   đẳng thức xảy ra, :math:`\lvert X \rvert = \lvert Y \rvert`.

.. figure:: ../../figures/maps/injection.*

    Đơn ánh

.. figure:: ../../figures/maps/surjection.*

    Toàn ánh

.. figure:: ../../figures/maps/bijection.*

    Song ánh

Cho song ánh :math:`f : X \to Y`. Khi đó với mỗi :math:`y \in Y` 
tồn tại duy nhất một phần tử :math:`x \in X` mà :math:`f(x) = y`.

Phần tử duy nhất :math:`x \in X` này được gọi là ảnh của phần 
tử :math:`y \in Y` qua **ánh xạ ngược** của :math:`f`.

.. prf:definition:: Ánh xạ ngược của song ánh
    :label: def-map-invertible

    Ánh xạ ngược của :math:`f: X \to Y`, kí hiệu là :math:`f^{-1}` 
    là ánh xạ từ :math:`Y` tới :math:`X` biến phần tử 
    :math:`y \in Y` thành phần tử :math:`x \in X` duy nhất, như vậy 

    .. math:: f^{-1}(y) = x \Longleftrightarrow f(x) = y.

Như vậy, nếu :math:`f` không phải song ánh thì chúng ta 
không thể xác định ánh xạ ngược.

.. prf:example:: 
    :label: exp-bijection

    Xét hàm số :math:`f: \mathbb{R} \to \mathbb{R}`, 
    :math:`x \to y = f(x) = x^3`.

    Lúc này, :math:`f` là song ánh và mình có thể biểu diễn 
    :math:`x` theo :math:`y` là :math:`x = f^{-1}(y) = \sqrt[3]{y}`.

.. prf:definition:: Ánh xạ hợp
    :label: def-anh-xa-hop

    Xét hai ánh xạ :math:`f: X \to Y`, :math:`f(x) = y` và 
    :math:`g: Y \to Z`, :math:`z = g(y)`. Ánh xạ hợp của 
    :math:`g` và :math:`f` được kí hiệu là 
    
    .. math:: g \circ f: X \to Z, \quad z = g(y) = g(f(x)).

.. prf:definition:: Tích Descartes
    :label: def-tich-Descartes

    Tích Descartes của hai tập hợp :math:`A = \{ a_1, a_2, \cdots, a_n \}` 
    và :math:`B = \{ b_1, b_2, \cdots, b_m \}` là tập hợp
    
    .. math:: A \times B = \{ (a_i, b_j) : a_i \in A, b_j \in B\}.

.. prf:example:: 
    :label: exp-tich-Descartes

    Với :math:`A = \{1, 2, 3\}` và :math:`B = \{ 4, 5 \}` thì tích Descartes là 

    .. math:: S = A \times B = \{(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)\}.

Với nhiều tập hợp ta định nghĩa tich Descartes tương tự.

.. prf:example:: 
    :label: exp-anh-xa-tich-Descartes
    
    Xét ba tập nguồn :math:`X`, :math:`Y`, :math:`Z`, 
    và tập đích là :math:`T`, ánh xạ :math:`\phi : X \times Y \times Z \to T`, 
    với :math:`\phi(x, y, z) \to t` là ánh xạ ba biến, 
    tập nguồn của ánh xạ khi này là tích Descartes :math:`X \times Y \times Z`.
