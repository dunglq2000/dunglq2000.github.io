==========================
Phá mã vi sai trên TinyDES
==========================

-------------
Mô tả TinyDES
-------------

TinyDES là một phiên bản thu nhỏ của chuẩn mã hóa DES. TinyDES là mã hóa khối theo mô hình Feistel, kích thước khối là :math:`8` bit, kích thước khóa cũng là :math:`8` bit. Mỗi vòng khóa con có độ dài :math:`6` bit.

.. figure:: ../../figures/tinydes/tinydes.*

    Một vòng TinyDES

Mã TinyDES khá đơn giản. Theo mô hình Feistel, khối đầu vào :math:`8` bit được chia thành hai nửa trái phải :math:`4` bit. Nửa phải sẽ đi qua các hàm Expand, SBox và PBox, sau đó XOR với nửa trái để được nửa phải mới. Còn nửa trái mới là nửa phải cũ. Tóm lại 
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

--------------------------
Phá mã vi sai trên TinyDES
--------------------------

Giả sử :math:`X_1` và :math:`X_2` là hai khối input có cùng số bit.

Ta định nghĩa vi sai của :math:`X_1` và :math:`X_2` là :math:`X = X_1 \oplus X_2`.

Xét các phép biến đổi trong TinyDES

^^^^^^^^^^^^
Phép XOR key
^^^^^^^^^^^^

Gọi :math:`K` là khóa con ở vòng nào đó trong thuật toán. Khi đó nếu đặt :math:`Y_1 = X_1 \oplus K` và :math:`Y_2 = X_2 \oplus K` thì vi sai của output là :math:`Y = Y_1 \oplus Y_2 = X_1 \oplus X_2`. Như vậy :math:`K` không tác động lên vi sai và đây là tính chất quan trọng để chúng ta phá mã vi sai.

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
    \end{pmatrix}

Do đó nếu đặt :math:`Y_1 = \mathsf{PBox}(X_1)` và :math:`Y_2 = \mathsf{PBox} (X_2)` thì

.. math:: 
    
    Y_1 \oplus Y_2 = \mathsf{PBox}(X_1) \oplus \mathsf{PBox}(X_2) = \mathsf{PBox} (X_1 \oplus X_2).

Như vậy nếu vi sai input là cố định thì vi sai output cũng cố định do tính tuyến tính.

^^^^^^^^^^^
Phép Expand
^^^^^^^^^^^

Tương tự, phép Expand cũng là biến đổi tuyến tính và nếu đặt :math:`Y_1 = \mathsf{Expand}(X_1)` và :math:`Y_2 = \mathsf{Expand}(X_2)` thì

.. math:: 
    
    Y_1 \oplus Y_2 = \mathsf{Expand}(X_1) \oplus \mathsf{Expand}(X_2) = \mathsf{Expand}(X_1 \oplus X_2).

Cũng tương tự, nếu vi sai input là cố định thì vi sai output cũng cố định.

^^^^^^^^^
Phép SBox
^^^^^^^^^

Phép SBox là một biến đổi không tuyến tính với input :math:`6` bits và output :math:`4` bits.

Đặt :math:`Y_1 = \mathsf{SBox}(X_1)` và :math:`Y_2 = \mathsf{SBox}(X_2)`.

Với mỗi :math:`X = X_1 \oplus X_2` cố định thì cứ một giá trị :math:`X_1` sẽ có duy nhất một giá trị :math:`X_2` cho ra vi sai :math:`X`. Tuy nhiên vi sai output :math:`Y_1 \oplus Y_2` phân bố không đều nhau.

Thực hiện bruteforce đơn giản trên SBox với vi sai input :math:`X = X_1 \oplus X_2` có :math:`6` bits, ta tìm được sự phân bố vi sai output :math:`Y = Y_1 \oplus Y_2`.

Chúng ta mong muốn rằng trên một hàng có càng ít phần tử khác :math:`0` càng tốt.  Từ đó sự phân bố xác suất sẽ dễ kiểm soát hơn.

