==============================
Phá mã tuyến tính trên TinyDES
==============================

-------------
Mô tả TinyDES
-------------

Trong phần mô tả phá mã vi sai mình đã sử dụng TinyDES để làm ví dụ. Ở đây mình tiếp tục sử dụng TinyDES để ví dụ cho phá mã tuyến tính. Nhằm gợi nhớ cấu trúc của TinyDES thì mình xin chép lại.

TinyDES là một phiên bản thu nhỏ của chuẩn mã hóa DES. TinyDES là mã hóa khối theo mô hình Feistel, kích thước khối là :math:`8` bit, kích thước khóa cũng là :math:`8` bit. Mỗi vòng khóa con có độ dài :math:`6` bit.

.. figure:: ../../figures/tinydes/tinydes.*

    Một vòng TinyDES

Mã TinyDES khá đơn giản. Theo mô hình Feistel, khối đầu vào :math:`8` bit được chia thành hai nửa trái phải :math:`4` bit. Nửa phải sẽ đi qua các hàm Expand, :math:`\mathsf{SBox}` và PBox, sau đó XOR với nửa trái để được nửa phải mới. Còn nửa trái mới là nửa phải cũ. Tóm lại 
công thức mô hình Feistel là: 

.. math:: 
    
    L_{i+1} = R_i, \quad R_{i+1} = L_i \oplus F(R_i, K_{i+1})

với :math:`i = 1, 2, 3` tương ứng :math:`3` vòng với đầu vào của khối là :math:`(L_0, R_0)`.

Chúng ta cần các động tác sau:

1. Expand: mở rộng và hoán vị :math:`R_i` từ :math:`4` bits lên :math:`6` bits. Giả sử :math:`4` bits của :math:`R_i` là :math:`b_0 b_1 b_2 b_3` thì kết quả sau khi Expand là :math:`b_2 b_3 b_1 b_2 b_1 b_0`.
2. SBox: gọi :math:`6` bits đầu vào là :math:`b_0 b_1 b_2 b_3 b_4 b_5`. Khi đó ta tra cứu theo bảng SBox với :math:`b_0 b_5` chỉ số **hàng**, :math:`b_1 b_2 b_3 b_4` chỉ số **cột**. Nói cách khác bảng SBox có :math:`4` hàng, :math:`16` cột. Kết quả của SBox là một số :math:`4` bit.
3. PBox: là hàm hoán vị :math:`4` bits :math:`b_0 b_1 b_2 b_3` thành :math:`b_2 b_0 b_3 b_1`.

Như vậy, hàm :math:`F` của mô hình Feistel đối với mã TinyDES là:

.. math:: 
    
    F(R_i, K_i) = \mathsf{PBox}(\mathsf{SBox}(\mathsf{Expand}(R_i) \oplus K_{i+1})).

Để sinh khóa con cho :math:`3` vòng, khóa ban đầu được chia thành hai nửa trái phải lần lượt là :math:`KL_0` và :math:`KR_0`. TinyDES thực hiện như sau:

1. Vòng 1: :math:`KL_0` và :math:`KR_0` được dịch vòng trái :math:`1` bit để được :math:`KL_1` và :math:`KR_1`;
2. Vòng 2: :math:`KL_1` và :math:`KR_1` được dịch vòng trái :math:`2` bit để được :math:`KL_2` và :math:`KR_2`;
3. Vòng 3: :math:`KL_2` và :math:`KR_2` được dịch vòng trái :math:`1` bit để được :math:`KL_3` và :math:`KR_3`.

Khi đó, khóa :math:`K_i` ở vòng thứ :math:`i` (với :math:`i = 1, 2, 3`) là hoán vị và nén :math:`8` bits của :math:`KL_i` và :math:`KR_i` lại thành :math:`6` bits.

