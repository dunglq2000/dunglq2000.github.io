Công thức truy hồi
******************

Dãy số là một ánh xạ từ :math:`\mathbb{N}` tới :math:`\mathbb{R}`

.. math:: u : \mathbb{N} \to \mathbb{R}, \quad n \mapsto u(n).

Khi đó các giá trị :math:`u(1)`, :math:`u(2)`, ... được gọi là **số hạng** của dãy số. Chúng ta cũng có thể viết :math:`u_1`, :math:`u_2`, ... thay vì :math:`u(1)`, :math:`u(2)`, ..., hoặc thậm chí là :math:`\{ u_ n \}`.


Cấp số cộng và công thức truy hồi bậc nhất
==========================================

Cho dãy số :math:`\{ u_n \}` với phần tử đầu :math:`u_0` và công sai :math:`d`. Khi đó các phần tử sau đó được tính với công thức

.. math:: u_{n} = u_{n-1} + d

với mọi :math:`n \geqslant 1` thì :math:`\{ u_n \}` được gọi là **cấp số cộng**.

Như vậy cấp số cộng là một dãy số có dạng

.. math:: u_n = \varphi(n, u_{n-1}).

Dãy số có dạng như trên gọi là **truy hồi bậc nhất** (hay **first order**).

.. prf:example:: 
    :label: recurr-1-order-1

    Dãy số :math:`\{ u_n \}` xác định bởi

    .. math:: u_n = a u_{n-1} + b n + c

    với :math:`u_0` là số hạng đầu; :math:`a`, :math:`b` và :math:`c` là các số thực.

.. prf:example:: 
    :label: recurr-1-order-2

    Dãy số :math:`\{ u_ n \}` xác định bởi

    .. math:: u_n = a u_{n-1}^2 + b u_{n-1} + c

    với :math:`u_0` là số hạng đầu; :math:`a`, :math:`b` và :math:`c` là các số thực.

Ta cần chú ý rằng việc nói truy hồi bậc nhất mang nghĩa là số hạng thứ :math:`n` chỉ phụ thuộc vào số hạng thứ :math:`n - 1`, chứ không phải các số hạng trước đó như số hạng thứ :math:`n - 2`, :math:`n - 3`, vân vân và mây mây.

Ở ví dụ thứ hai thì số hạng thứ :math:`n` là hàm bậc hai theo số hạng thứ :math:`n - 1` nhưng đây là công thức truy hồi bậc nhất.


Dãy số Fibonacci và công thức truy hồi bậc hai
==============================================

Đây có lẽ là dãy số nổi tiếng nhất trong toán học. Công thức của dãy số là với hai phần tử ban đầu :math:`u_0 = 0` và :math:`u_1 = 1`, các phần tử sau sẽ được tính với công thức

.. math:: u_n = u_{n-1} + u_{n-2}

với mọi :math:`n \geqslant 2`.

Ở đây, số hạng thứ :math:`n` được tính bởi hai số hạng trước nó nên đây là ví dụ của **truy hồi bậc hai**. Dãy số truy hồi bậc hai là dãy số có dạng

.. math:: u_n = \varphi(n, u_{n-1}, u_{n-2}).

.. prf:example:: 
    :label: recurr-2-order

    Dãy số :math:`\{ u_n \}` được xác định bởi

    .. math:: u_n = a u_{n-1} + b u_{n-2} + c

    với :math:`u_0` và :math:`u_1` là số hạng đầu; :math:`a`, :math:`b` và :math:`c` là các số thực.


Công thức truy hồi bậc cao
==========================

Tổng quát, nếu số hạng thứ :math:`n` của dãy số :math:`\{ u_n \}` được tính bởi :math:`k` số hạng trước nó, nghĩa là

.. math:: u_n = \varphi(n, u_{n-1}, u_{n-2}, \ldots, u_{n-k})

thì ta gọi là **công thức truy hồi bậc** :math:`k`.

