AES
===

AES biến đổi theo khối :math:`128` bit, sử dụng mô hình mạng SPN.

Bốn phép biến đổi chính là Add Round Key, Substitute Bytes, Shift Rows và Mix Columns.

Quá trình giải mã sử dụng phép biến đổi ngược của bốn phép biến đổi trên là Inverse Sub Bytes, Inverse Shift Rows, Inverse Mix Columns. Đối với Add Round Key bản thân là phép XOR nên phép biến đổi ngược là chính nó.

AES hỗ trợ key với các kích thước: :math:`128` bit, :math:`192` bit và :math:`256` bit. 

Đối với kích thước khóa :math:`128` bit, AES dùng hàm Expand Key để mở rộng khóa thành :math:`44` words, mỗi word có :math:`32` bits, với key :math:`128` bit thành :math:`11` cụm khóa con. Mỗi :math:`4` words làm tham số cho một phép Add Round Key.

Mỗi block bản rõ :math:`16` byte :math:`p_0`, :math:`p_1`, ..., :math:`p_{15}` được tổ chức dưới dạng một ma trận :math:`4 \times 4` (gọi là **ma trận state**)

.. math:: 

    \begin{pmatrix}
        p_0 & p_1 & p_2 & p_3 \\
        p_4 & p_5 & p_6 & p_7 \\
        p_8 & p_9 & p_{10} & p_{11} \\
        p_{12} & p_{13} & p_{14} & p_{15}
    \end{pmatrix} \longrightarrow \begin{pmatrix}
        s_{00} & s_{01} & s_{02} & s_{03} \\
        s_{10} & s_{11} & s_{12} & s_{13} \\
        s_{20} & s_{21} & s_{22} & s_{23} \\
        s_{30} & s_{31} & s_{32} & s_{33}
    \end{pmatrix}

1. Các phép biến đổi Add Round Key, Substitute Bytes, Shift Rows, Mix Columns được thực hiện trên ma trận :math:`4 \times 4` này.
2. Các phép tính số học trong AES được thực hiện trong :math:`\mathrm{GF}(2^8)` với đa thức tối giản là :math:`f(x) = x^8 + x^4 + x^3 + x + 1`.

Substitute Bytes
----------------

Substitute Bytes
^^^^^^^^^^^^^^^^

Ta sử dụng một bảng tra cứu :math:`16 \times 16` (S-box).

1. Điền các số từ :math:`0` tới :math:`255` theo từng hàng.
2. Thay thế mối byte trong bảng bằng nghịch đảo trong :math:`\mathrm{GF}(2^8)`. Quy ước :math:`(00)^{-1} = 00`.
3. Với mỗi byte trong bảng, ta kí hiệu :math:`8` bit là :math:`b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0`. Thay thế mỗi :math:`b_i` bằng :math:`b_i'` như sau

.. math:: b'_i = b_i \oplus b_{(i+4) \bmod 8} \oplus b_{(i+5) \bmod 8} \oplus b_{(i+6) \bmod 8} \oplus b_{(i+7) \bmod 8} \oplus c_i,

với :math:`c_i` là bit thứ :math:`i` của số ``0x63``.

Việc tính trên tương đương với phép nhân trên ma trận :math:`\mathrm{GF}(2)` là :math:`B' = XB + C`

.. math:: 

    \begin{bmatrix}
        b'_0 \\ b'_1 \\ b'_2 \\ b'_3 \\ b'_4 \\ b'_5 \\ b'_6 \\ b'_7
    \end{bmatrix} = 
    \begin{bmatrix}
        1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
        1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\
        1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\
        1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\
        1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
        0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
        0 & 0 & 1 & 1 & 1 & 1 & 1 & 0 \\
        0 & 0 & 0 & 1 & 1 & 1 & 1 & 1
    \end{bmatrix} 
    \begin{bmatrix}
        b_0 \\ b_1 \\ b_2 \\ b_3 \\ b_4 \\ b_5 \\ b_6 \\ b_7
    \end{bmatrix} + 
    \begin{bmatrix}
        1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 1 \\ 1 \\ 0
    \end{bmatrix}.

Ma trận :math:`X` là ma trận khả nghịch, do đó phép biến đổi S-box là song ánh (one-to-one và onto mapping).

