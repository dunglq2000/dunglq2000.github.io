Đại cương về tập hợp
********************

Tập hợp là khái niệm nền tảng, có mặt trong hầu khắp các ngả rẽ của toán học. Mình có dịp đọc quyển *Toán học qua các câu chuyện về tập hợp* của Tủ sách Sputnik :cite:`Sputnik008`, dịch từ quyển *Рассказы о множествах* của Виленкин Н.Я. :cite:`Vilenkin19` và thấy những câu chuyện rất thú vị. Nếu hứng thú các bạn có thể tìm đọc.

Tập hợp
=======

Mở đầu về tập hợp
-----------------

Một **tập hợp** (**set**) bao gồm các phần tử khác nhau. Tập hợp là khái niệm cơ sở cho nhiều vấn đề của toán học. Tuy nhiên chúng ta lại không có một định nghĩa chặt chẽ về tập hợp mà chỉ có thể biểu diễn nó. Để biểu diễn tập hợp ta có hai cách.

1. Liệt kê. Ví dụ :math:`A = \{ 1, 2, 3, 4 \}`, :math:`B = \{ a, b , c \}`.
2. Sử dụng tính chất đặc trưng. Ví dụ :math:`A = \{ a \in \mathbb{N}^* : a < 5 \}`.

Ở đây hai cách biểu diễn tập hợp :math:`A` là giống nhau.

.. prf:definition:: Tập hợp rỗng
    :label: def-empty-set

    Tập hợp rỗng không chứa phần tử nào, kí hiệu là :math:`\emptyset`.

.. prf:definition:: Tập hợp con
    :label: def-subset

    Xét tập hợp :math:`A`. Tập hợp :math:`B` được gọi là **tập hợp con** của tập :math:`A` nếu mọi phần tử của :math:`B` đều nằm trong :math:`A`. Nói cách khác với mọi :math:`b \in B` thì :math:`b \in A`. Ta kí hiệu :math:`B \subset A`.

.. prf:remark:: 
    :label: rmk-subset
    
    Tập hợp rỗng là con của mọi tập hợp.

Dễ thấy rằng mọi tập hợp là tập hợp con của chính nó. Do đó tập con này được gọi là tập con tầm thường (trivial subset). Để kí hiệu một tập con có thể bằng tập chứa nó ta viết :math:`B \subseteq A`. Trong trường hợp :math:`B` là tập con của :math:`A` nhưng không bằng :math:`A` ta có thể viết :math:`B \subsetneq A`.

Toán tử trên tập hợp
--------------------

Chúng ta xem xét ba toán tử cơ bản trên tập hợp là **giao**, **hợp** và **hiệu** của hai tập hợp. Để biểu diễn các toán tử này ta có thể dùng biểu đồ Venn.

.. prf:definition:: Giao của hai tập hợp
    :label: def-set-intersection
    
    Giao của hai tập hợp :math:`A` và :math:`B` là tập hợp các phần tử thuộc cả :math:`A` và :math:`B`.

    .. math:: A \cap B = \{ x : x \in A \text{ và } x \in B \}.

.. _set1:

.. figure:: ../../figures/set/venn_diagram-01.*

    Phép giao hai tập hợp

:numref:`set1` là biểu đồ Venn tương ứng của phép giao hai tập hợp. Khi giao của hai tập hợp :math:`A` và :math:`B` là rỗng thì ta nói hai tập rời nhau. Kí hiệu :math:`A \cap B = \emptyset`.

.. prf:definition:: Hợp của hai tập hợp
    :label: def-union-set

    Hợp của hai tập hợp :math:`A` và :math:`B` là tập hợp các phần tử thuộc :math:`A` hoặc :math:`B`.

    .. math:: A \cup B = \{ x : x \in A \text{ hoặc } x \in B \}.

:numref:`set2` là biểu đồ Venn tương ứng của phép hợp hai tập hợp.

.. _set2: 

.. figure:: ../../figures/set/venn_diagram-02.*

    Phép hợp hai tập hợp

