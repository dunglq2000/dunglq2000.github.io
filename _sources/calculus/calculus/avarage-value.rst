====================================
Một số định lí về giá trị trung bình
====================================

.. prf:theorem:: Bổ đề Fermat
    :label: fermat-lemma

    Cho :math:`f` là một hàm số có đạo hàm trên :math:`(a; b)`. Nếu :math:`x_0 \in (a; b)` là một điểm cực trị của :math:`f` thì ta có :math:`f'(x_0) = 0`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta chứng minh trong trường hợp :math:`x_0` là điểm cực tiểu. Trường hợp điểm cực đại tương tự.

    Hàm :math:`f` có đạo hàm trên :math:`(a; b)` nên tại điểm :math:`x_0` nó có đạo hàm bên trái và đạo hàm bên phải, và hai đạo hàm này bằng nhau.

    Ta có :math:`\displaystyle{f'(x_0^+) = \lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0}}`. Vì :math:`x \to x_0^+` nghĩa là :math:`x > x_0` (:math:`x` tiến tới :math:`x_0` từ bên phải), và do :math:`x_0` là cực tiểu :math:`f(x) - f(x_0) \geqslant 0` nên phân số dưới dấu giới hạn lớn hơn :math:`0`. Suy ra :math:`f'(x_0^+) \geqslant 0`.

    Hoàn toàn tương tự ta chứng minh được :math:`f'(x_0^-) \leqslant 0`. Và do :math:`f'(x_0^+) = f'(x_0^-) = f'(x_0)` nên :math:`f'(x_0) = 0`.

    Ta có điều phải chứng minh.

.. prf:theorem:: Định lí Rolle
    :label: thm-rolle
    
    Xét hàm số :math:`f` liên tục trên đoạn :math:`[a; b]`, có đạo hàm trên khoảng :math:`(a; b)` và :math:`f(a) = f(b)`. Khi đó tồn tại :math:`c` thuộc :math:`(a; b)` sao cho :math:`f'(c) = 0`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh định lí Rolle chúng ta cần bổ để Fermat và một tính chất của hàm liên tục

        Nếu :math:`f` là một hàm số liên tục trên đoạn :math:`[a; b]` thì :math:`f` đạt giá trị lớn nhất và giá trị nhỏ nhất trên đoạn đó.

    Nếu cả hai giá trị lớn nhất (GTLN) và giá trị nhỏ nhất (GTNN) của :math:`f` đều đạt tại biên thì do giả thiết :math:`f(a) = f(b)` ta suy ra GTLN = GTNN. Như vậy :math:`f` là hàm hằng nên :math:`f'(c) = 0` với mọi :math:`c \in (a; b)`.

    Ngược lại, có một trong hai giá trị đó đạt được tại điểm :math:`c \in (a; b)`. Khi đó :math:`c` là điểm cực trị nên theo bổ đề Fermat thì :math:`f'(c) = 0`.

Về mặt vật lí, định lí Rolle cho biết rằng nếu một chất điểm chuyển động trên đường thẳng bắt đầu từ điểm :math:`a` và quay lại điểm xuất phát ở thời điểm :math:`b` thì có một thời điểm :math:`c` nào đó thuộc :math:`(a; b)` mà chất điểm dừng lại, kể cả ta không biết tốc độ của chất điểm như nào.

Định lí Rolle là công cụ giúp khảo sát, đánh giá số nghiệm của các phương trình rất tốt.

Khi mở rộng định lí Rolle chúng ta được định lí Lagrange. Nếu trong khoảng thời gian từ :math:`a` tới :math:`b`, chất điểm di chuyển trên đường thẳng từ vị trí :math:`s(a)` tới :math:`s(b)` (so với gốc tọa độ) thì vận tốc trung bình trong thời gian này là :math:`\dfrac{s(b) - s(a)}{b - a}`. Định lí Lagrange nói rằng tồn tại thời điểm :math:`c` thuộc :math:`(a; b)` sao cho vận tốc tức thời tại thời điểm này bằng vận tốc trung bình trên cả quãng đường :math:`s(a)` tới :math:`s(b)`.

.. prf:theorem:: Định lí Lagrange
    :label: thm-lagrange

    Xét hàm số :math:`f` liên tục trên đoạn :math:`[a; b]`, có đạo hàm trên khoảng :math:`(a; b)`. Khi đó tồn tại :math:`c` thuộc :math:`(a; b)` sao cho :math:`f'(c) (b - a) = f(b) - f(a)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Xét hàm

    .. math:: 

        g(x) = f(x) - \dfrac{f(b) - f(a)}{b - a} \cdot (x - a).

    Khi đó ta có :math:`g(a) = f(a)` và

    .. math:: 

        g(b) = f(b) - \dfrac{f(b) - f(a)}{b - a} \cdot (b - a) = f(b) - (f(b) - f(a)) = f(a).

    Do :math:`g` liên tục trên :math:`[a; b]`, có đạo hàm trên :math:`(a; b)` và :math:`g(a) = g(b)` nên theo định lí Rolle tồn tại :math:`c \in (a; b)` sao cho :math:`g'(c) = 0`. Ta lại có

    .. math:: 

        g'(x) = f'(x) - \dfrac{f(b) - f(a)}{b - a},

    nên thay :math:`c` và :math:`g'(x)` ta có

    .. math:: 

        0 = g'(c) = f'(c) - \dfrac{f(b) - f(a)}{b - a} \Longleftrightarrow f'(c) = \dfrac{f(b) - f(a)}{b - a}.

