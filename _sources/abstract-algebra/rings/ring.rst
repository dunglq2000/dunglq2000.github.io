====
Vành
====

.. prf:definition:: Vành
    :label: def-ring

    Cho tập hợp :math:`R`, trên đó ta định nghĩa hai toán tử **cộng** (kí hiệu là :math:`+`) và **nhân** (kí hiêu là :math:`\times`).

    Khi đó, :math:`(R, +, \times)` tạo thành **vành** (hay **ring**, **кольцо**) nếu

    1. :math:`(R, +)` là nhóm Abel.
    2. :math:`(R, \times)` có tính kết hợp với phép nhân: với mọi :math:`a, b, c \in R` thì :math:`a \times (b \times c) = (a \times b) \times c`.
    3. Tính phân phối của phép cộng và phép nhân: với mọi :math:`a, b, c \in R` thì :math:`(a + b) \times c = a \times c + b \times c`.

Tóm lại, :math:`(R, +, \times)` là vành nếu nó là nhóm Abel đối với phép cộng và có tính kết hợp với phép nhân.

Ta thường kí hiệu :math:`0_R` (hoặc ngắn gọn là :math:`0`) là phần tử đơn vị của phép cộng :math:`(R, +)` và gọi là **phần tử trung hòa**.

Khi đó phần tử nghịch đảo của phép cộng gọi là **phần tử đối** và được kí hiệu là :math:`-a`, chỉ phần tử đối của phần tử :math:`a`.

.. prf:remark:: 
    :label: rmk-ring
    
    Phép nhân ở đây không nhất thiết có phần tử đơn vị, hay phần tử nghịch đảo như trong định nghĩa nhóm. Trong trường hợp này :math:`(R, \times)` gọi là **semigroup** (hay **nửa nhóm**).

.. prf:property:: Tính chất của vành
    :label: prop-ring

    1. Với mọi :math:`a \in R` thì :math:`a \times 0_R = 0_R \times a = 0_R`.
    2. Với mọi :math:`a, b \in R` thì :math:`(-a) \times b = -(a \times b)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh hai tính chất trên ta dùng định nghĩa vành.

    1. Với mọi :math:`a \in R`, ta có

    .. math:: a \times 0_R = a \times (0_R + 0_R) = a \times 0_R + a \times 0_R.

    Rút gọn :math:`a \times 0_R` hai vế ta có :math:`a \times 0_R = 0_R`. Tương tự cho :math:`0_R \times a = 0_R`.

    2. Vì :math:`(-a) + a = 0_R` với mọi :math:`a \in R`, nhân :math:`b` hai vế và dùng tính chất đầu suy ra

    .. math:: (-a) \times b + a \times b = 0_R \times b = 0_R.

    Chuyển vế ta có :math:`(-a) \times b = - (a \times b)`.

.. prf:definition:: Vành với đơn vị

    Nếu có phần tử :math:`1_R \neq 0_R \in R` sao cho với mọi :math:`r \in R` ta đều có

    .. math:: 1_R \times r = r \times 1_R = r

    thì :math:`1_R` được gọi là **phần tử đơn vị** đối với phép nhân và :math:`R` được gọi là **vành với đơn vị** (hay **ring with identity**, **кольцо с единицей**).

Ta kí hiệu :math:`1_R` (hoặc ngắn gọn là :math:`1`) là **phần tử đơn vị** đối với phép nhân :math:`(R, \times)`.

Từ phần tử đơn vị đối với phép nhân ta có khái niệm **đặc số** (hay **số đặc trưng**, **characteristic**) của vành với đơn vị.

.. prf:definition:: Characteristic
    :label: def-ring-char
    
    Xét trường :math:`R` với phần tử đơn vị là :math:`1` và phần tử trung hòa là :math:`0`. Số dương :math:`p` nhỏ nhất sao cho

    .. math:: \underbrace{1 + 1 + \ldots + 1 + 1}_{p \text{ lần}} = 0

    được gọi là **đặc số** (hay **characteristic**, **характеристика**) của :math:`R`.

.. prf:definition:: Vành giao hoán
    :label: def-commutative-ring

    Nếu ta có tính giao hoán đối với phép nhân, nghĩa là với mọi :math:`a, b \in R` đều thỏa

    .. math:: a \times b = b \times a,

    thì ta nói :math:`R` là **vành giao hoán** (hay **commutative ring**, **коммутативное кольцо**).
