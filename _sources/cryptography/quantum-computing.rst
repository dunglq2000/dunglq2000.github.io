*****************
Quantum computing
*****************

=========================
Qubit và toán tử quantum
=========================

Trên máy tính hiện nay, đơn vị xử lý cơ bản là bit (0 hoặc 1). Trong máy tính lượng tử, đơn vị tính toán là qubit (quantum bit).

-----
Qubit
-----

Mỗi qubit :math:`\lvert \psi \rangle` được biểu diễn dưới dạng tổ hợp tuyến tính của cơ sở gồm :math:`\lvert 0 \rangle = (1, 0)` và :math:`\lvert 1 \rangle = (0, 1)`. Khi đó qubit :math:`\lvert \psi \rangle = \alpha \lvert 0 \rangle + \beta \lvert 1 \rangle`. Ở đây :math:`\alpha, \beta \in \mathbb{C}` (tập số phức).

Tích của :math:`n` qubit là các tổ hợp :math:`\lvert 0, 0, \ldots, 0 \rangle`, :math:`\lvert 0, 0, \ldots, 1 \rangle`, ..., :math:`\lvert 1, 1, \ldots, 1 \rangle`. Ta cũng kí hiệu :math:`\lvert 0 \rangle \otimes \lvert 1 \rangle = \lvert 01 \rangle`. 

.. prf:example:: 
    :label: exp-qubit

    Nếu :math:`\lvert \psi \rangle = \alpha \lvert 0 \rangle + \beta \lvert 1 \rangle` và :math:`\lvert \Psi \rangle = \gamma \lvert 0 \rangle + \delta \lvert 1 \rangle` thì

.. math:: \lvert \psi \rangle \otimes \lvert \Psi \rangle = (\alpha \lvert 0 \rangle + \beta \lvert 1 \rangle) \otimes (\gamma \lvert 0 \rangle + \delta \lvert 1 \rangle) = \alpha \gamma \lvert 00 \rangle + \alpha \delta \lvert 0 1 \rangle + \beta \gamma \lvert 10 \rangle + \beta \delta \lvert 11 \rangle


Tiếp theo là **toán tử quantum** và tương ứng với nó là các cổng (gate) trên mạch.

Toán tử quantum tác động lên một qubit hoặc tích của nhiều qubit.

Qubit có dạng :math:`\lvert \psi \rangle = a \lvert 0 \rangle + b \lvert 1 \rangle`. Ta có thể viết hệ số dưới dạng vector cột :math:`\begin{pmatrix} a \\ b \end{pmatrix}`. Khi đó, toán tử quantum sẽ là một ma trận :math:`2 \times 2` biến đổi vector trên thành vector mới :math:`\begin{pmatrix} c \\ d \end{pmatrix}` tương ứng với qubit :math:`\lvert \Psi \rangle = c \lvert 0 \rangle + d \lvert 1 \rangle`.

Nói cách khác, đặt toán tử quantum là ma trận :math:`\mathcal{U} = \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix}` thì ta có

.. math:: \lvert \psi \rangle \to \lvert \Psi \rangle = \mathcal{U} \lvert \psi \rangle, \quad \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix} \cdot \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} c \\ d \end{pmatrix}

------------------------------
Các toán tử quantum thường gặp
------------------------------

.. prf:definition:: Toán tử đồng nhất
    :label: def-op-quan-id

    Toán tử đồng nhất identity giữ nguyên qubit đầu vào. Ma trận tương ứng là ma trận đơn vị :math:`I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}`.

.. prf:definition:: Toán tử NOT
    :label: def-op-quan-not

    Toán tử NOT có ma trận tương ứng là :math:`\text{NOT} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}`. Khi đó :math:`\text{NOT} \lvert \psi \rangle = b \lvert 0 \rangle + a \lvert 1 \rangle` với :math:`x \in \{ 0, 1 \}`.