.. prf:definition:: Hiệu của hai tập hợp
    :label: def-set-minus
    
    Hiệu (hay phần bù) của tập hợp :math:`A` đối với tập hợp :math:`B` là tập hợp các phần tử thuộc :math:`A` nhưng không thuộc :math:`B`.

    .. math:: A \backslash B = \{ x : x \in A \text{ và } x \not\in B \}.

:numref:`set3` là biểu đồ Venn tương ứng của hiệu hai tập hợp.

.. _set3: 

.. figure:: ../../figures/set/venn_diagram-03.*

    Phép hiệu hai tập hợp

Lực lượng của tập hợp
=====================

Để chỉ số lượng phần tử của một tập hợp ta dùng khái niệm lực lượng của tập hợp.

Kí hiệu lực lượng của tập hợp :math:`A` là :math:`\lvert A \rvert` hoặc :math:`\# A`.

Khi một tập hợp có vô số phần tử, ta gọi đó là tập vô hạn. Ngược lại ta gọi là tập hữu hạn.

.. prf:example:: 
    :label: exp-cadinality

    Các tập hợp số thông dụng :math:`\mathbb{N}`, :math:`\mathbb{Z}`, :math:`\mathbb{Q}`, :math:`\mathbb{R}` là các tập vô hạn.

    Tập hợp :math:`A = \{ 1, 2, 3, 4, 5 \}` là tập hữu hạn có :math:`5` phần tử. Kí hiệu :math:`\lvert A \rvert = 5`.

Từ biểu đồ Venn chúng ta cũng có thể tìm được công thức tính lực lượng của tập :math:`A \cup B`.

.. _set4:

.. figure:: ../../figures/set/venn_diagram-04.*

    Nguyên lý bù trừ cho hai tập hợp

Dựa vào hình ta có thể suy ra công thức sau:

.. math:: \lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert.

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

Hàm số
======

Hàm số
------

Khi hai tập nguồn và đích của ánh xạ là hai tập hợp 
số, ta có hàm số.

.. prf:example:: 
    :label: exp-function
    
    Hàm số :math:`f: \mathbb{R} \to \mathbb{R}` với 
    :math:`y = f(x) = x^3 + x + 1`. Ở đây :math:`f: X \to Y` 
    vói :math:`X \equiv \mathbb{R}` và :math:`Y \equiv \mathbb{R}`.

Lưu ý rằng tập nguồn và đích không nhất thiết là tập 
hợp số cơ bản (:math:`\mathbb{Q}`, :math:`\mathbb{R}`) 
mà cũng có thể là tích Descartes của chúng.

.. prf:example:: 
    :label: exp-function-with-Descartes

    Hàm số :math:`f: \mathbb{R} \times \mathbb{R} \to \mathbb{R}` 
    với :math:`z = f(x, y) = x + y + xy`. Ở đây :math:`f: X \times Y \to Z` 
    với :math:`X \equiv \mathbb{R}`, :math:`Y \equiv \mathbb{R}` 
    và :math:`Z \equiv \mathbb{R}`.

.. prf:example:: 
    :label: exp-function-bijection

    Hàm số :math:`f: \mathbb{R} \to \mathbb{R}` cho bởi 
    :math:`y = f(x) = x^3` là song ánh.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta thấy nếu :math:`f(x_1) = f(x_2)`, tương đương 
    :math:`x_1^3 = x_2^3` nên :math:`x_1 = x_2`. Do 
    đó :math:`f` là đơn ánh.

    Với mọi :math:`y = x^3 \in \mathbb{R}`, do căn bậc 
    ba luôn tồn tại nên ta có :math:`x = \sqrt[3]{y}`, 
    nghĩa là luôn tồn tại :math:`x` để :math:`f(x) = y` 
    với mọi :math:`y \in \mathbb{R}`. Do đó :math:`f` 
    là toàn ánh.

    Kết luận :math:`f` là song ánh.

Đồng biến và nghịch biến
------------------------

.. prf:definition:: Hàm số đồng biến
    :label: def-monotone-inc

    Xét hàm số :math:`f(x)` xác định trên khoảng 
    :math:`(a; b) \subset \mathbb{R}`. Ta nói 
    :math:`f(x)` **đồng biến** (**tăng**) trên 
    :math:`(a; b)` nếu với mọi :math:`x_1, x_2 \in (a; b)` 
    mà :math:`x_1 < x_2` ta có :math:`f(x_1) < f(x_2)`.

