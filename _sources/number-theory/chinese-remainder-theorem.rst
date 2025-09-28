Định lý số dư Trung Hoa
***********************

Định lý số dư Trung Hoa (Chinese Remainder Theorem - CRT) là một trong những định lý quan trọng nhất của số học nói riêng và toán học nói chung.

Chứng minh định lý số dư Trung Hoa
==================================

Giả sử ta có hệ phương trình đồng dư

.. math:: 

    x & \equiv x_1 \pmod{m_1} \\
    x & \equiv x_2 \pmod{m_2} \\
    & \ldots \\
    x & \equiv x_k \pmod{m_k}.

Trong đó :math:`\gcd(m_i, m_j) = 1` với mọi :math:`i \neq j`, :math:`1 \leqslant i, j \leqslant k`.

Khi đó định lý số dư Trung Hoa phát biểu rằng hệ phương trình đồng như này có nghiệm duy nhất trong modulo :math:`M = m_1 m_2 \ldots m_k`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Chúng ta cần chứng minh sự tồn tại và tính duy nhất của nghiệm.

    Để chứng minh sự tồn tại, ta xây dựng cách tính nghiệm bằng quy nạp.

    *Bước cơ sở*. Với :math:`k = 2`, ta có :math:`x \equiv x_1 \pmod{m_1}` và :math:`x \equiv x_2 \pmod{m_2}`.

    Do :math:`\gcd(m_1, m_2) = 1` nên tồn tại hai số nguyên :math:`n_1`, :math:`n_2` sao cho :math:`m_1 n_1 + m_2 n_2 = 1` (bổ đề Bézout).

    Quan sát một chút, nếu ta modulo hai vế :math:`m_1 n_1 + m_2 n_2 = 1` cho :math:`m_1` thì sẽ có :math:`m_2 n_2 \equiv 1 \pmod{m_1}`. Như vậy

    .. math:: x \equiv x_1 \cdot 1 \pmod{m_1} \Longleftrightarrow x \equiv x_1 \cdot (m_2 n_2) \pmod{m_1}.

    Tương tự, :math:`m_1 n_1 \equiv 1 \pmod{m_2}` nên

    .. math:: x \equiv x_2 \cdot 1 \pmod{m_2} \Longleftrightarrow x \equiv x_2 \cdot (m_1 n_1) \pmod{m_2}.

    Từ đó ta có công thức nghiệm là

    .. math:: x \equiv x_1 m_2 n_2 + x_2 m_1 n_1 \pmod{m_1 m_2}.

    Khi modulo cho :math:`m_1` và :math:`m_2` thì kết quả là hai phương trình đồng dư ban đầu.

    Tiếp theo chúng ta sử dụng quy nạp để chứng minh với mọi :math:`k \geqslant 2` thì nghiệm của hệ phương trình đồng dư là

    .. math:: 
        :label: crt-eq1

        x \equiv x_1 M_1 N_1 + x_2 M_2 N_2 + \ldots + x_k M_k N_k \pmod{M}.

    Trong đó

    - :math:`M = m_1 \cdot m_2 \cdots m_k`;
    - :math:`M_i = M / m_i`;
    - :math:`N_i` là nghịch đảo của :math:`M_i` trong modulo :math:`m_i`.

    *Giả thiết quy nạp*. Giả sử :eq:`crt-eq1` đúng với :math:`k \geqslant 2`. Đặt :math:`M = m_1 \cdots m_k` và

    .. math:: X_k = x_1 M_1 N_1 + \ldots +  x_k M_k N_k.

    Với :math:`k+1` ta có

    .. math:: x \equiv X_k \pmod{M}, \quad x \equiv x_{k+1} \pmod{m_{k+1}}.

    Tương tự với hai modulo ở bước cơ sở, do :math:`\gcd(m_{k+1}, m_i) = 1` với mọi :math:`1 \leqslant i \leqslant k` nên

    .. math:: \gcd(m_{k+1}, m_1 \cdots m_k) = \gcd(m_{k+1}, M) = 1.

    Khi đó tồn tại các số nguyên :math:`\alpha` và :math:`\beta` sao cho :math:`\alpha M + \beta m_{k+1} = 1`.

    Nghiệm của hệ hai phương trình đồng dư khi này là

    .. math:: x \equiv X_k \beta m_{k+1} + x_{k+1} \alpha M \pmod{M \cdot m_{k+1}}.

    Đặt :math:`M' = M \cdot m_{k+1} = m_1 \cdots m_k \cdot m_{k+1}`. Ở đây :math:`M = M' / m_{k+1}` chính là :math:`M'_{k+1}` trong cách xây dựng nghiệm ở trên.

    Từ đó :math:`\alpha` chính là :math:`N'_{k+1}`.

    Ta có

    .. math:: X_k \beta m_{k+1} = (x_1 M_1 N_1 + \ldots + x_k M_k N_k) \beta m_{k+1}.

    Để ý rằng

    .. math:: M_i = M / m_i = M' / (m_i \cdot m_{k+1}),

    nên suy ra

    .. math:: M_i \cdot m_{k+1} = M' / m_i = M'_i.

    Tiếp theo, do :math:`\beta m_{k+1} \equiv 1 \pmod{M}` và :math:`M = m_1 \cdots m_k` nên :math:`\beta m_{k+1} \equiv 1 \pmod{m_i}` với :math:`1 \leqslant i \leqslant k`.

    Ở trên ta có :math:`N_i M_i \equiv 1 \pmod{m_i}` nên suy ra :math:`\beta m_{k+1} \cdot N_i M_i \equiv 1 \pmod{m_i}`, tương đương với :math:`(\beta N_i) \cdot (M_i m_{k+1}) \equiv 1 \pmod{m_i}`.

    Ta đã chứng minh ở trước :math:`M_i m_{k+1} = M'/m_i = M'_i` nên :math:`\beta N_i = N'_i`. Tới đây thì ta đã hoàn thành chứng minh do

    .. math:: 
        
        & X_k \cdot \beta \cdot m_{k+1} + x_{k+1} \cdot \alpha \cdot M \\ 
        = & (x_1 M_1 N_1 + \ldots + x_k M_k N_k) \cdot \beta \cdot m_{k+1} + x_{k+1} \cdot N'_{k+1} \cdot M'_{k+1} \\ 
        = & x_1 \cdot (\beta N_1) \cdot (M_1 m_{k+1}) + \ldots + x_k \cdot (\beta N_k) \cdot (M_k m_{k+1}) \\ 
        & + x_{k+1} \cdot N'_{k+1} \cdot M'_{k+1} \\ 
        = & x_1 N'_1 M'_1 + \ldots x_k N'_k M'_k + x_{k+1} N'_{k+1} M'_{k+1}.
        
    Để chứng minh sự duy nhất của nghiệm, giả sử :math:`y` là một nghiệm khác :math:`x` của hệ phương trình đồng dư (modulu :math:`M`). Khi đó :math:`y \equiv x_i \equiv x \pmod{m_i}`. Như vậy :math:`y = x + t_i m_i`, hay nói cách khác :math:`y` khác :math:`x` một bội của :math:`m_i`. Do đó trong modulo :math:`m_i` chỉ có thể có trường hợp :math:`y \equiv x` nên nghiệm tìm được ở modulo tổng là duy nhất.