Đặt :math:`8` bits khi ghép :math:`KL_i \Vert KR_i` là :math:`k_0 k_1 k_2 k_3 k_4 k_5 k_6 k_7`, kết quả là :math:`6` bits :math:`k_5 k_1 k_3 k_2 k_7 k_0`.

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
            for i in range(3):
                left, right = right, Xor(left, PBox(SBox(Xor(Expand(right), keys[i+1]))))
            
            return left + right

        #print(encrypt_block([0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 0]))


------------------------------
Phá mã tuyến tính trên TinyDES
------------------------------

Trong các phép biến đổi trên TinyDES thì chỉ có :math:`\mathsf{SBox}` là không tuyến tính. Tuy nhiên nếu chỉ xét một số bit nhất định giữa đầu vào và đầu ra thì ta có quan hệ tuyến tính.

Nhắc lại, một biến đổi :math:`f: \mathbb{F}_2^n \to \mathbb{F}_2^m` gọi là tuyến tính nếu với mọi :math:`\bm{x}_1, \bm{x}_2 \in \mathbb{F}_2^n` ta đều có

.. math:: 
    
    f(\bm{x}_1 \oplus \bm{x}_2) = f(\bm{x}_1) \oplus f(\bm{x}_2).

Ta sẽ xét các phép biến đổi trong TinyDES.

^^^^^^^^^^^^^
Phép XOR key
^^^^^^^^^^^^^

Gọi :math:`K` là khóa con ở vòng nào đó trong thuật toán. Khi đó nếu đặt :math:`Y_1 = X_1 \oplus K` và :math:`Y_2 = X_2 \oplus K` thì ta có :math:`Y_1 \oplus Y_2 = X_1 \oplus X_2`. Như vậy phép XOR là biến đổi tuyến tính.

^^^^^^^^^
Phép PBox
^^^^^^^^^

Phép PBox bảo toàn số bit (hoán vị :math:`4` bits thành :math:`4` bits) và cách xây dựng hoán vị là một biến đổi tuyến tính. Việc hoán vị :math:`4` bits :math:`b_0 b_1 b_2 b_3` thành :math:`b_2 b_0 b_3 b_1` tương đương với phép nhân ma trận

.. math:: 

    \begin{pmatrix}
        0 & 0 & 1 & 0 \\
        1 & 0 & 0 & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 1 & 0 & 0
    \end{pmatrix} \cdot
    \begin{pmatrix}
        b_0 \\ b_1 \\ b_2 \\ b_3
    \end{pmatrix} =
    \begin{pmatrix}
        b_2 \\ b_0 \\ b_3 \\ b_1
    \end{pmatrix}.


Do đó nếu đặt :math:`Y_1 = \mathsf{PBox}(X_1)` và :math:`Y_2 = \mathsf{PBox} (X_2)` thì

.. math:: 
    
    Y_1 \oplus Y_2 = \mathsf{PBox}(X_1) \oplus \mathsf{PBox}(X_2) = \mathsf{PBox} (X_1 \oplus X_2).

^^^^^^^^^^^
Phép Expand
^^^^^^^^^^^

Tương tự, phép Expand cũng là biến đổi tuyến tính và nếu đặt :math:`Y_1 = \mathsf{Expand}(X_1)` và :math:`Y_2 = \mathsf{Expand}(X_2)` thì

.. math:: 
    
    Y_1 \oplus Y_2 = \mathsf{Expand}(X_1) \oplus \mathsf{Expand}(X_2) = \mathsf{Expand}(X_1 \oplus X_2).

^^^^^^^^^
Phép SBox
^^^^^^^^^

Phép SBox là một biến đổi không tuyến tính với input :math:`6` bits và output :math:`4` bits.

Đặt :math:`\bm{y} = \mathsf{SBox}(\bm{x})` với :math:`\bm{x} = (x_0, x_1, x_2, x_3, x_4, x_5) \in \mathbb{F}_2^6` và :math:`\bm{y} = (y_0, y_1, y_2, y_3) \in \mathbb{F}_2^4`.

Gọi :math:`\bm{a} = (a_0, a_1, a_2, a_3, a_4, a_5) \in \mathbb{F}_2^6` với biểu diễn thập phân là các số từ :math:`1` tới :math:`63`, nghĩa là trừ vector không.

