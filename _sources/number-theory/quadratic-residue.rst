Thặng dư chính phương
*********************

.. prf:definition:: Số chính phương modulo :math:`p`
    :label: def-quadratic-residue

    Xét số nguyên tố lẻ :math:`p`. Số :math:`a` được gọi là **số chính phương modulo** :math:`p` nếu :math:`(a, m) = 1` và tồn tại số :math:`x` sao cho :math:`x^2 = a \pmod p`.

    Nói cách khác phương trình đồng dư :math:`x^2 \equiv a \pmod p` có nghiệm.

Chúng ta sử dụng kí hiệu Legendre (Legendre symbol) để thể hiện một số :math:`a` có phải là số chính phương modulo nguyên tố :math:`p` không.

.. prf:definition:: Legendre symbol
    :label: def-legendre-symbol

    Xét :math:`p` là số nguyên tố, :math:`a` là số nguyên không chia hết cho :math:`p`. Khi đó kí hiệu Legendre được định nghĩa là

    .. math:: 

        \left(\frac{a}{p}\right) = \begin{cases}
            1, & \text{ nếu } a \text{ là số chính phương modulo } p. \\
            -1, & \text{ nếu ngược lại}.
        \end{cases}

Một trường hợp tổng quát hơn của kí hiệu Legendre là kí hiệu Jacobi áp dụng cho số nguyên dương bất kì.

.. prf:definition:: Jacobi symbol
    :label: def-jacobi-symbol

    Xét :math:`n` là số nguyên dương, :math:`a` là số nguyên không chia hết cho :math:`n`. Khi đó kí hiệu Jacobi được định nghĩa là

    .. math:: 

        \left(\frac{a}{n}\right) = \begin{cases}
            1, & \text{ nếu } a \text{ là số chính phương modulo } n \\
            -1, & \text{ nếu ngược lại.}
        \end{cases}

Bài tập sưu tầm
===============

**Câu 1** (đề kiểm tra, ITMO). Số :math:`3` có là số chính phương modulo :math:`323` không?

Vì :math:`323 = 17 \cdot 19`, ta sử dụng tiêu chuẩn Euler cho từng modulo :math:`17` và :math:`19`:

.. math:: 

    \left(\frac{3}{17}\right) = 3^{\frac{17 - 1}{2}} \equiv -1 \pmod{17}, \\
    \left(\frac{3}{19}\right) = 3^{\frac{19 - 1}{2}} \equiv -1 \pmod{19}.
    
Như vậy :math:`3` không là số chính phương trong modulo :math:`17` và :math:`19`.

Kết luận: :math:`3` không là số chính phương modulo :math:`323`.
