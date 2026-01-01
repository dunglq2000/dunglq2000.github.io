Đạo hàm riêng
=============

Đạo hàm riêng
-------------

.. prf:definition:: 
   :label: def-partial-derivative

   Xét hàm :math:`z = f(x, y)` xác định trên :math:`D` và điểm :math:`M_0(x_0, y_0) \in D`.

   1. Cho :math:`x` thay đổi, cố định :math:`y = y_0`, ta có hàm theo biến :math:`x`. Nếu hàm số có đạo hàm tại :math:`x = x_0` thì đạo hàm đó được gọi là **đạo hàm riêng** (hay **partial derivative**) của :math:`z` theo :math:`x`, kí hiệu là :math:`z'_x` hoặc :math:`\dfrac{\partial z}{\partial x}`. Đặt 

      .. math:: \Delta_x z = f(x_0 + \Delta x, y_0) - f(x_0, y_0)

      thì

      .. math:: \frac{\partial z}{\partial x} = \lim_{\Delta x \to 0} \frac{\Delta_x z}{\Delta x}.

   2. Tương tự, đạo hàm riêng của :math:`z` đối với :math:`y` tại :math:`(x_0, y_0)` là :math:`\dfrac{\partial z}{\partial y}`.

Vi phân toàn phần
-----------------

Nếu số gia

.. math:: \Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)

có thể biểu diễn dưới dạng

.. math:: \Delta z = A \cdot \Delta x + B \cdot \Delta y + \alpha \beta,

trong đó :math:`A`, :math:`B` không phụ thuộc :math:`\Delta x`, :math:`\Delta y`; :math:`\alpha \to 0` khi 

.. math:: \beta = \sqrt{(\Delta x)^2 + (\Delta y)^2} \to 0

thì ta nói hàm số :math:`z` khả vi tại :math:`(x_0, y_0)`. Phần chính bậc nhất

.. math:: dz = A \cdot \Delta x + B \cdot \Delta y

được gọi là **vi phân toàn phần** của :math:`z = f(x, y)` tại :math:`(x_0, y_0)`.

.. note:: 

   - nếu :math:`z` khả vi tại mọi điểm của :math:`D` thì nó khả vi trên :math:`D`;
   - :math:`dz` là phần chính của :math:`\Delta z`.
   
.. prf:theorem:: 
   :label: thm-partial-der-1

   Nếu :math:`z` khả vi tại :math:`M_0(x_0, y_0)` thì tồn tại :math:`z_x'(M_0)`, :math:`z_y'(M_0)` và 

   .. math:: dz = z_x'(M_0) \Delta x + z_y'(M_0) \Delta y.

.. prf:theorem:: 
   :label: thm-partial-der-2

   Nếu :math:`z = f(x, y)` có các đạo hàm riêng ở lân cận của :math:`M_0(x_0, y_0)` và các đạo hàm riêng ấy liên tục tại :math:`M_0(x_0, y_0)` thì :math:`f(x, y)` khả vi tại :math:`M_0(x_0, y_0)` và 

   .. math:: dz = z_x' \Delta x + z_y' \Delta y.

.. prf:example:: 
   :label: exp-partial-der-1

   Cho :math:`z = x^2 e^y + y^3`. Khi đó :math:`z_x' = 2x e^y`, :math:`z_y' = x^2 e^y + 3y^2`
   
   .. math:: \Longrightarrow dz = 2x e^y \, dx + (x^2 e^y + 3y^2) \, dy.

Đạo hàm một số hàm nhiều biến
=============================

Hàm số cho giá trị là số vô hướng
---------------------------------
	
Giả sử ta có vector hàng :math:`\bm{x} = (x_1, \ldots, x_n)` và hàm số :math:`f` có biến là vector :math:`\bm{x}`. Nói cách khác là :math:`f: \mathbb{R}^n \to \mathbb{R}`, :math:`f(\bm{x}) = f(x_1, \ldots, x_n)`.

Khi đó đạo hàm riêng của hàm :math:`f` theo vector :math:`\bm{x}` cũng là một vector (nếu :math:`\bm{x}` là vector hàng thì đạo hàm riêng cũng là vector hàng và ngược lại) và được kí hiệu

.. math:: 

    \nabla f(\bm{x}) = \begin{pmatrix}
        \dfrac{\partial f}{\partial x_1} & \cdots & \dfrac{\partial f}{\partial x_n}
    \end{pmatrix}

Ví dụ, đối với hàm tuyến tính

.. math:: 
    
    f(\bm{x}) = a_1 x_1 + \ldots + a_n x_n = \bm{a} \cdot \bm{x}^\top

thì ta thấy rằng :math:`\dfrac{\partial f}{\partial x_i} = a_i`. Khi đó 

.. math:: 
    
    \nabla f (\bm{x}) = \begin{pmatrix}
    \dfrac{\partial f}{\partial x_1} & \cdots & \dfrac{\partial f}{\partial x_n}
    \end{pmatrix} = (a_1, \ldots, a_n) = \bm{a}.

Ta thấy rằng :math:`f(\bm{x}) = \bm{a} \cdot \bm{x}^\top = \bm{x} \cdot \bm{a}^\top`. Do đó

.. math:: 
    
    \nabla (\bm{a} \cdot \bm{x}^\top) = \nabla (\bm{x} \cdot \bm{a}^\top) = \bm{a}.

Đạo hàm riêng cấp hai được cho bởi ma trận được gọi là ma trận Hessian.