Tương tự :math:`f(x)` **nghịch biến** (**giảm**) 
trên :math:`(a; b)` nếu với mọi :math:`x_1, x_2 \in (a; b)` 
mà :math:`x_1 < x_2` ta có :math:`f(x_1) > f(x_2)`.

Lưu ý ở các so sánh trên dấu bằng có thể xảy ra. Khi đó 
hàm số được gọi là tăng **không nghiêm ngặt** (hoặc 
giảm **không nghiêm ngặt**).

Nếu hàm số đồng biến (hoặc nghịch biến) trên khoảng xác 
định nào đó thì ta nói hàm số đơn điệu trên khoảng đó.

Đồ thị của hàm số khi đồng biến sẽ đi lên (theo chiều từ 
trái sang phải), và đi xuống nếu nghịch biến.

.. prf:example:: 
    :label: exp-monotone
    
    Khảo sát sự biến thiên của hàm số :math:`f(x) = x^2 + 3`.

    Để khảo sát sự biến thiên, một cách làm đơn giản theo 
    định nghĩa là ta xét :math:`x_1 < x_2` và so sánh 
    :math:`f(x_1)` với :math:`f(x_2)`.

    Ta có 

    .. math:: f(x_1) - f(x_2) = x_1^2 + 3 - x_2^2 - 3 = (x_1 - x_2)(x_1 + x_2).

    Do :math:`x_1 < x_2`, nên với :math:`x_1, x_2 > 0` 
    thì :math:`x_1 + x_2 > 0` và :math:`x_1 - x_2 < 0`. 
    Ta suy ra :math:`f(x_1) - f(x_2) < 0` và từ đó 
    :math:`f(x_1) < f(x_2)`. Như vậy :math:`f(x)` đồng 
    biến trên :math:`(0; +\infty)`.

    Tương tự, khi :math:`x_1, x_2 < 0` thì :math:`x_1 + x_2 < 0`. 
    Khi đó :math:`f(x_1) > f(x_2)` nên :math:`f(x)` nghịch 
    biến trên :math:`(-\infty; 0)`.

Để thể hiện sự biến thiên của hàm số ta sử dụng bảng biến thiên.

Đối với hàm số :math:`y = x^2 + 3` ở trên bảng biến thiên có dạng:

.. figure:: ../../figures/table_of_variation/table_of_variation-01.*

    Bảng biến thiên hàm số :math:`y=x^2 + 3`

Ta đã chứng minh được hàm số nghịch biến trên :math:`(-\infty; 0)` 
và đồng biến trên :math:`(0; +\infty)`, giá trị :math:`f(0) = 3` 
nên bảng biến thiên thể hiện sự tăng giảm trên các khoảng. Dựa 
vào bảng biến thiên ta có thể hình dung ra dạng của đồ thị hàm số.

Đồ thị hàm số
-------------

Để biểu diễn sự phụ thuộc của biến :math:`y` theo biến :math:`x`, 
hay nói cách khác là biểu diễn hàm số :math:`y = f(x)`, ta có 
thể dùng đồ thị.

Đồ thị được vẽ trên hệ tọa độ Descartes :math:`Oxy`. Bảng biến 
thiên cho ta thấy tính đơn điệu trên các khoảng xác định, và 
đồ thị sẽ cho ta thấy rõ hơn độ "cong" của những đường cong.

.. prf:example:: 
    :label: exp-graph-of-funcs
    
    Với hàm số :math:`y = x^2 + 3` ở trên. Đồ thị hàm số có 
    dạng như :numref:`hình %s <func1>`.

    Với hàm số :math:`y = \dfrac{1}{x}`. Ta thấy rằng hàm số 
    không xác định tại :math:`x = 0`. Khảo sát sự biến thiên 
    như bên trên ta thấy hàm số nghịch biến ở hai khoảng xác 
    định là :math:`(-\infty; 0)` và :math:`(0; +\infty)`. Đồ 
    thị hàm số có dạng như :numref:`hình %s <func2>`.

