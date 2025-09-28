Mô hình Feistel
===============

Mô tả mô hình Feistel
---------------------

Trong mô hình Feistel, mỗi block đầu vào được chia thành hai nửa trái phải có số bit bằng nhau.

Một cách hình thức, giả sử plaintext đầu vào là :math:`P` có :math:`2n` bit, thì :math:`P` được chia thành nửa trái :math:`L_0` và :math:`R_0`, mỗi nửa có :math:`n` bits.

Mỗi hệ mã Feistel có một hàm :math:`F(R_{i-1}, K_i)` nhận đầu vào là nửa phải ở vòng thứ :math:`(i-1)` và khóa :math:`K_i` ở vòng thứ :math:`i`. Hàm :math:`F` được gọi là **round function**.

Ở mỗi vòng :math:`i = 1, 2, \ldots`, hai nửa trái phải mới sẽ được tính theo công thức

.. math:: L_i = R_{i-1}, \quad R_i = L_{i-1} \oplus F(R_{i-1}, K_i),

trong đó:

- :math:`L_{i-1}` và :math:`R_{i-1}` là nửa trái và nửa phải ở vòng thứ :math:`(i-1)`;
- :math:`L_i` và :math:`R_i` là nửa trái và nửa phải ở vòng thứ :math:`i`;
- :math:`K_i` là khóa con được dùng ở vòng :math:`i`;
- :math:`F` là round function.

.. figure:: ../../figures/feistel/feistel.*
    
    Mô hình Feistel

Nếu thuật toán kết thúc sau :math:`r` vòng (với :math:`r` khóa con) thì ciphertext tương ứng sẽ là :math:`C = L_r \Vert R_r`.

Tính chất của mô hình Feistel
-----------------------------

Mô hình Feistel không đòi hỏi round function :math:`F` phải khả nghịch. Giả sử ciphertext là :math:`C = L_r \Vert R_r`. Khi đó dựa trên công thức mã hóa ở trên thì có thể dễ dàng suy ra công thức giải mã là

.. math:: R_{i - 1} = L_i, \quad L_{i-1} = R_i \oplus F(R_i, K_i),

với :math:`i = r-1, \ldots, 0`.

Plaintext nhận được sẽ là :math:`P = L_0 \Vert R_0`.

Một số thuật toán sử dụng mô hình Feistel
-----------------------------------------

Mô hình Feistel chuẩn
^^^^^^^^^^^^^^^^^^^^^

Mô hình Feistel chuẩn là mô hình ở trên. Các thuật toán sử dụng mô hình Feistel chuẩn có thể kể đến là: DES, Magma (tiêu chuẩn mã hóa Nga, định nghĩa trong GOST 34.12.2015, version :math:`64` bit), CAST-128 (tiêu chuẩn mã hóa Canada).

Mô hình Feistel tổng quát
^^^^^^^^^^^^^^^^^^^^^^^^^

Mô hình Feistel tổng quát (generalized Feistel model) có nhiều biến thể. Trong đó khối đầu vào không được chia thành hai nửa trái phải mà có thể được chia thành bốn phần :math:`P = X_0 \Vert X_1 \Vert X_2 \Vert X_3`, mỗi phần có số bit bằng nhau.

Sau đó, ở mỗi vòng, bốn phần ở vòng :math:`i` nhận được từ bốn phần ở vòng :math:`(i - 1)`, thông thường là từ việc giữ lại ba phần (nhưng ở vị trí khác) và XOR phần còn lại với một round function lấy tham số là ba phần kia cùng với khóa con ở vòng :math:`i`. Ví dụ

.. math::
    
    & X^{(i)}_0 = X^{(i-1)}_1, \\
    & X^{(i)}_1 = X^{(i-1)}_2, \\
    & X^{(i)}_2 = X^{(i-1)}_3, \\
    & X^{(i)}_3 = X^{(i-1)}_0 \oplus F(X^{(i-1)}_1, X^{(i-1)}_2, X^{(i-1)}_3, K_i),
    

trong đó:

- :math:`X^{(i)}_0`, :math:`X^{(i)}_1`, :math:`X^{(i)}_2`, :math:`X^{(i)}_3` là bốn phần ở vòng thứ :math:`i`;
- :math:`X^{(i-1)}_0`, :math:`X^{(i-1)}_1`, :math:`X^{(i-1)}_2`, :math:`X^{(i-1)}_3` là bốn phần ở vòng thứ :math:`(i-1)`;
- :math:`K_i` là khóa con ở vòng thứ :math:`i`;
- :math:`F` là round function nhận bốn đầu vào gồm ba phần ở vòng thứ :math:`(i-1)` và khóa con ở vòng thứ :math:`i`.

Lưu ý rằng trên đây chỉ trình bày một dạng biến thể của mô hình Feistel tổng quát.

Một số thuật toán sử dụng mô hình Feistel tổng quát: SM4 (tiêu chuẩn mã hóa mạng không dây của Trung Quốc).
