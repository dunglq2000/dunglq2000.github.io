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

.. figure:: ../../figures/table_of_variation/table_of_variation-1.*

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

.. figure:: ../../figures/table_of_variation/table_of_variation-2.*

    Đồ thị hàm số :math:`y = x^2 + 3`

.. _func2:

.. figure:: ../../figures/table_of_variation/table_of_variation-3.*

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