Dựa vào bảng S-box, Substitute Bytes thực hiện như sau: mỗi byte trong ma trận state :math:`S` dưới dạng thập lục phân là :math:`xy` sẽ được thay bằng giá trị ở hàng :math:`x` và cột :math:`y` của S-box.

Inverse Sub Bytes
^^^^^^^^^^^^^^^^^

Ta cần xây dựng bảng Inverse Sub Bytes (IS-box).

Việc xây dựng bảng này giống với bảng S-box ở bước 1 và 2. Tại bước 3:

.. math:: b_i = b'_{(i+2) \bmod 8} \oplus b'_{(i+5) \bmod 8} \oplus b'_{(i+7) \bmod 8} \oplus d_i,

với :math:`d_i` là bit thứ :math:`i` của số ``0x05``.

Ý nghĩa
^^^^^^^

Bảng S-box dùng để chống lại known-plaintext và là bước duy nhất trong bốn bước không có quan hệ tuyến tính.

Shift Rows
----------

Shift Rows
^^^^^^^^^^

Trong Shift Rows, các dòng của ma trận state được biến đổi như sau:

1. Dòng thứ nhất giữ nguyên.
2. Dòng 2 dịch vòng trái 1 ô.
3. Dòng 3 dịch vòng trái 2 ô.
4. Dòng 4 dịch vòng trái 3 ô.

.. figure:: ../../figures/aes/shiftrows.*

Inverse Shift Rows
^^^^^^^^^^^^^^^^^^

Các dòng thứ 2, 3, 4 dịch phải tương ứng 1, 2, 3 ô.

Ý nghĩa
^^^^^^^

Xáo trộn các byte để tạo ra các cột cho Mix Columns.

Mix Columns
-----------

Mix Columns
^^^^^^^^^^^

Mix cols biến đổi từng cột của ma trận state một cách độc lập bằng phép nhân đa thức. Giả sử cột đầu tiên của ma trận state viết dưới dạng đa thức là

.. math:: f(z) = s_{00} z^3 + s_{10} z^2 + s_{20} z + s_{30},

với :math:`z \in \mathrm{GF}(2^8)`.

Khi đó :math:`f(z)` sẽ được nhân với :math:`a(z) = 3z^3 + z^2 + z + 2`, lưu ý rằng tất cả hệ số, phép cộng và nhân thực hiện trên :math:`\mathrm{GF}(2^8)`, và sau đó modulo cho :math:`n(z) = z^4 + 1`.

Bốn byte hệ số của kết quả sẽ thay thế cho bốn byte tương ứng trong cột. Nếu viết dưới dạng ma trận, ta có

.. math:: 

    \begin{bmatrix}
        s'_{00} \\ s'_{10} \\ s'_{20} \\ s'_{30}
    \end{bmatrix} = \begin{bmatrix}
        02 & 03 & 01 & 01 \\
        01 & 02 & 03 & 01 \\
        01 & 01 & 02 & 03 \\
        03 & 01 & 01 & 02
    \end{bmatrix} 
    \begin{bmatrix}
        s_{00} \\ s_{10} \\ s_{20} \\ s_{30}
    \end{bmatrix}.

Lưu ý rằng các số :math:`01`, :math:`02`, :math:`03` tuy viết dưới dạng thập phân nhưng khi tính toán phải ở dạng :math:`\mathrm{GF}(2^8)`. Việc sử dụng :math:`1`, :math:`2`, :math:`3` giúp tăng tốc độ tính toán vì :math:`1` và :math:`2` chỉ cần phép dịch bit, còn :math:`3` là XOR của :math:`1` và :math:`2`.

Inverse Mix Columns
^^^^^^^^^^^^^^^^^^^

Lúc này ma trận nghịch đảo có dạng

.. math:: 

    \begin{bmatrix}
        \text{0E} & \text{0B} & \text{0D} & \text{09} \\
        \text{09} & \text{0E} & \text{0B} & \text{0D} \\
        \text{0D} & \text{09} & \text{0E} & \text{0B} \\
        \text{0B} & \text{0D} & \text{09} & \text{0E}
    \end{bmatrix}.

Ý nghĩa
^^^^^^^