.. _func1:

.. figure:: ../../figures/table_of_variation/table_of_variation-02.*

    Đồ thị hàm số :math:`y = x^2 + 3`

.. _func2:

.. figure:: ../../figures/table_of_variation/table_of_variation-03.*

    Đồ thị hàm số :math:`y = \dfrac{1}{x}`

Từ đồ thị của hai hàm số trên ta thấy rằng mặc dù cùng là 
nghịch biến trên :math:`(-\infty; 0)` nhưng nghịch biến của 
:math:`y = x^2+3` nhìn "nhẹ nhàng" hơn. Trong khi đồ thị 
:math:`y = \dfrac{1}{x}` thì ban đầu "nhẹ nhàng", sau thì 
như "rơi tự do".

Một số loại hàm số
------------------

Một số hàm số có tính chất đặc biệt giúp chúng ta tiết kiệm 
công sức trong chứng minh, tính toán.

Hàm chẵn và hàm lẻ
^^^^^^^^^^^^^^^^^^

Xét hàm số :math:`y = f(x)` xác định trên miền :math:`D` có 
tính đối xứng, nghĩa là với mỗi phần tử dương :math:`x \in D` thì 
có phần tử đối :math:`-x \in D` hoặc ngược lại. Khi đó

.. prf:definition:: Hàm số chẵn
    :label: def-even-func

    Hàm số :math:`y = f(x)` được gọi là **hàm số chẵn** nếu 
    với mọi :math:`x \in D` ta có :math:`f(-x) = f(x)`.

Ví dụ như hàm số :math:`y = x^2 + 3` ở trên là một hàm chẵn 
vì với mọi :math:`x \in \mathbb{R}` ta có

.. math:: f(x) = x^2 + 3 = (-x)^2 + 3 = f(-x).
    
Dễ thấy rằng đồ thị của hàm chẵn đối xứng qua trục tung. Dựa 
vào tính chất này, trong lúc khảo sát hoặc tính toán đôi khi 
ta chỉ cần quan tâm một bên trục tung, bên kia tương tự.

.. prf:definition:: Hàm số lẻ
    :label: def-odd-func

    Hàm số :math:`y = f(x)` được gọi là **hàm số lẻ** nếu với 
    mọi :math:`x \in D` ta có :math:`f(-x) = -f(x)`.

Ví dụ như hàm số :math:`y = \dfrac{1}{x}` ở trên là một hàm lẻ 
vì với mọi :math:`x \in (-\infty; 0) \cup (0; +\infty)` ta có

.. math:: f(-x) = \dfrac{1}{-x} = -\dfrac{1}{x} = -f(x).
    
Dễ thấy rằng hàm lẻ đối xứng qua gốc tọa độ :math:`O(0, 0)`.

Hàm cộng tính
^^^^^^^^^^^^^

Xét hàm số :math:`y = f(x)` xác định trên miền :math:`D`. 

.. prf:definition:: Hàm cộng tính
    :label: def-additive-func

    Hàm số :math:`y = f(x)` được gọi là **cộng tính** nếu với 
    mọi :math:`x, y \in D` mà :math:`x + y \in D`, ta có 
    :math:`f(x+y) = f(x) + f(y)`.

.. prf:example:: 
    :label: exp-additive-func

    Hàm số :math:`y = 2x` trên :math:`\mathbb{R}` là hàm cộng 
    tính vì với mọi :math:`x, y \in \mathbb{R}`, ta có
    
    .. math:: f(x+y) = 2(x+y) = 2x + 2y = f(x) + f(y).

Hàm nhân tính
^^^^^^^^^^^^^

Tương tự hàm cộng tính, ta định nghĩa hàm nhân tính.

.. prf:definition:: Hàm nhân tính
    :label: def-multiplicative-func

    Hàm số :math:`y = f(x)` được gọi là **nhân tính** 
    nếu với mọi :math:`x, y \in D` ta có 
    :math:`f(xy) = f(x) \cdot f(y)`.

Hàm nhân tính quan trọng được sử dụng trong số học là 
hàm :math:`\varphi` Euler về số lượng các số nguyên tố 
cùng nhau với số nguyên dương :math:`n`. Nếu một hàm số 
học là nhân tính thì chúng ta chỉ cần quan tâm giá trị 
của hàm số đó tại các số nguyên tố là đủ.

