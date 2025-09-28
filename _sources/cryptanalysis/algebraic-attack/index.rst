***********************
Algebraic cryptanalysis
***********************

Theo :cite:`10.5555/1618541` thì algebraic cryptanalysis (mình tạm dịch là **phá mã đại số**) là kỹ thuật phá mã dựa trên việc giải một hệ phương trình các đa thức trên trường :math:`\mathbb{F}_2` hoặc đôi khi là vành khác.

Algebraic cryptanalysis gồm hai giai đoạn:

1. Tìm sự liên kết giữa bản rõ và bản mã dưới dạng các hệ phương trình đa thức. Do đó algebraic cryptanalysis thuộc loại tấn công known-plaintext hoặc chosen-plaintext.
2. Giải hệ phương trình đại số. Ở bước này chúng ta có thể giải tay hoặc sử dụng những phần mềm chuyên dụng gọi là SAT-solver vì thông thường các loại mã hóa rất phức tạp.

====================
Interpolation Attack
====================

Interpolation, hay tiếng Việt gọi là nội suy (ví dụ Lagrange's interpolation là nội suy Lagrange) được giới thiệu vào 1997 :cite:`fse-1997-3078`.

Mình xin phép nhắc lại ý tưởng của nội suy Lagrange như sau:

- chúng ta không biết hệ số của đa thức bậc :math:`n`, giả sử là

.. math:: f(x) = a_0 + a_1 x + \cdots + a_n x^n

với :math:`a_n \neq 0`;

- chúng ta biết :math:`n+1` điểm thuộc đồ thị của đa thức là

.. math:: (x_0, f(x_0), (x_1, f(x_1)), \ldots, (x_n, f(x_n)));

- khi đó chúng ta hoàn toàn có thể tìm lại được đa thức :math:`f(x)` ban đầu.

Ở đây, interpolation attack sử dụng ý tưởng tương tự.

1. Chúng ta cố gắng xây dựng một đa thức liên hệ giữa bản rõ :math:`p` và bản mã :math:`c`, nghĩa là :math:`f(p) = c` với mọi cặp bản rõ :math:`p` và bản mã :math:`c`. Ở đây chúng ta không biết khóa.
2. Với một lượng cặp bản rõ-bản mã nhất định và bậc của đa thức :math:`f` thấp chúng ta hy vọng tìm lại được đa thức bằng nội suy.
3. Sử dụng đa thức tìm được để khôi phục khóa.

Ở :cite:`fse-1997-3078`, các tác giả xây dựng một toy cipher gọi là :math:`\mathcal{PURE}` nhằm demo cho phương pháp tấn công này.

.. _gioi-thieu-pure-cipher:

----------------------------------------
Giới thiệu :math:`\mathcal{PURE}` cipher
----------------------------------------

Thuật toán dựa trên mô hình Feistel với độ dài khối là :math:`64` bits và độ dài khóa là :math:`192` bits. Khóa :math:`K` gồm :math:`6` khóa con cho :math:`6` vòng là :math:`k_1`, :math:`k_2`, ..., :math:`k_6` với :math:`k_i \in \mathbb{F}_{2^{32}}`, nghĩa là mỗi khóa có :math:`32` bits (bằng một nửa độ dài khối, tương ứng với mô hình Feistel).

Ở vòng thứ :math:`i`, giả sử nửa trái là :math:`L_i` và nửa phải là :math:`R_i` thì round function của mô hình Feistel là

.. math:: L_{i+1} = R_i, \quad R_{i+1} = L_i \oplus (R_i \oplus K_{i+1})^3.

Ở đây, phép tính :math:`z^3` được tính trong trường :math:`\mathbb{F}_{2^{32}}`. Chúng ta có thể sử dụng bất kì đa thức tối giản nào làm modulo cho :math:`\mathbb{F}_{2^{32}}`.

Để demo cho interpolation attack chúng ta sẽ xét :math:`\mathcal{PURE}` cipher với :math:`3` vòng như hình sau.

.. figure:: ../../figures/cryptanalysis/interpolation-attack/pure_cipher.*
    
    :math:`\mathcal{PURE}` cipher với :math:`3` vòng

-----------------------------------------------
Thiết lập hệ phương trình giữa bản rõ và bản mã
-----------------------------------------------

Tiếp theo, chúng ta ... thay từng biểu thức vào để biểu diễn bản mã theo bản rõ.

Đầu tiên chúng ta cần chú ý một điều là do trường :math:`\mathbb{F}_{2^{32}}` có đặc số (characteristic) là :math:`2` nên :math:`3 \equiv 1`.

Ở vòng :math:`1`:

.. math:: 

    L_1 & = R_0, \\
    R_1 & = L_0 \oplus (R_0 \oplus K_1)^3 \\
    & = L_0 \oplus R_0^3 \oplus 3 R_0^2 K_1 \oplus 3 R_0 K_1^2 \oplus K_1^3 \\
    & = L_0 \oplus R_0^3 \oplus R_0^2 K_1 \oplus R_0 K_1^2 \oplus K_1^3.

Chúng ta có thể nói rằng :math:`L_1` và :math:`R_1` phụ thuộc vào :math:`L_0` và :math:`R_0`, nghĩa là có ánh xạ

.. math:: 
    
    \begin{cases}
        L_1 = \alpha_1(L_0, R_0) \\
        R_1 = \beta_1(L_0, R_0).
    \end{cases}

Ở vòng :math:`2`:

.. math:: 

    L_2 & = R_1 = L_0 \oplus R_0^3 \oplus R_0^2 K_1 \oplus R_0 K_1^2 \oplus K_1^3, \\
    R_2 & = L_1 \oplus (R_1 \oplus K_2)^3 = R_0 \oplus R_1^3 \oplus R_1^2 K_2 \oplus R_1 K_2^2 \oplus K_2^3.

Lúc này ta có :math:`L_2` và :math:`R_2` được biểu diễn theo :math:`L_1` và :math:`R_1`, giả sử chúng ta có ánh xạ

.. math:: 
    
    \begin{cases}
        L_2 = \alpha_2(L_1, R_1) = \alpha_2(\alpha_1(L_0, R_0), \beta_1(L_0, R_0)) \\
        R_2 = \beta_2(L_1, R_1) = \beta_2(\alpha_1(L_0, R_0), \beta_1(L_0, R_0)).
    \end{cases}

Tương tự ở vòng :math:`3`:

.. math:: 

    L_3 & = R_2 = R_0 \oplus R_1^3 \oplus R_1^2 K_2 \oplus R_1 K_2^2 \oplus K_2^3, \\
    R_3 & = L_2 \oplus (R_2 \oplus K_3)^3 = R_1 \oplus R_2^3 \oplus R_2^2 K_2 \oplus R_2 K_2^2 \oplus K_3^3.

Chúng ta thực hiện tương tự như hai vòng trước và nhanh chóng nhận ra rằng việc thay thế này rất cồng kềnh. Do đó mình sử dụng SageMath để thực hiện khai triển giúp mình. Các bạn có thể xem đoạn code sau nếu hứng thú.

.. admonition:: Code tính :math:`L_3` và :math:`R_3` theo :math:`L_0`, :math:`R_0`, và khóa con
    :class: dropdown

    .. code-block:: python

        from sage.all import *

        F = GF(2)['x']; x = F.gen()
        F32 = GF(2**3, name='x', modulus='random')
        Pr = PolynomialRing(F32, names='l0, r0, k1, k2, k3')
        l0, r0, k1, k2, k3 = Pr.gens()

        l1 = r0
        r1 = l0 + (r0 + k1)**3

        l2 = r1
        r2 = l1 + (r1 + k2)**3

        l3 = r2
        r3 = l2 + (r2 + k3)**3

        # Format for LaTeX
        f = str(l3) \
            .replace('r0', 'R_0') \
            .replace('l0', 'L_0') \
            .replace('k1', r'{\color{red}K_1}') \
            .replace('k2', r'{\color{red}K_2}') \
            .replace('k3', r'{\color{red}K_3}') \
            .replace('+', r'\oplus') \
            .replace('*', ' ')
        print(f)

Như vậy chúng ta biểu diễn được :math:`L_3` và :math:`R_3` theo :math:`L_0`, :math:`R_0` và các khóa con như sau.

.. math:: 

    R_3 & = R_0^{27} + \cdots \\
    L_3 & = R_0^9 \oplus R_0^8 {\color{red}K_1} \oplus R_0 {\color{red}K_1}^8 \oplus {\color{red}K_1}^9 \oplus L_0 R_0^6 \\
    & \oplus L_0 R_0^4 {\color{red}K_1}^2 \oplus L_0 R_0^2 {\color{red}K_1}^4 \oplus L_0 {\color{red}K_1}^6 \oplus R_0^6 {\color{red}K_2} \oplus R_0^4 {\color{red}K_1}^2 {\color{red}K_2} \\
    & \oplus R_0^2 {\color{red}K_1}^4 {\color{red}K_2} \oplus {\color{red}K_1}^6 {\color{red}K_2} \oplus L_0^2 R_0^3 \oplus L_0^2 R_0^2 {\color{red}K_1} \oplus L_0^2 R_0 {\color{red}K_1}^2 \\
    & \oplus L_0^2 {\color{red}K_1}^3 \oplus R_0^3 {\color{red}K_2}^2 \oplus R_0^2 {\color{red}K_1} {\color{red}K_2}^2 \oplus R_0 {\color{red}K_1}^2 {\color{red}K_2}^2 \oplus {\color{red}K_1}^3 {\color{red}K_2}^2 \\
    & \oplus L_0^3 \oplus L_0^2 {\color{red}K_2} \oplus L_0 {\color{red}K_2}^2 \oplus {\color{red}K_2}^3 \oplus R_0.

Ở đây :math:`R_3` là đa thức bậc :math:`27` theo :math:`R_0` và :math:`L_0`, có lẽ chúng ta không nên dây dưa với anh bạn này.

Nhìn :math:`L_3` cũng khá rối rắm nhưng vẫn có thể xử lý được (hoặc mình tin vậy). Hơn nữa trong biểu thức của :math:`L_3` không có sự xuất hiện của :math:`K_3`. Tuy nhiên chỉ với một cặp bản rõ :math:`P = L_0 \Vert R_0` và bản mã :math:`C = L_3 \Vert R_3` thì không đủ để chúng ta tìm lại khóa.

Ý tưởng của interpolation attack cũng như nội suy Lagrange là dựa trên nhiều cặp bản rõ-bản mã. Trong biểu thức của :math:`L_3` nếu chúng ta nhóm hạng tử theo bậc của :math:`R_0` lại thì ta có các hệ số:

- trước :math:`R_0^9` là :math:`1`;
- trước :math:`R_0^8` là :math:`K_1`;
- trước :math:`R_0^6` là :math:`L_0 \oplus K_2`;
- trước :math:`R_0^4` là :math:`L_0 K_1^2 \oplus K_1^2 K_2`;
- trước :math:`R_0^3` là :math:`L_0^2 \oplus K_2^2`;
- trước :math:`R_0^2` là :math:`K_1^4 K_2 \oplus L_0^2 K_1^2 \oplus K_1 K_2^2`;
- trước :math:`R_0` là :math:`L_0^2 K_1^2 \oplus K_1^2 K_2^2`;
- hệ số tự do là các đơn thức còn lại không chứa :math:`R_0`.

Như vậy chúng ta sẽ có biểu diễn :math:`L_3` theo :math:`R_0` là đa thức dạng

.. math:: L_3 = R_0^9 \oplus a_8 R_0^8 \oplus a_6 R_0^6 \oplus a_4 R_0^4 \oplus a_3 R_0^3 \oplus a_2 R_0^2 \oplus a_1 R_0 \oplus a_0

với :math:`a_i` có thể xem là hàm của theo các khóa con và :math:`L_0`.

Nếu chúng ta cố định :math:`L_0` và thay đổi :math:`R_0` thì với :math:`7` cặp bản rõ-bản mã là đủ để khôi phục đa thức trên nếu chúng ta giải hệ phương trình tuyến tính. Trong trường hợp :math:`\mathcal{PURE}` với :math:`6` vòng như bản gốc thì chúng ta cần nhiều cặp bản rõ-bản mã hơn nhiều, theo đó việc tính toán đa thức sẽ tốn công sức hơn.

Khi đã khôi phục được đa thức, tức là đã tìm được các hệ số, thì chúng ta có thể mã hóa bất kì thông điệp nào mà không cần quan tâm khóa. Vậy nếu chúng ta muốn tìm khóa thì sao?

Như đã nói, các hệ số của đa thức có thể được xem như các hàm theo các khóa con và nửa trái ban đầu :math:`L_0`. Lúc này ta có một hệ phương trình không tuyến tính và việc giải quyết khá khó khăn. Trong phiên bản đơn giản với :math:`3` vòng như trên, để ý rằng hệ số trước :math:`R_0^8` chính là :math:`K_1`. Từ đây, kết hợp với các phương trình khác có thể tìm được :math:`K_2`. Tuy nhiên với :math:`K_3` thì chúng ta không còn cách nào khác ngoài vét cạn. Như vậy có thể kết luận:

1. Với phiên bản :math:`\mathcal{PURE}` cipher đơn giản với :math:`3` vòng cần :math:`7` cặp bản rõ-bản mã (để tìm :math:`K_1` và :math:`K_2`) và vét cạn :math:`2^{32}` trường hợp khóa :math:`K_3`.
2. Với :math:`\mathcal{PURE}` cipher gốc :math:`6` vòng thì ta cần nhiều cặp bản rõ-bản mã hơn để tìm :math:`5` khóa con đầu và vét cạn :math:`2^{32}` trường hợp khóa :math:`K_6`.

Ở đây là đoạn code demo cho :math:`\mathcal{PURE}` cipher với :math:`3` vòng của mình.

.. admonition:: Demo tấn công :math:`\mathcal{PURE}` cipher :math:`3` vòng
    :class: dropdown

    .. code-block:: python

        from sage.all import GF, matrix, vector
        import random

        # Define fields
        F = GF(2)['x'] # GF(2)
        x = F.gen()
        F32 = GF(2**32, name='x', modulus='random') # GF(2^{32})

        K = [F32.random_element() for _ in range(3)] # round keys

        for i in range(3):
            print(f"K_{i + 1} =", K[i].to_integer())

        def encrypt(pt: bytes):
            # encrypt with PURE cipher
            pL, pR = F32.from_bytes(pt[:4]), F32.from_bytes(pt[4:])
            for i in range(3):
                pL, pR = pR, pL + (pR + K[i])**3
            return pL.to_bytes()[1:] + pR.to_bytes()[1:]

        pts = []
        cts = []
        M = []
        v = []

        for _ in range(7):
            # Chosen-plaintext with fixed left-half
            pt = bytes(range(12, 16)) + random.randbytes(4)
            ct = encrypt(pt)
            pR = F32.from_bytes(pt[4:])
            cL = F32.from_bytes(ct[:4])
            m = [pR**i for i in [0, 1, 2, 3, 4, 6, 8]]
            M.append(m)
            v.append(cL - pR**9)

        M = matrix(F32, M)
        v = vector(F32, v)
        sol = M.solve_right(v)
        print(sol[-1].to_integer())