Khi qubit là :math:`\lvert 0 \rangle` hoặc :math:`\lvert 1 \rangle`, tác dụng của toán tử NOT là phép XOR nên ta có :math:`\text{NOT} \lvert x \rangle = \lvert x \oplus 1 \rangle`.

.. prf:definition:: Toán tử Hadamard
    :label: def-op-quan-hadamard
    
    Ma trận của toán tử Hadamard là :math:`H = \dfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & - 1 \end{pmatrix}`. 

.. prf:example:: 
    :label: exp-op-quan-hadamard

    Xét qubit :math:`\lvert \psi \rangle = a \lvert 0 \rangle + b \lvert 1 \rangle`, toán tử Hadamard tương ứng với phép nhân ma trận

    .. math:: \dfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & - 1 \end{pmatrix} \cdot \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} \dfrac{1}{\sqrt{2}} (a + b) \\ \dfrac{1}{\sqrt{2}} (a - b) \end{pmatrix}
    
    Ta chuyển cột kết quả về lại dạng tổ hợp tuyến tính thì cổng Hadamard hoạt động trên qubit :math:`\lvert \psi \rangle = a \lvert 0 \rangle + b \lvert 1 \rangle` cho kết quả là

    .. math:: H \lvert \psi \rangle = H(a \lvert 0 \rangle + b \lvert 1 \rangle) = \dfrac{1}{\sqrt{2}} (a + b) \lvert 0 \rangle + \dfrac{1}{\sqrt{2}} (a - b) \lvert 1 \rangle

Nếu :math:`\lvert \psi \rangle \equiv \lvert 0 \rangle` thì tương đương với :math:`a = 1, b = 0`. Ta có :math:`H \lvert 0 \rangle = \dfrac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}}`.

Nếu :math:`\lvert \psi \rangle \equiv \lvert 1 \rangle` thì tương đương với :math:`a = 0, b = 1`. Ta có :math:`H \lvert 1 \rangle = \dfrac{\lvert 0 \rangle - \lvert 1 \rangle}{\sqrt{2}}`.

Tổng quát ta nhận thấy, với :math:`x \in \{ 0, 1 \}` thì :math:`H \lvert x \rangle = \dfrac{\lvert 0 \rangle + (-1)^x \lvert 1 \rangle}{\sqrt{2}}`.

Ta thấy rằng toán tử ngược của toán tử Hadamard là chính nó.

Tiếp theo là toán tử thường được dùng nhất khi tính toán trên tích của nhiều qubit: toán tử control.

Như đã xem xét ở trên, tích của :math:`n` qubit sẽ có :math:`2^n` phần tử tương ứng các bộ :math:`\lvert 0, 0, \ldots, 0, 0 \rangle`, :math:`\lvert 0, 0, \ldots, 0, 1 \rangle`, ... Do đó toán tử control sẽ là ma trận kích thước :math:`2^n \times 2^n`.

.. prf:definition:: Toán tử control 
    :label: def-op-quan-control

    Gọi :math:`\mathcal{U} = \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix}` là toán tử tác động lên một qubit. Xét hai qubit là :math:`\lvert x \rangle = a \lvert 0 \rangle + b \lvert 1 \rangle` và :math:`\lvert y \rangle = c \lvert 0 \rangle + d \lvert 1 \rangle`. Ta có tích

    .. math:: \lvert x \rangle \otimes \lvert y \rangle = ac \lvert 00 \rangle + ad \lvert 01 \rangle + bc \lvert 10 \rangle + bd \lvert 11 \rangle


    Khi đó toán tử control có dạng ma trận là

    .. math:: c \mathcal{U} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & c_{11} & c_{12} \\ 0 & 0 & c_{21} & c_{22} \end{pmatrix}


    Hay viết dưới dạng ma trận khối là :math:`c \mathcal{U} = \begin{pmatrix} I & \mathcal{O} \\ \mathcal{O} & \mathcal{U} \end{pmatrix}`.