.. prf:example:: 
    :label: exp-CRT-problem

    Tìm nghiệm của hệ phương trình đồng dư sau

    .. math:: 

        x & \equiv 1 \pmod 3 \\
        x & \equiv 4 \pmod 7.
        
    Ta có :math:`\gcd(3, 7) = 1` và :math:`3 \cdot 5 + 7 \cdot (-2) = 1`. Do đó nghiệm của hệ phương trình có dạng 

    .. math:: x \equiv 1 \cdot 7 \cdot (-2) + 4 \cdot 3 \cdot 5 = 4 \pmod{21}.

    Ta kiểm tra :math:`4 \equiv 1 \pmod 3` và :math:`4 \equiv 4 \pmod 7` thỏa mãn hệ phương trình đồng dư.

Bài tập sưu tầm
===============

**Câu 1** (đề kiểm tra, ITMO). Giải hệ đồng dư

.. math:: 
    
    \begin{cases}
        x \equiv 11 \pmod{56} \\
        x \equiv 25 \pmod{77}.
    \end{cases}

Do :math:`\gcd(56, 77) = 7` nên đầu tiên cần tách mỗi phương trình thành các module nguyên tố cùng nhau.

.. math:: 
    
    x \equiv 11 \pmod{56} \Rightarrow \begin{cases}
        x \equiv 11 \equiv 3 \pmod{8} \\
        x \equiv 11 \equiv 4 \pmod{7}.
    \end{cases}

