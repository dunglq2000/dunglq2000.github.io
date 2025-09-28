************
Slide attack
************

Phá mã vi sai (differential cryptanalysis) và phá mã tuyến tính (linear cryptanalysis) dựa trên các phân bổ xác suất khi sử dụng S-box. Một ý tưởng đơn giản để chống lại phân tích xác suất là tăng số vòng lên, khi đó chúng ta cần nhiều cặp bản rõ-bản mã hơn để tìm liên hệ giữa các bit của khóa. Rõ ràng nếu số lượng cặp bản rõ-bản mã quá nhiều thì rất khó để tính toán và lưu trữ nên có thể nói cách tiếp cận này hợp lý.

Tuy nhiên slide attack ra đời và đã chứng minh được rằng số vòng nhiều không đồng nghĩa với an toàn hơn.

Tương tự với hai phần trước, mình vẫn dùng TinyDES làm ví dụ cho slide attack.

============
Slide attack
============

Slide attack là kỹ thuật tấn công mã khối dạng know-plaintext hoặc chosen-plaintext.

Gọi :math:`F` là một hoặc hợp của nhiều phép biến đổi trong thuật toán. Giả sử bản rõ ban đầu là :math:`P = P_0`, sau khi đi qua hàm :math:`F` sẽ trở thành :math:`P_1 = F(P_0)`. Tương tự, :math:`P_1` đi qua hàm :math:`F` sẽ trở thành :math:`P_2 = F(P_1)`. Cứ như vậy tới khi nhận được bản rõ ở cuối thuật toán, giả sử là sau :math:`n` lần biến đổi, :math:`C = P_n`.

Thông thường, mỗi lần thực hiện phép biến đổi :math:`F` cũng sẽ đi kèm một hoặc nhiều khóa con. Khi khóa con được sử dụng lặp lại, gọi là :math:`K`, thì ta có sơ đồ

.. math:: P = P_0 \xrightarrow{F_K} P_1 \xrightarrow{F_K} P_2 \xrightarrow{F_K} \cdots \xrightarrow{F_K} P_n = C.

Mục tiêu của slide attack là tìm một cặp bản rõ-bản mã :math:`(P, C)` và :math:`(P', C')` mà chúng ta gọi là **slid pair**.

.. prf:definition:: Slid pair
    :label: def-slid-pair

    Xét một phép biến đổi :math:`F_K` với :math:`K` là khóa được sử dụng lặp lại cho mỗi lần thực hiện hàm :math:`F`. Để mã hóa bản rõ :math:`P` thành bản mã :math:`C` giả sử ta thực hiện theo thứ tự

    .. math:: P = P_0 \xrightarrow{F_K} P_1 \xrightarrow{F_K} P_2 \xrightarrow{F_K} \cdots \xrightarrow{F_K} P_n = C.

    Tương tự, để mã hóa bản rõ :math:`P'` thành bản mã :math:`C'` giả sử ta thực hiện theo thứ tự

    .. math:: P' = P_0' \xrightarrow{F_K} P_1' \xrightarrow{F_K} P_2' \xrightarrow{F_K} \cdots \xrightarrow{F_K} P_n' = C'.

    Khi đó, cặp bản rõ-bản mã :math:`(P, C)` và :math:`(P', C')` được gọi là **slid pair** nếu :math:`F_K(P) = P'` và :math:`F_K(C) = C'`.

.. figure:: ../../figures/cryptanalysis/slide_attack/slide_attack.*
    
    Sơ đồ mô tả slid pair

Nếu chúng ta có một cặp bản rõ-bản mã là slid pair thì chúng ta có thể trích xuất khóa :math:`K` từ hai phương trình. Điểm quan trọng của slide attack là chúng ta chỉ quan tâm hai điều kiện :math:`F_K(P) = P'` và :math:`F_K(C) = C'`, còn việc hàm :math:`F` thực hiện bao nhiêu lần không quan trọng. Đây chính là ý nghĩa mình nói ở đầu bài, tăng số vòng không đồng nghĩa với an toàn hơn.

Sau đây mình sẽ ví dụ đơn giản về slide attack. Giống như hai bài trước, mình vẫn dùng TinyDES nhưng ở đây sẽ có hai thay đổi nhỏ.