Các dãy truy hồi có ứng dụng rộng rãi trong toán học và các ngành khoa học khác, tiêu biểu nhất là dãy Fibonacci ở trên. Trong khoa học máy tính, công thức truy hồi có một ứng dụng để sinh một dãy số cho nhiều mục đích khác nhau như sinh số giả ngẫu nhiên (pseudo-random), sinh khóa cho thuật toán mã hóa dòng (stream cipher). Các ứng dụng này thường sử dụng dãy truy hồi **tuyến tính**, tức là bậc của các hạng tử :math:`u_{n-1}`, :math:`u_{n-2}`, ..., :math:`u_{n-k}` không quá :math:`1`. Nói cách khác thì

.. math:: u_n = a_{n-1} u_{n-1} + a_{n-2} u_{n-2} + \cdots + a_{n-k} u_{n-k} + \phi(n),

trong đó :math:`\phi(n)` là một hàm số nào đó không phụ thuộc các hạng tử :math:`u_{n-1}`, ..., :math:`u_{n-k}`. Các hệ số :math:`a_{n-1}`, ..., :math:`a_{n-k}` nằm trong trường số nào đó tùy thuộc bài toán. Ví dụ với các dãy LFSR (Linear Feedback Shift Register) để sinh dãy trong tin học ở trên thì các phép tính được thực trên trên trường :math:`\mathbb{F}_2`. Hiện tại chúng ta sẽ khảo sát dãy số với hệ số thực.

Chúng ta quan tâm đến công thức tổng quát của dãy số truy hồi. Dễ thấy rằng, để tính số hạng thứ :math:`n` theo truy hồi thì ta phải biết đủ :math:`k` số hạng trước đó. Nhưng với mỗi số hạng trong :math:`k` số hạng đó ta lại cần đi ngược về trước đó nữa cho đến khi tới các số hạng ban đầu :math:`u_0`, :math:`u_1`, ..., :math:`u_{k-1}`. Tuy nhiên đôi khi chúng ta quan tâm một số tính chất đại số mà cần công thức tổng quát cho :math:`\{ u_n \}` và chỉ phụ thuộc :math:`n`, nghĩa là :math:`u_n = f(n)`. Khi đó chúng ta sẽ sử dụng **phương pháp hàm sinh** (hay **generating function method**, hay **метод проводящих функций**).


Phương pháp hàm sinh
====================

Phương pháp hàm sinh thực hiện theo các bước sau:

1. Xác định các số hạng ban đầu :math:`u_0`, :math:`u_1`, ..., :math:`u_{k-1}`.
2. Gọi :math:`G(x)` là đa thức với hệ số là các số hạng của dãy số, tức là

.. math:: G(x) = u_0 + u_1 x + u_2 x^2 + \cdots + u_n x^n + \cdots

3. Phân tích :math:`G(x)` thành tổng các phân thức dạng :math:`\dfrac{1}{H(x)}`. Sau đó ta gom các số hạng có cùng lũy thừa của :math:`x` lại để được công thức tổng quát của :math:`\{ u_n \}`. Các hàm :math:`H(x)` sẽ được trình bày ở phần cuối với các ví dụ, và ta gọi chúng là **hàm sinh**.

Một ví dụ hay dùng của hàm sinh là khai triển sau.

.. math:: 
    :label: eq-mx

    \dfrac{1}{1 - mx} = 1 + mx + m^2 x^2 + \cdots + m^n x^n + \cdots


Công thức trên có thể thu được từ khai triển Taylor-Maclaurin hoặc bằng quy nạp.


Ví dụ I
-------

Xét dãy số :math:`\{ u_n \}` với :math:`u_0 = 0`, :math:`u_1 = 1`, và

.. math:: u_n = 5 u_{n-1} - 6 u_{n-2} \ \text{với mọi} \ n \geqslant 2.

Đặt

