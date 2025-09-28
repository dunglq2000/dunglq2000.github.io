Magma
=====

Hệ mật mã Magma được chính phủ Xô Viết chọn làm chuẩn mã hóa. Cũng giống như hệ mật mã DES, Magma sử dụng mô hình Feistel cho các vòng mã hóa, được định nghĩa trong GOST 34.12-2015, trước đây gọi là GOST 28147-89.

Phần này tham khảo chính từ :cite:`Gashkov2010`.

Độ dài khóa là :math:`256` bits. Độ dài khối là :math:`64` bits. Magma biến đổi trên :math:`32` vòng để cho ra ciphertext.

Magma thực hiện biến đổi trên :math:`32` vòng Feistel. Khối đầu vào :math:`64` bits được chia thành hai nửa trái phải, mỗi nửa :math:`32` bits.

Key schedule
------------

Khóa :math:`256` bit được chia thành :math:`8` cụm khóa con, mỗi khóa con :math:`32` bit.

Nếu ta kí hiệu :math:`256` bit của khóa là :math:`k_{0} k_{1} \ldots k_{254} k_{255}` thì ta có các khóa con là

.. math:: \underbrace{k_0 \ldots k_{31}}_{K_0} \underbrace{k_{32} \ldots k_{63}}_{K_1} \ldots \underbrace{k_{224} \ldots k_{255}}_{K_7}.

Từ vòng :math:`1` tới :math:`24` sử dụng lần lượt các khóa :math:`K_0`, :math:`K_1`, ..., :math:`K_7` rồi lặp lại thứ tự đó.

Từ vòng :math:`25` tới :math:`32` sử dụng theo thứ tự ngược lại, từ :math:`K_7`, :math:`K_6`, ..., :math:`K_0`.

.. figure:: ../../figures/magma/blocky.*

    Mô hình mã khối Magma

Round function
--------------

Như ta đã biết, trong mô hình Feistel, mỗi khối plaintext được chia thành hai nửa trái phải :math:`(L_0, R_0)`. Sau đó ở mỗi vòng biến đổi thì

.. math:: L_{i+1} = R_i, \quad R_{i+1} = L_i \oplus f(R_i, K_i),

với :math:`i = 0, 1, \ldots` và :math:`K_i` là khóa con ở vòng :math:`i`.

Hàm :math:`f` của Magma khá đơn giản, bao gồm ba động tác là cộng modulo :math:`2^{32}`, SBox và xoay :math:`11` bits.

Đối với việc cộng modulo :math:`2^{32}`, ta xem block :math:`R_i` và :math:`K_i` như những số nguyên :math:`32` bit, cộng chúng lại và modulo :math:`2^{32}`, nghĩa là :math:`(R_i + K_i) \bmod 2^{32}`.

Đặt :math:`T_i = (R_i + K_i) \bmod 2^{32}`. Như vậy :math:`T_i` có :math:`32` bits. Ta chia :math:`32` bits này thành :math:`8` cụm :math:`4` bits. Ứng với mỗi cụm :math:`4` bits chúng ta cho qua một hoán vị. Như vậy cần :math:`8` hoán vị (SBox). SBox được sử dụng chung cho tất cả vòng.

Theo wiki thì SBox có thể bí mật. Tuy nhiên việc mã hóa và giải mã cần sử dụng SBox giống nhau. Do đó thiết bị mã hóa và giải mã có cùng cơ chế pseudo-random để sinh ra SBox giống nhau.

SBox được quy định theo tiêu chuẩn chính phủ Nga là

.. code-block:: python

    sbox = [
        [0xC, 0x4, 0x6, 0x2, 0xA, 0x5, 0xB, 0x9, 0xE, 0x8, 0xD, 0x7, 0x0, 0x3, 0xF, 0x1],
        [0x6, 0x8, 0x2, 0x3, 0x9, 0xA, 0x5, 0xC, 0x1, 0xE, 0x4, 0x7, 0xB, 0xD, 0x0, 0xF],
        [0xB, 0x3, 0x5, 0x8, 0x2, 0xF, 0xA, 0xD, 0xE, 0x1, 0x7, 0x4, 0xC, 0x9, 0x6, 0x0],
        [0xC, 0x8, 0x2, 0x1, 0xD, 0x4, 0xF, 0x6, 0x7, 0x0, 0xA, 0x5, 0x3, 0xE, 0x9, 0xB],
        [0x7, 0xF, 0x5, 0xA, 0x8, 0x1, 0x6, 0xD, 0x0, 0x9, 0x3, 0xE, 0xB, 0x4, 0x2, 0xC],
        [0x5, 0xD, 0xF, 0x6, 0x9, 0x2, 0xC, 0xA, 0xB, 0x7, 0x8, 0x1, 0x4, 0x3, 0xE, 0x0],
        [0x8, 0xE, 0x2, 0x5, 0x6, 0x9, 0x1, 0xC, 0xF, 0x4, 0xB, 0x0, 0xD, 0xA, 0x3, 0x7],
        [0x1, 0x7, 0xE, 0xD, 0x0, 0x5, 0x8, 0x3, 0x4, 0xF, 0xA, 0x6, 0x9, 0xC, 0xB, 0x2],
    ]

Nếu :math:`T_i` được viết dưới dạng :math:`32` bits là :math:`t_{31} t_{30} \ldots t_1 t_0` thì SBox tương ứng của nó là

.. math:: 

    \underbrace{t_{31} \ldots t_{28}}_{S_7}
    \underbrace{t_{27} \ldots t_{24}}_{S_6}
    \ldots
    \underbrace{t_{7} \ldots t_{4}}_{S_1}
    \underbrace{t_3 \ldots t_0}_{S_0}

Nói cách khác, :math:`t_{4i+3} t_{4i+2} t_{4i+1} t_{4i}` dùng :math:`S_{7-i}` với :math:`i = 0, 1, 2, \ldots, 7`.

Cuối cùng, việc xoay trái :math:`11` bits (rot11) chỉ đơn giản là đưa :math:`11` bit đầu về cuối và đưa :math:`21` bit cuối lên đầu.

Để giải mã ta vẫn sử dụng round function như lúc mã hóa, chỉ cần viết với thứ tự ngược lại là được. Như vậy

.. math:: R_i = L_{i+1}, \quad L_i = R_{i+1} \oplus f(L_{i+1}, K_i)

do :math:`R_i = L_{i+1}`. Lưu ý rằng khóa con lúc này là :math:`0` tới :math:`7` cho :math:`8` vòng đầu, và :math:`7` về :math:`0` (rồi lặp lại) cho :math:`24` vòng sau.