Hàm tuần hoàn
^^^^^^^^^^^^^

Xét hàm số :math:`y = f(x)` xác định trên miền :math:`D`.

.. prf:definition:: Hàm tuần hoàn
    :label: def-periodic-func
    
    Hàm số :math:`y = f(x)` được gọi là **tuần hoàn** nếu 
    tồn tại số :math:`T` sao cho :math:`f(x+T) = f(x)` với 
    mọi :math:`x \in D`.

Nói cách khác, hàm số sẽ lặp lại sau một đoạn nhất định.

Số :math:`T` nhỏ nhất thỏa mãn :math:`f(x+T) = f(x)` được 
gọi là **chu kỳ** của hàm tuần hoàn.

Vì sao số :math:`T` cần là nhỏ nhất?

Ta thấy rằng, nếu :math:`f(x+T) = f(x)` với mọi 
:math:`x \in D`, ta thay :math:`x` bởi :math:`x + T` 
thì thu được :math:`f(x + T + T) = f(x + T)`, hay 
:math:`f(x + 2T) = f(x + T)`. Như vậy ta suy ra 
:math:`f(x + 2T) = f(x + T) = f(x)`. Tiếp tục như 
vậy, sau :math:`2T` hàm số cũng lặp lại đúng trạng 
thái đó với :math:`3T`, :math:`4T`, ... Do đó số 
:math:`T` nhỏ nhất thỏa mãn đẳng thức 
:math:`f(x + T) = f(x)` sẽ là chu kỳ.

.. prf:example:: 
    :label: exp-periodic-func

    Hàm số :math:`y = \sin(x)` là hàm tuần hoàn với 
    chu kỳ :math:`T = 2\pi`. Do đó chúng ta chỉ cần 
    khảo sát hàm số trong khoảng :math:`(-\pi; \pi)` 
    thôi là đủ.

Các nghịch lý về tập vô hạn
===========================

Tiếp theo chúng ta sẽ xem hết những bài toán hết sức thú vị 
cùng những lập luận cũng thú vị không kém để thấy rằng có 
nhiều điều bất ngờ sẽ xảy ra nếu vận dụng những lý luận chặt chẽ.

Nghịch lý Zeno
---------------

Zeno là nhà triết học cổ Hy Lạp nổi tiếng với bài toán *Achilles 
và rùa* (Achilles là anh hùng trong thần thoại Hy Lạp). Bài toán 
được phát biểu đơn giản như sau: 

    Nếu Achilles chạy đua và xuất phát sau con rùa thì 
    Achilles sẽ không bao giờ bắt kịp con rùa.

Bài toán nghe thật nực cười nhưng dưới lập luận của Zeno thì 
bài toán sẽ trở nên "có lý".

Zeno lập luận như sau: gọi :math:`d_1` là khoảng cách ban đầu giữa 
Achilles và con rùa. Achilles sẽ mất một khoảng thời gian :math:`t_1` 
để đi tới vị trí con rùa. Tuy nhiên trong khoảng thời gian :math:`t_1` 
đó con rùa cũng đã đi một đoạn :math:`d_2` nào đó rồi. Dĩ nhiên 
:math:`d_2` sẽ ngắn hơn :math:`d_1`. Nhưng nếu quá trình này lặp đi 
lặp lại, :math:`d_n` sẽ trở nên càng ngày càng nhỏ, tuy nhiên không 
bao giờ bằng :math:`0`. Nói cách khác, Achilles không bao giờ bắt 
kịp con rùa.

Dưới góc nhìn của toán học hiện đại, điều này chưa hẳn đúng. Vì thời 
Zeno chưa có nhiều khái niệm lẫn công cụ về vô cực, nên người ta đã 
công nhận tổng vô hạn sẽ là vô hạn. Học sinh lớp 11 hiện nay khi học 
tới cấp số nhân lùi vô hạn sẽ biết cách tính tổng 

.. math:: \frac{1}{10} + \frac{1}{100} + \cdots \frac{1}{10^n} = \frac{1}{9}