.. math:: 
    :label: eq-g

    G(x) = u_0 + u_1 x + u_2 x^2 + \cdots + u_n x^n + \cdots

Khi đó, ta nhân :math:`G(x)` với :math:`x`, :math:`x^2` và nhân thêm số hạng để khử các hạng tử theo công thức truy hồi

.. math:: u_n - 5 u_{n-1} + 6 u_{n-2} = 0.

Cụ thể, ta tính

.. math:: x \cdot G(x) = u_0 x + u_1 x^2 + u_2 x^3 + \cdots + u_{n-1} x^n + \cdots,

và

.. math:: x^2 \cdot G(x) = u_0 x^2 + u_1 x^3 + u_2 x^4 + \cdots + u_{n-2} x^n + \cdots

Khi đó

.. math:: 
    
    G(x) - 5 x \cdot G(x) + 6 x^2 \cdot G(x) & = u_0 + u_1 x + {\color{blue} u_2 x^2} + {\color{green} u_3 x^3} + \cdots {\color{red} + u_n x^n} + \cdots \\
                                            & - 5 u_0 x {\color{blue} - 5 u_1 x^2} {\color{green} - 5 u_2 x^3} -  \cdots {\color{red} - 5 u_{n-1} x^n} + \cdots \\
                                            & {\color{blue} + 6 u_0 x^2} {\color{green} + 6 u_1 x^3} + \cdots {\color{red} + 6 u_{n-2} x^n} + \cdots
    

Các bạn có thấy điều gì không? Các số hạng trước :math:`x^2`, :math:`x^3`, ... đều bằng :math:`0` theo công thức truy hồi. Như vậy thu gọn vế trái và thay :math:`u_0`, :math:`u_1` vào vế phải ta có

.. math:: (1 - 5x + 6x^2) \cdot G(x) = u_0 + u_1 x - 5 u_0 x = x,

tương đương với

.. math:: G(x) = \dfrac{x}{1 - 5x + 6x^2}.

Vì :math:`1 - 5x + 6x^2` phân tích thành nhân tử là :math:`(1 - 2x)(1 - 3x)` nên ta muốn phân tích :math:`G(x)` thành tổng

.. math:: G(x) = \dfrac{\alpha}{1 - 2x} + \dfrac{\beta}{1 - 3x} = \dfrac{(\alpha + \beta) + (-3\alpha  -2\beta) x}{(1 - 2x)(1 - 3x)},

với :math:`\alpha` và :math:`\beta` là hệ số cần tìm để

.. math:: (\alpha + \beta) + (-3\alpha - 2\beta)x \equiv x.

Như vậy, đồng nhất hệ số ta có

.. math:: \alpha + \beta = 0, \quad -3\alpha - 2\beta = 1,

giải hệ ta có :math:`\alpha = -1` và :math:`\beta = 1`. Ta thu được

.. math:: G(x) = \dfrac{-1}{1 - 2x} + \dfrac{1}{1 - 3x}.

Theo công thức :eq:`eq-mx`, ta có

.. math:: \dfrac{1}{1 - 2x} = 1 + 2x + 2^2 x^2 + \cdots + 2^n x^n + \cdots,

và

.. math:: \dfrac{1}{1 - 3x} = 1 + 3x + 3^2 x^2 + \cdots + 3^n x^n + \cdots.

Thay hai khai triển trên vào :math:`G(x)` ta có

.. math:: 
    
    G(x) = & - (1 + 2x + 2^2 x^2 + \cdots + 2^n x^n + \cdots) \\
    & + (1 + 3x + 3^2 x^2 + \cdots + 3^n x^n + \cdots) \\
    = & 0 + (3 - 2) x + (3^2 - 2^2) x^2 + \cdots + (3^n - 2^n) x^n + \cdots

Đồng nhất hệ số với :eq:`eq-g` ta có

.. math:: u_n = 3^n - 2^n.

Đây chính là công thức tổng quát của dãy :math:`\{ u_n \}`.