.. code-block:: python

    # check_sbox.py

    import tinydes


    def int_to_vec6(n: int) -> list[int]:
        return list(map(int, format(n, "06b")))


    def int_to_vec8(n: int) -> list[int]:
        return list(map(int, format(n, "08b")))


    def vec_to_int(v: list[int]) -> int:
        return int("".join(map(str, v)), 2)


    # Know about distribution of differential input-output
    dist = []
    for _ in range(2**6):
        X = int_to_vec6(_)
        row = [0] * 16
        for __ in range(2**6):
            X1 = int_to_vec6(__)
            X2 = tinydes.Xor(X, X1)
            Y1 = tinydes.SBox(X1)
            Y2 = tinydes.SBox(X2)
            Y = tinydes.Xor(Y1, Y2)
            row[vec_to_int(Y)] += 1
        dist.append(row)

    for i, row in enumerate(dist):
        print(f'Row = {row}')
        print(f'Row {i} has {row.count(0)} zero elements')
        print(f'Element that has maximal probability is {row.index(max(row))} with prob {max(row)}')
        print()

Sau khi xem bảng phân phối vi sai input và output ta có thể thấy được rằng:

1. Nếu vi sai input :math:`X = 0` thì chắc chắn vi sai output :math:`Y = 0`.
2. Nếu vi sai input :math:`X = 16` thì có :math:`9` vi sai output :math:`Y` khác :math:`0`.
3. Nếu vi sai input :math:`X = 52` thì có :math:`8` vi sai output :math:`Y` khác :math:`0`.

Dựa trên nhận xét này, chúng ta sẽ tấn công trên các :math:`X_1`, :math:`X_2` mà :math:`X = X_1 \oplus X_2 \in \{ 16, 52 \}`.

Xét hai hàng :math:`16` và :math:`52`, ta thấy rằng:

1. Nếu vi sai input :math:`X = 16` thì vi sai output :math:`Y = 7` là cao nhất với xác suất :math:`14/64`.
2. Nếu vi sai input :math:`X = 52` thì vi sai output :math:`Y = 2` là cao nhất với xác suất :math:`16/64`.

^^^^^^^^^^^^^
Hàm :math:`F`
^^^^^^^^^^^^^

Như vậy, phép XOR key, phép PBox và phép Expand cho xác suất đều nhau với các cặp vi sai :math:`(X, Y)`. Trong khi đó thì SBox lại cho xác suất các cặp vi sai :math:`(X, Y)` không đều nhau.

Đặt :math:`Y_1 = F(X_1)` và :math:`Y_2 = F(X_2)`.

Đi từ trong ra ngoài (:math:`\mathsf{Expand}`, tới :math:`\mathsf{SBox}`, tới :math:`\mathsf{PBox}` và cuối cùng là :math:`F`) ta thấy rằng:

- vi sai input của hàm :math:`F` chính là vi sai input của :math:`\mathsf{Expand}`;
- vi sai output của :math:`\mathsf{Expand}` là vi sai input của :math:`\mathsf{SBox}` (không phụ thuộc vào khóa);
- vi sai output của :math:`\mathsf{SBox}` là vi sai input của :math:`\mathsf{PBox}`;
- vi sai output của :math:`\mathsf{PBox}` là vi sai output của hàm :math:`F`.

Ta có thể đưa ra nhận xét về xác suất vi sai output :math:`Y = Y_1 \oplus Y_2` từ vi sai :math:`X = X_1 \oplus X_2` như sau:

