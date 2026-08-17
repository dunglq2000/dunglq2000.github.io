=======
Đạo hàm
=======

-------
Đạo hàm
-------

.. prf:definition:: Đạo hàm
    :label: def-derivative
    
    Cho hàm số :math:`f(x)` xác định trên miền :math:`D` và :math:`x_0` là điểm thuộc :math:`D`. Ta nói hàm số :math:`f(x)` có đạo hàm tại :math:`x_0` (hoặc khả vi tại :math:`x_0`) nếu tồn tại giới hạn hữu hạn

    .. math:: 
        :label: der1

        \lim_{x \to x_0}\frac{f(x) - f(x_0)}{x - x_0}.

    Kí hiệu đạo hàm của :math:`f` tại :math:`x_0` là :math:`f'(x_0)`.

Lưu ý rằng nếu giới hạn trên không phải là giới hạn hữu hạn (không tồn tại hoặc tiến tới vô cực) thì hàm số không có đạo hàm tại điểm :math:`x_0`.

.. prf:example:: 
    :label: exp-derivative

    Tính đạo hàm của hàm số :math:`f(x) = x^3 + 2 x^2 - 4` tại :math:`x_0 = 4`.
    
    Ta khai triển

    .. math:: \frac{f(x) - f(x_0)}{x - x_0} = & \frac{f(x) - f(4)}{x - 4} \\ = & \frac{x^3 + 2x^2 - 4 - (4^3 + 2 \cdot 4^2 - 4)}{x - 4} \\ = & \frac{(x^3 - 4^3) + 2(x^2 - 4^2)}{x - 4} \\ = & \frac{(x-4)(x^2 + 4x + 16) + 2 (x-4)(x+4)}{x - 4} \\ = & x^2 + 4 x + 16 + 2(x+4).
        
    Cho :math:`x` tiến tới :math:`4` thì ta có đạo hàm tại :math:`x = 4` là

    .. math:: f'(4) = & \lim_{x \to 4} \frac{f(x) - f(4)}{x - 4} \\ = & \lim_{x \to 4} (x^2 + 4x + 16 + 2(x+4)) \\ = & 4^2 + 4 \cdot 4 + 16 + 2 \cdot (4 + 4) = 64.
        
.. prf:example:: 
    :label: exp-derivative-2

    Xét hàm số :math:`f(x) = x^2 + 1` trên :math:`\mathbb{R}`. Tìm đạo hàm tại :math:`x_0 \in \mathbb{R}`.

    Ta có 

    .. math:: f(x)-f(x_0) = x^2 + 1 - (x_0^2 + 1) = (x - x_0) (x + x_0).

    Khi đó :math:`\dfrac{f(x)-f(x_0)}{x-x_0} = x + x_0` nên ta có :math:`\displaystyle{\lim_{x \to x_0} (x + x_0) = 2 x_0}`.

Trong định nghĩa ở :eq:`der1`, nếu ta đặt

.. math:: \Delta x = x - x_0, \quad \Delta y = y - y_0 = f(x) - f(x_0),
    
ta gọi :math:`\Delta x` là **số gia của biến** :math:`x`, tương tự :math:`\Delta y` là **số gia của biến** :math:`y`.

Trong định nghĩa, :math:`x` tiến tới :math:`x_0` tương đương với :math:`\Delta x` tiến tới :math:`0`. Chuyển vế :math:`x_0` ta có :math:`x = x_0 + \Delta x` và từ đó :math:`f(x) = f(x_0 + \Delta x)`. Định nghĩa đạo hàm ở trên có thể được viết lại

.. math:: f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}.

Nếu hàm số có đạo hàm tại mọi điểm trên khoảng :math:`(a, b)` thì ta nói hàm số khả vi trên khoảng đó.

Ví dụ đối với hàm số :math:`f(x) = x^3 + 2x^2 - 4` như trên. Với mọi :math:`x_0 \in \mathbb{R}` ta có

.. math:: f'(x_0) = & \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} \\ = & \lim_{x \to x_0} \frac{x^3 + 2x^2 - 4 - (x_0^3 + 2x_0^2 - 4)}{x - x_0} \\ = & \lim_{x \to x_0} \frac{(x^3 - x_0^3) + 2 (x^2 - x_0^2)}{x - x_0} \\ = & \lim_{x \to x_0} (x^2 + x x_0 + x_0^2) + 2 (x + x_0) \\ = & x_0^2 + x_0 \cdot x_0 + x_0^2 + 2 (x_0 + x_0) = 3x_0^2 + 4 x_0.
	
Ta thấy rằng giới hạn trên luôn tồn tại với mọi :math:`x_0 \in \mathbb{R}` nên thay :math:`x_0` thành :math:`x` ta có đạo hàm :math:`f'(x) = 3x^2 + 4x` của :math:`f(x)` trên :math:`\mathbb{R}`.

.. prf:remark:: 
    :label: rmk-diff-and-der

    Từ định nghĩa ta thấy rằng nếu :math:`f(x)` khả vi tại :math:`x_0` thì nó cũng liên tục tại :math:`x_0`. Tuy nhiên chiều ngược lại không đúng. Ví dụ với hàm số :math:`y = \lvert x \rvert`, hàm số liên tục tại :math:`x = 0` nhưng giới hạn (đạo hàm) phải là :math:`1`, còn giới hạn (đạo hàm) trái là :math:`-1`.

Về mặt hình ảnh, khi hàm số khả vi tại một điểm thì đồ thị sẽ "trơn", không gấp khúc tại điểm đó.

