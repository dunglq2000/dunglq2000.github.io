=============================
Đạo hàm một số hàm nhiều biến
=============================

---------------------------------
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

----------------------------
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
