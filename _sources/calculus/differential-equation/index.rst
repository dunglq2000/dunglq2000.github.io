*********************
Phương trình vi phân
*********************

=============================
Phương trình vi phân bậc nhất
=============================

Phương trình vi phân bậc nhất có dạng:

.. math:: 

    P(x, y)\,dx + Q(x, y)\,dy = 0.

Nghiệm tổng quát có dạng :math:`y = \varphi(x, c)` khả vi và thỏa mãn điều kiện của phương trình vi phân.

1. Hàm :math:`\varphi(x, c)` là nghiệm của phương trình vi phân với hằng số :math:`c`.
2. Nếu :math:`y(x_0) = y_0` thì có thể tìm được :math:`c_0`. Khi đó nghiệm được gọi là **nghiệm riêng** :math:`y = \varphi(x, c_0)`.

.. prf:definition:: Phương trình tách biến
    :label: def-pt-tach-bien

    **Phương trình tách biến** (hay **разделяющие переменные**) là phương trình có dạng:

    .. math:: 

        P_1(x) \cdot Q_1(y) \, dx + P_2(x) \cdot Q_2(y) \, dy = 0.

Để giải phương trình tách biến ta chia hai vế cho :math:`Q_1(y) \cdot P_2(x) \neq 0` và giải

.. math:: 

    \int \frac{P_1(x)}{P_2(x)} \, dx + \int \frac{Q_2(y)}{Q_1(y)} \, dy = 0.

Nếu :math:`Q_1(y) \cdot P_2(x) = 0` thì ta giải từng hàm riêng :math:`Q_1(y) = 0` hoặc :math:`P_2(x) = 0`.

.. prf:definition:: Hàm thuần nhất bậc :math:`n`
    :label: def-ham-thuan-nhat-n

    Hàm thuần nhất bậc :math:`n` với tham số :math:`\lambda` bất kì ta luôn có :math:`f(\lambda x, \lambda y) = \lambda^n f(x, y)`.

Ví dụ, :math:`f(x, y) = x^2 - 2xy`. Với các hàm thuần nhất ta có định nghĩa phương trình vi phân thuần nhất.

.. prf:definition:: Phương trình vi phân thuần nhất
    :label: def-ptvp-thuan-nhat
    
    Phương trình vi phân :math:`y' = f(x, y)` được gọi là thuần nhất nếu hàm :math:`f(x, y)` là hàm thuần nhất bậc :math:`0`. Khi đó :math:`y' = \varphi\left(\dfrac{y}{x}\right)`.

Để giải dạng này ta đặt :math:`\dfrac{y}{x} = u`. Như vậy :math:`y = ux` và :math:`y' = u'x + ux'`.

=================================================
Phương trình tuyến tính và phương trình Bernoulli
=================================================

.. prf:definition:: Phương trình vi phân tuyến tính
    :label: def-ptvp-tuyen-tinh
    
    Phương trình vi phân được gọi là tuyến tính bậc nhất nếu nó có dạng :math:`y' + p(x) \cdot y = g(x)`.

Để giải phương trình tuyến tính ta có hai phương pháp là phương pháp Bernoulli và phương pháp Lagrange.

Đối với phương pháp Bernoulli, ta đặt :math:`y = uv` với :math:`u = u(x)` và :math:`v = v(x)` là một hàm được chọn từ lớp các hàm thỏa mãn với hằng số cố định. Khi đó :math:`y' = u'v + uv'`.

Phương trình vi phân khi này có dạng:

.. math:: 
    
    & y' + p(x) \cdot y = g(x) \\
    \Leftrightarrow & u'v + v'u + p(x) \cdot u v = g(x) \\
    \Leftrightarrow & u'v + u(v' + p(x) \cdot v) = g(x)

Ta chọn :math:`v` sao cho :math:`v' + p(x) \cdot v = 0`. Điều này tương đương với :math:`\dfrac{dv}{dx} + p(x) \cdot v = 0` nên :math:`\ln \lvert v \rvert = -\int p(x)\, dx + \ln \lvert C \rvert`. Ở đây :math:`C` là hằng số.

Để đơn giản, ta chọn :math:`C = 1` thì :math:`v = e^{-\int p(x) \, dx}`.

Suy ra :math:`u'v = u' e^{-\int p(x)\, dx} = g(x)` và biến đổi

.. math:: 
    
    & \frac{du}{dx} \cdot e^{-\int p(x) \, dx} = g(x) \\
    \Longleftrightarrow \ & u = \int g(x) \cdot e^{-\int p(x) \, dx} \, dx + C \\
    \Longleftrightarrow \ & y = uv = \ldots
    