=================================
Slide attack trên mô hình Feistel
=================================

------------------------
Slide attack với TinyDES
------------------------

TinyDES là một phiên bản thu nhỏ của chuẩn mã hóa DES. TinyDES là mã hóa khối theo mô hình Feistel, kích thước khối là :math:`8` bit, kích thước khóa cũng là :math:`8` bit. Mỗi vòng khóa con có độ dài :math:`6` bit. Trong phần slide attack này chúng ta sẽ thay đổi một vài điểm so với TinyDES ở hai bài trước.

.. figure:: ../../figures/tinydes/tinydes.*
    
    Một vòng TinyDES

Theo mô hình Feistel, khối đầu vào :math:`8` bit được chia thành hai nửa trái phải :math:`4` bit. Nửa phải sẽ đi qua các hàm Expand, SBox và PBox, sau đó XOR với nửa trái để được nửa phải mới. Còn nửa trái mới là nửa phải cũ. Tóm lại công thức mô hình Feistel là: 

.. math:: L_{i+1} = R_i, \quad R_{i+1} = L_i \oplus F(R_i, K)

với :math:`i = 1, 2, \ldots, 100` với đầu vào của khối là :math:`(L_0, R_0)`. Ở đây chúng ta lưu ý **hai** thay đổi so với TinyDES ở hai bài trước:

- hiện tại chúng ta sử dụng :math:`100` vòng thay vì :math:`3` như hai bài trước;
- cả :math:`100` vòng sử dụng duy nhất một khóa con là :math:`K`.

Chúng ta vẫn dùng các động tác sau:

1. Expand: mở rộng và hoán vị :math:`R_i` từ :math:`4` bits lên :math:`6` bits. Giả sử :math:`4` bits của :math:`R_i` là :math:`b_0 b_1 b_2 b_3` thì kết quả sau khi Expand là :math:`b_2 b_3 b_1 b_2 b_1 b_0`.
2. SBox: gọi :math:`6` bits đầu vào là :math:`b_0 b_1 b_2 b_3 b_4 b_5`. Khi đó ta tra cứu theo bảng SBox với :math:`b_0 b_5` chỉ số **hàng**, :math:`b_1 b_2 b_3 b_4` chỉ số **cột**. Nói cách khác bảng SBox có :math:`4` hàng, :math:`16` cột. Kết quả của SBox là một số :math:`4` bits.
3. PBox: là hàm hoán vị :math:`4` bit :math:`b_0 b_1 b_2 b_3` thành :math:`b_2 b_0 b_3 b_1`.

Như vậy, hàm :math:`F` của mô hình Feistel đối với mã TinyDES là:

.. math:: F(R_i, K) = \mathsf{PBox}(\mathsf{SBox}(\mathsf{Expand}(R_i) \oplus K)).

Để sinh khóa con cho :math:`100` vòng, khóa ban đầu được chia thành hai nửa trái phải lần lượt là :math:`KL_0` và :math:`KR_0`. TinyDES thực hiện như sau:

- :math:`KL_0` và :math:`KR_0` được dịch vòng trái :math:`1` bit để được :math:`KL_1` và :math:`KR_1`;
- khóa :math:`K` dùng chung cho :math:`100` vòng là hoán vị và nén :math:`8` bits của :math:`KL_1 \Vert KR_1`. Đặt :math:`8` bits khi ghép :math:`KL_1 \Vert KR_1` là :math:`k_0 k_1 k_2 k_3 k_4 k_5 k_6 k_7`. Khi đó khóa :math:`K` là :math:`6` bits :math:`k_5 k_1 k_3 k_2 k_7 k_0`.