.. math::

    \nabla^2 f(\bm{x}) = \begin{pmatrix}
        \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1 x_n} \\ \dfrac{\partial^2 f}{\partial x_2 x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2 x_n} \\ \cdots & \cdots & \ddots & \cdots \\ \dfrac{\partial^2 f}{\partial x_n x_1} & \dfrac{\partial^2 f}{\partial x_n x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
    \end{pmatrix}.

Theo tính chất của đạo hàm riêng cấp hai có thể thấy ma trận trên là ma trận đối xứng.

Nếu đầu vào là một ma trận, hay :math:`f: \mathbb{R}^{n \times m} \to \mathbb{R}`, :math:`f(\bm{X})` thì ta làm tương tự

Giả sử

.. math:: 
    
    \bm{X} = \begin{pmatrix}
    x_{11} & x_{12} & \cdots & x_{1m} \\ x_{21} & x_{22} & \cdots & x_{2m} \\ \cdots & \cdots & \ddots & \cdots \\ x_{n1} & x_{n2} & \cdots & x_{nm}
    \end{pmatrix}.

Khi đó đạo hàm của hàm :math:`f` theo ma trận :math:`\bm{X}` là

.. math:: 

    \nabla f(\bm{X}) = \begin{pmatrix}
        \dfrac{\partial f}{\partial x_{11}} & \dfrac{\partial f}{\partial x_{12}} & \cdots & \dfrac{\partial f}{\partial x_{1m}} \\ \dfrac{\partial f}{\partial x_{21}} & \dfrac{\partial f}{\partial x_{22}} & \cdots & \dfrac{\partial f}{\partial x_{2m}} \\ \cdots & \cdots & \ddots & \cdots \\ \dfrac{\partial f}{\partial x_{n1}} & \dfrac{\partial f}{\partial x_{n2}} & \cdots & \dfrac{\partial f}{\partial x_{nm}}
    \end{pmatrix}.

Như vậy đạo hàm theo ma trận cũng là ma trận cùng cỡ với ma trận đầu vào.

Hàm số cho giá trị là vector
----------------------------

Xét hàm vector

.. math:: 
    
    F(\bm{x}) = (f_1(\bm{x}), f_2(\bm{x}), \ldots, f_m(\bm{x}))

với :math:`\bm{x} = (x_1, x_2, \ldots, x_n) \in \mathbb{R}^n` và các hàm :math:`f_i (\bm{x})` là hàm từ :math:`\mathbb{R}^n` tới :math:`\mathbb{R}`. Khi đó hàm vector :math:`F` là hàm từ :math:`\mathbb{R}^n` tới :math:`\mathbb{R}^m`.

Nếu :math:`f_i` là các hàm tuyến tính như trên thì hàm :math:`F` là một ánh xạ tuyến tính, hay tương đương với phép nhân ma trận :math:`F(\bm{x}) = \bm{x} \cdot \bm{A}`. Ở đây :math:`\bm{x}` là vector hàng, còn :math:`\bm{A}` là ma trận :math:`n \times m`.

.. math:: 
    
    \bm{A} = \begin{pmatrix}
    a_{11} & a_{21} & \cdots & a_{m1} \\ a_{12} & a_{22} & \cdots & a_{m2} \\ \cdots & \cdots & \ddots & \cdots \\ a_{1n} & a_{2n} & \cdots & a_{mn}
    \end{pmatrix}.

Ở đây,

.. math:: 
    
    f(\bm{x}) = f_i(x_1, x_2, \ldots, x_n) = a_{i1} x_1 + a_{i2} x_2 + \ldots + a_{in} x_n.

Nếu đặt :math:`\bm{a}_i = (a_{i1}, a_{i2}, \ldots, a_{in})` thì ma trận :math:`\bm{A}` có các cột là :math:`\bm{a}_i^\top`. Nói cách khác

.. math:: 
    
    \bm{A} = \begin{pmatrix}
        \bm{a}_1^\top & \bm{a}_2^\top & \cdots & \bm{a}_m^\top
    \end{pmatrix}.

Nếu ta xét từng cột của ma trận :math:`\bm{A}` thì hoàn toàn giống trường hợp trên. Giả sử với cột đầu tiên (ứng với :math:`f_1`) ta có

.. math:: 
    
    f_1 (\bm{x}) = \begin{pmatrix}
    x_1 & x_2 & \cdots & x_n
    \end{pmatrix} \cdot \begin{pmatrix}
    a_{11} \\ a_{12} \\ \vdots \\ a_{1n}\end{pmatrix} = \bm{x} \cdot \bm{a}_1^\top.

Đạo hàm của :math:`f_1` theo vector :math:`\bm{x}` là

.. math:: 
    
    \nabla f_1 (\bm{x}) = \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} 
    \end{pmatrix} = \bm{a_1}.

Xếp các hàm :math:`f_i` từ trên xuống dưới, ta có được đạo hàm của hàm :math:`F` theo vector :math:`\bm{x}` là 

.. math::

    \nabla F(\bm{x}) = \begin{pmatrix}
        \nabla f_1 (\bm{x}) \\ \nabla f_2 (\bm{x}) \\ \vdots \\ \nabla f_m(\bm{x})
    \end{pmatrix}  = \begin{pmatrix}
    \bm{a}_1 \\ \bm{a}_2 \\ \vdots \\ \bm{a}_m
    \end{pmatrix} = \bm{A}^\top