Tương tự, gọi :math:`\bm{b} = (b_0, b_1, b_2, b_3) \in \mathbb{F}_2^4` với biểu diễn thập phân là các số từ :math:`1` tới :math:`15`, ta cũng không xét vector không.

Tích vô hướng là một biểu diễn tuyến tính giữa :math:`\bm{a}` và :math:`\bm{x}`:

.. math:: 
    
    \langle \bm{a}, \bm{x} \rangle = a_0 x_0 \oplus a_1 x_1 \oplus a_2 x_2 \oplus a_3 x_3 \oplus a_4 x_4 \oplus a_5 x_5 \oplus a_6 x_6.

Tương tự, quan hệ tuyến tính giữa :math:`\bm{b}` và :math:`\bm{y}` là

.. math:: 
    
    \langle \bm{b}, \bm{y} \rangle = b_0 y_0 \oplus b_1 y_1 \oplus b_2 y_2 \oplus b_3 y_3.

Lúc này ta sẽ quan tâm xem với các vector :math:`\bm{a}` và :math:`\bm{b}` nào sẽ khiến nhiều bit của :math:`\bm{y}` phụ thuộc tuyến tính vào các bit của :math:`\bm{x}`, cụ thể là khi :math:`\langle \bm{x}, \bm{a} \rangle = \langle \bm{y}, \bm{b} \rangle`.

Với hai vector :math:`\bm{a} \in \mathbb{F}_2^6` và :math:`\bm{b} \in \mathbb{F}_2^4`, gọi :math:`S(\bm{a}, \bm{b})` là số lượng cặp vector :math:`(\bm{x}, \bm{y})` sao cho

.. math:: 
    
    \langle \bm{x}, \bm{a} \rangle = \langle \bm{y}, \bm{b} \rangle.

Bảng dưới liệt kê các giá trị :math:`S(\bm{a}, \bm{b}) - 32` với hàng đầu là các vector :math:`\bm{b}` từ :math:`1` tới :math:`15`, và cột đầu là các vector :math:`\bm{a}` từ :math:`1` tới :math:`32`.