là hữu hạn.

So sánh :math:`\mathbb{N}` và :math:`\mathbb{Z}`
-------------------------------------------------

    Hai tập hợp :math:`\mathbb{N}` và :math:`\mathbb{Z}` là các tập vô hạn, như vậy lực lượng của tập hợp nào lớn hơn?

Câu hỏi tưởng chừng như vô vị vì nhìn vào mọi người đều thấy rằng 
:math:`\mathbb{Z}` "bao trọn" :math:`\mathbb{N}` (số nguyên kéo dài 
vô hạn về bên trái lẫn phải trong khi số tự nhiên chỉ kéo dài vô hạn 
về bên phải). Tuy nhiên, nhà toán học Cantor đã tìm ra một lý luận đầy 
*tính thuyết phục* để chứng minh rằng lực lượng của hai tập là bằng nhau.

Ta xét ánh xạ :math:`f: \mathbb{Z} \to \mathbb{N}` như sau:

- :math:`f(0) = 0`;
- các số âm của :math:`\mathbb{Z}` biến thành các số lẻ của :math:`\mathbb{N}`;
- các số dương của :math:`\mathbb{Z}` thì biến thành các số chẵn của :math:`\mathbb{N}`.

Ví dụ :math:`f(-1) = 1`, :math:`f(-2) = 3`, :math:`f(-3) = 5` và cứ như vậy tăng lên.

Tương tự với số dương :math:`f(1) = 2`, :math:`f(2) = 4`.

Ta có công thức

.. math:: 
    
    z = f(n) = \begin{cases} 2n, & \quad \text{nếu} \ n \geqslant 0 \\
    -1-2n, & \quad \text{nếu} \ n < 0.\end{cases}

Như vậy :math:`f` là đơn ánh vì hai phần tử khác nhau của :math:`\mathbb{Z}` 
sẽ cho ra hai phần tử khác nhau thuộc :math:`\mathbb{N}`. Tương tự :math:`f` 
cũng là toàn ánh vì mọi phần tử thuộc :math:`\mathbb{N}` đều có một phần tử 
từ :math:`\mathbb{Z}` biến thành. Như vậy :math:`f` là song ánh. Vậy lực 
lượng :math:`\mathbb{N}` và :math:`\mathbb{Z}` bằng nhau.

Bằng lập luận tương tự cũng có thể chứng minh số phần tử của :math:`\mathbb{Q}` 
bằng số phần tử của :math:`\mathbb{N}`. Những lập luận này đã gây ra tiếng vang 
lớn vào thời đó.

.. only:: html

   Ở :numref:`hình %s <meme-1>` cho thấy một cách xây dựng song ánh từ 
   :math:`\mathbb{N}` tới :math:`\mathbb{Z}^2`, trong đó:

   - điểm :math:`(0, 0)` tương ứng với :math:`1`;
   - điểm :math:`(1, 0)` tương ứng với :math:`2`;
   - điểm :math:`(1, 1)` tương ứng với :math:`3`;
   - điểm :math:`(0, 1)` tương ứng với :math:`4`;
   - cứ tiếp tục như vậy theo hình xoắn vuông.

   Vietsub cho :numref:`hình %s <meme-1>`: Không có chuyện :math:`\mathbb{N}` và 
   :math:`\mathbb{Z}^2` có cùng số phần tử. Ở đây thuật ngữ "số phần tử" không 
   thực sự chính xác mà nên gọi là "lực lượng" vì khi nói đến các tập vô hạn (tức 
   tập có vô hạn phần tử) thì vô hạn không thể so sánh với vô hạn. Hai tập hợp 
   vô hạn chỉ có thể có cùng lực lượng.

   .. _meme-1:

   .. figure:: https://sun9-41.userapi.com/impg/zmz_1-_MamZ7dwVLXKooNar7f1hC5crUItC2YA/sCWd3BmHVqc.jpg?size=640x550&quality=95&sign=53e3e82934396255a586fb2e39f0c82e&type=album 

      Song ánh giữa :math:`\mathbb{N}` và :math:`\mathbb{Z}^2`. Nguồn: https://vk.com/wall-91031095_82482.