Mỗi cột mới chỉ phụ thuộc cột ban đầu. Cùng với sự kết hợp Shift Rows sau một vài vòng biến đổi (cụ thể là :math:`2`, các bạn có thể thử chứng minh), :math:`128` bit kết quả phụ thuộc vào tất cả :math:`128` bit ban đầu. Từ đó tạo ra tính khuếch tán (diffusion).

Add Round Key
-------------

Add Round Key
^^^^^^^^^^^^^

:math:`128` bit của ma trận state được XOR với :math:`128` bit của khóa con từng vòng (:math:`4` dword :math:`32` bit). Phép biến đổi ngược của Add Round Key là chính nó.

Ý nghĩa
^^^^^^^

Sự kết hợp với khóa tạo ra tính làm rối (confusion).

Expand Key
-----------

Expand Key
^^^^^^^^^^^

Đầu vào của thao tác Expand Key là :math:`16` bytes (:math:`4` words) của khóa, sinh ra một mảng :math:`44` words (:math:`176` bytes) sử dụng cho :math:`11` vòng AES, mỗi vòng :math:`4` words.

.. figure:: ../../figures/aes/expandkey.*

Từ bốn word đầu vào :math:`w_0 w_1 w_2 w_3`, lần lặp đầu sinh ra :math:`w_4 w_5 w_6 w_7`, lần lặp thứ hai sinh ra :math:`w_8 w_9 w_{10} w_{11}`, ...

.. prf:algorithm:: 
    :label: algo-AES-expand-key

    1. if :math:`i \bmod 4 = 0`
        
       1. :math:`g \gets \mathsf{SubWord}(\mathsf{RotWord}(w_{i-1})) \oplus \mathrm{Rcon}[i/4]`
       2. :math:`w_i = w_{i-4} \oplus g`
    
    2. else
        
       1. :math:`w_i = w_{i-4} \oplus w_{i-1}`
    
    3. endif

Trong đó:

1. :math:`\mathsf{RotWord}` dịch vòng trái :math:`1` byte, nghĩa là từ bốn byte :math:`b_0 b_1 b_2 b_3` trở thành :math:`b_1 b_2 b_3 b_0`.
2. :math:`\mathsf{SubWord}` thay mỗi byte trong word bằng bảng S-box.
3. :math:`\mathrm{Rcon}` là một mảng hằng số gồm :math:`10` words tương ứng với :math:`10` vòng AES. :math:`4` bytes của một phần tử :math:`\mathrm{Rcon}[j]` là :math:`\mathrm{RC}[j], 0, 0, 0` với :math:`\mathrm{RC}[j]` là mảng :math:`10` bytes như sau

+------------------------+-----------+-----------+-----------+-----------+------------+------------+------------+------------+------------+------------+
| :math:`j`              | :math:`1` | :math:`2` | :math:`3` | :math:`4` | :math:`5`  | :math:`6`  | :math:`7`  | :math:`8`  | :math:`9`  | :math:`10` |
+========================+===========+===========+===========+===========+============+============+============+============+============+============+
| :math:`\mathrm{RC}[j]` | :math:`1` | :math:`2` | :math:`4` | :math:`8` | :math:`10` | :math:`20` | :math:`40` | :math:`80` | :math:`18` | :math:`36` |
+------------------------+-----------+-----------+-----------+-----------+------------+------------+------------+------------+------------+------------+

Ý nghĩa của Expand Key
^^^^^^^^^^^^^^^^^^^^^^

Dùng để chống lại known-plaintext (giống Sub Bytes dùng S-box). Đặc điểm của Expand Key gồm:

1. Biết một số bit của khóa hay khóa con không thể tính được các bit còn lại.
2. KHÔNG THỂ tính ngược.
3. Khuếch tán: mỗi bit của khóa chính tác động lên tất cả khóa con.

Kết luận
--------

Mã hóa AES đơn giản và có thể chạy trên các chip :math:`8` bit.

AES cung cấp ba biến thể cho độ dài khóa là:

- :math:`128` bits: :math:`44` words :math:`4` bytes cho :math:`10` vòng (:math:`11` lần ARK);
- :math:`192` bits: :math:`52` words :math:`4` bytes cho :math:`12` vòng (:math:`13` lần ARK);
- :math:`256` bits: :math:`60` words :math:`4` bytes cho :math:`14` vòng (:math:`15` lần ARK).

