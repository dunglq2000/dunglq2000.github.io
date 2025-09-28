Phép chia Euclid. Thuật toán Euclid
***********************************

Phép chia Euclid
================

Đây là nền tảng, cơ sở của số học. Từ khi biết tới phép chia hai số nguyên, ta có thể tìm **thương** và **số dư**. Nói theo toán học, nếu ta có hai số nguyên dương :math:`a` và :math:`b` thì tồn tại cặp số :math:`q`, :math:`r` sao cho :math:`a = qb + r` với :math:`0 \leqslant r < b`.

Khi đó, :math:`a` gọi là số bị chia, :math:`b` gọi là số chia, :math:`q` là thương (q trong quotient) và :math:`r` là số dư (r trong remainder).

Đặc biệt, sự tồn tại của cặp số :math:`q` và :math:`r` là duy nhất. Thật vậy, nếu ta giả sử tồn tại hai cặp số :math:`(q_1, r_1)` và :math:`(q_2, r_2)` đều thỏa đẳng thức trên, nghĩa là

.. math:: a = q_1 b + r_1, \quad a = q_2 b + r_2.

Trừ hai đẳng thức vế theo vế ta có

.. math:: (q_1 - q_2) b + (r_1 - r_2) = 0,
    
tương đương :math:`(r_2 - r_1) = (q_1 - q_2) b`, mà :math:`0 \leqslant r_1, r_2 < b` nên :math:`-b < r_2 - r_1 < b`.

Như vậy chỉ có thể xảy ra trường hợp :math:`r_2 - r_1 = 0` (vì giá trị tuyệt đối của vế phải là bội của :math:`b` nên sẽ lớn hơn :math:`b`, còn vế trái lại có giá trị tuyệt đối nhỏ hơn :math:`b`) hay :math:`r_2 = r_1`, kéo theo :math:`q_1 = q_2`.

Thuật toán Euclid
=================

Dựa trên phép chia Euclid, ta có một thuật toán hiệu quả để tìm ước chung lớn nhất giữa hai số :math:`a` và :math:`b`.

Kí hiệu :math:`\gcd(a, b)` là ước chung lớn nhất của :math:`a` và :math:`b`. Chúng ta thực hiện đệ quy như sau:

.. math:: 

    \gcd(a, b) = \begin{cases}
        a, \ & \text{nếu} \, b = 0 \\
        \gcd(b, a \bmod b), \ & \text{nếu} \, b \neq 0.
    \end{cases} 

Điểm quan trọng ở thuật toán Euclid là thuật toán chắc chắn sẽ dừng sau một số hữu hạn bước, và kết quả sẽ là ước chung lớn nhất của hai số :math:`a` và :math:`b`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`r_0 = a` và :math:`r_1 = b`. Theo phép chia Euclid tồn tại các số :math:`q_0` và :math:`r_2` sao cho :math:`r_0 = r_1 q_0 + r_2` với :math:`0 \leqslant r_2 < r_1`.

    Trong thuật toán Euclid, ở bước thứ :math:`i` (:math:`i = 1, 2, \ldots`) vì đã biết :math:`r_i` và :math:`r_{i+1}` nên ta tìm được thương :math:`q_i` và số dư :math:`r_{i+2}` trong phép chia :math:`r_i` cho :math:`r_{i+1}`.

    .. math:: 
        
        
            r_0 & = r_1 q_0 + r_2 \\
            r_1 & = r_2 q_1 + r_3 \\
            r_2 & = r_3 q_2 + r_4 \\
            \ldots & = \ldots \\
            r_i & = r_{i+1} q_i + r_{i+2} \\
            \ldots & = \ldots \\
            r_k & = r_{k+1} q_k + 0 \\
        
    Ở mỗi bước, :math:`r_{i+2}` luôn nhỏ hơn :math:`r_{i+1}`. Do đó cuối cùng sẽ bằng :math:`0`, và khi đó ta có ước chung lớn nhất là :math:`r_{k+1}` như trên.