.. math:: 
    
    x \equiv 25 \pmod{77} \Rightarrow \begin{cases}
        x \equiv 25 \equiv 4 \pmod{7} \\
        x \equiv 25 \equiv 3 \pmod{11}.
    \end{cases}

Sử dụng định lý số dư Trung Hoa cho hệ

.. math:: 
    
    \begin{cases}
        x \equiv 3 \pmod 8 \\
        x \equiv 4 \pmod 7 \\
        x \equiv 3 \pmod{11}
    \end{cases}

giải ra nghiệm :math:`x \equiv 179 \pmod{616}`.

**Câu 2** (đề kiểm tra, ITMO). Tìm hai chữ số cuối của số

.. math:: 318^{17683732657328}.

Tìm hai chữ số cuối cũng có nghĩa là tính đồng dư trong modulo :math:`100`.

Thay vì tính trong modulo :math:`100`, chúng ta tính trong modulo :math:`4` và :math:`25` rồi dùng định lý số dư Trung Hoa để gom nghiệm lại.

Đặt :math:`A = 318^{17683732657328}`.

Vì :math:`318 \equiv 0 \pmod 2` nên :math:`318^2 \equiv 0 \pmod{2^2}`. Nói cách khác :math:`A \equiv 0 \pmod 4`.

Vì :math:`\gcd(318, 25) = 1` nên :math:`318^{\varphi(25)} \equiv 1 \pmod{25}`. Do :math:`\varphi(25) = 20` nên suy ra

.. math:: 318^{17683732657320} \equiv 1 \pmod{25}.

Như vậy chỉ cần tính :math:`318^{8} \pmod{25}` nữa. Vì :math:`318 \equiv 18 \pmod{25}`, ta tính

.. math:: 18^2 = 1 \pmod{25} \Rightarrow 18^8 \equiv 1 \pmod{25}.

Như vậy :math:`318^{8} \equiv 1 \pmod{25}`. Ta có hệ đồng dư

.. math:: 
    
    \begin{cases}
        A \equiv 0 \pmod 4 \\
        A \equiv 1 \pmod{25}
    \end{cases}

Như vậy :math:`A \equiv 76 \pmod{100}`. Vậy hai chữ số cuối là :math:`76`.

**Câu 3** (đề kiểm tra, ITMO). Tìm tất cả nghiệm của phương trình

.. math:: x^2 \equiv 1 \pmod{5929}.

Vì :math:`5929 = 7^2 \cdot 11^2` nên ta giải trên hai modulo :math:`7^2` và :math:`11^2`.

Trên modulo :math:`7^2`, vì chỉ có :math:`\pm 1` thỏa :math:`x^2 \pmod 7` nên cũng chỉ có :math:`\pm 1` thỏa :math:`x^2 \equiv 1 \pmod{7^2}`.

Tương tự, trên modulo :math:`11^2`, vì chỉ có :math:`\pm 1` thỏa :math:`x^2 \pmod{11}` nên cũng chỉ có :math:`\pm 1` thỏa :math:`x^2 \equiv 1 \pmod{11^2}`.

Ta tính :math:`(7^2)^{-1} \equiv 42 \pmod{11^2}` và :math:`(11^2)^{-1} \equiv 32 \pmod{7^2}`.

Khi đó nghiệm của phương trình

.. math:: x^2 \equiv 1 \pmod{5929}

cũng là nghiệm của hệ

.. math:: 
    
    \begin{cases}
        x \equiv \pm 1 \pmod{7^2} \\
        x \equiv \pm 1 \pmod{11^2}.
    \end{cases}

Như vậy có :math:`4` nghiệm là

.. math:: x \equiv \pm 1 \cdot 7^2 \cdot 42 \pm 1 \cdot 32 \cdot 11^2 \equiv 1, 4115, 1814, 5928 \pmod{5929}.