Tất nhiên là ví dụ trên có thể được giải bằng cách khác là *đa thức đặc trưng* và đây là phương pháp phổ biến ở phổ thông. Tuy nhiên một số bài toán khác không thể sử dụng đa thức đặc trưng. Trước khi đến với các bài toán như vậy thì mình sẽ liệt kê một số hàm sinh thông dụng để giải quyết các bài toán đó.


Một số hàm sinh thông dụng
--------------------------

.. math:: \boxed{\dfrac{1}{1 - mx} = 1 + mx + m^2 x^2 + \cdots + m^n x^n + \cdots}

.. math:: \boxed{\dfrac{1}{(1-x)^t} = \sum_{i=0}^{\infty} C^i_{t+i-1} x^i.}

Khi :math:`t = 2` thì :math:`C^i_{i+1} = \dfrac{(i+1)!}{i! \cdot 1!} = i + 1` nên ta có kết quả

.. math:: \boxed{\dfrac{1}{(1-x)^2} = \sum_{i=0}^\infty (i+1) x^i.}

Kết hợp hai công thức trên

.. math:: \boxed{\dfrac{1}{(1 - mx)^t} = \sum_{i=0}^\infty C^i_{t+i-1} m^i x^i.}


Ví dụ II
--------

Cho dãy số :math:`\{ u_n \}` xác định bởi :math:`u_0 = 1`, :math:`u_1 = 2` và

.. math:: u_n = 6 u_{n-1} - 8 u_{n-2} + n, \ \text{với mọi} \ n \geqslant 2.

Tương tự, đầu tiên ta đặt :math:`G(x)` là đa thức có hệ số là dãy :math:`\{ u_n \}`, nghĩa là

.. math:: G(x) = u_0 + u_1 x + u_2 x^2 + \cdots + u_n x^n + \cdots

Ta cũng nhân :math:`x` và :math:`x^2` cho :math:`G(x)` và thu được

.. math:: x \cdot G(x) = u_0 x + u_1 x^2 + u_2 x^3 + \cdots + u_{n-1} x^n + \cdots,

và

.. math:: x^2 \cdot G(x) = u_0 x^2 + u_1 x^3 + u_2 x^4 + \cdots + u_{n-2} x^n + \cdots

Như vậy, hoàn toàn tương tự ví dụ I, mình tính được

.. math:: 
     
    G(x) - 6x \cdot G(x) + 8x^2 \cdot G(x) & = u_0 \\
    & + (u_1 - 6 u_0) x \\
    & + (u_2 - 6 u_1 + 8 u_0) x^2 \\
    & + (u_3 - 6 u_2 + 8 u_1) x^3 \\
    & + \cdots \\
    & + (u_n - 6 u_{n-1} + 8 u_{n-2}) x^n \\
    & + \cdots
    
Cơ mà ở đây :math:`u_n - 6 u_{n-1} + 8 u_{n-2}` không đủ để triệt tiêu thành :math:`0` mà cần thêm :math:`n` nữa. Vậy phải làm sao?

Chúng ta sẽ cần một hàm :math:`F(x)` sao cho

.. math:: 
    
    G(x) - 6x \cdot G(x) + 8x^2 \cdot G(x) + F(x) & = u_0 \\
    & + (u_1 - 6 u_0) x \\
    & + (u_2 - 6 u_1 + 8 u_0 {\color{red} - 2}) x^2 \\
    & + (u_3 - 6 u_2 + 8 u_1 {\color{red} - 3}) x^3 \\
    & + \cdots \\
    & + (u_n - 6 u_{n-1} + 8 u_{n-2} {\color{red} - n}) x^n \\
    & + \cdots
    
Như vậy mình gom các hệ số màu đỏ lại sẽ được

.. math:: F(x) = -2x^2 - 3x^3 + \cdots - nx^n + \cdots

Khi đó

