Difference và differential
==========================

Ở phần này, kí hiệu :math:`\boxplus` là phép cộng modulo :math:`2^n`, :math:`\boxminus` là phép trừ modulo :math:`2^n`, và :math:`\oplus` là toán tử bitwise-XOR.

Nếu số nguyên :math:`a` có :math:`n` bit và biểu diễn dưới dạng

.. math:: a = a_0 + 2 a_1 + 2^2 a_2 + \cdots + 2^{n-1} a_{n-1}

thì số nguyên :math:`a` tương đương với vector

.. math:: (a_0, a_1, a_2, \ldots, a_{n-1}) \in \mathbb{F}_2^n.

Như vậy, phần tử :math:`a \in \mathbb{Z}_{2^n}` tương đương phần tử :math:`(a_0, a_1, \ldots, a_{n-1}) \in \mathbb{F}_2^n` và các bạn cần lưu ý rằng phép :math:`\boxplus` và :math:`\boxminus` thực hiện trên :math:`\mathbb{Z}_{2^n}`, còn phép XOR thực hiện trên :math:`\mathbb{F}_2^n`.

Cụ thể hơn, giả sử

.. math:: 

    a & = a_0 + 2 a_1 + 2^2 a_2 + \cdots + 2^{n-1} a_{n-1}, \\
    b & = b_0 + 2 b_1 + 2^2 b_2 + \cdots + 2^{n-1} b_{n-1},

thì ta có

.. math:: 

    a \boxplus b = a + b \bmod 2^n, \quad a \boxminus b = a - b \bmod 2^n, \\
    a \oplus b = c = c_0 + 2 c_1 + \cdots 2^{n-1} c_{n-1}, \ \text{với} \ c_i = a_i \oplus b_i.

Ví dụ, với :math:`n = 4`, xét các số nguyên :math:`4` bit là :math:`a = 9` và :math:`b = 11`. Khi đó

.. math:: a \boxplus b = 4, \ a \boxminus b = 14, \ a \oplus b = 2.

Difference (hiệu)
-----------------

Giả sử ta có hàm :math:`f: \mathbb{Z}_{2^n} \to \mathbb{Z}_{2^m}`, khi đó với hai phần tử :math:`a, b \in \mathbb{Z}_{2^n}` thì ta nói

* :math:`b \boxminus a` là hiệu đầu vào;
* :math:`f(b) \boxminus f(a)` là hiệu đầu ra.

Dưới góc độ phá mã, với :math:`\delta \in \mathbb{Z}_{2^n}` và :math:`\Delta \in \mathbb{Z}_{2^m}` cố định, ta xem xét có bao nhiêu cặp :math:`a, b \in \mathbb{Z}_{2^n}` mà

.. math:: b \boxminus a = \delta, \quad f(b) \boxminus f(a) = \Delta.

Chuyển vế ta có các đẳng thức trên tương với

.. math:: b = a \boxplus \delta \Longrightarrow f(b) = f(a \boxplus \delta) = f(a) \boxplus \Delta.

Nói cách khác, ta xem xét xác suất

.. math:: 

   \mathrm{adp}^f(\delta \mapsto \Delta) = \Pr\left[f(a \boxplus \delta) = f(a) \boxplus \Delta\right]

với mọi :math:`a \in \mathbb{Z}_{2^n}`.

Tổng quát, nếu ta xét :math:`k` hiệu đầu vào :math:`\alpha_0`, :math:`\alpha_1`, ..., :math:`\alpha_{k-1}` và hiệu đầu ra :math:`\alpha_k` thì ta quan tâm xác suất

.. math:: 
    
    \mathrm{adp}^f(\alpha_0, \alpha_1, \ldots, \alpha_{k-1} \mapsto \alpha_{k}) = 
    \Pr\left[f(x_0 \boxplus \alpha_0, x_1 \boxplus \alpha_1, \ldots, x_{k-1} \boxplus \alpha_{k-1}) 
    = f(x_0, x_1, \ldots, x_{k-1}) \boxplus \alpha_{k}\right].

.. prf:example:: 
    :label: exp-adp-1

    Xét hàm :math:`f(x, y) = x \oplus y` với :math:`x, y \in \mathbb{Z}_{2^n}`. Với :math:`\alpha`, :math:`\beta` và :math:`\gamma` thuộc :math:`\mathbb{Z}_{2^n}` ta xem xét

    .. math:: \mathrm{adp}^f(\alpha, \beta \mapsto \gamma) = \Pr\left[(x \boxplus \alpha) \oplus (y \boxplus \beta) = (x \oplus y) \boxplus \gamma\right].

Differential (vi sai)
---------------------

Giả sử ta có hàm :math:`f: \mathbb{Z}_{2^n} \to \mathbb{Z}_{2^m}`, khi đó với hai phần tử :math:`a, b \in \mathbb{Z}_{2^n}` thì ta nói

* :math:`b \oplus a` là vi sai đầu vào;
* :math:`f(b) \oplus f(a)` là vi sai đầu ra.