.. prf:definition:: Đạo hàm của hàm số trên một nửa khoảng hay một đoạn
    :label: def-derivative-on-segment

    Cho hàm số :math:`f(x)` xác định trên tập :math:`K`, trong đó :math:`K` là một nửa khoảng hay một đoạn.

    Hàm số :math:`f(x)` được gọi là có đạo hàm trên nửa khoảng :math:`K = [a; b)` nếu nó có đạo hàm tại mọi điểm thuộc :math:`(a; b)` và có đạo hàm phải tại :math:`x = a`. Định nghĩa tương tự với :math:`K = [a; +\infty)`.

    Hàm số :math:`f(x)` được gọi là có đạo hàm trên nửa khoảng :math:`K = (a; b]` nếu nó có đạo hàm tại mọi điểm thuộc :math:`(a; b)` và có đạo hàm trái tại :math:`x = b`. Định nghĩa tương tự với :math:`K = (-\infty; b]`.

    Hàm số :math:`f(x)` được gọi là có đạo hàm trên đoạn :math:`[a; b]` nếu nó có đạo hàm tại mọi điểm thuộc khoảng :math:`(a; b)`, có đạo hàm phải tại :math:`x = a` và có đạo hàm trái tại :math:`x = b`.

----------------------
Đạo hàm của hàm số hợp
----------------------

.. prf:theorem:: 
    :label: thm-derivative-comb
    
    Nếu hàm số :math:`h = h(x)` có đạo hàm tại điểm :math:`x_0` và hàm số :math:`y = g(h)` có đạo hàm tại điểm :math:`h_0 = h(x_0)` thì hàm số hợp :math:`f(x) = g(h(x))` có đạo hàm tại điểm :math:`x_0` và

    .. math:: f'(x) = g'(h_0) \cdot h'(x_0).

Nếu giả thiết trên đúng với mọi điểm :math:`x` thuộc tập xác định :math:`J` thì hàm số hợp :math:`y = f(x)` có đạo hàm trên :math:`J` và

.. math:: f'(x) = g'(h(x)) \cdot h'(x).

Công thức trên còn được viết gọn là

.. math:: f'_x = g'_h \cdot h'_x.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Theo định nghĩa đạo hàm thì

    .. math:: 
        h(x_0 + a) - h(x_0) = h'(x_0) \cdot a + \varepsilon(a) \cdot a,

    với :math:`\varepsilon(a) \to 0` khi :math:`a \to 0`. Ở đây :math:`a` đóng vai trò như :math:`\Delta x` trong định nghĩa.

    Tương tự cho hàm :math:`g` ta có

    .. math:: 
        g(h(x_0) + b) - g(h(x_0)) = g'(h(x_0)) \cdot b + \eta(b) \cdot b,

    với :math:`\eta(b) \to 0` khi :math:`b \to 0`.

    Bây giờ xét

    .. math:: 

        g(h(x_0 + a)) - g(h(x_0)) & = g(h(x_0) + h'(x_0) \cdot a + \varepsilon(a) \cdot a) - g(h(x_0)) \\
        & = g(h(x_0) + c) - g(h(x_0)) = g'(h(x_0)) \cdot c + \eta(c) \cdot c
        
    với :math:`h'(x_0) \cdot a + \varepsilon(a) \cdot a = c`.

    Ta thấy rằng khi :math:`a \to 0` thì :math:`\dfrac{c}{a} \to h'(x_0)` và :math:`c \to 0`, như vậy :math:`\eta(n) \to 0`.

    Từ đây suy ra

    .. math:: \dfrac{g(h(x_0 + a)) - g(h(x_0))}{a} \to g'(h(x_0)) \cdot \dfrac{c}{a} + 0 \to g'(h(x_0)) \cdot h'(x_0)

    khi :math:`a \to 0`.

------------------------
Đạo hàm của hàm số ngược
------------------------

Giả sử hàm số :math:`f: I \to J` là một hàm khả nghịch, nghĩa là có hàm ngược. Khi đó nếu :math:`f` có đạo hàm khác :math:`0` tại điểm :math:`f^{-1}(x_0)` thì :math:`f^{-1}` cũng có đạo hàm tại điểm :math:`x_0` theo đẳng thức

.. math:: (f^{-1})'(x_0) = \dfrac{1}{f'(f^{-1}(x_0))}.

Chúng ta sẽ không chứng minh ở đây vì chứng minh khá phức tạp.

Về mặt hình học, vì đồ thị của hàm số :math:`y = f(x)` và :math:`y = f^{-1}(x)` đối xứng với nhau qua đường thẳng :math:`y = x` nên theo công thức trên, nếu hệ số góc của tiếp tuyến đồ thị hàm số :math:`y = f(x)` tại điểm :math:`(x_0, y_0)` là :math:`k` thì hệ số góc của tiếp tuyến đồ thị hàm số :math:`y = f^{-1}(x)` tại điểm :math:`(y_0, x_0)` là :math:`\dfrac{1}{k}`.

-------
Vi phân
-------

Trong cách kí hiệu

.. math:: f'(x) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x},

ta thay :math:`\Delta y` thành :math:`dy` và :math:`\Delta x` thành :math:`dx` thì vi phân được định nghĩa là 

.. math:: f'(x) = \frac{dy}{dx} \Leftrightarrow dy = f'(x)\, dx.

Cách kí hiệu vi phân có ý nghĩa là vế trái là vi phân theo biến :math:`y` và vế phải là vi phân theo biến :math:`x`. Do :math:`y = f(x)` nên khi vi phân hai vế sẽ cho ra :math:`dy = f'(x)\, dx` (vế trái là đa thức bậc :math:`1` theo biến :math:`y`).

Ví dụ phương trình :math:`y^2 = x^3 + 4x - 7` thì khi vi phân hai vế ta có

.. math:: (y^2)' \, dy = (x^3 + 4x - 7) \, dx \Longleftrightarrow 2y \, dy = (3x^2 + 4) \, dx.