+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
|            | :math:`1`  | :math:`2`  | :math:`3`  | :math:`4`  | :math:`5`  | :math:`6`  | :math:`7`   | :math:`8`   | :math:`9`  | :math:`10` | :math:`11` | :math:`12` | :math:`13` | :math:`14` | :math:`15`  |
+============+============+============+============+============+============+============+=============+=============+============+============+============+============+============+============+=============+
| :math:`1`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`   | :math:`0`   | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`2`  | :math:`0`  | :math:`-2` | :math:`6`  | :math:`2`  | :math:`2`  | :math:`4`  | :math:`-4`  | :math:`2`   | :math:`6`  | :math:`0`  | :math:`-4` | :math:`0`  | :math:`-4` | :math:`-6` | :math:`-18` |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`3`  | :math:`0`  | :math:`-2` | :math:`6`  | :math:`-2` | :math:`6`  | :math:`0`  | :math:`0`   | :math:`-2`  | :math:`2`  | :math:`4`  | :math:`0`  | :math:`0`  | :math:`4`  | :math:`2`  | :math:`-2`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`4`  | :math:`-4` | :math:`-6` | :math:`2`  | :math:`-2` | :math:`2`  | :math:`0`  | :math:`0`   | :math:`4`   | :math:`-4` | :math:`-6` | :math:`-2` | :math:`6`  | :math:`-2` | :math:`-4` | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`5`  | :math:`4`  | :math:`-2` | :math:`-2` | :math:`-2` | :math:`2`  | :math:`-4` | :math:`12`  | :math:`4`   | :math:`4`  | :math:`-2` | :math:`-6` | :math:`-2` | :math:`6`  | :math:`0`  | :math:`4`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`6`  | :math:`4`  | :math:`0`  | :math:`0`  | :math:`8`  | :math:`4`  | :math:`4`  | :math:`-4`  | :math:`2`   | :math:`-2` | :math:`6`  | :math:`-2` | :math:`2`  | :math:`6`  | :math:`2`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`7`  | :math:`4`  | :math:`-4` | :math:`-4` | :math:`4`  | :math:`0`  | :math:`4`  | :math:`-4`  | :math:`-10` | :math:`2`  | :math:`-2` | :math:`6`  | :math:`2`  | :math:`6`  | :math:`-2` | :math:`-2`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`8`  | :math:`-2` | :math:`-2` | :math:`0`  | :math:`-2` | :math:`8`  | :math:`-4` | :math:`-6`  | :math:`2`   | :math:`4`  | :math:`0`  | :math:`-2` | :math:`-4` | :math:`2`  | :math:`-6` | :math:`12`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`9`  | :math:`2`  | :math:`2`  | :math:`0`  | :math:`-6` | :math:`0`  | :math:`4`  | :math:`-10` | :math:`2`   | :math:`0`  | :math:`4`  | :math:`6`  | :math:`-8` | :math:`2`  | :math:`2`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`10` | :math:`2`  | :math:`-8` | :math:`6`  | :math:`0`  | :math:`-2` | :math:`4`  | :math:`-2`  | :math:`4`   | :math:`6`  | :math:`-4` | :math:`2`  | :math:`4`  | :math:`2`  | :math:`0`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`11` | :math:`-2` | :math:`4`  | :math:`6`  | :math:`-8` | :math:`2`  | :math:`0`  | :math:`-2`  | :math:`8`   | :math:`-2` | :math:`4`  | :math:`6`  | :math:`8`  | :math:`-6` | :math:`0`  | :math:`-2`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`12` | :math:`2`  | :math:`0`  | :math:`2`  | :math:`0`  | :math:`6`  | :math:`0`  | :math:`6`   | :math:`-2`  | :math:`0`  | :math:`2`  | :math:`-4` | :math:`6`  | :math:`-4` | :math:`2`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`13` | :math:`-2` | :math:`8`  | :math:`-2` | :math:`-4` | :math:`-2` | :math:`4`  | :math:`-2`  | :math:`6`   | :math:`-4` | :math:`2`  | :math:`-8` | :math:`2`  | :math:`12` | :math:`6`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`14` | :math:`-2` | :math:`2`  | :math:`0`  | :math:`2`  | :math:`4`  | :math:`0`  | :math:`2`   | :math:`-4`  | :math:`-2` | :math:`-6` | :math:`4`  | :math:`2`  | :math:`0`  | :math:`-4` | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`15` | :math:`-6` | :math:`-6` | :math:`-4` | :math:`10` | :math:`0`  | :math:`0`  | :math:`-2`  | :math:`0`   | :math:`6`  | :math:`-2` | :math:`4`  | :math:`-2` | :math:`-8` | :math:`8`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`16` | :math:`2`  | :math:`-2` | :math:`4`  | :math:`-2` | :math:`0`  | :math:`-4` | :math:`-6`  | :math:`-2`  | :math:`0`  | :math:`0`  | :math:`-2` | :math:`-4` | :math:`6`  | :math:`6`  | :math:`4`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`17` | :math:`-2` | :math:`2`  | :math:`4`  | :math:`-2` | :math:`-4` | :math:`0`  | :math:`10`  | :math:`2`   | :math:`0`  | :math:`0`  | :math:`10` | :math:`0`  | :math:`6`  | :math:`6`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`18` | :math:`-6` | :math:`-4` | :math:`2`  | :math:`0`  | :math:`2`  | :math:`0`  | :math:`6`   | :math:`4`   | :math:`2`  | :math:`4`  | :math:`6`  | :math:`0`  | :math:`6`  | :math:`4`  | :math:`-10` |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`19` | :math:`-2` | :math:`0`  | :math:`-6` | :math:`-4` | :math:`-6` | :math:`0`  | :math:`2`   | :math:`-4`  | :math:`-2` | :math:`0`  | :math:`6`  | :math:`-4` | :math:`-2` | :math:`4`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`20` | :math:`-2` | :math:`0`  | :math:`-2` | :math:`0`  | :math:`-2` | :math:`8`  | :math:`-2`  | :math:`-2`  | :math:`0`  | :math:`6`  | :math:`0`  | :math:`2`  | :math:`4`  | :math:`2`  | :math:`4`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`21` | :math:`2`  | :math:`0`  | :math:`2`  | :math:`0`  | :math:`-6` | :math:`0`  | :math:`2`   | :math:`2`   | :math:`-8` | :math:`2`  | :math:`0`  | :math:`-2` | :math:`-4` | :math:`-2` | :math:`-4`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`22` | :math:`-2` | :math:`-2` | :math:`-4` | :math:`-6` | :math:`0`  | :math:`4`  | :math:`2`   | :math:`0`   | :math:`-2` | :math:`-2` | :math:`4`  | :math:`2`  | :math:`0`  | :math:`4`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`23` | :math:`2`  | :math:`6`  | :math:`8`  | :math:`6`  | :math:`0`  | :math:`0`  | :math:`2`   | :math:`0`   | :math:`2`  | :math:`6`  | :math:`0`  | :math:`-2` | :math:`0`  | :math:`0`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`24` | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`4`  | :math:`0`  | :math:`-4`  | :math:`0`   | :math:`-4` | :math:`4`  | :math:`0`  | :math:`4`  | :math:`4`  | :math:`0`  | :math:`-8`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`25` | :math:`0`  | :math:`8`  | :math:`0`  | :math:`4`  | :math:`0`  | :math:`4`  | :math:`0`   | :math:`4`   | :math:`-8` | :math:`-8` | :math:`4`  | :math:`-4` | :math:`-4` | :math:`0`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`26` | :math:`4`  | :math:`2`  | :math:`-2` | :math:`2`  | :math:`2`  | :math:`0`  | :math:`0`   | :math:`6`   | :math:`2`  | :math:`-4` | :math:`0`  | :math:`0`  | :math:`0`  | :math:`2`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`27` | :math:`4`  | :math:`2`  | :math:`6`  | :math:`2`  | :math:`2`  | :math:`8`  | :math:`0`   | :math:`6`   | :math:`-6` | :math:`-4` | :math:`0`  | :math:`-8` | :math:`0`  | :math:`2`  | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`28` | :math:`4`  | :math:`2`  | :math:`2`  | :math:`-2` | :math:`6`  | :math:`0`  | :math:`-4`  | :math:`0`   | :math:`4`  | :math:`2`  | :math:`2`  | :math:`-2` | :math:`-2` | :math:`0`  | :math:`4`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`29` | :math:`-4` | :math:`6`  | :math:`6`  | :math:`2`  | :math:`2`  | :math:`-8` | :math:`4`   | :math:`-4`  | :math:`0`  | :math:`-6` | :math:`2`  | :math:`6`  | :math:`6`  | :math:`4`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`30` | :math:`0`  | :math:`4`  | :math:`0`  | :math:`0`  | :math:`-4` | :math:`0`  | :math:`0`   | :math:`2`   | :math:`6`  | :math:`-2` | :math:`-2` | :math:`-2` | :math:`-2` | :math:`-2` | :math:`2`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`31` | :math:`0`  | :math:`-8` | :math:`-4` | :math:`0`  | :math:`4`  | :math:`4`  | :math:`4`   | :math:`2`   | :math:`-2` | :math:`2`  | :math:`2`  | :math:`-2` | :math:`-2` | :math:`2`  | :math:`-2`  |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+
| :math:`32` | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`   | :math:`0`   | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`  | :math:`0`   |
+------------+------------+------------+------------+------------+------------+------------+-------------+-------------+------------+------------+------------+------------+------------+------------+-------------+

.. admonition:: check_sbox.py
    :class: dropdown

    .. code-block:: python

        # check_sbox.py

        from tinydes import SBox


        S = [[0 for _ in range(15)] for __ in range(63)]

        for a in range(1, 64):
            va = list(map(int, f"{a:06b}"))[::-1]
            for b in range(1, 16):
                vb = list(map(int, f"{b:04b}"))[::-1]
                for x in range(64):
                    vx = list(map(int, f"{x:06b}"))[::-1]
                    vy = SBox(vx)
                    u = sum(i * j for i, j in zip(va, vx)) % 2
                    v = sum(i * j for i, j in zip(vb, vy)) % 2
                    if u == v:
                        S[a - 1][b - 1] += 1

        print(S)

Sau khi xem bảng phân phối :math:`S(\bm{a}, \bm{b})` thì chúng ta quan tâm một số giá trị.

Xét :math:`S(16, 15) = 14`, tương ứng với vector :math:`\bm{a} = (0, 1, 0, 0, 0, 0)` và :math:`\bm{b} = (1, 1, 1, 1)`, thì

.. math:: 
    
    x_1 = y_0 \oplus y_1 \oplus y_2 \oplus y_3

với xác suất :math:`14 / 64`.

Ngược lại ta cũng có

.. math:: 
    
    x_1 \neq y_0 \oplus y_1 \oplus y_2 \oplus y_3

với xác suất :math:`1 - 14 / 64`.

Ta kí hiệu mối quan hệ này là

.. math:: 
    
    \bm{y}[0, 1, 2, 3] = \bm{x}[1].

^^^^^^^^^^^^^
Hàm :math:`F`
^^^^^^^^^^^^^

Xét :math:`\bm{y} = F(\bm{x}, \bm{k})` là round function của TinyDES, trong đó

- :math:`\bm{x} = (x_0, x_1, x_2, x_3) \in \mathbb{F}_2^4` là đầu vào cho round function (nửa phải);
- :math:`\bm{k} = (k_0, k_1, k_2, k_3, k_4, k_5, k_6) \in \mathbb{F}_2^6` là khóa con ở vòng nào đó;
- :math:`\bm{y} = (y_0, y_1, y_2, y_3) \in \mathbb{F}_2^4` là đầu ra của round function.

Ta có các động tác biến đổi sau.

Hàm Expand:

.. math:: 
    
    (x_0, x_1, x_2, x_3) \xrightarrow{\mathsf{Expand}} (x_2, x_3, x_1, x_2, x_1, x_0).

Hàm XOR key:

.. math:: 
    
    (x_2, x_3, x_1, x_2, x_1, x_0) \oplus (k_0, k_1, k_2, k_3, k_4, k_5) \rightarrow (x_0', x_1', x_2', x_3', x_4', x_5').

Hàm SBox:

.. math:: 
    
    \bm{x}' = (x_0', x_1', x_2', x_3', x_4', x_5') \xrightarrow{\mathsf{SBox}} \bm{y}' = (y_0', y_1', y_2', y_3').

Hàm PBox:

.. math:: 
    
    (y_0', y_1', y_2', y_3') \xrightarrow{\mathsf{PBox}} (y_2', y_0', y_3', y_1') \equiv (y_0, y_1, y_2, y_3).

Theo phân tích tuyến tính ở trên ta tập trung vào phần :math:`\mathsf{SBox}`, như vậy

.. math:: 
    
    \bm{y}'[0, 1, 2, 3] = \bm{x}'[1].

Từ PBox suy ra :math:`y_0 = y_2'`, :math:`y_1 = y_0'`, :math:`y_2 = y_3'` và :math:`y_3 = y_1'`, nên suy ra

.. math:: 
    
    \bm{y}'[0, 1, 2, 3] = \bm{y}[0, 1, 2, 3].

Điều này có vẻ khá rõ ràng vì tuyến tính :math:`y_0 \oplus y_1 \oplus y_2 \oplus y_3` có mặt ở mọi bit nên :math:`\bm{y}'` hay :math:`\bm{y}` đều như nhau. Tuy nhiên nếu trong các trường hợp tuyến tính không có đủ tất cả bit là :math:`1` như :math:`\bm{b} \neq 15` thì chúng ta cần chú ý sự biến đổi của PBox.