.. prf:example:: 
    :label: exp-gcd

    Tìm ước chung lớn nhất của :math:`784` và :math:`74`.

    .. math:: 
        
        \begin{array}{ccccc}
            r_i & = & r_{i+1} \cdot q_i & + & r_{i+2} \\
            784 & = & {\color{red}{74}} \cdot 10 & + & {\color{blue}{44}} \\
            {\color{red}74} & = & {\color{blue}{44}} \cdot 1 & + & {\color{green}{30}} \\
            {\color{blue}{44}} & = & {\color{green}{30}} \cdot 1 & + & {\color{magenta}{14}} \\
            {\color{green}{30}} & = & {\color{magenta}{14}} \cdot 2 & + & {\color{orange}{2}} \\
            {\color{magenta}{14}} & = & {\color{orange}{2}} \cdot 7 & + & {\boxed{\color{purple}{0}}}
        \end{array}

    Vậy :math:`\gcd(784, 74) = 2`.

Thuật toán Euclid mở rộng
=========================

.. prf:definition:: Phương trình Diophantus
    :label: def-diophantus-eq

    Cho trước các số nguyên :math:`a`, :math:`b` và :math:`c`. Phương trình  Diophantus là phương trình có dạng

    .. math:: ax + by = c

    với :math:`x`, :math:`y` là các số nguyên.

.. prf:example:: 
    :label: exp-solve-diophantus-eq

    Giải phương trình :math:`5x+3y = 1`.

    Ta có

    .. math:: y = \dfrac{1-5x}{3} = \dfrac{1-2x-3x}{3} = \dfrac{1-2x}{3} - x.

    Như vậy nếu :math:`y \in \mathbb{Z}` thì :math:`\dfrac{1-2x}{3} \in \mathbb{Z}`, nghĩa là :math:`1-2x` chia hết cho :math:`3`. Vậy :math:`1-2x = 3k` với :math:`k \in \mathbb{Z}`.

    Tiếp tục, :math:`1-2x = 3k`, suy ra

    .. math:: x = \dfrac{1-3k}{2} = \dfrac{1-k-2k}{2} = \dfrac{1-k}{2} - k.

    Do :math:`x` nguyên nên tương tự :math:`\dfrac{1-k}{2}` cũng nguyên, hay :math:`1-k = 2t`, tương đương với :math:`k = 1-2t`.

    Thay ngược lại ta có

    .. math:: x = \dfrac{1-3k}{2} = \dfrac{1-3(1-2t)}{2} = {-1+3t}.

    Tiếp tục thay vào để tìm :math:`y` thì 

    .. math:: y = \dfrac{1-5x}{3} = \dfrac{1-5(-1+3t)}{3} = 2 - 5t.

    Như vậy nghiệm của phương trình là tất cả các nghiệm :math:`(x, y)` mà :math:`x = -1+3t`, :math:`y = 2-5t` với :math:`t \in \mathbb{Z}`.

Ở đây chúng ta đã thực hiện phép chia có dư liên tiếp để tìm nghiệm. Nói cách khác ta đã thực hiện thuật toán Euclid ở bên trên để làm giảm độ phức tạp ở mỗi bước giải.

Tổng quát ta có thuật toán Euclid mở rộng để tìm ước chung lớn nhất :math:`\gcd(a, b)` của hai số :math:`a`, :math:`b`, và **một** nghiệm của phương trình :math:`ax + by = \gcd(a, b)`.

Ở ví dụ trên, ta đã tìm được một nghiệm của phương trình :math:`5x + 3y = 1` là :math:`(-1, 2)` khi :math:`t = 0`. Khi đó ta có thể suy ra tất cả nghiệm (họ nghiệm) của phương trình có dạng :math:`(-1+3t, 2-5t)` với :math:`t \in \mathbb{Z}`.

