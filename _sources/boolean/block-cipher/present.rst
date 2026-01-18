PRESENT
=======

PRESENT là mã khối lightweight, nghĩa là được thiết kế cho các thiết bị có bộ xử lý nhỏ gọn, tập trung vào độ dài khóa không quá lớn (tối đa :math:`128` bits) nhưng vẫn đảm bảo an toàn và có thể thực hiện trên các thiết bị có bộ xử lý :math:`8` bit (ví dụ embedded systems).

Phần này mình tham khảo trong tài liệu về xây dựng PRESENT cipher ở :cite:`ches-2007-848`.

Mô tả thuật toán
----------------

PRESENT gồm :math:`32` động tác ``addRoundKey``, duyệt qua :math:`31` vòng.

.. prf:algorithm:: 
    :label: algo-PRESENT

    1. generateRoundKeys()
    2. for :math:`i = 1` to :math:`31` do

       1. addRoundKey(STATE, :math:`K_i`)
       2. sBoxLayer(STATE)
       3. pLayer(STATE)
    
    3. end for
    4. addRoundKey(STATE, :math:`K_{32})`


PRESENT sử dụng mạng SP để mã hóa. Kích thước khối là :math:`64` bits. PRESENT hỗ trợ hai kích thước khóa là :math:`80` và :math:`128` bits. Trong :cite:`ches-2007-848`, các tác giả khuyến nghị sử dụng khóa :math:`80` bits cho phù hợp với cài đặt phần cứng. Điều này dễ hiểu vì kích thước khóa lớn thì vấn đề lưu trữ trên bộ nhớ và tính toán sẽ chiếm nhiều không gian, ngoài ra tốc độ tính toán sẽ bị giảm vì khả năng của CPU không lớn.

addRoundKey
^^^^^^^^^^^

Giả sử round key ở vòng thứ :math:`i` là

.. math:: K_i = \kappa_{63}^i \ldots \kappa_0^i,

với :math:`1 \leqslant i \leqslant 32`, cùng với STATE hiện tại là :math:`b_{63} \ldots b_0`, khi đó ``addRoundKey`` chính là phép XOR bit

.. math:: b_j \to b_j \kappa_{j}^i

với :math:`0 \leqslant j \leqslant 63`.

sBoxLayer
^^^^^^^^^

PRESENT sử dụng S-box biến đổi :math:`4` bits thành :math:`4` bits, nghĩa là :math:`S: \mathbb{F}_2^4 \to \mathbb{F}_2^4`. S-box được cho bởi bảng sau.

+--------------+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
| :math:`x`    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
+==============+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+===+
| :math:`S[x]` | C | 5 | 6 | B | 9 | 0 | A | D | 3 | E | F | 8 | 4 | 7 | 1 | 2 |
+--------------+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

STATE được biểu diễn ở dạng :math:`b_{63} \ldots b_0` sẽ được chia thành :math:`16` đoạn, mỗi đoạn :math:`4` bits và từng đoạn sẽ đi qua S-box. Sau đó các đoạn được nối lại theo thứ tự thành khối có :math:`64` bits mới.

pLayer
^^^^^^

Hoán vị bit (bit permutation) được thực hiện theo bảng sau với bit thứ :math:`i` của STATE sẽ trở thành bit thứ :math:`P(i)` của kết quả.

+--------------+---+----+----+----+---+----+----+----+---+----+----+----+----+----+----+----+
| :math:`i`    | 0 | 1  | 2  | 3  | 4 | 5  | 6  | 7  | 8 | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
+==============+===+====+====+====+===+====+====+====+===+====+====+====+====+====+====+====+
| :math:`P(i)` | 0 | 16 | 32 | 48 | 1 | 17 | 33 | 49 | 2 | 18 | 34 | 50 | 3  | 19 | 35 | 51 |
+--------------+---+----+----+----+---+----+----+----+---+----+----+----+----+----+----+----+

+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
| :math:`i`    | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
+==============+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+
| :math:`P(i)` | 4  | 20 | 36 | 52 | 5  | 21 | 37 | 53 | 6  | 22 | 38 | 54 | 7  | 23 | 39 | 55 |
+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+

+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
| :math:`i`    | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
+==============+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+
| :math:`P(i)` | 8  | 24 | 40 | 56 | 9  | 25 | 41 | 57 | 10 | 26 | 42 | 58 | 11 | 27 | 43 | 59 |
+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+

+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
| :math:`i`    | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |
+==============+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+
| :math:`P(i)` | 12 | 28 | 44 | 60 | 13 | 29 | 45 | 61 | 14 | 30 | 46 | 62 | 15 | 31 | 47 | 63 |
+--------------+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+

Thực ra, việc hoán vị bit tương ứng với một phép nhân ma trận. Ma trận này có tính chất là trên mỗi hàng và mỗi cột có duy nhất một phần tử :math:`1`, các phần tử còn lại bằng :math:`0`. Ví dụ với :math:`4` bit,

.. math:: 

    \begin{pmatrix}
        0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0
    \end{pmatrix} \begin{pmatrix}
        b_3 \\ b_2 \\ b_1 \\ b_0
    \end{pmatrix} = \begin{pmatrix}
        b_2 \\ b_3 \\ b_0 \\ b_1
    \end{pmatrix}.

Phép nhân ma trận tương ứng với bảng hoán vị

+--------------+---+---+---+---+
| :math:`i`    | 0 | 1 | 2 | 3 |
+==============+===+===+===+===+
| :math:`P(i)` | 1 | 0 | 3 | 2 |
+--------------+---+---+---+---+

key schedule
^^^^^^^^^^^^

Ở phần này chúng ta xem xét phiên bản khóa :math:`80` bits của PRESENT.

Giả sử khóa đầu vào được lưu trong thanh ghi :math:`K` và được biểu diễn ở dạng :math:`k_{79} k_{78} \ldots k_0`.

Tại vòng thứ :math:`i`, khóa :math:`K_i` là :math:`64` bits ngoài cùng của :math:`K`, nghĩa là ở vòng thứ :math:`i` ta có

.. math:: K_i = \kappa_{63} \ldots \kappa_0 = k_{79} k_{78} \ldots k_{16}.

Sau khi trích xuất round key :math:`K_i`, thanh ghi :math:`K` sẽ được cập nhật theo các bước sau

1. :math:`[k_{79} k_{78} \ldots k_1 k_0] = [k_{18} k_{17} \ldots k_{20} k_{19}]` - dịch vòng trái :math:`61` vị trí.
2. :math:`[k_{79} k_{78} k_{77} k_{76}] = S[k_{79} k_{78} k_{77} k_{76}]` - dùng S-box biến đổi :math:`4` bits thành :math:`4` bits.
3. Gọi :math:`\mathtt{round\_counter}` là :math:`i` ở dạng :math:`5` bits, khi đó

.. math:: [k_{19} k_{18} k_{17} k_{16} k_{15}] = [k_{19} k_{18} k_{17} k_{16} k_{15}] \oplus \mathtt{round\_counter}.