1. Nếu vi sai input của :math:`F` là :math:`0` :math:`\Rightarrow` vi sai output của :math:`\mathsf{Expand}` là :math:`0` :math:`\Rightarrow` vi sai output của :math:`\mathsf{SBox}` chắc chắn là :math:`0` :math:`\Rightarrow` vi sai output của :math:`\mathsf{PBox}` chắc chắn là :math:`0` :math:`\Rightarrow` vi sai output của hàm :math:`F` chắc chắn là :math:`0`.
2. Nếu vi sai input của :math:`F` là :math:`1` :math:`\Rightarrow` vi sai output của :math:`\mathsf{Expand}` là :math:`16` :math:`\Rightarrow` vi sai output của :math:`\mathsf{SBox}` là :math:`7` với xác suất :math:`14/64` :math:`\Rightarrow` vi sai output của :math:`\mathsf{PBox}` là :math:`11` với xác suất là :math:`14/64` :math:`\Rightarrow` hàm :math:`F` là :math:`11` với xác suất :math:`14/64 = 7/32`.
3. Nếu vi sai input của :math:`F` là :math:`3` :math:`\Rightarrow` vi sai output của :math:`\mathsf{Expand}` là :math:`52` :math:`\Rightarrow` vi sai output của :math:`\mathsf{SBox}` là :math:`2` với xác suất :math:`16/64` :math:`\Rightarrow` vi sai output của :math:`\mathsf{PBox}` là :math:`8` với xác suất :math:`16/64` :math:`\Rightarrow` hàm :math:`F` là :math:`8` với xác suất :math:`16/64 = 1/4`.

Nói chung, chúng ta chọn output của :math:`\mathsf{Expand}` (input cho :math:`\mathsf{SBox}`) giống với xác suất cao nhất với phân tích :math:`\mathsf{SBox}` ở trên kia.

----------------
Chosen plaintext
----------------

Differential attack là một dạng chosen plaintext, trong đó chúng ta tận dụng các xác suất ở trên.

^^^^^^^^^^^^^^^^^^^^^^^^^
Chosen plaintext phần một
^^^^^^^^^^^^^^^^^^^^^^^^^

Do tính chất vi sai, chúng ta sẽ mong muốn tìm những cặp (plaintext, ciphertext) :math:`(P_1, C_1)` và :math:`(P_2, C_2)` nào đó mà vi sai input :math:`P_1 \oplus P_2` và vi sai output :math:`C_1 \oplus C_2` có thể tối ưu xác suất trên.

Giả sử chúng ta xét trường hợp 3 ở trên, khi vi sai input của :math:`F` là :math:`3` thì vi sai output của :math:`F` là :math:`8` với xác suất :math:`1/4`. Đây là xác suất lớn nhất nên ta mong muốn trong 3 vòng của TinyDES sẽ tận dụng được càng nhiều càng tốt.

Chúng ta đi từ dưới lên. Đặt

.. math:: 
    
    L_3 = R_2, \quad R_3 = L_2 \oplus F(R_2, K_3),

và