.. prf:algorithm:: Thuật toán Euclid mở rộng
    :label: algo-xgcd

    **Input:** :math:`a, b \in \mathbb{Z}`

    **Output:** :math:`\gcd(a, b)`, :math:`x`, :math:`y`

    1. :math:`r_0 \gets a`, :math:`r_1 \gets b`, :math:`r_2 \gets 0`
    2. :math:`x_0 \gets 1`, :math:`x_1 \gets 0`, :math:`x_2 \gets 0`
    3. :math:`y_0 \gets 0`, :math:`y_1 \gets 1`, :math:`y_2 \gets 0`
    4. While :math:`r_1 \neq 0`

       1. :math:`q \gets r_0 \;\text{div}\; r_1`
       2. :math:`r_2 \gets r_0 - q * r_1`, :math:`r_0 \gets r_1`, :math:`r_1 \gets r_2`
       3. :math:`x_2 \gets x_0 - q * x_1`, :math:`x_0 \gets x_1`, :math:`x_1 \gets x_2`
       4. :math:`y_2 \gets y_0 - q * y_1`, :math:`y_0 \gets y_1`, :math:`y_1 \gets y_2`

    5. EndWhile
    6. Return :math:`r_0`, :math:`x_0`, :math:`y_0`

Ở thuật toán trên, :math:`r_0`, :math:`r_1` và :math:`r_2` hoạt động như thuật toán Euclid chuẩn. 

Ở mỗi bước, :math:`q` là thương của phép chia :math:`r_0` cho :math:`r_1`, và ta sử dụng :math:`q` đó để tính :math:`x_0` và :math:`y_0` mới. Kết quả cuối cùng :math:`(r_0, x_0, y_0)` lần lượt là ước chung lớn nhất :math:`r_0`, và hai số :math:`x_0`, :math:`y_0` thỏa mãn :math:`a x_0 + y b_0 = r_0`.

Tại sao chúng ta lại có :math:`(x_0, x_1) = (1, 0)` và :math:`(y_0, y_1) = (0, 1)`? Thêm nữa, làm sao biết thuật toán hoạt động đúng?

Mục đích của chúng ta là tìm các số :math:`(x, y)` sao cho :math:`ax + by = \gcd(a, b)`. Khi đó, dựa trên thuật toán Euclid cơ bản ở trên, ta xây dựng dãy số :math:`\{ x_n \}` và :math:`\{ y_n \}` sao cho ở mọi bước thứ :math:`n` ta đều có

.. math:: 
    :label: euclid-1

    a x_n + b y_n = r_n.

Từ thuật toán Euclid, với :math:`r_i` và :math:`r_{i+1}` ở bước thứ :math:`i` ta thực hiện phép chia Euclid :math:`r_i = r_{i+1} q_i + r_{i+2}` để tìm :math:`q_i` và :math:`r_{i+2}`. Từ :math:`q_i` ở mỗi bước ta tính

.. math:: x_{i+2} = x_i - x_{i+1} q_i, \quad y_{i+2} =  y_i - y_{i+1} q_i.

Chuyển vế hai phương trình trên ta có

.. math:: x_i = x_{i+1} q_i + x_{i+2}, \quad y_i = y_{i+1} q_i + y_{i+2}.

Nếu thay hai phương trình vừa rồi vào :eq:`euclid-1` ta được

.. math:: a (x_{i+1} q_i + x_{i+2}) + b (y_{i+1} q_i + y_{i+2}) = r_i,

tương đương với

.. math:: (a x_{i+1} + b y_{i+1}) \cdot q_i + (a x_{i+2} + b x_{i+2}) = r_i.

Do

.. math:: a x_{i+1} + b y_{i+1} = r_{i+1}, \quad a x_{i+2} + b y_{i+2} = r_{i+2},

nên :math:`r_{i+1} q_i + r_{i+2} = r_i`, đúng với thuật toán Euclid chuẩn ban đầu. Như vậy thuật toán mở rộng hoạt động đúng.

Bây giờ ta cần chọn :math:`(x_0, x_1)` và :math:`(y_0, y_1)` vì chúng ta đã đặt :math:`r_0 = a` và :math:`r_1 = b`.

Ở bước thứ :math:`0`, vì

.. math:: r_0 = a = a x_0 + b y_0,