Về phép Mix Columns
-------------------

Sau đây mình sẽ nói về việc phép nhân trên đa thức có hệ số trong :math:`\mathrm{GF}(2^8)` lại tương đương với phép nhân ma trận trong Mix Columns ở trên.

Giả sử ma trận trạng thái trước khi bước vào phép tính Mix Column của AES là

.. math:: 

    \begin{pmatrix}
        c_0 & c_1 & c_2 & c_3 \\
        c_4 & c_5 & c_6 & c_7 \\
        c_8 & c_9 & c_{10} & c_{11} \\
        c_{12} & c_{13} & c_{14} & c_{15}
    \end{pmatrix}.

Phép tính Mix Column lấy mỗi cột của ma trận trạng thái trên làm tham số cho đa thức với hệ số trong :math:`\mathrm{GF}(2^8)` và nhân với đa thức :math:`c(z) = 2 + z + z^2 + 3z^3` rồi modulo cho :math:`z^4 + 1`.

Giả sử với cột đầu tiên, ta viết hệ số theo thứ tự bậc tăng dần :math:`d(z) = c_0 + c_4 z + c_8 z^2 + c_{12} z^3`.

Tính trong :math:`\mathrm{GF}(2^8)`:

.. math:: 
    
    c(z) \cdot d(z) & = (2 + z + z^2 + 3 z^3) \cdot (c_0 + c_4 z + c_8 z^2 + c_{12} z^3) \\
    & = 2 c_0 + 2 c_4 z + 2 c_8 z^2 + 2 c_{12} z^3 + c_0 z + c_4 z^2 + c_8 z^3 + c_{12} z^4 \\
    & + c_0 z^2 + c_4 z^3 + c_8 z^4 + c_{12} z^5 + 3 c_0 z^3 + 3 c_4 z^4 + 3 c_8 z^5 + 3 c_{12} z^6 \\
    & = 2 c_0 + (2 c_4 + c_0) z + (2 c_8 + c_4 + c_0) z^2 + (2 c_{12} + c_8 + c_4 + 3 c_0) z^3 \\
    & + (c_{12} + c_8 + 3 c_4) z^4 + (c_{12} + 3 c_8) z^5 + 3 c_{12} z^6.
    
Trong :math:`\mathrm{GF}(2^8)` thì mọi phần tử đều có tính chất :math:`2 x^n = 0`, tương đương với :math:`x^n = -x^n`. Do đó

.. math:: 
    
    & z^6 \pmod{z^4 + 1} \equiv -z^2 \equiv z^2 \\
    & z^5 \pmod{z^4 + 1} \equiv -z \equiv z \\
    & z^4 \pmod{z^4 + 1} \equiv -1 \equiv 1.

Suy ra

.. math:: 

    c(z) \cdot d(z) & = 2 c_0 + (2 c_4 + c_0) z + (2 c_8 + c_4 + c_0) z^2 + (2 c_{12} + c_8 + c_4 + 3 c_0) z^3 \\
    & + (c_{12} + c_8 + 3 c_4) + (c_{12} + 3 c_8) z + 3 c_{12} z^2 \\
    & = (c_{12} + c_8 + 3 c_4 + 2 c_0) + (c_{12} + 3 c_8 + 2 c_4 + c_0) z \\
    & + (3 c_{12} + 2 c_8 + c_4 + c_0) z^2 + (2 c_{12} + c_8 + c_4 + 3 c_0) z^3.

Như vậy xét hệ số lần lượt trước :math:`1`, :math:`z`, :math:`z^2` và :math:`z^3` thì tương đương với phép nhân ma trận

.. math:: 

    \begin{pmatrix}
        2 & 3 & 1 & 1 \\
        1 & 2 & 3 & 1 \\
        1 & 1 & 2 & 3 \\
        3 & 1 & 1 & 2
    \end{pmatrix} \cdot
    \begin{pmatrix}
        c_0 \\ c_4 \\ c_8 \\ c_{12}
    \end{pmatrix}.

Đây chính là kết quả cần tìm.