.. math:: G(x) - 6x \cdot G(x) + 8x^2 \cdot G(x) + F(x) = u_0 + (u_1 - 6 u_0) x,

và việc của chúng ta là tìm một hàm sinh biểu thị cho :math:`F(x)` nữa để có thể biểu diễn :math:`G(x)` như ở ví dụ I.

Ta có

.. math::  
    
    F(x) & = -2x^2 - 3x^3 - \cdots - nx^n + \cdots \\
    & = 1 x - x (1 + 2x + 3x^2 + \cdots + nx^{n-1} + \cdots) \\
    & = x - x (1 + x + x^2 + x^3 + \cdots + x^n + \cdots)' \\
    & = x - x \cdot \left(\dfrac{1}{1-x}\right)' \\
    & = x - x \cdot \dfrac{1}{(1-x)^2} \\
    & = \dfrac{x(1 - 2x + x^2) + x}{(1-x)^2} = -\dfrac{x^2(2 - x)}{(1-x)^2}.

Thay :math:`u_0`, :math:`u_1` và :math:`F(x)` vào ta tính được :math:`G(x)` là hàm

.. math:: (1 - 6x + 8x^2) \cdot G(x) - \dfrac{x^2 (2 - x)}{(1-x)^2} = 1 - 4x,

tương đương với

.. math::  
    
    G(x) & = \dfrac{1}{1 - 6x + 8x^2} \left[ 1 - 4x + \dfrac{x^2(2-x)}{(1-x)^2} \right] \\
    & = \dfrac{(1 - 4x)(1 - 2x + x^2) - 2x^2 + x^3}{(1 - 6x + 8x^2)(1-x)^2} \\
    & = \dfrac{1 - 2x + x^2 - 4x + 8x^2 - 4x^3 + 2x^2 - x^3}{(1 - 6x + 8x^2)(1-x)^2} \\
    & = \dfrac{1 - 6x + 11x^2 - 5x^3}{(1 - 6x + 8x^2)(1 - x)^2}.
    
Bây giờ, :math:`1 - 6x + 8x^2` phân tích thành nhân tử :math:`(1 - 2x)(1 - 4x)`. Vậy mình sẽ cần tách :math:`G(x)` thành

.. math:: G(x) = \dfrac{A}{1 - 2x} + \dfrac{B}{1 - 4x} + \dfrac{C}{1 - x} + \dfrac{D}{(1-x)^2}

với :math:`A`, :math:`B`, :math:`C` và :math:`D` là các hệ số cần tìm. Quy đồng mẫu số mình có

.. math:: G(x) = \dfrac{A(1-4x)(1-x)^2 + B(1-2x)(1-x)^2 + C(1-2x)(1-4x)(1-x) + D(1-2x)(1-4x)}{(1 - 6x + 8x^2)(1-x)^2}.

Thu gọn tử số lại mình được

.. math:: (A + B + C + D) + (-6A - 4B - 7C - 6D) x + (9A + 5B + 14C + 8D) x^2 + (-4A - 2B - 8C) x^3,

và đồng nhất hệ số thì mình cần giải hệ phương trình

.. math:: 
    
    \begin{cases}
        A + B + C + D & = 1 \\
        -6A - 4B - 7C - 6D & = -6 \\
        9A + 5B + 14C + 8D & = 11 \\
        -4A - 2B - 8C & = -5
    \end{cases} \Longleftrightarrow \begin{cases}
        A = -1/2 \\
        B = 7/18 \\
        C = 7/9 \\
        D = 1/3
    \end{cases}

Bây giờ thay các hàm sinh vào :math:`G(x)` (chưa cần thay :math:`A`, :math:`B`, :math:`C` và :math:`D` vội) thì mình có

.. math:: 
    
    G(x) & = A \cdot \left( 1 + 2x + 2^2 x^2 + \cdots + 2^n x^n + \cdots \right) \\
    & + B \cdot \left( 1 + 4x + 4^2 x^2 + \cdots + 4^n x^n + \cdots \right) \\
    & + C \cdot \left( 1 + x + x^2 + \cdots + x^n + \cdots \right) \\
    & + D \cdot \left( 1 + 2x + 3x + \cdots + (n+1) x^n + \cdots \right).

