AES
===

Phần này sử dụng tài liệu mô tả thuật toán AES của NIST :cite:`1250461`.

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

Ma trận :math:`X` khả nghịch, do đó S-box là một song ánh.

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

.. figure:: ../../figures/symmetric-key/aes/shiftrows.*

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

Mỗi cột mới chỉ phụ thuộc vào một cột ban đầu. Khi kết hợp với Shift Rows,
sau hai vòng, mỗi bit đầu ra phụ thuộc vào toàn bộ :math:`128` bit đầu vào;
đây là tính khuếch tán.

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

.. figure:: ../../figures/symmetric-key/aes/expandkey.*

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
2. Không thể suy ngược toàn bộ khóa từ một phần thông tin khóa.
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

Phép nhân đa thức với hệ số trong :math:`\mathrm{GF}(2^8)` tương đương với
phép nhân ma trận dùng trong MixColumns như sau.

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

Phiên bản AES thu nhỏ
---------------------

Để khảo sát đại số mà không phải xử lí ngay hệ AES-128 rất lớn, Cid, Murphy
và Robshaw xây dựng họ mã khối :math:`\operatorname{SR}(n,r,c,e)` giữ lại
cấu trúc của AES nhưng cho phép thay đổi kích thước trạng thái
:cite:`10.1007/11502760_10`. Các tham số có ý nghĩa như sau:

* :math:`n` là số vòng, :math:`1 \leqslant n \leqslant 10`;
* :math:`r \in \{ 1, 2, 4 \}` và :math:`c \in \{ 1, 2, 4 \}` là số hàng và số cột;
* :math:`e \in \{ 4, 8 \}` là số bit của mỗi phần tử trạng thái.

Một khối gồm :math:`rc` phần tử thuộc :math:`\FF_{2^e}`. Khi :math:`e=4` và
:math:`e=8`, các trường lần lượt được biểu diễn bởi

.. math:: \FF_{2^4} = \FF_2[t]/(t^4+t+1), \quad \FF_{2^8} =. \FF_2[t]/(t^8+t^4+t^3+t+1).

Mọi vòng của :math:`\operatorname{SR}` đều gồm SubBytes, ShiftRows,
MixColumns và AddRoundKey. Đây là một khác biệt với AES: vòng cuối của AES
không có MixColumns :cite:`1250461`. Phần dưới xét mô hình
:math:`\operatorname{SR}(n, 2, 2, 4)`, có trạng thái và khóa chỉ gồm
:math:`16` bit.

S-box 4 bit
^^^^^^^^^^^

Giả sử ta có :math:`x = \sum_{i=0}^3 x_i t^i \in \FF_{2^4}` và đặt
:math:`y = x^{-1} =. \sum_{i=0}^3 y_i t^i`, với quy ước :math:`0^{-1}=0`. S-box
thực hiện phép nghịch đảo rồi áp dụng ánh xạ affine

.. math::

   \begin{pmatrix}z_0\\z_1\\z_2\\z_3\end{pmatrix}
   =
   \begin{pmatrix}
   1&1&1&0\\0&1&1&1\\1&0&1&1\\1&1&0&1
   \end{pmatrix}
   \begin{pmatrix}y_0\\y_1\\y_2\\y_3\end{pmatrix}
   +\begin{pmatrix}0\\1\\1\\0\end{pmatrix}.

Do đó, nếu :math:`S:\FF_2^4\to\FF_2^4` là S-box thì SubBytes là ánh xạ

.. math::

   \mathcal S(s_0\Vert s_1\Vert s_2\Vert s_3)
   =S(s_0)\Vert S(s_1)\Vert S(s_2)\Vert S(s_3).

Ánh xạ affine trên cũng có thể viết dưới dạng đa thức trong vành
:math:`\FF_2[t]/(t^4+1)`:

.. math::
   :label: eq-small-aes-affine

   A(y)=ay+b\pmod{t^4+1},\qquad
   a=1+t^2+t^3,\quad b=t+t^2.

Thật vậy, phép nhân với :math:`a` cho ma trận tuần hoàn trong công thức S-box,
còn cộng :math:`b` tương ứng với cộng vector :math:`(0,1,1,0)^\top`.
Vì vậy S-box là ánh xạ hợp thành :math:`A\circ I`, trong đó
:math:`I(x)=x^{14}` trên :math:`\FF_{2^4}`.

ShiftRows và MixColumns
^^^^^^^^^^^^^^^^^^^^^^^