.. admonition:: tinydes.py
    :class: dropdown

    .. code-block:: python

        # tindeys.py

        sbox = [
            0xE, 0x4, 0xD, 0x1, 0x2, 0xF, 0xB, 0x8, 0x3, 0xA, 0x6, 0xC, 0x5, 0x9, 0x0, 0x7,
            0x0, 0xF, 0x7, 0x4, 0xE, 0x2, 0xD, 0x1, 0xA, 0x6, 0xC, 0xB, 0x9, 0x5, 0x3, 0x8,
            0x4, 0x1, 0xE, 0x8, 0xD, 0x6, 0x2, 0xB, 0xF, 0xC, 0x9, 0x7, 0x3, 0xA, 0x5, 0x0,
            0xF, 0xC, 0x8, 0x2, 0x4, 0x9, 0x1, 0x7, 0x5, 0xB, 0x3, 0xE, 0xA, 0x0, 0x6, 0xD
        ]


        def Xor(a: list[int], b: list[int]) -> list[int]:
            return [x^y for x, y in zip(a, b)]


        def Expand(R: list[int]) -> list[int]:
            return [R[2], R[3], R[1], R[2], R[1], R[0]]


        def SBox(R: list[int]) -> list[int]:
            row = int("".join(map(str, [R[0], R[5]])), 2)
            col = int("".join(map(str, R[1:5])), 2)

            return list(map(int, format(sbox[row*16 + col], "04b")))


        def PBox(R: list[int]) -> list[int]:
            return [R[2], R[0], R[3], R[1]]


        def PBox_inv(R: list[int]) -> list[int]:
            return [R[1], R[3], R[0], R[2]]


        def Compress(K: list[int], round: int) -> list[int]:
            left, right = K[:4], K[4:]
            if round == 0 or round == 2:
                left = left[1:] + left[:1]
                right = right[1:] + right[:1]
            elif round == 1:
                left = left[2:] + left[:2]
                right = right[2:] + right[:2]

            Ki = left + right
            return left, right, [Ki[5], Ki[1], Ki[3], Ki[2], Ki[7], Ki[0]]


        def encrypt_block(plaintext: list[int], key: list[int]) -> list[int]:
            keys = [key]
            left, right = key[:4], key[4:]
            for i in range(3):
                left, right, key = Compress(left + right, i)
                keys.append(key)

            left, right = plaintext[:4], plaintext[4:]
            for i in range(100):    # 100 vòng
                # chỉ sử dụng mỗi K_1 trong TinyDES gốc
                left, right = right, Xor(left, PBox(SBox(Xor(Expand(right), keys[1]))))

            return left + right

        # print(encrypt_block([0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 0]))

Ở đây chúng ta thấy mô hình mã hóa sẽ diễn ra như sau. Gọi :math:`(L_0, R_0)` là hai nửa trái phải của bản rõ ban đầu :math:`P`. Khi đó, ở mỗi vòng biến đổi sẽ sử dụng chung khóa con :math:`K` theo mô hình

.. math:: P = (L_0, R_0) \xrightarrow{F_K} (L_1, R_1) \xrightarrow{F_K} (L_2, R_2) \xrightarrow{F_K} (L_3, R_3) = C.

Theo mô hình Feistel thì

.. math:: L_1 = R_0, \quad R_1 = L_0 \oplus f(R_0, K)

với :math:`f` là round function tương ứng với thuật toán TinyDES. Nói cách khác thì :math:`F_k` là

.. math:: F_K(L_i, R_i) = (R_i, L_i \oplus f(R_i, K)).

Lúc này slid pair có dạng

.. math:: 
    
    \begin{cases}
        F_K(P) = P' \\ F_K(C) = C' 
    \end{cases} \Longleftrightarrow \begin{cases}
        F_K(L_0, R_0) = (L_0', R_0') \\
        F_K(L_3, R_3) = (L_3', R_3')
    \end{cases}

hay tương đương với

.. math:: 
    :label: eq:slid

    \begin{cases}
        (R_0, L_0 \oplus f(R_0, K)) = (L_0', R_0') \\
        (R_3, L_3 \oplus f(R_3, K)) = (L_3', R_3')
    \end{cases} \Longleftrightarrow \begin{cases}
        R_0 = L_0' \\ L_0 \oplus f(R_0, K) = L_0' \\
        R_3 = L_3' \\ L_3 \oplus f(R_3, K) = R_3'.
    \end{cases}

Như vậy:

    nếu chúng ta có :math:`(P, C)` và :math:`(P', C')` thỏa các điều kiện ở :eq:`eq:slid` thì chúng ta có slid pair.