Ở đây cần lưu ý rằng, vi sai bản chất là phép trừ, nhưng trên :math:`\mathbb{F}_2^n` thì phép trừ cũng chính là phép cộng :math:`\oplus`.

Tương tự, dưới góc độ phá mã, với :math:`\delta \in \mathbb{Z}_{2^n}` và :math:`\Delta \in \mathbb{Z}_{2^m}` cố định, ta xem xét có bao nhiêu cặp :math:`a, b \in \mathbb{Z}_{2^n}` mà

.. math:: b \oplus a = \delta, \quad f(b) \oplus f(a) = \Delta.

Chuyển vế ta có các đẳng thức trên tương với

.. math:: b = a \oplus \delta \Longrightarrow f(b) = f(a \oplus \delta) = f(a) \oplus \Delta.

Nói cách khác, ta xem xét xác suất

.. math:: 

   \mathrm{xdp}^f(\delta \mapsto \Delta) = \Pr\left[f(a \oplus \delta) = f(a) \oplus \Delta\right]

với mọi :math:`a \in \mathbb{Z}_{2^n}`.

Tổng quát, nếu ta xét :math:`k` hiệu đầu vào :math:`\alpha_0`, :math:`\alpha_1`, ..., :math:`\alpha_{k-1}` và hiệu đầu ra :math:`\alpha_k` thì ta quan tâm xác suất

.. math:: 
    
    \mathrm{adp}^f(\alpha_0, \alpha_1, \ldots, \alpha_{k-1} \mapsto \alpha_{k}) = 
    \Pr\left[f(x_0 \oplus \alpha_0, x_1 \oplus \alpha_1, \ldots, x_{k-1} \oplus \alpha_{k-1}) 
    = f(x_0, x_1, \ldots, x_{k-1}) \oplus \alpha_{k}\right].

.. prf:example:: 
    :label: exp-xdp-1

    Xét hàm :math:`f(x, y) = x \boxplus y` với :math:`x, y \in \mathbb{Z}_{2^n}`. Với :math:`\alpha`, :math:`\beta` và :math:`\gamma` thuộc :math:`\mathbb{Z}_{2^n}` ta xem xét

    .. math:: \mathrm{xdp}^f(\alpha, \beta \mapsto \gamma) = \Pr\left[(x \oplus \alpha) \boxplus (y \oplus \beta) = (x \boxplus y) \oplus \gamma\right].

Một số lưu ý và nhận xét
------------------------

Một số nguyên :math:`n` bit cũng có thể xem xét dưới dạng vector :math:`n` phần tử, do đó cho phép chúng ta xem xét hai dạng vi sai theo phép XOR và theo phép cộng modulo :math:`2^n`.

Ở đây, :math:`\mathrm{adp}` là viết tắt của *addition differential probability* (xác suất vi sai theo phép cộng) và :math:`\mathrm{xdp}` là viết tắt của *xor differential probability* (xác suất vi sai theo phép xor).

Trong nhiều thuật toán mã khối, các phép biến đổi có thể sử dụng phép XOR lẫn phép cộng modulo :math:`2^n`, do đó việc nghiên cứu mối liên hệ giữa các toán tử trên nhằm đưa ra đánh giá vi sai nào đạt được xác suất mong muốn là việc quan trọng. Tuy nhiên hiện chưa có nhiều nghiên cứu cho việc này, ví dụ như phép cộng modulo :math:`2^n` sẽ có xác suất như thế nào đối với vi sai là phép XOR, và ngược lại.

Lý do đơn giản nhất của ứng dụng vi sai là loại bỏ sự có mặt của khóa trong mỗi vòng.

Ví dụ thứ nhất, rất phổ biến, là hệ mã DES. Nếu ta xét một S-box vòng thì biến đổi trên nửa phải có dạng

.. math:: F(R, K) = \mathsf{SBox}(R \oplus K)

với :math:`R` là nửa phải đầu vào và :math:`K` là khóa ở vòng hiện tại, thì ta có vi sai đầu vào là

.. math:: \delta = R \oplus R' = (R \oplus K) \oplus (R' \oplus K)

và vi sai đầu ra là

.. math:: \Delta = \mathsf{SBox}(R \oplus K) \oplus \mathsf{SBox}(R' \oplus K).

Ở đây, vi sai đầu vào không phụ thuộc vào khóa :math:`K`.

Ví dụ thứ hai là round function của hệ mã Magma. Nếu ta lấy S-box của Magma có dạng

.. math:: F(R, K) = \mathsf{SBox}(R \boxplus K)

thì vi sai đầu vào là

.. math:: \delta = R' \boxminus R = (R' \boxplus K) \boxminus (R \boxplus K)

và vi sai đầu ra là

.. math:: \Delta = \mathsf{SBox}(R' \boxplus K) \boxminus \mathsf{SBox}(R \boxplus K).

Ở đây ta cũng có vi sai đầu vào không phụ thuộc vào khóa :math:`K` nhưng đối với toán tử hiệu :math:`\boxminus`, không phải hiệu :math:`\oplus`.