Từ đây tập hợp vô hạn có thể chia ra **đếm được** (countable) 
và **không đếm được** (uncountable). Tiếp theo ta định nghĩa hai 
dạng tập hợp này.

1. Tập hợp được gọi là **đếm được** khi tồn tại song ánh từ nó tới :math:`\mathbb{N}`.
2. Tập hợp được gọi là **không đếm được** khi nó không phải là tập đếm được.

Định lý về :math:`\mathbb{R}`
-----------------------------

.. prf:theorem:: 
    :label: thr-about-R

    Tập hợp số thực :math:`\mathbb{R}` là tập không đếm được.

Chúng ta cần một nhận xét sau:

    Khoảng :math:`(0; 1)` là tương đương với tập :math:`\mathbb{R}`.

Chúng ta có thể xây dựng một song ánh từ :math:`\mathbb{R}` tới :math:`(0, 1)`, 
ví dụ :math:`f(x) = \dfrac{e^x}{e^x+1}`.

Khi đó, thay vì chứng minh :math:`\mathbb{R}` không đếm được, ta chỉ 
cần chứng minh đoạn :math:`(0; 1)` không đếm được.

.. admonition:: Chứng minh
    :class: danger

    Cantor đưa ra hai phương pháp chứng minh và cả hai đều độc đáo. 

    **Phương án 1:** Phương pháp chéo hóa (diagonalization).

    Xét ánh xạ

    .. math::   
        
        & 0 \to 0,a_{0, 0}a_{0, 1}a_{0, 2} \cdots \\
        & 1 \to 0,a_{1, 0}a_{1, 1}a_{1, 2} \cdots \\
        & 2 \to 0,a_{2, 0}a_{2, 1}a_{2, 2} \cdots \\
        & \cdots

    Ta chứng minh ánh xạ này không phải toàn ánh.

    Xét số :math:`y = 0,b_0 b_1 b_2 \ldots` với :math:`b_i \neq a_{i, i}` 
    với mọi :math:`i`, tức là trên đường chéo của các số trên ta chọn số 
    :math:`b_i` khác với số trên đường chéo. Như vậy số :math:`y` này có 
    chữ số ở vị trí :math:`0` khác :math:`f(0)`, chữ số ở vị trí :math:`1` 
    khác :math:`f(1)`, vân vân và mây mây, nên không tìm được số :math:`n` 
    nào mà :math:`f(n) = y`. Ta suy ra :math:`f` không phải toàn ánh và 
    từ đó không phải song ánh.

    **Phương án 2.** Phương pháp dãy các đoạn thẳng đóng bị chặn lồng vào 
    nhau (sequence of closed bounded nested).

    Giả sử đoạn :math:`(0; 1)` đếm được. Khi đó ta có thể liệt kê các 
    phần tử của đoạn là :math:`I = \{ x_1, x_2, \ldots \}`.

    Từ tập :math:`I` ta lấy ra một đoạn con :math:`I_1` sao cho :math:`x_1 \not\in I_1`.

    Tiếp theo, từ tập :math:`I_1` ta lấy ra một đoạn con :math:`I_2` 
    sao cho :math:`x_2 \not\in I_2`.

    Tiếp tục như vậy, ta lấy ra các đoạn con

    .. math:: \cdots \subset I_n \subset \cdots \subset I_2 \subset I_1 \subset I

    với :math:`x_n \not\in I_n` với mọi :math:`n \in \mathbb{N}`.

    Theo định lý về các đoạn thẳng đóng bị chặn lồng vào nhau thì giao của 
    chúng không rỗng, tức là tồn tại số :math:`x` thuộc giao giao của các tập 
    :math:`I_1`, ..., :math:`I_n`. Phần tử :math:`x \in I_n` với mọi :math:`n`. 
    Do :math:`x_n \not\in I_n` và :math:`x \in I_n` nên :math:`x \neq x_n` với 
    mọi :math:`n`, tức là không nằm trong tập :math:`I`. Điều này mâu thuẫn 
    với giả sử đoạn :math:`(0; 1)` đếm được, suy ra đoạn :math:`(0; 1)` là tập 
    không đếm được.