và ở bước thứ :math:`1`,

.. math:: r_1 = b = a x_1 + b y_1.

Dễ thấy ở bước :math:`0` ta chọn :math:`x_0 = 1` và :math:`x_1 = 0`, còn ở bước :math:`1` ta chọn :math:`y_0 = 0` và :math:`y_1 = 1` là được.

.. prf:example:: 
    :label: exp-xgcd

    Tìm một nghiệm nguyên của phương trình :math:`784 x + 74 y = 2`.

    .. math:: 
        
        \begin{array}{ccccc|ccccc|ccccc}
            r_i & = & r_{i+1} \cdot q_i & + & r_{i+2} & x_{i+2} & = & x_i & - & x_{i+1} \cdot q_i & y_{i+2} & = & y_i & - & y_{i+1} \cdot q_i \\
            784 & = & {\color{red}{74}} \cdot 10 & + & {\color{blue}{44}} & {\color{blue}1} & = & 1 & - & {\color{red}0} \cdot 10 & {\color{blue}-10} & = & 0 & - & {\color{red}1} \cdot 10 \\
            {\color{red}74} & = & {\color{blue}{44}} \cdot 1 & + & {\color{green}{30}} & {\color{green}-1} & = & {\color{red}0} & - & {\color{blue}1} \cdot 1 & {\color{green}11} & = & {\color{red}1} & - & {\color{blue}(-10)} \cdot 1 \\
            {\color{blue}{44}} & = & {\color{green}{30}} \cdot 1 & + & {\color{magenta}{14}} & {\color{magenta}2} & = & {\color{blue}1} & - & {\color{green}(-1)} \cdot 1 & {\color{magenta}-21} & = & {\color{blue}-10} & - & {\color{green}11} \cdot 1 \\
            {\color{green}{30}} & = & {\color{magenta}{14}} \cdot 2 & + & {\color{orange}{2}} & {\color{orange}-5} & = & {\color{green}(-1)} & - & {\color{magenta}2} \cdot 2 & {\color{orange}53} & = & {\color{green}11} & - & {\color{magenta}(-21)} \cdot 2\\
            {\color{magenta}{14}} & = & {\color{orange}{2}} \cdot 7 & + & {\boxed{\color{purple}{0}}}
        \end{array}

    Các bạn có thể thấy ước chung lớn nhất là số màu cam. Do đó các số :math:`x_{i+2}` và :math:`y_{i+2}` cũng chính là điểm dừng và mình không cần tính toán thêm.

    Như vậy một nghiệm của phương trình :math:`784 x + 74 y = 2` là :math:`(-5, 53)`.

Chúng ta cũng có một cách trình bày khác để giải phương trình nghiệm nguyên trên là sử dụng biến đổi tương đương của ma trận.

Ví dụ, để tìm một nghiệm nguyên :math:`(x, y)` của phương trình :math:`a x + b y = c` với :math:`a`, :math:`b`, :math:`c` là các số cho trước, chúng ta viết ma trận

.. math:: 
    
    \left(\begin{array}{cc|c}
        1 & 0 & a \\ 0 & 1 & b
    \end{array}\right)

và biến đổi tương đương về dạng

.. math:: 
    
    \left(\begin{array}{cc|c}
       * & * & c \\ * & * & 0
   \end{array}\right)

Khi đó hai số ở hàng trên sẽ là nghiệm cần tìm.