Với trạng thái

.. math::

   \begin{pmatrix}s_0&s_1\\s_2&s_3\end{pmatrix},
   \qquad s_i\in\FF_{2^4},

ShiftRows đổi chỗ hai phần tử ở hàng thứ hai, còn MixColumns nhân mỗi cột với
ma trận trên :math:`\FF_{2^4}`:

.. math::

   \begin{pmatrix}s_0&s_1\\s_2&s_3\end{pmatrix}
   \xmapsto{\mathcal R}
   \begin{pmatrix}s_0&s_1\\s_3&s_2\end{pmatrix}
   \xmapsto{\mathcal M}
   \begin{pmatrix}t+1&t\\t&t+1\end{pmatrix}
   \begin{pmatrix}s_0&s_1\\s_3&s_2\end{pmatrix}.

Khi ghép bốn nibble thành vector của :math:`\FF_2^{16}`, đặt

.. math::

   M=\begin{pmatrix}
   1&0&0&1\\1&1&0&1\\0&1&1&0\\0&0&1&1
   \end{pmatrix},\qquad
   M'=\begin{pmatrix}
   0&0&0&1\\1&0&0&1\\0&1&0&0\\0&0&1&0
   \end{pmatrix}.

Hai phép biến đổi tuyến tính được biểu diễn bởi

.. math::

   M_{\mathrm{SR}}=
   \begin{pmatrix}
   I_4&O_4&O_4&O_4\\O_4&I_4&O_4&O_4\\
   O_4&O_4&O_4&I_4\\O_4&O_4&I_4&O_4
   \end{pmatrix},
   \qquad
   M_{\mathrm{MC}}=
   \begin{pmatrix}
   M&M'&O_4&O_4\\O_4&O_4&M&M'\\
   M'&M&O_4&O_4\\O_4&O_4&M'&M
   \end{pmatrix},

trong đó :math:`I_4` và :math:`O_4` lần lượt là ma trận đơn vị và ma trận
không cấp :math:`4`.

Phương trình biểu diễn một vòng
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gọi :math:`b_i\in\FF_2^{16}` là đầu vào vòng :math:`i`,
:math:`k_i\in\FF_2^{16}` là khóa vòng và
:math:`c_i=\mathcal S(b_i)`. Một vòng đầy đủ được viết gọn thành

.. math::
   :label: eq-small-aes-round

   b_{i+1}=\mathcal M\circ\mathcal R\circ\mathcal S(b_i)+k_{i+1},

hay dưới dạng vector cột,

.. math::

   b_{i+1}^{\top}=M_{\mathrm{MC}}M_{\mathrm{SR}}c_i^{\top}
   +k_{i+1}^{\top}.

Vì hai ma trận tuyến tính khả nghịch, đầu ra của lớp S-box có thể được biểu
diễn trực tiếp theo đầu ra vòng và khóa vòng:

.. math::
   :label: eq-small-aes-sbox-output

   c_i^{\top}=(M_{\mathrm{MC}}M_{\mathrm{SR}})^{-1}
   (b_{i+1}^{\top}+k_{i+1}^{\top}).

Với bản rõ đã biết :math:`p` và bản mã :math:`c`, điều kiện biên là
:math:`b_0=p+k_0` và :math:`b_n=c`. Công thức
:eq:`eq-small-aes-sbox-output` là phép thế dùng để loại các biến trung gian
sau SubBytes khi xây dựng hệ phương trình cho từng vòng.

Hệ phương trình bậc hai của S-box
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Các hệ phương trình bậc hai nhiều biến cho S-box AES có thể được sinh tự động
bằng SageMath :cite:`8073822`. Với S-box 4 bit, cần điều chỉnh mô hình để quy
ước :math:`0^{-1}=0` không tạo ra phương trình sai :math:`0=1`.

Cho :math:`x,y\in\FF_{2^4}` và :math:`y=x^{-1}`. Quan hệ :math:`xy=1` chỉ
đúng khi :math:`x\ne0`. Nhân thêm :math:`x` và liên tiếp bình phương trong
trường đặc số :math:`2` cho

.. math::

   x=x^2y\Longrightarrow x^8=xy^8
   \Longrightarrow x^8+xy^8=0\pmod{t^4+t+1}.

Đẳng thức này đúng cả khi :math:`x=0`; đổi vai trò :math:`x,y` cũng cho

.. math::

   y^8+yx^8=0\pmod{t^4+t+1}.