Tiếp theo, do :math:`\bm{x}'[1] = x_1' = x_3 \oplus k_1` nên có thể suy ra quan hệ tuyến tính giữa đầu vào :math:`\bm{x}` và :math:`\bm{y}` là

.. math:: 
    
    \bm{y}[0, 1, 2, 3] = \bm{x}[3] \oplus \bm{k}[1].

---------------
Known-plaintext
---------------

Linear attack là một dạng known-plaintext, trong đó chúng ta tận dụng các xác suất ở trên.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Phụ thuộc tuyến tính giữa các vòng
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gọi :math:`P = (L_0, R_0)` là plaintext ban đầu với :math:`L_0` và :math:`R_0` là hai nửa trái phải.

Ở vòng 1 ta có

.. math:: 
    
    L_1 = R_0, \ R_1 = L_0 \oplus F(R_0, K_1),

suy ra

.. math:: 
    :label: r1-1

    F(R_0, K_1) = R_1[0, 1, 2, 3] \oplus L_0[0, 1, 2, 3] = R_0[3] \oplus K_1[1]

với xác suất :math:`14 / 64`. Ngược lại ta có

.. math:: 
    :label: r1-2

    F(R_0, K_1) = R_1[0, 1, 2, 3] \oplus L_0[0, 1, 2, 3] = R_0[3] \oplus K_1[1] \oplus 1