.. prf:example:: 
    :label: exp-xgcd-matrix

    Sử dụng bài toán ở trên làm ví dụ: tìm một nghiệm nguyên của phương trình :math:`784 x + 74 y = 2`.

    .. math:: 
        
        \left(\begin{array}{cc|c}
            1 & 0 & 784 \\ 0 & 1 & 74
        \end{array}\right) \sim \left(\begin{array}{cc|c}
            {\color{blue}1} & {\color{blue}-10} & {\color{blue}44} \\ 0 & 1 & 74
        \end{array}\right) \sim \left(\begin{array}{cc|c}
            {\color{blue}1} & {\color{blue}-10} & {\color{blue}44} \\ {\color{green}-1} & {\color{green}11} & {\color{green}30}
        \end{array}\right) \\ \sim \left(\begin{array}{cc|c}
            {\color{magenta}2} & {\color{magenta}-21} & {\color{magenta}14} \\ {\color{green}-1} & {\color{green}11} & {\color{green}30}
        \end{array}\right) \sim \left(\begin{array}{cc|c}
            {\color{magenta}2} & {\color{magenta}-21} & {\color{magenta}14} \\ {\color{orange}-5} & {\color{orange}53} & {\color{orange}2}
        \end{array}\right) \sim \left(\begin{array}{cc|c}
            37 & -392 & 0 \\ {\color{orange}-5} & {\color{orange}53} & {\color{orange}2}
        \end{array}\right)

Về bản chất thì hai cách trình bày là giống nhau.

Bài tập sưu tầm
===============

**Câu 1** (đề kiểm tra, ITMO). Tính

.. math:: \gcd(61^{610} + 1, 61^{671} - 1).

Mình thay :math:`61` bởi biến :math:`x` và thực hiện phép chia đa thức theo thuật toán Euclid.

Đầu tiên, xét phép chia :math:`x^{671} - 1` cho :math:`x^{610} + 1`. Kết quả phép chia là

.. math:: x^{671} - 1 = (x^{610} + 1) \cdot x^{61} - x^{61} - 1.

Tiếp theo, xét phép chia :math:`x^{610} + 1` cho :math:`-x^{61} - 1`. Kết quả là

.. math:: x^{610} + 1 = (-x^{61} - 1) \cdot (-x^{549} + x^{488} - \cdots + 1) + 2.

Như vậy, ước chung lớn nhất của hai đa thức là :math:`2`.

**Câu 2** (đề kiểm tra, ITMO). Chứng minh rằng với mọi :math:`a, b, c \in \mathbb{N}` thì

.. math:: [a, b, c] = \frac{a \cdot b \cdot c \cdot (a, b, c)}{(a, b) \cdot (a, c) \cdot (b, c)},

trong đó

- :math:`[a, b, c]` là bội chung nhỏ nhất của ba số :math:`a`, :math:`b`, :math:`c`
- :math:`(a, b, c)` là ước chung lớn nhất của ba số :math:`a`, :math:`b`, :math:`c`
- :math:`(a, b)` là ước chung lớn nhất của hai số :math:`a`, :math:`b`.

*Chưa làm ra.*

**Câu 3** (đề kiểm tra, ITMO). Tìm ít nhất một nghiệm nguyên của phương trình

.. math:: 311 x - 28 y = 2.

Sử dụng thuật toán Euclid:

.. math:: 
    
    & \left(\begin{array}{cc|c}
    1 & 0 & 311 \\ 0 & 1 & -28
    \end{array}\right) \stackrel{(1) \to (1) + 11 \cdot (2)}{\sim}
    \left(\begin{array}{cc|c}
    1 & 11 & 3 \\ 0 & 1 & -28
    \end{array}\right) \stackrel{(2) \to (2) + 10 \cdot (1)}{\sim}
    \left(\begin{array}{cc|c}
    1 & 11 & 3 \\ 10 & 111 & 2
    \end{array}\right) \\
    \stackrel{(1) \to (1) - (2)}{\sim}
    & \left(\begin{array}{cc|c} 
    -9 & -100 & 1 \\ 10 & 111 & 2
    \end{array}\right) \stackrel{(2) \to (2) - 2 \cdot (1)}{\sim}
    \left(\begin{array}{cc|c}
    -9 & -100 & 1 \\ 28 & 311 & 0
    \end{array}\right)

Như vậy mình có :math:`(-9, -100)` là một nghiệm của phương trình

.. math:: 311 x - 28 y = 1.

Từ đó suy ra một nghiệm của phương trình

.. math:: 311 x - 28 y = 2

là :math:`(2 \cdot (-9), 2 \cdot (-100)) = (-18, -200)`.