.. math:: 
    
    L_3' = R_2', \quad R_3' = L_2' \oplus F(R_2', K_3).

Chọn :math:`R_2 \oplus R_2' = 3` thì :math:`F(R_2, K_3) \oplus F(R_2', K_3) = 8` với xác suất :math:`1/4`. Vì là bước cuối nên ta hy vọng ciphertext cuối cùng sẽ càng ít phức tạp càng tốt. Do đó có thể lựa chọn :math:`L_2 = L_2' = 0` để bảo toàn vi sai sau khi vòng 3 kết thúc.

    Ở vòng 3, xác suất để vi sai input bằng :math:`3` và vi sai output bằng :math:`8` là :math:`1/4`.

Tiếp theo, đặt:

.. math:: 
    
    L_2 = R_1, \quad R_2 = L_1 \oplus F(R_1, K_2),

và

.. math:: 
    
    L_2' = R_1', \quad R_2' = L_1' \oplus F(R_1', K_2).

Do :math:`L_2 = R_1` nên :math:`R_1 = 0`. Tương tự :math:`R_1' = L_2' = 0`. Điều đáng chú ý là :math:`R_1 \oplus R_1' = 0`, nghĩa là vi sai input bằng :math:`0`, nên vi sai output :math:`F(R_1, K_2) \oplus F(R_1', K_2)` chắc chắn bằng :math:`0` (xác suất bằng :math:`1`).

    Ở vòng 2, xác suất để vi sai input bằng :math:`0` và vi sai output bằng :math:`0` là :math:`1`.

Ta lại có

.. math:: 
    
    R_2 \oplus R_2' = 3 = L_1 \oplus F(R_1, K_2) \oplus L_1' \oplus F(R_1', K_2) = L_1 \oplus L_1',

do vi sai output hàm :math:`F` chắc chắn bằng :math:`0`. Do đó :math:`L_1 \oplus L_1' = 3`.

Tuy nhiên, :math:`L_1 = R_0` và :math:`L_1' = R_0'` nên :math:`L_1 \oplus L_1' = R_0 \oplus R_0' = 3`. Do đó vi sai output của hàm :math:`F` là :math:`F(R_0, K_1) \oplus F(R_0', K_1) = 8` có xác suất :math:`1/4`.

    Ở vòng 1, xác suất để vi sai input bằng :math:`3` và vi sai output bằng :math:`8` là :math:`1/4`.

Cuối cùng,

.. math:: 
    
    R_1 \oplus R_1' = L_0 \oplus F(R_0, K_1) \oplus L_0' \oplus F(R_0', K_1) = L_0 \oplus L_0' \oplus 8,

mà ta nhớ lại ở trên :math:`R_1 \oplus R_1' = 0` nên suy ra :math:`L_0 \oplus L_0' = 8`.

Tổng kết lại, ta chọn vi sai input :math:`(L, R) = (8, 3)` thì xác suất để vi sai output bằng :math:`(3, 8)` là :math:`(1/4) \times 1 \times (1/4) = 1/16`. Đây là xác suất cao nhất có thể sau khi TinyDES chạy đủ 3 vòng.

^^^^^^^^^^^^^^^^^^^^^^^^^
Chosen plaintext phần hai
^^^^^^^^^^^^^^^^^^^^^^^^^

Tương tự, chúng ta xét trường hợp 2 ở trên, khi vi sai input của :math:`F` là :math:`1` thì vi sai output của :math:`F` là :math:`11` với xác suất :math:`7/32`. Ta cũng mong muốn sau 3 vòng của TinyDES sẽ tận dụng được càng nhiều càng tốt.

Chúng ta lại đi dưới lên. Đặt

.. math:: 
    
    L_3 = R_2, \quad R_3 = L_2 \oplus F(R_2, K_3)

và

.. math:: 
    
    L_3' = R_2', \quad R_3' = L_2' \oplus F(R_2', K_3).

Chọn :math:`R_2 \oplus R_2' = 1` thì :math:`F(R_2, K_3) \oplus F(R_2', K_3) = 11` với xác suất :math:`7/32`. Vì là bước cuối cùng nên ta cũng hy vọng ciphertext sẽ càng ít phức tạp càng tốt. Do đó ta chọn :math:`L_2 = L_2' = 0`.

    Ở vòng 3, xác suất để vi sai input bằng :math:`1` và vi sai output bằng :math:`11` là :math:`7/32`.

Tiếp theo, đặt

.. math:: 
    
    L_2 = R_1, \quad R_2 = L_1 \oplus F(R_1, K_2),

và

.. math:: 
    
    L_2' = R_1', \quad R_2' = L_1' \oplus F(R_1', K_2).

Do :math:`L_2 = R_1` nên :math:`R_1 = 0`. Tương tự :math:`R_1' = 0`. Suy ra :math:`R_1 \oplus R_1' = 0` và vi sai output :math:`F(R_1, K_2) \oplus F(R_1', K_2) = 0` với xác suất bằng :math:`1` (chắc chắn xảy ra).

    Ở vòng 2, xác suất để vi sai input bằng :math:`0` và vi sai output bằng :math:`0` là :math:`1`.

Ta lại có:

.. math:: 
    
    R_2 \oplus R_2' = L_1 \oplus F(R_1, K_2) \oplus L_1' \oplus F(R_1', K_2) = L_1 \oplus L_1',

do vi sai output của hàm :math:`F` chắc chắn bằng :math:`0`. Do đó :math:`L_1 \oplus L_1' = 1`.

Tuy nhiên :math:`L_1 = R_0` và :math:`L_1' = R_0'` nên :math:`R_0 \oplus R_0' = L_1 \oplus L_1' = 1`. Do đó vi sai output của hàm :math:`F` ở vòng :math:`1` là :math:`F(R_0, K_1) \oplus F(R_0', K_1) = 11` với xác suất :math:`7/32`.

    Ở vòng 1, xác suất để vi sai input bằng :math:`1` và vi sai output bằng :math:`11` là :math:`7/32`.

Cuối cùng, do

.. math:: 
    
    R_1 \oplus R_1' = L_0 \oplus F(R_0, K_1 \oplus L_0' \oplus F(R_0', K_1)),

mà :math:`R_1 \oplus R_1' = 0` và :math:`F(R_0, K_1) \oplus F(R_0', K_1) = 11` nên :math:`L_0 \oplus L_0' = 11`.

Tổng kết lại, ta chọn vi sai input :math:`(L, R) = (11, 1)` thì xác suất để vi sai output bằng :math:`(1, 11)` là :math:`(7/32) \times 1 \times (7/32) \approx 0.048`. Đây cũng là xác suất cao nhất có thể sau khi TinyDES chạy đủ 3 vòng.

^^^^^^^^^^^^
Final attack
^^^^^^^^^^^^

Như vậy, đối với TinyDES chúng ta phá mã vi sai như sau:

1. Tìm một số lượng cặp plaintext, ciphertext :math:`(P_1, C_1)`, :math:`(P_2, C_2)`, ... cho tới khi tìm được :math:`P_i \oplus P_j = \mathrm{0x83}` và :math:`C_i \oplus C_j = \mathrm{0x38}`.
2. Tìm một số lượng cặp plaintext, ciphertext :math:`(P_1', C_1')`, :math:`(P_2', C_2')`, ... cho tới khi tìm được :math:`P_i' \oplus P_j' = \mathrm{0xB1}` và :math:`C_i' \oplus C_j' = \mathrm{0x1B}`.

Sau khi đã tìm được một số lượng cặp plaintext, ciphertext thỏa vi sai trên, nhớ lại hàm :math:`F` ở vòng 3, do

.. math:: 
    
    L_3 = R_2, \ \text{và} \ R_3 = L_2 \oplus F(R_2, K_3) = L_2 \oplus F(L_3, K_3) = F(L_3, K_3),

theo cách chọn :math:`L_2 = 0` ở trên, dễ thấy rằng chúng ta có thể tìm được các :math:`K_3` thỏa mãn hàm :math:`F` ở vòng 3.

Để làm điều đó thì ta tính :math:`O = \mathsf{Expand}(L_3)`, và do :math:`\mathsf{SBox}(O \oplus K_3) = \mathsf{PBox}^{-1}(R_3)` cũng tính được nên có thể tìm các giá trị :math:`O \oplus K_3` mà khi đi qua :math:`\mathsf{SBox}` cho kết quả bằng :math:`\mathsf{PBox}^{-1}(R_3)`. Sau đó XOR lại cho :math:`O` thì sẽ tìm được các giá trị có thể của :math:`K_3`. Lưu ý rằng :math:`\mathsf{SBox}` làm giảm :math:`6` bits còn :math:`4` bits nên sẽ có nhiều giá trị khác nhau cho cùng giá trị :math:`\mathsf{SBox}`.

Thực hiện trên hai trường hợp vi sai input-output là :math:`(\mathrm{0x83}, \mathrm{0x38})` và :math:`(\mathrm{0xB1}, \mathrm{0x1B})` ta có tập các giá trị có thể xảy ra của :math:`K_3`.

Theo thuật toán sinh khóa con thì với khóa :math:`K` :math:`8` bits ban đầu, đặt là :math:`k_0 k_1 k_2 k_3 k_4 k_5 k_6 k_7`, thì khóa con :math:`K_3` là :math:`k_5 k_1 k_3 k_2 k_7 k_0`. Trong :math:`K_3` không có :math:`k_4` và :math:`k_6` nên chúng ta sẽ bruteforce hai bit này tới khi tìm được đúng khóa :math:`K` mà tương ứng với cặp :math:`(P_i, C_i)`.

.. code-block:: python

    # find_key.py

    import tinydes
    from itertools import product


    def int_to_vec6(n: int) -> list[int]:
        return list(map(int, format(n, "06b")))


    def int_to_vec8(n: int) -> list[int]:
        return list(map(int, format(n, "08b")))


    def vec_to_int(v: list[int]) -> int:
        return int("".join(map(str, v)), 2)


    def recover_key(k: list[int]) -> list[int]:
        return [k[5], k[1], k[3], k[2], 0, k[0], 0, k[4]]


    key = [1, 0, 0, 1, 1, 0, 1, 0]

    ptx = []
    ctx = []

    pt, ct = [0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 0]

    candidates = []
    K3 = []

    for _ in range(24):
        pt = int_to_vec8(_)
        ct = tinydes.encrypt_block(pt, key)
        pt_ = tinydes.Xor(int_to_vec8(0x83), pt)
        ct_ = tinydes.encrypt_block(pt_, key)
        if tinydes.Xor(ct_, ct) == list(map(int, format(0x38, "08b"))):
            ptx.append(pt_)
            ctx.append(ct_)
            candidates.append((pt, pt_))
            break

    for pt1, pt2 in candidates:
        o1, o2 = tinydes.PBox_inv(pt1[4:]), tinydes.PBox_inv(pt2[4:])
        q1, q2 = tinydes.Expand(pt1[:4]), tinydes.Expand(pt2[:4])
        for i in range(len(tinydes.sbox)):
            if tinydes.sbox[i] == vec_to_int(o1):
                row, col = i // 16, i % 16
                idx = [row // 2] + list(map(int, format(col, "04b"))) + [row % 2]
                K3.append(tinydes.Xor(q1, idx))
            if tinydes.sbox[i] == vec_to_int(o2):
                row, col = i // 16, i % 16
                idx = [row // 2] + list(map(int, format(col, "04b"))) + [row % 2]
                K3.append(tinydes.Xor(q2, idx))

    candidates = []

    for _ in range(24):
        pt = int_to_vec8(_)
        ct = tinydes.encrypt_block(pt, key)
        pt_ = tinydes.Xor(int_to_vec8(0xb1), pt)
        ct_ = tinydes.encrypt_block(pt_, key)
        if tinydes.Xor(ct_, ct) == list(map(int, format(0x1b, "08b"))):
            ptx.append(pt_)
            ctx.append(ct_)
            candidates.append((pt, pt_))
            break

    for pt1, pt2 in candidates:
        o1, o2 = tinydes.PBox_inv(pt1[4:]), tinydes.PBox_inv(pt2[4:])
        q1, q2 = tinydes.Expand(pt1[:4]), tinydes.Expand(pt2[:4])
        for i in range(len(tinydes.sbox)):
            if tinydes.sbox[i] == vec_to_int(o1):
                row, col = i // 16, i % 16
                idx = [row // 2] + list(map(int, format(col, "04b"))) + [row % 2]
                K3.append(tinydes.Xor(q1, idx))
            if tinydes.sbox[i] == vec_to_int(o2):
                row, col = i // 16, i % 16
                idx = [row // 2] + list(map(int, format(col, "04b"))) + [row % 2]
                K3.append(tinydes.Xor(q2, idx))

    for k3 in set([vec_to_int(k) for k in K3]):
        k = recover_key(int_to_vec6(k3))
        for k4, k6 in product(range(2), repeat=2):
            k[4], k[6] = k4, k6
            if tinydes.encrypt_block(pt, k) == ct:
                print(f"Recover key: {k}")