Đối với phương pháp Lagrange, ta xét phương trình vi phân tuyến tính thuần nhất tương ứng với :math:`y' + p(x) \cdot y = g(x)` là :math:`y' + p(x) \cdot y = 0`.

Khi đó ta biến đổi :math:`\dfrac{dy}{dx} = -p(x) \cdot y` và giải được :math:`y = c e^{-\int p(x)\,dx}` với :math:`c` là hằng số.

Ta thay :math:`c` bởi :math:`c(x)` là hàm theo :math:`x`:

.. math:: 
    
    & y = c(x) \cdot e^{-\int p(x)\,dx} \\
    \Longleftrightarrow \ & y' = c'(x) \cdot e^{-\int p(x)\,dx} + c(x) \cdot e^{-\int p(x)\,dx} \cdot (-p(x))

và thay vào phương trình vi phân ban đầu:

.. math:: 
    
    & c'(x) \cdot e^{-\int p(x)\,dx} + \cancel{c(x) \cdot e^{-\int p(x)\,dx} \cdot (-p(x))} + \cancel{c(x) \cdot e^{-\int p(x)\,dx} \cdot p(x)} = g(x) \\
    \Longleftrightarrow \ & c'(x) \cdot e^{-\int p(x)\,dx} = g(x) \\
    \Longleftrightarrow \ & d c(x) = e^{\int p(x)\,dx} \cdot g(x)\,dx.

Tới đây ta tìm được :math:`c(x)` để có :math:`y`.