Nhìn vào hệ số của :math:`x^n` mình có công thức tổng quát

.. math:: u_n = A \cdot 2^n + B \cdot 4^n + C + D \cdot (n + 1) = -2^{n-1} + \dfrac{7 \cdot 4^n}{18} + \dfrac{7}{9} + \dfrac{n+1}{3}.


Ví dụ III
----------

Trong một số trường hợp "hơi lú", ví dụ như

.. math:: u_n = 4u_{n-1} - 4u_{n-2}

thì nếu sử dụng đa thức đặc trưng ta có một phương trình bậc hai với nghiệm kép. Khi đó công thức tổng quát không còn ở dạng

.. math:: u_n = \alpha \cdot z_1^n + \beta \cdot z_2^n

với :math:`z_1` và :math:`z_2` là hai nghiệm phân biệt của phương trình đặc trưng, mà ở một dạng khác. Phương pháp hàm sinh sẽ giúp chúng ta tìm công thức tổng quát ở trường hợp này.

Xét đa thức :math:`G(x)` với hệ số là các số hạng của dãy :math:`\{ u_n \}` cho bởi công thức truy hồi ở trên:

.. math:: G(x) = u_0 + u_1 x + u_2 x^2 + \cdots + u_n x^n + \cdots

Thực hiện tương tự bên trên, mình tính

.. math:: x \cdot G(x) = u_0 x + u_1 x^2 + u_2 x^3 + \cdots + u_{n-1} x^n + \cdots

và

.. math:: x^2 \cdot G(x) = u_0 x^2 + u_1 x^3 + u_2 x^4 + \cdots + u_{n-2} x^n + \cdots

Như vậy

.. math:: 
    
    G(x) - 4x \cdot G(x) + 4x^2 \cdot G(x) & = u_0 \\
    & + (u_1 - 4u_0) x \\
    & + \cancelto{0}{(u_2 - 4u_1 + 4u_0)} x^2 \\
    & + \cdots \\
    & + \cancelto{0}{(u_n - 4u_{n-1} + 4u_{n-2})} x^n \\
    & + \cdots \\
    & = u_0 + (u_1 - 4u_0) x.

Đặt :math:`G(x)` làm nhân tử chung và chuyển vế mình có

.. math:: G(x) = \dfrac{u_0 + (u_1 - 4u_0) x}{(1 - 2x)^2}.

Mình cần tách :math:`G(x)` thành tổng

.. math:: G(x) = \dfrac{A}{1 - 2x} + \dfrac{B}{(1-2x)^2}.

Quy đồng mẫu số và đồng nhất hệ số mình cần tìm :math:`A` và :math:`B` thỏa mãn hệ phương trình

.. math:: 
    
    \begin{cases}
        A + B = u_0 \\
        -2A = (u_1 - 4u_0)
    \end{cases} \Longleftrightarrow \begin{cases}
        A = (-u_1 + 4u_0) / 2 \\
        B = (u_1 - 2u_0) / 2
    \end{cases}

Thay hàm sinh vào :math:`G(x)` mình được

.. math:: 
    
    G(x) & = A \cdot (1 + 2x + 2^2 x^2 + \cdots + 2^n x^n + \cdots) \\
    & + B \cdot \left[1 + 2 \cdot 2x + 3 \cdot 2^2 x^2 + \cdots + (n+1) \cdot 2^n x^n \right].
    
Hệ số trước :math:`x^n` cho ta công thức tổng quát của dãy số

.. math:: u_n = A \cdot 2^n + B \cdot (n+1) \cdot 2^n = 2^{n-1} \cdot \left[ 2u_0 + (u_1 - 2u_0) \cdot n \right].