với xác suất :math:`1 - 14 / 64`.

Ở vòng 2 ta có

.. math:: 
    
    L_2 = R_1, \ R_2 = L_1 \oplus F(R_1, K_2).

Ở vòng 3 ta có

.. math:: 
    
    L_3 = R_2, \ R_3 = L_2 \oplus F(R_2, K_3),

suy ra

.. math:: 
    :label: r3-1

    F(R_2, K_3) = R_3[0, 1, 2, 3] \oplus L_2[0, 1, 2, 3] = R_2[3] \oplus K_3[1]

với xác suất :math:`14 / 64`. Tương tự ta cũng có

.. math:: 
    :label: r3-2

    F(R_2, K_3) = R_3[0, 1, 2, 3] \oplus L_2[0, 1, 2, 3] = R_2[3] \oplus K_3[1] \oplus 1

với xác suất :math:`1 - 14 / 64`.

Ta lại có :math:`L_2 = R_1`, kết hợp thêm vòng 1 ta có phương trình

.. math:: 
    
    
        F(R_2, K_3) & = R_3[0, 1, 2, 3] \oplus R_1[0, 1, 2, 3] \\
        & = R_3[0, 1, 2, 3] \oplus L_0[0, 1, 2, 3] \oplus R_0[3] \oplus K_1[1] \\
        & = R_2[3] \oplus K_3[1] = L_3[3] \oplus K_3[1],
    

