==============
Ba đường Conic
==============

Ba đường Conic bao gồm ellipse, hyperbol và parabol.

-------
Ellipse
-------

.. prf:definition:: Ellipse
    :label: def-ellipse
    
    Đường ellipse là tập hợp các điểm sao cho tổng khoảng cách từ nó tới hai điểm cố định là hằng số.

Nói cách khác, với hai điểm cố định :math:`F_1` và :math:`F_2`, tập hợp các điểm :math:`M` sao cho

.. math:: M F_1 + M F_2 = 2a,
    
với :math:`a` là hằng số tạo thành đường ellipse.

Ở trên hệ tọa độ, nếu ta chọn :math:`F_1` và :math:`F_2` nằm trên :math:`Ox` và đối xứng qua :math:`Oy`, tức là :math:`F_1 = (-c, 0)` và :math:`F_2 = (c, 0)` với :math:`c \geqslant 0`, thì các điểm :math:`M = (x, y)` nằm trên ellipse thỏa

.. math:: MF_1 + MF_2 = \sqrt{(x+c)^2 + y^2} + \sqrt{(x-c)^2 + y^2} = 2a,

tương ứng với biển đổi thành phương trình

.. math:: \frac{x^2}{a^2} + \frac{y^2}{a^2 - c^2} = 1.

Đặt :math:`b^2 = a^2 - c^2` thì phương trình của ellipse trở thành

.. math:: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1.

Phương trình này gọi là **phương trình chính tắc**.

.. figure:: ../../figures/conics/ellipse.*

    Ellipse với phương trình :math:`\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1`

Trong phương trình 

.. math:: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1

thì :math:`a` là khoảng cách từ tâm tới hai biên trái hoặc phải, nên :math:`a` là **độ dài bán trục lớn**.

Tương tự, :math:`b` là **độ dài bán trục nhỏ** (khoảng cách từ tâm tới hai biên trên dưới).

Từ cách đặt :math:`b^2 = a^2 - c^2` tương đương với :math:`c^2 = a^2 - b^2` thì :math:`c` gọi là **tiêu cự** của ellipse.

Các điểm :math:`F_1` và :math:`F_2` gọi là **tiêu điểm** của ellipse.

Với ví dụ trên :math:`\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1` thì :math:`a = 5`, :math:`b = 3`. Ta suy ra :math:`c = 4` (lưu ý là :math:`a, b > 0` và :math:`c \geqslant 0`).

Các đỉnh nằm ở các tọa độ :math:`(-a, 0)`, :math:`(a, 0)`, :math:`(0, b)`, :math:`(0, -b)`.

Các tiêu điểm nằm ở :math:`(-c, 0), (c, 0)`.

.. prf:remark:: 
    :label: rmk-ellipse-to-circle
    
    Khi :math:`c = 0`, tức là hai tiêu điểm trùng nhau, ta có đường tròn.

Tâm sai của ellipse là :math:`e = \dfrac{c}{a} < 1`.

--------
Hyperbol
--------

.. prf:definition:: Hyperbol
    :label: def-hyperbol
    
    Đường hyperbol là tập hợp các điểm sao cho giá trị tuyết đối hiệu số khoảng cách từ nó tới hai điểm cố định là hằng số.

Nói cách khác, với hai điểm cố định :math:`F_1` và :math:`F_2`, tập hợp các điểm :math:`M` sao cho

.. math:: \lvert M F_1 - M F_2 \rvert = 2a,
    
với :math:`a` là hằng số tạo thành đường hyperbol.

Ở trên hệ tọa độ, nếu ta chọn :math:`F_1` và :math:`F_2` nằm trên :math:`Ox` và đối xứng qua :math:`Oy`, tức là :math:`F_1 = (-c, 0)` và :math:`F_2 = (c, 0)`, thì các điểm :math:`M = (x, y)` nằm trên hyperbol thỏa

.. math:: \lvert MF_1 - MF_2 \rvert = \lvert \sqrt{(x+c)^2 + y^2} - \sqrt{(x-c)^2 + y^2} \rvert = 2a,

tương ứng với biển đổi thành phương trình

.. math:: \frac{x^2}{a^2} - \frac{y^2}{a^2 - c^2} = 1.

Đặt :math:`b^2 = a^2 - c^2` thì phương trình của hyperbol trở thành

.. math:: \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1.

Đường hyperbol cắt trục :math:`Ox` tại hai điểm :math:`A_1 = (-a, 0)` và :math:`A_2 = (a, 0)`.

Tiêu điểm của hyperbol ở :math:`F_1 = (-c, 0)` và :math:`F_2 = (c, 0)`.

Đường hyperbol có hai tiệm cận là đường thẳng :math:`y = \dfrac{b}{a} x` và :math:`y = -\dfrac{b}{a} x`.

Tâm sai của hyperbol là :math:`e = \dfrac{c}{a} > 1`.

-------
Parabol
-------

.. prf:definition:: Parabol
    :label: def-parabol
    
    Đường parabol là tập hợp các điểm cách đều một điểm cố định và một đường thẳng cố định.

.. figure:: ../../figures/conics/parabola.*

    Parabol với phương trình :math:`y = -x^2 + 4`

Nghĩa là, với điểm cố định :math:`F` và đường thẳng cố định :math:`(d)`, parabol là tập hợp các điểm :math:`M` sao cho

.. math:: MF = d(M, (d))
    
với :math:`d(M, (d))` là khoảng cách từ :math:`M` tới đường thẳng :math:`(d)`.

Phép dời tọa độ cho phép ta dời một hình parabol có đỉnh ở bất kì điểm nào về gốc tọa độ.

Tức là, không mất tính tổng quát, ta chỉ cần xét các parabol dạng :math:`y = ax^2` là đủ.

Điểm cố định ở trên được gọi là **tiêu điểm**. Đường thẳng cố định ở trên gọi là **đường chuẩn**.

Parabol có tính đối xứng nên tiêu điểm nằm trên :math:`Oy`. Đặt tọa độ của tiêu điểm là :math:`F = (0, f)`.

Đường chuẩn nằm ngang nên ta có parabol là các điểm :math:`M = (x, y)` sao cho

.. math:: MF = \sqrt{x^2 + (y-f)^2}, \quad d(M, (d)) = y+f,
    
trường hợp :math:`M` trùng với đỉnh nên điều kiện của parabol xảy ra tương đương với :math:`M` cách đều tiêu điểm và đường chuẩn, nghĩa là đường chuẩn có dạng :math:`y = -f`.

Do đó :math:`\sqrt{x^2 + (y-f)^2} = y + f`. Bình phương và biến đổi ta thu gọn được :math:`f = \dfrac{1}{4a}`.

Thường thì ta đặt :math:`p = f`, khi đó phương trình parabol trở thành :math:`x^2 = 4py`.

Đây là dạng chính tắc của parabol với trục đối xứng dọc.

Tâm sai của parabol là :math:`e = \dfrac{c}{a} = 1`.