Câu hỏi đặt ra là nếu chúng ta không biết khóa con :math:`K` thì làm sao kiểm tra được các điều kiện trên?

Câu trả lời (mà cũng là cách chúng ta thực hiện trên thực tế) là chúng ta **giả sử đã tìm được slid pair**. Như vậy điều kiện đầu và điều kiện thứ ba phải thỏa mãn trước. Sau đó từ điều kiện thứ hai và thứ tư chúng ta tìm ngược lại :math:`K`. Cuối cùng chúng ta thử mã hóa :math:`P` với :math:`K` đã tìm được. Nếu chúng ta thu được chính xác :math:`C` thì :math:`K` là khóa con cần tìm, ngược lại thì chúng ta thử với slid pair khác.

.. admonition:: solve.py
    :class: dropdown

    .. code-block:: python

        # solve.py

        from tinydes import encrypt_block, PBox, SBox, Expand, Xor
        import random


        def fault_encrypt_block(plaintext: list[int], key: list[int]) -> list[int]:
            left, right = plaintext[:4], plaintext[4:]
            for _ in range(100):
                left, right = right, Xor(left, PBox(SBox(Xor(Expand(right), key))))
            
            return left + right


        pts = []
        cts = []
        secret_key = [1, 0, 0, 1, 1, 1, 1, 0]

        L = 2**4

        for _ in range(L):
            pt = [random.randint(0, 1) for __ in range(8)]
            ct = encrypt_block(pt, secret_key)
            pts.append(pt)
            cts.append(ct)

        for i in range(L):
            L0, R0 = pts[i][:4], pts[i][4:]
            L3, R3 = cts[i][:4], cts[i][4:]
            for j in range(i + 1, L):
                l0, r0 = pts[j][:4], pts[j][4:]
                l3, r3 = cts[j][:4], cts[j][4:]
                # Lazy bruteforce for K
                for k in range(2**6):
                    key = list(map(int, f"{k:06b}"))
                    # Check slid pair
                    if l0 == R0 and r0 == Xor(L0, PBox(SBox(Xor(Expand(R0), key)))):
                        if l3 == R3 and r3 == Xor(R3, PBox(SBox(Xor(Expand(R3), key)))):
                            if fault_encrypt_block(pts[i], key) == cts[i]:
                                print(key)

Ở đoạn code trên mình bruteforce khóa con :math:`K` vì SBox của TinyDES (và cũng là của DES) nhận đầu vào :math:`6` bit nhưng đầu ra giảm còn :math:`4` bit (chứ không phải do mình lười đâu hiuhiu). Do đó có thể có nhiều trường hợp của khóa con :math:`K` có thể thỏa mãn điều kiện của slid pair. Chúng ta cũng có thể tạo lookup table và thực hiện ngược lại round function để tìm các khả năng của khóa con :math:`K`.

Gọi :math:`\mathsf{PBox}^{-1}` là phép biến đổi ngược của :math:`\mathsf{PBox}`. Khi đó từ điều kiện thứ hai :math:`L_0 \oplus f(R_0, K) = L_0'` suy ra

.. math:: L_0 \oplus L_0' = f(R_0, K) = \mathsf{PBox}(\mathsf{SBox}(\mathsf{Expand}(R_0) \oplus K)),

suy ra