tương đương với

.. math:: K_1[1] \oplus K_3[1] = R_3[0, 1, 2, 3] \oplus L_0[0, 1, 2, 3,] \oplus R_0[3] \oplus L_3[3].

Phương trình xảy ra:

- với xác suất :math:`(14 / 64)^2` khi là xảy ra hai phương trình :eq:`r1-1` và :eq:`r3-1`;
- với xác suất :math:`(1 - 14 / 64)^2` khi xảy ra hai phương trình :eq:`r1-2` và :eq:`r3-2`.

Như vậy tổng xác suất là :math:`(14 / 64)^2 + (1 - 14 / 64)^2` xấp xỉ :math:`0,66`, khoảng :math:`2/3`.

^^^^^^^^^^^^^^^^^^
Tính toán khóa con
^^^^^^^^^^^^^^^^^^

Giả sử khóa ban đầu gồm :math:`8` bit là

.. math:: KL_0 = (k^{(0)}_0, k^{(0)}_1, k^{(0)}_2, k^{(0)}_3), \ KR_0 = (k^{(0)}_4, k^{(0)}_5, k^{(0)}_6, k^{(0)}_7).

Dịch vòng trái :math:`1` bit :math:`KL_0` và :math:`KR_0` ta được :math:`KL_1` và :math:`KR_1` lần lượt là