Ta cũng viết tích :math:`\lvert x \rangle \otimes \lvert y \rangle` dưới dạng vector cột (4 phần tử). Khi đó

.. math:: \mathcal{U} (\lvert x \rangle \otimes \lvert y \rangle) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & c_{11} & c_{12} \\ 0 & 0 & c_{21} & c_{22} \end{pmatrix} \cdot \begin{pmatrix} ac \\ ad \\ bc \\ bd \end{pmatrix} = \begin{pmatrix} ac \\ ad \\ c_{11} \cdot bc + c_{12} \cdot bd \\ c_{21} \cdot bc + c_{22} \cdot bd \end{pmatrix}

Hai phần tử đầu của vector kết quả không thay đổi, còn phần sau có "một phần" là :math:`\mathcal{U} \lvert y \rangle`. Khi viết lại kết quả dưới dạng qubit thì

.. math:: ac \lvert 00 \rangle + ad \lvert 01 \rangle + (c_{11} \cdot bc + c_{12} \cdot bd) \lvert 10 \rangle + (c_{21} \cdot bc + c_{22} \cdot bd) \lvert 11 \rangle

Ta có một số nhận xét sau đây.

.. prf:remark::
    :label: rmk-op-quan-control

    Nếu :math:`\lvert x \rangle \equiv \lvert 0 \rangle`, tức là :math:`a = 1, b = 0` thì tích trên tương ứng với 

    .. math:: c \lvert 00 \rangle + d \lvert 01 \rangle + 0 \lvert 10 \rangle + 0 \lvert 11 \rangle = \lvert 0 \rangle \otimes (c \lvert 0 \rangle + d \lvert 1 \rangle) = \lvert x \rangle \otimes \lvert y \rangle.

    Nếu :math:`\lvert x \rangle \equiv \lvert 1 \rangle`, tức là :math:`a = 0, b = 1` thì tích trên tương ứng với 

    .. math:: 0 \lvert 00 \rangle + 0 \lvert 01 \rangle + (c_{11} c + c_{12} d) \lvert 10 \rangle + (c_{21} c + c_{22} d) \lvert 11 \rangle = \lvert 1 \rangle \otimes ((c_{11} c + c_{12} d) \lvert 0 \rangle + (c_{21} c + c_{22} d) \lvert 1 \rangle) = \lvert 1 \rangle \otimes \mathcal{U} \lvert y \rangle = \lvert x \rangle \otimes \mathcal{U} \lvert y \rangle.

Tổng kết lại, với :math:`x \in \{ 0, 1\}` thì

- nếu :math:`x = 0` thì :math:`\lvert x \rangle \otimes \lvert y \rangle \to \lvert x \rangle \otimes \lvert y \rangle`.
- nếu :math:`x = 1` thì :math:`\lvert x \rangle \otimes \lvert y \rangle \to \lvert x \rangle \otimes \mathcal{U} \lvert y \rangle`.

Tùy vào :math:`x` là 0 hay 1 mà toán tử quantum :math:`\mathcal{U}` sẽ bị bỏ qua hoặc xem xét. Ở đây qubit :math:`\lvert x \rangle` đóng vai trò điều khiển nên đây được gọi là toán tử control.

.. prf:definition:: Toán tử control CNOT, Control NOT
    :label: def-op-quan-control-not

    Toán tử quantum CNOT có ma trận là

    .. math:: \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} I & \mathcal{O} \\ \mathcal{O} & \text{NOT} \end{pmatrix}

Qubit :math:`\lvert x \rangle` với :math:`x \in \{ 0, 1 \}` đóng vai trò control cho qubit :math:`\lvert y \rangle`. Khi :math:`x \equiv 0` thì :math:`y` giữ nguyên, hay :math:`\lvert y \oplus 0 \rangle = \lvert y \oplus x \rangle`. Khi :math:`x \equiv 1` thì áp dụng cổng NOT bên trên, khi đó :math:`y` biến đổi thành :math:`y \oplus 1 = y \oplus x`.