.. math:: \mathsf{PBox}^{-1}(L_0 \oplus L_0') = \mathsf{SBox}(\mathsf{Expand}(R_0) \oplus K).

Chúng ta có thể tính được :math:`\mathsf{PBox}^{-1}(L_0 \oplus L_0')` và :math:`\mathsf{Expand}(R_0)` nên việc "đoán" :math:`K` không phải vấn đề khó khăn. Thêm nữa điều kiện thứ tư cũng cho chúng ta các ứng cử viên cho khóa con :math:`K`. Kết hợp hai điều kiện này chúng ta có khóa con :math:`K` và chúng ta sẽ thử mã hóa :math:`P` thành :math:`C`.

--------------------
Slide attack với DES
--------------------

Ở olympiad mật mã học quốc tế NSUCRYPTO 2024 có một bài slide attack trên DES là bài 4 ở round 2 "Weak key schedule for DES". Bài này được giải bởi bạn Chương (vnc) đội mình. Ở phần sau mình sẽ trình bày lời giải cho bài này. Mình sẽ sử dụng code của bạn Chương trong lời giải. Xin cám ơn bạn Chương vì đã đóng góp :D :D :D

Trong bài này, thông tin ban đầu là file ``Book.txt`` và được mã hóa thành file ``Book_Cipher.txt``.

Thuật toán được sử dụng để mã hóa là DES. Tuy nhiên trong bài này đặc biệt ở chỗ mỗi vòng đều dùng chung một khóa con (khóa con đầu tiên của thuật toán sinh khóa con).

Nhiệm vụ của chúng ta là tìm khóa con đó và giải mã thông điệp sau:

.. code-block:: 

    86991641D28259604412D6BA88A5C0A6471CA7222C52482BF2D0E841D4343DFB877DC8E0147F3D5F20FC18FF28CB5C4DA8A0F4694861AB5E98F37ADBC2D69B35779D9001BB4B648518FE6EBC00B2AB10

^^^^^^^^^^^^^^^^^^
Cài đặt FAULTY_DES
^^^^^^^^^^^^^^^^^^

Ở đây bạn Chương gọi thuật toán của đề bài là ``FAULTY_DES`` và bạn sẽ cài đặt thuật toán này cùng với một số hàm bổ trợ cho việc giải bài.

.. admonition:: faulty_des.py
    :class: dropdown

    .. code-block:: python

        # faulty_des.py

        from typing import List, Tuple

        class DES_CONST:
            PC1 = (
                57, 49, 41, 33, 25, 17, 9 ,
                1 , 58, 50, 42, 34, 26, 18,
                10, 2 , 59, 51, 43, 35, 27,
                19, 11, 3 , 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7 , 62, 54, 46, 38, 30, 22,
                14, 6 , 61, 53, 45, 37, 29,
                21, 13, 5 , 28, 20, 12, 4 ,
            )

            PC2 = (
                14, 17, 11, 24, 1 , 5 ,
                3 , 28, 15, 6 , 21, 10,
                23, 19, 12, 4 , 26, 8 ,
                16, 7 , 27, 20, 13, 2 ,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32,
            )

            KEY_ROTATION = (
                1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1,
            )

            INITIAL_PERMUTATION = (
                58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9 , 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7,
            )

            ROUND_PERMUTATION = (
                16, 7 , 20, 21,
                29, 12, 28, 17,
                1 , 15, 23, 26,
                5 , 18, 31, 10,
                2 , 8 , 24, 14,
                32, 27, 3 , 9 ,
                19, 13, 30, 6 ,
                22, 11, 4 , 25,
            )

            INV_ROUND_PERMUTATION = (
                9, 17, 23, 31,
                13, 28, 2, 18,
                24, 16, 30, 6,
                26, 20, 10, 1,
                8, 14, 25, 3 ,
                4, 29, 11, 19,
                32, 12, 22, 7,
                5, 27, 15, 21,
            )

            FINAL_PERMUTATION = (
                40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9 , 49, 17, 57, 25,
            )

            EXPANSION = (
                32, 1 , 2 , 3 , 4 , 5 ,
                4 , 5 , 6 , 7 , 8 , 9 ,
                8 , 9 , 10, 11, 12, 13,
                12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21,
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1 ,
            )

            SBOX = [
                (
                    14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
                    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
                    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
                    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,
                ),
                (
                    15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
                    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,
                ),
                (
                    10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                    13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                    13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                    1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
                ),
                (
                    7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                    13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                    10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                    3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,
                ),
                (
                    2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                    14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                    4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                    11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,
                ),
                (
                    12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                    9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                    4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
                ),
                (
                    4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                    13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                    1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                    6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
                ),
                (
                    13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                    1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                    7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                    2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11,
                ),
            ]

        class HELP:
            @classmethod
            def INT_TO_BITS(cls, value: int, size: int) -> List[int]:
                bits = []
                for i in reversed(range(size)):
                    bits.append((value >> i) & 1)
                return bits

            @classmethod
            def BITS_TO_INT(cls, bits: List[int]) -> int:
                value = 0
                for bit in bits:
                    value <<= 1
                    value |= bit
                return value
            
            @classmethod
            def BLOCK_TO_BITS(cls, block: bytes) -> List[int]:
                bits = []
                for byte in block:
                    bits.extend(cls.INT_TO_BITS(byte, 8))
                return bits
            
            @classmethod
            def BITS_TO_BLOCK(cls, bits: List[int], size: int) -> bytes:
                block_bytes = []
                for i in range(size):
                    byte = cls.BITS_TO_INT(bits[i * 8 : (i + 1) * 8])
                    block_bytes.append(byte)
                return bytes(block_bytes)
            
            @classmethod
            def PERMUTATE(cls, bits: List[int], table: List[int]) -> List[int]:
                return [
                    bits[table[i] - 1] for i in range(len(table))
                ]

            @classmethod
            def XOR(cls, bits1: List[int], bits2: List[int]) -> List[int]:
                return [x ^ y for x, y in zip(bits1, bits2)]

            @classmethod
            def EXPAND(cls, bits: List[int], table: List[Tuple]) -> List[int]:
                return [
                    bits[table[i] - 1]
                    for i in range(len(table))
                ]
            @classmethod
            def SUBSTITUTE(cls, bits: List[int], mapping: List[Tuple]) -> List[int]:
                pieces = []

                for i in range(8):
                    piece_bits = bits[i * 6 : (i + 1) * 6]

                    piece = HELP.BITS_TO_INT(piece_bits)
                    pieces.append(piece)

                values = []

                for i, piece in enumerate(pieces):
                    row = (piece & 1) | ((piece >> 4) & 0b10)
                    column = (piece & 0b011110) >> 1

                    values.append(mapping[i][row * 16 + column])

                result_bits = []

                for value in values:
                    result_bits.extend(HELP.INT_TO_BITS(value, 4))

                return result_bits
            
        class FAULTY_DES:
            def __init__(self, rk: bytes, rounds: int = 16):
                self.rounds = rounds
                self.round_keys = [HELP.BLOCK_TO_BITS(rk) for _ in range(rounds)]
                self.reversed_round_keys = self.round_keys[::-1]

            def encrypt(self, plaintext: bytes) -> bytes:
                assert len(plaintext)%8 == 0
                blocks = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
                return b"".join([self._process_block(block, self.round_keys) for block in blocks])

            def decrypt(self, ciphertext: bytes) -> bytes:
                assert len(ciphertext)%8 == 0
                blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
                return b"".join([self._process_block(block, self.reversed_round_keys) for block in blocks])

            def _process_block(self, block: bytes, schedule) -> bytes:
                bits = HELP.BLOCK_TO_BITS(block)

                bits = HELP.PERMUTATE(bits, DES_CONST.INITIAL_PERMUTATION)
                left, right = bits[:32], bits[32:]

                for i in range(self.rounds):
                    new_right = self._function(right, schedule[i])
                    left, right = right, HELP.XOR(new_right, left)

                result_bits = right + left
                result_bits = HELP.PERMUTATE(result_bits, DES_CONST.FINAL_PERMUTATION)

                return HELP.BITS_TO_BLOCK(result_bits, 8)

            def _function(self, bits: List[int], key_bits: List[int]) -> List[int]:
                bits = HELP.EXPAND(bits, DES_CONST.EXPANSION)
                bits = HELP.XOR(bits, key_bits)
                bits = HELP.SUBSTITUTE(bits, DES_CONST.SBOX)
                bits = HELP.PERMUTATE(bits, DES_CONST.ROUND_PERMUTATION)

                return bits

^^^^^^^^^^^^^^^^^^
Thực hiện solve.py
^^^^^^^^^^^^^^^^^^

Phần này mình sẽ viết ``solve.py`` để giải bài này từ jupyter notebook của bạn Chương.

Đầu tiên chúng ta gọi một số thư viện.

.. code-block:: python

    from faulty_des import DES_CONST, HELP, FAULTY_DES
    from collections import defaultdict
    from typing import List, Tuple
    from itertools import product
    from tqdm import tqdm

Tiếp theo, chúng ta cần thống nhất rằng mỗi khối trong thuật toán ``FAULTY_DES`` sẽ được biểu diễn bởi mảng gồm :math:`8` phần tử (``list[int]``). Khi đó nửa trái (left-half) là :math:`4` phần tử đầu của mảng và nửa phải (right-half) là :math:`4` phần tử sau. Do đó chúng ta cần một số lambda để lấy nửa trái/phải. Sau bước cuối chúng ta ghép nửa phải cuối cùng với nửa trái cuối cùng nên cần thêm hàm ``Swap_f``.

.. code-block:: python

    Left_f  = lambda block: block[:4]
    Right_f = lambda block: block[4:]
    Swap_f  = lambda block: Right_f(block) + Left_f(block)

Sau đó đọc bản rõ và bản mã từ file đề cho rồi tách chúng thành các khối :math:`8` bytes.

.. code-block:: python

    # Known-Plaintext-Ciphertext Pairs
    plaintext  = open("Book.txt", "rb").read()[:-1]     # độ dài bản rõ chia hết cho 8
    ciphertext = open("Book_cipher.txt", "rb").read()

    # Divide them into blocks
    pts        = [plaintext[i:i+8] for i in range(0, len(plaintext), 8)]
    cts        = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]