.. math:: 
    
    
    KL_0 = (k^{(0)}_0, k^{(0)}_1, k^{(0)}_2, k^{(0)}_3) \xrightarrow{\ll 1} KL_1 = (k^{(0)}_1, k^{(0)}_2, k^{(0)}_3, k^{(0)}_0) = (k^{(1)}_0, k^{(1)}_1, k^{(1)}_2, k^{(1)}_3) \\ 
    KR_0 = (k^{(0)}_4, k^{(0)}_5, k^{(0)}_6, k^{(0)}_7) \xrightarrow{\ll 1} KR_1 = (k^{(0)}_5, k^{(0)}_6, k^{(0)}_7, k^{(0)}_4) = (k^{(1)}_4, k^{(1)}_5, k^{(1)}_6, k^{(1)}_7)
    

nên suy ra

.. math:: K_1 = (k^{(1)}_5, k^{(1)}_1, k^{(1)}_3, k^{(1)}_2, k^{(1)}_7, k^{(1)}_0).

Ở đây, :math:`K_1[1] = k^{(1)}_1 = k^{(0)}_2`.

Thực hiện tiếp quá trình này sẽ dẫn chúng ta tới :math:`K_3[1] = k^{(0)}_1`.

Như vậy chúng ta có một mối phụ thuộc giữa hai bit khóa ban đầu :math:`k^{(0)}_1` và :math:`k^{(0)}_2`.

Giả sử ta phá mã known-plaintext với :math:`100` cặp plaintext-ciphertext và có được kết quả sau của biểu thức

.. math:: R_3[0, 1, 2, 3] \oplus L_0[0, 1, 2, 3,] \oplus R_0[3] \oplus L_3[3]

bằng :math:`1` ở :math:`66` lần và bằng :math:`0` ở :math:`34` lần. Như vậy theo phân tích xác suất ở phần phụ thuộc tuyến tính ở trên có thể kết luận :math:`k^{(0)}_1 \oplus k^{(0)}_2 = 1`. Điều này cho chúng ta hai trường hợp về hai bit của khóa, và nếu ta vét cạn :math:`6` bits còn lại thì tổng cộng cần :math:`2 \cdot 2^6 = 128` trường hợp. Như vậy chúng ta không phải vét cạn :math:`8` bits, tốn :math:`2^8 = 256` trường hợp. Hiện tại chúng ta chỉ mới xét một liên hệ giữa :math:`k^{(0)}_1` và :math:`k^{(0)}_2` nên độ phức tạp chỉ giảm một nửa. Nếu xét thêm các liên hệ khác thì sẽ có thể giảm thêm.

.. admonition:: solve.py
    :class: dropdown
    
    .. code-block:: python

        # solve.py

        from tinydes import encrypt_block, SBox
        from functools import reduce
        import random

        random.seed(4)

        secret_key = [1, 1, 0, 1, 0, 0, 1, 0]
        count = 0
        plaintext = [random.randint(0, 1) for __ in range(8)]
        ciphertext = encrypt_block(plaintext, secret_key)

        for _ in range(100):
            pt = [random.randint(0, 1) for __ in range(8)]
            ct = encrypt_block(pt, secret_key)
            L0, R0 = pt[:4], pt[4:]
            L3, R3 = ct[:4], ct[4:]
            S = reduce(lambda x, y: x ^ y, R3) ^ reduce(lambda x, y: x ^ y, L0) ^ R0[3] ^ L3[3]
            if S == 1:
                count += 1

        if count > 100 - count:
            for k1 in range(2):
                k2 = k1 ^ 1
                for k0 in range(2):         # Bruteforce k_0
                    for k in range(2**5):   # Bruteforce k_3 to k_7
                        K = [k0, k1, k2] + list(map(int, f"{k:05b}"))
                        if encrypt_block(plaintext, K) == ciphertext:
                            print(f"Found key: {K}")