.. prf:example:: 
    :label: exp-pt-tttn

    Giải phương trình vi phân

    .. math:: y\,dx = (y^2 - x)\,dy.

    Đầu tiên ta biến đổi phương trình

    .. math::
        :label: eq-tttn

        y\,dx = (y^2 - x)\,dy \Longleftrightarrow & \, \frac{dx}{dy} + \frac{x}{y} = y \\ \Longleftrightarrow & \, x' + \frac{1}{y} = y.

    Đối với phương pháp Bernoulli, đặt :math:`x = uv` với :math:`u = u(y)` và :math:`v = v(y)`. Khi đó ta có :math:`x' = u'v + uv'`.

    Từ :eq:`eq-tttn` suy ra

    .. math:: 

        & u'v + v'u + \frac{1}{y} \cdot uv = y \\
        \Longleftrightarrow & u'v + u \left(v' + \frac{1}{y} \cdot v\right) = y.
    
    Ta tìm :math:`v` sao cho :math:`v' + \dfrac{1}{y} v = 0`, tương đương với

    .. math::

        \frac{dv}{dy} = -\frac{v}{y} \Longleftrightarrow \cdots \Longleftrightarrow v = \frac{1}{y}.

    Thay vào :eq:`eq-tttn` ta được

    .. math::

        u'v = u' \cdot \frac{1}{y} = y \Longleftrightarrow u' = y^2 \Longrightarrow u = \frac{y^3}{3} + C.

    Như vậy

    .. math::

        x = uv = \left(\frac{y^3}{3} + c\right) \cdot \frac{1}{y} = \frac{y^2}{3} + \frac{C}{y}.

    Đối vơi phương pháp Lagrange, ta xét dạng tuyến tính thuần nhất là :math:`x' + \dfrac{1}{y} \cdot x = 0`.

    Khi đó

    .. math:: \frac{dx}{x} = -\frac{dy}{y} \Longleftrightarrow x = \frac{c}{y}

    với :math:`c` là hằng số. Bây giờ thay :math:`c` thành :math:`c(y)` ta có :math:`x = \dfrac{c(y)}{y}`.

    Thay vào :eq:`eq-tttn` ta có

    .. math:: 

        & \, \frac{c'(y) y - c(y)}{y^2} + \frac{1}{y} \cdot \frac{c(y)}{y} = y \\
        \Longleftrightarrow & \, \frac{c'(y)}{y} - \cancel{\frac{c(y)}{y^2}} + \cancel{\frac{c(y)}{y^2}} = y \\
        \Longrightarrow & \, c(y) = \int\limits y^2\,dy = \frac{y^3}{3} + C.

    Như vậy ta có kết quả

    .. math:: x = \frac{c(y)}{y} = \left(\frac{y^3}{3} + C\right) \cdot \frac{1}{y} = \frac{y^2}{3} + \frac{C}{y}.

.. prf:definition:: Phương trình Bernoulli
    :label: def-pt-bernoulli
    
    Phương trình Bernoulli là phương trình có dạng:

    .. math::
        
        y' + p(x) \cdot y = g(x) \cdot y^n, \ n \in \mathbb{N}, n \neq 0, n \neq 1.

Khi :math:`n = 0` thì phương trình trở thành phương trình tuyến tính.

Để giải phương trình Bernoulli ta chia hai vế cho :math:`y^n` thì được:

.. math:: 

    \frac{y'}{y^n} + \frac{p(x)}{y^{n-1}} = g(x).

Đặt :math:`\dfrac{1}{y^{n-1}} = z` thì

.. math:: 
    
    z' = \dfrac{dz}{dx} = (1-n) \dfrac{1}{y^n} y'.

Như vậy :math:`\dfrac{1}{y^n} \cdot y' = \dfrac{z'}{1-n}` và thay vào phương trình ban đầu ta có

.. math:: 

    \frac{1}{1-n} z' + p(x) \cdot z = g(x).

Từ đây ta giải phương trình tuyến tính.

=================================================
Phương trình vi phân toàn phần. Nhân tử tích phân
=================================================

.. prf:definition:: Phương trình vi phân toàn phần
    :label: def-ptvp-toan-phan

    Phương trình vi phân được gọi là **toàn phần** (hay **уравнение в полных дифферециалах**) nếu vế trái có vi phân toàn phần là hàm :math:`u(x, y)`, nghĩa là:

    .. math::

        P(x, y) \, dx + Q(x, y) \, dy = d u(x, y).

.. prf:theorem:: 
    :label: thm-conditions-ptvp-toan-phan

    Điều kiện cần và đủ để biểu thức

    .. math:: 

        \Delta = P(x, y) \,dx + Q(x, y)\,dy,

    với :math:`P(x,y)` và :math:`Q(x,y)` và đạo hàm riêng :math:`\dfrac{\partial P}{\partial y}` và :math:`\dfrac{\partial Q}{\partial x}` liên tục trên tập :math:`D` nào đó, là phương trình vi phân toàn phần:

    .. math::

        \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh điều kiện cần, đặt :math:`\Delta` là biểu thức có vi phân toàn phần, nghĩa là

    .. math:: 
        
        & P(x, y) \, dx + Q(x, y) \, dy = d u(x, y) \\
        \Longleftrightarrow \ & d u(x, y) = \frac{\partial u}{\partial x} \, dx + \frac{\partial u}{\partial y} \, dy,

    với :math:`P(x, y) = \dfrac{\partial u}{\partial x}` và :math:`Q(x, y) = \dfrac{\partial u}{\partial y}`.

    Suy ra :math:`\dfrac{\partial P}{\partial y} = \dfrac{\partial^2 u}{\partial x \partial y}` và :math:`\dfrac{\partial Q}{\partial x} = \dfrac{\partial^2 u}{\partial y \partial x}`.

    Khi đó :math:`\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}` và ta có điều phải chứng minh.

    Để chứng minh điều kiện đủ, trên tập :math:`D` ta có :math:`\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}`.

    Lúc này ta chứng minh tồn tại hàm :math:`u(x, y)` trên :math:`D` mà

    .. math:: 
        
        d u(x, y) = P(x, y)\,dx + Q(x, y)\,dy.

    Giả sử ngược lại, :math:`\dfrac{\partial u}{\partial x} = P(x, y)` và :math:`\dfrac{\partial u}{\partial y} = Q(x, y)`.

    Ở đây, ta cố định :math:`y` và lấy tích phân theo :math:`x` thì được:

    .. math:: 

        u(x, y) = \int P(x, y)\,dx + \varphi(y),

    với :math:`c = \varphi(y)` là hằng số (do :math:`y` cố định nên :math:`\varphi(y)` cũng cố định). Suy ra ta có:

    .. math::
        
        \frac{\partial u}{\partial y} = \left( \int P(x, y)\,dx\right)'_y + \varphi'(y) \\
        \Longleftrightarrow Q(x, y) = \left( \int P(x, y)\,dx\right)'_y + \varphi'(y) \\
        \Longleftrightarrow \varphi'(y) = Q(x, y) - \left( \int P(x, y)\,dx\right)'_y.

    Vế phải khi đạo hàm theo :math:`x` là:

    .. math:: 
        
        & \frac{\partial}{\partial x}\left( Q(x, y) - \frac{\partial}{\partial y} \left(\int P(x, y)\,dx\right) \right) \\
        = & \frac{\partial Q}{\partial x} - \frac{\partial}{\partial x}\left( \frac{\partial}{\partial y} \left( \int P(x, y)\,dx \right) \right) \\
        = & \frac{\partial Q}{\partial x} - \frac{\partial}{\partial y}\left( \frac{\partial}{\partial x} \left( \int P(x, y)\,dx \right) \right) \\
        = & \frac{\partial Q}{\partial x} - \frac{\partial}{\partial y} (P) = 0,

    từ đây suy ra:

    .. math:: 

        \varphi(y) = \int \left( Q(x, y) - \frac{\partial}{\partial y} \left(\int P(x, y)\,dx\right) \right)\,dy + c,

    với :math:`c` là hằng số.

    Khi điều kiện :math:`\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}` không thỏa mãn, ta nhân thêm hàm :math:`t(x, y)` để thỏa điều kiện:

    .. math:: 

        \frac{\partial}{\partial y}(t(x, y) \cdot P(x, y)) = \frac{\partial}{\partial x} (t(x, y) \cdot Q(x, y)).

    Hàm :math:`t(x, y)` khi đó được gọi là **nhân tử tích phân** (hay **интегрирующий множитель**). Lúc này phương trình biến đổi thành:

    .. math:: 
        
        \frac{\partial t}{\partial y} \cdot P + \frac{\partial P}{\partial y} \cdot t = \frac{\partial t}{\partial x} \cdot Q + \frac{\partial Q}{\partial x} \cdot t \\
        \Longleftrightarrow \frac{\partial t}{\partial y} \cdot P - \frac{\partial t}{\partial x} \cdot Q = t \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right).

    Lúc này ta chỉ cần tìm hàm :math:`t` chỉ phụ thuộc :math:`x` hoặc :math:`y`. Ví dụ với :math:`t = t(x)` ta có thể biến đổi:

    .. math:: 
        
        & -\frac{dt}{dx} Q = t \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) \\
        \Longleftrightarrow \ & \frac{dt}{t} = \frac{\partial P / \partial y - \partial Q / \partial x}{Q} \, dx \\
        \Longleftrightarrow \ & t(x) = \exp\left(\int \frac{\partial P / \partial y - \partial Q / \partial x}{Q} \, dx \right).

    Tương tự, :math:`\displaystyle t(y) = \exp \left( \int \frac{\partial Q / \partial x - \partial P / \partial y}{P} \, dy \right)`.

=================================
Phương trình Lagrange và Clairaut
=================================

.. prf:definition:: Phương trình Lagrange
    :label: def-pt-lagrange

    Phương trình Lagrange (уравнение Лагранжа) là phương trình có dạng:

    .. math:: 

        y = x \varphi(y') + \psi(y'),

    với :math:`\varphi` và :math:`\psi` là hai hàm số với :math:`y' = \dfrac{dy}{dx}`.

Để giải phương trình Lagrange ta đặt :math:`p = y'`. Khi đó :math:`y = x \varphi(p) + \psi(p)`. Lấy vi phân hai vế ta có:

.. math:: 
    
    \frac{dy}{dx} & = \varphi(p) + x \varphi'(p) p'+ \psi'(p) p' \\
    & = \varphi(p) + x \varphi'(p) \frac{dp}{dx} + \psi'(p) \frac{dp}{dx}.

Thay vào điều kiện ban đầu ta được:

.. math:: 

    (p - \varphi(p)) \frac{dx}{dp} - x \varphi'(x) = \psi'(p).

Đây là phương trình vi phân tuyến tính theo :math:`x = x(p)`.

Giải phương trình tìm được :math:`x = \lambda(p, c)` với :math:`c` là hằng số, thay lại điều kiện :math:`p = y'` tìm được :math:`y = \gamma(x, c)`.

Chú ý rằng khi thay vào điều kiện ban đầu ta chia cho :math:`dp` nên trước đó phải xét trường hợp :math:`dp = 0`, nói cách khác :math:`p = p_0` là hằng số và :math:`p - \varphi(p) = 0`.

Nghiệm :math:`y = x \varphi(p_0) + \psi(p_0)` gọi là **nghiệm đặc trưng** (hay **особое решение**).

.. prf:definition:: Phương trình Clairaut
    :label: def-pt-clairaut
    
    Phương trình Clairaut (уравнение Клеро) có dạng:

    .. math:: 

        y = x y' + \psi(y').

Đây là phương trình Lagrange khi :math:`\varphi(y') = y'`.

Để giải phương trình này, đặt :math:`y' = p` thì :math:`y = xp + \psi(p)`. Khi đó:

.. math:: 
    
    & \frac{dy}{dx} = p + xp' + \psi'(p) p' \\
    \Longleftrightarrow \ & p = p + x \frac{dp}{dx} + \psi'(p) \frac{dp}{dx} \\
    \Longleftrightarrow \ & (x + \psi'(p)) \frac{dp}{dx} = 0. 

Nếu :math:`\dfrac{dp}{dx} = 0` thì :math:`p = c` là hằng số. Nghiệm tổng quát là :math:`y = cx + \psi(c)`.

Nếu :math:`x + \psi'(p) = 0` thì :math:`x = -\psi'(p)`. Suy ra :math:`y = xp + \psi(p)`  là nghiệm đặc trưng và không có dạng tổng quát.