Tiếp theo chúng ta tìm các slid pair. Ở đây chúng ta cần xem lại cách hoạt động của thuật toán DES. Hình sau mình lấy từ :cite:`TikZ:for:Cryptographers` và chỉnh sửa lại.

.. figure:: ../../figures/des-round/des-round.*
    
    Round function của DES

Tóm tắt cách hoạt động thì DES cũng theo mô hình

.. math:: L_{i+1} = R_i, \quad R_{i+1} = L_i \oplus \mathsf{PBox}(\mathsf{SBox}(\mathsf{Expand}(R_i) \oplus K_{i+1})),

trong đó

- :math:`\mathsf{Expand}` mở rộng nửa khối từ :math:`32` bits lên :math:`48` bits;
- :math:`\mathsf{SBox}`: :math:`48` bits sẽ được chia thành :math:`8` đoạn, mỗi đoạn có :math:`6` bits. Sau đó mỗi đoạn sẽ đi qua các S-Box và giảm từ :math:`6` bits xuống :math:`4` bits. Các kết quả được nối lại với nhau nên kết quả sau :math:`\mathsf{SBox}` là :math:`4 \cdot 8 = 32` bits;
- :math:`\mathsf{PBox}`: thực hiện hoán vị :math:`32` bit sau :math:`\mathsf{SBox}`.