So sánh bốn hệ số theo cơ sở :math:`1,t,t^2,t^3` trong mỗi đẳng thức thu được
tám phương trình bậc hai. Ba phương trình thuần nhất còn lại đến từ ba hệ số
bằng không của :math:`xy=1`. Cuối cùng, từ :eq:`eq-small-aes-affine` và
:math:`a^4=1\pmod{t^4+1}`, thay

.. math::

   y=a^3(z+b)\pmod{t^4+1}

vào các phương trình trên. Kết quả là hệ
:math:`F(x_0,\ldots,x_3,z_0,\ldots,z_3)=0` gồm
:math:`3+4+4=11` phương trình bậc hai mô tả chính xác quan hệ vào--ra của
S-box. Phương pháp tương tự cho S-box 8 bit của AES tạo hệ gồm
:math:`7+8+8=23` phương trình :cite:`Cui14`.

Để mô hình hóa một vòng, áp dụng 11 phương trình này cho từng cặp nibble

.. math::

   (b^{(i)}_{4j},\ldots,b^{(i)}_{4j+3}),\qquad
   (c^{(i)}_{4j},\ldots,c^{(i)}_{4j+3}),quad 0\leqslant j\leqslant3,

rồi thay mỗi :math:`c^{(i)}_j` bằng biểu thức tuyến tính trong
:eq:`eq-small-aes-sbox-output`. Sau một vòng, mỗi bit đầu ra phụ thuộc vào
tám bit đầu vào; sau hai vòng, mỗi bit đầu ra phụ thuộc vào toàn bộ 16 bit.

Quá trình sinh khóa thu nhỏ
^^^^^^^^^^^^^^^^^^^^^^

Viết khóa vòng dưới dạng bốn nibble
:math:`k_i=k_{i,0}\Vert k_{i,1}\Vert k_{i,2}\Vert k_{i,3}`. Với
:math:`q\in\{0,1\}`, lịch sinh khóa là :cite:`10.1007/11502760_10`

.. math::

   \begin{pmatrix}k_{i,2q}\\k_{i,2q+1}\end{pmatrix}
   =\begin{pmatrix}S(k_{i-1,3})\\S(k_{i-1,2})\end{pmatrix}
   +\begin{pmatrix}\kappa_i\\0\end{pmatrix}
   +\sum_{j=0}^{q}\begin{pmatrix}k_{i-1,2j}\\k_{i-1,2j+1}\end{pmatrix},

trong đó :math:`\kappa_i` là hằng số vòng. Với một vòng và
:math:`\kappa_1=1`, công thức trở thành

.. math::

   \begin{aligned}
   k_{1,0}&=S(k_{0,3})+1+k_{0,0},&
   k_{1,1}&=S(k_{0,2})+k_{0,1},\\
   k_{1,2}&=k_{1,0}+k_{0,2},&
   k_{1,3}&=k_{1,1}+k_{0,3}.
   \end{aligned}

Hai phương trình đầu được mô hình hóa bằng hai bản sao của hệ 11 phương
trình S-box; hai phương trình sau là tuyến tính. Nếu tính cơ sở Gröbner với
thứ tự lex

.. math::

   k_{16}>k_{17}>\cdots>k_{31}>k_0>k_1>\cdots>k_{15},

ta thu được các đa thức

.. math::
   :label: eq-small-aes-key-elimination

   k_{i+16}+F_i(k_0,\ldots,k_{15}),\qquad0\leqslant i\leqslant15.

Do đó mọi bit của :math:`k_1` có thể được thay bằng đa thức theo 16 bit của
khóa ban đầu :math:`k_0`.

Hệ phương trình cho một vòng hoàn chỉnh
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Với một cặp bản rõ--bản mã đã biết :math:`(p,c)`, phương trình vòng là

.. math::

   (M_{\mathrm{MC}}M_{\mathrm{SR}})^{-1}(c^{\top}+k_1^{\top})
   =\mathcal S(p+k_0)^{\top}.

Thay 16 bit của :math:`k_1` bằng các đa thức :math:`F_i` trong
:eq:`eq-small-aes-key-elimination`, rồi áp dụng hệ 11 phương trình cho mỗi
trong bốn S-box, ta thu được **44 phương trình bậc hai theo 16 biến khóa**.
Đây là hệ đa thức biểu diễn đầy đủ một vòng
:math:`\operatorname{SR}(1,2,2,4)` và có thể được giải bằng cơ sở Gröbner.
