===============
Tích phân đường
===============

-------------------------------
Tích phân đường trên mặt phẳng
-------------------------------

Tích phân đường dùng để tính độ dài đường cong :math:`f(x)` trên đoạn :math:`[a; b]` nào đó thuộc tập xác định.

Sau đây mình sẽ dùng tổng vô hạn để giải thích một số công thức tính tích phân đường được học ở trường.

Giả sử mình chia đoạn :math:`[a; b]` thành :math:`n` phần bằng nhau

.. math:: 
    
    a = x_0 < x_1 < \cdots < x_n = b

với :math:`x_{i+1} - x_i = \dfrac{b-a}{n}`.

Gọi các điểm

.. math:: 
    
    L_0 = (x_0, f(x_0) = y_0), \ L_1 = (x_1, f(x_1) = y_1), \ \ldots, L_n = (x_n, f(x_n) = y_n).

Khi đó độ dài đường cong là tổng độ dài các đoạn thẳng :math:`L_0 L_1`, :math:`L_1 L_2`, ..., :math:`L_{n-1} L_n` khi :math:`n` tiến tới vô cùng.

Độ dài đoạn thẳng :math:`L_{i-1} L_i` là khoảng cách từ điểm :math:`(x_{i-1}, f(x_{i-1}))` tới :math:`(x_i, f(x_i))`, nghĩa là

.. math:: 
    
    L_{i-1} L_i = \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2} = \lvert x_i - x_{i-1} \rvert \cdot \sqrt{1 + \left(\frac{y_i - y_{i-1}}{x_i - x_{i-1}}\right)^2}.

Khi :math:`n` tiến tới vô cùng thì :math:`\Delta x = x_i - x_{i-1} = \dfrac{b-a}{n}` tiến tới :math:`0`. Các bạn có thấy biểu thức :math:`\dfrac{y_i - y_{i-1}}{x_i - x_{i-1}}` khi :math:`x_i - x_{i-1}` tiến tới :math:`0` quen không? Chính là định nghĩa đạo hàm :math:`f'(x) = \lim\limits_{\Delta x \to 0} \Delta y / \Delta x` mà chúng ta học ở phổ thông.

Kí hiệu :math:`l` là độ dài đường cong trên. Do :math:`l` là tổng của những đoạn :math:`L_{i-1} L_i` cực nhỏ nên có thể nói 

.. math:: 
    
    l = \underbrace{\Delta l_1}_{L_0 L_1} + \underbrace{\Delta l_2}_{L_1 L_2} + \ldots + \underbrace{\Delta l_n}_{L_{n-1} L_n}

khi :math:`n` tiến tới vô cùng.

Điều này có nghĩa là nếu :math:`y = f(x)` thì chúng ta có

.. math:: 
    
    \Delta l_i = \lvert x_i - x_{i-1} \rvert \cdot \sqrt{1 + \left( \frac{y_i - y_{i-1}}{x_i - x_{i-1}} \right)^2} = \Delta x_i \cdot \sqrt{1 + \left(\Delta y_i / \Delta x_i\right)^2}

với :math:`\Delta y_i = y_{i} - y_{i-1}`, và :math:`\Delta x_i = x_i - x_{i-1}` tiến về :math:`0`. Thay các :math:`\Delta` bởi vi phân ta sẽ có công thức

.. math:: 
    
    \boxed{dl = \sqrt{1 + (dy / dx)^2} \ dx = \sqrt{1 + (f'(x))^2} \ dx.}

Công thức này có thể dùng khi :math:`y` phụ thuộc vào :math:`x` hay :math:`y = f(x)`.

Làm ngược lại quá trình trên, thay :math:`x` thành :math:`y` và :math:`y` thành :math:`x` chúng ta có công thức trên nhưng theo :math:`dy` là

.. math:: 
    
    \boxed{dl = \sqrt{1 + (f'(y))^2} \ dy.}

Vậy còn trường hợp :math:`x` và :math:`y` là hai hàm số theo tham số :math:`t`? Ví dụ như cung tròn bán kính bằng :math:`1` cho bởi :math:`x = x(t) = \cos(t)` và :math:`y = y(t) = \sin(t)`, trong đó :math:`t \in [a; b] \subset [0, 2\pi]`.

Cách tiếp cận vẫn như vậy, ta chia đoạn :math:`[a; b]` thành :math:`n` phần bằng nhau

.. math:: 
    
    a = t_0 < t_1 < \cdots < t_n = b

với :math:`t_{i+1} - t_i = \dfrac{b-a}{n}`.

Khi đó mỗi đoạn thẳng :math:`L_{i-1} L_i` sẽ có dạng

.. math:: 
    
    
    \Delta l_i & = L_{i-1} L_i = \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2} \\
    & = (t_i - t_{i-1}) \cdot \sqrt{\left(\frac{x_i - x_{i-1}}{t_i - t_{i-1}}\right)^2 + \left(\frac{y_i - y_{i-1}}{t_i - t_{i-1}}\right)^2} \\ 
    & = \Delta t_i \cdot \sqrt{(\Delta x_i / \Delta t_i)^2 + (\Delta y_i / \Delta t_i)^2}.
    

Khi :math:`n` tiến tới vô cực thì :math:`\Delta t_i` tiến về :math:`0`, mà :math:`x` và :math:`y` là các hàm số theo biến :math:`t` nên nói cách khác :math:`\Delta x_i / \Delta t_i` chính là đạo hàm của hàm số :math:`x = x(t)`, tương tự :math:`\Delta y_i / \Delta t_i` là đạo hàm của hàm số :math:`y = y(t)`.

Thay các :math:`\Delta` bởi vi phân thì ta có công thức

.. math:: 
    
    \boxed{dl = \sqrt{(x'(t))^2 + (y'(t))^2} \ dt.}