Ở đây slid pair cũng tương tự TinyDES ở trên. Giả sử slid pair là cặp :math:`(P, C)` và :math:`(P', C')`. Khi đó

.. math:: F_K(P) = P', \quad F_K(C) = C'

với :math:`F_K` là round function

.. math:: (L_i, R_i) \xrightarrow{F_K} (L_{i+1}, R_{i+1}) \equiv (R_i, L_i \oplus \mathsf{PBox}(\mathsf{SBox}(\mathsf{Expand}(R_i) \oplus K_{i+1}))),

như trên.

.. code-block:: python

    # Before and After DES' rounds operations, there is a Block Permutation step!
    def BlockPermutate(block: bytes, table: list):
        assert len(block) == 8
        block_bits = HELP.BLOCK_TO_BITS(block)
        block_bits = HELP.PERMUTATE(block_bits, table)
        block      = HELP.BITS_TO_BLOCK(block_bits, 8)

        return block
        
    # Create Lookup Table
    lookup = defaultdict(list)

    for pi, ci in tqdm(zip(pts, cts), desc="[+] Creating Lookup Table..."):
        pi_initial = BlockPermutate(pi, DES_CONST.INITIAL_PERMUTATION)
        ci_preout  = BlockPermutate(ci, DES_CONST.INITIAL_PERMUTATION)
        # Why Left_f(Ci) -> Remember that the final round doesn't swap two-halfs
        lookup[Right_f(pi_initial) + Left_f(ci_preout)].append((pi_initial, ci_preout))

    # Finding "slid pairs"
    slid_pairs = []

    for pj, cj in tqdm(zip(pts, cts), desc="[+] Finding slid pairs..."):
        pj_initial = BlockPermutate(pj, DES_CONST.INITIAL_PERMUTATION)
        cj_preout  = BlockPermutate(cj, DES_CONST.INITIAL_PERMUTATION)

        try:
            # Why Right_f(Cj) -> Remember that the final round doesn't swap two-halfs
            for pi_initial, ci_preout in lookup[Left_f(pj_initial) + Right_f(cj_preout)]:
                slid_pairs.append([
                    # Now we swap to ensure that (P,C) and (P',C') is slid pair
                    # <=> F(P) = P' and F(C) = C'
                    (pi_initial, Swap_f(ci_preout)),
                    (pj_initial, Swap_f(cj_preout)),
                ])
        except:
            continue

    print(f"[!] Found {len(slid_pairs)} possible slid pairs!")