Với cách tiếp cận và trình bày như trên thì định lí Lagrange được gọi là *định lí giá trị trung bình*.

Thay đổi cách kí hiệu, đặt :math:`a = x` và :math:`b = x + \Delta x` thì ta có

.. math:: 

    f(x + \Delta x) - f(x) = f'(c) \cdot \Delta x

với :math:`c \in (x, x + \Delta x)`. Lúc này định lí Lagrange được gọi là *định lí về số gia hữu hạn*.

Về mặt hình học có thể thấy :math:`\dfrac{f(b) - f(a)}{b - a}` là hệ số góc của dây cung nối hai điểm :math:`(a, f(a))` và :math:`(b, f(b))` của đồ thị hàm số :math:`y = f(x)`, còn :math:`f'(c)` là hệ số góc của tiếp tuyến tại điểm có hoành độ :math:`x = c` thuộc đường cong. Khi đó định lí Lagrange có ý nghĩa

    Nếu hàm số :math:`f` liên tục trên :math:`[a; b]` và có đạo hàm trên :math:`(a; b)` thì tồn tại điểm :math:`c \in (a; b)` sao cho tiếp tuyến tại điểm :math:`(c, f(c))` song song với dây cung :math:`AB` nối hai điểm :math:`(a, f(a))` và :math:`(b, f(b))`.

.. figure:: ../../figures/calculus/lagrange_theorem.*
    
    Minh hoạ hình học của định lí Lagrange

Ở biểu thức của định lí Lagrange, đặt :math:`g(x) = x` thì :math:`g(b) = b`, :math:`g(a) = a` và :math:`g'(x) = 1` với mọi :math:`x \in (a; b)`. Khi đó ta có

.. math:: 

    f'(c) = \dfrac{f(b) - f(a)}{b - a} \Longleftrightarrow \dfrac{f'(c)}{1} = \dfrac{f'(c)}{g'(c)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}.

Nếu ta thay :math:`g(x)` là một hàm số khả vi tùy ý thì biểu thức này còn đúng không?

.. prf:theorem:: Định lí Cauchy
    :label: thm-cauchy
    
    Nếu :math:`f(x)` và :math:`g(x)` là hai hàm số liên tục trên :math:`[a; b]`, có đạo hàm trên :math:`(a; b)` và :math:`g'(x) \neq 0` với mọi :math:`x \in (a; b)` thì tồn tại :math:`c \in (a; b)` sao cho

    .. math:: 

        \dfrac{f(b) - f(a)}{g(b) - g(a)} = \dfrac{f'(c)}{g'(c)}.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta xét hàm số

    .. math:: 

        h(x) = (f(b) - f(a)) \cdot (g(x) - g(a)) - (g(b) - g(a)) \cdot (f(x) - f(a))

    thì ta có :math:`h(a) = h(b) = 0`. Hơn nữa hàm số :math:`h(x)` cũng liên tục trên :math:`[a; b]` và có đạo hàm trên :math:`(a; b)`. Áp dụng định lí Rolle cho hàm số :math:`h(x)` thì tồn tại số :math:`c \in (a; b)` sao cho :math:`h'(x) = 0`. Vì

    .. math:: 

        h'(x) = (f(b) - f(a)) \cdot g'(x) - (g(b) - g(a)) \cdot f'(x)

    nên suy ra

    .. math:: 

        h'(c) = (f(b) - f(a)) \cdot g'(c) - (g(b) - g(a)) \cdot f'(c) = 0

    và ta có điều phải chứng minh.

.. prf:theorem:: Quy tắc L'Hôpital
    :label: lhopital-rule

    Xét :math:`V` là lân cận của điểm :math:`x_0`, :math:`f(x)` và :math:`g(x)` là hai hàm số liên tục trên :math:`V` và có đạo hàm trên :math:`V \setminus \{ x_0 \}`. Giả sử

    .. math:: 

        f(x_0) = g(x_0) = 0, \ \lim_{x \to x_0} \dfrac{f'(x)}{g'(x)} = a.

    Khi đó ta có

    .. math:: 
        
        \lim_{x \to x_0} \dfrac{f(x)}{g(x)} = a.

Quy tắc L'Hôpital là công cụ khử dạng vô định :math:`\dfrac{0}{0}` rất hiệu quả. Tuy nhiên chúng ta cũng cần chú ý rằng nếu không phải dạng vô định thì quy tắc L'Hôpital không còn đúng.