Các phép biến đổi ngược của các phép biến đổi trong DES nhằm tìm các "ứng cử viên" cho khóa. Quan trọng là S-Box vì chúng ta đã biết mỗi S-Box biến đổi :math:`6` bits thành :math:`4` bits nên với nhiều đầu vào cho cùng đầu ra. Khi đi ngược lại để tìm "ứng cử viên" thì ta phải xét tất cả trường hợp đầu vào S-Box cho cùng đầu ra mà ta đang có.

.. code-block:: python

    # Enumerate all possible candidates
    def RevSubtitute(out: List[int], mapping: List[Tuple]):
        cands = [[] for _ in range(8)]
        out   = [out[i:i+4] for i in range(0, len(out), 4)]

        for idx in range(8):
            for piece in range(2**6):
                row = (piece & 1) | ((piece >> 4) & 0b10)
                column = (piece & 0b011110) >> 1
                if HELP.INT_TO_BITS(mapping[idx][row * 16 + column], 4) == out[idx]:
                    cands[idx].append(HELP.INT_TO_BITS(piece, 6))

        for rk in product(*cands):
            yield sum(rk, [])

    def RevFeistel(inp, out):
        out = HELP.PERMUTATE(out, DES_CONST.INV_ROUND_PERMUTATION)
        inp = HELP.EXPAND(inp, DES_CONST.EXPANSION)
        for rev_out in RevSubtitute(out, DES_CONST.SBOX):
            yield HELP.BITS_TO_BLOCK(HELP.XOR(rev_out, inp), 6)

    def RevRound(state0: bytes, state1: bytes):
        L0, R0 = Left_f(state0), Right_f(state0)
        L1, R1 = Left_f(state1), Right_f(state1)
        return set(RevFeistel(
            inp=HELP.BLOCK_TO_BITS(R0),
            out=HELP.XOR(HELP.BLOCK_TO_BITS(R1), HELP.BLOCK_TO_BITS(L0))
        ))

Tìm các khóa con có thể và thử giải mã thông điệp đề cho với khóa con đó.

.. code-block:: python

    rk_cands = set()

    for (pi, ci), (pj, cj) in tqdm(slid_pairs, desc="[+] Recovering Possible RoundKey..."):
        rks_1    = RevRound(pi, pj)
        rks_2    = RevRound(ci, cj)
        rk_cands = rk_cands.union(rks_1.intersection(rks_2))

    print(f"[!] Found {len(rk_cands)} possible RoundKeys!")

    # Try to decrypt intercepted ciphertext
    intercepted_ciphertext = b"".join([
        bytes.fromhex("86991641D28259604412D6BA88A5C0A6471CA722"),
        bytes.fromhex("2C52482BF2D0E841D4343DFB877DC8E0147F3D5F"),
        bytes.fromhex("20FC18FF28CB5C4DA8A0F4694861AB5E98F37ADB"),
        bytes.fromhex("C2D69B35779D9001BB4B648518FE6EBC00B2AB10")
    ])

    for rk in tqdm(rk_cands, desc="[+] Try to decrypt intercepted ciphertext..."):
        cipher = FAULTY_DES(rk)
        try:
            print("> Readable Message:", cipher.decrypt(intercepted_ciphertext).decode())
            print("> WRT RoundKey:", rk.hex(), end="\n\n")
        except:
            continue

    # Verify again?
    assert FAULTY_DES(bytes.fromhex("0c74fa6a642a")).encrypt(plaintext) == ciphertext
