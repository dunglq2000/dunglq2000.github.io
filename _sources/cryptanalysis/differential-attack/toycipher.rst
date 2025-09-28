Nhập môn phá mã vi sai
======================

Phần này mình tham khảo ở :cite:`TAK`. Bạn này viết khá nhiều bài nhập môn cryptanalysis trên block cipher nên rất tốt để tham khảo.

Differential (vi sai)
---------------------

.. prf:definition:: 
    :label: def-differential-attack
    
    Gọi :math:`\mathbb{F}_2^n` và :math:`\mathbb{F}_2^m` là hai không gian vector trên :math:`\mathbb{F}_2` với số chiều lần lượt là :math:`n` và :math:`m`. Gọi :math:`S` là ánh xạ từ :math:`\mathbb{F}_2^n` tới :math:`\mathbb{F}_2^m`. Với mỗi vector :math:`\bm{a}, \bm{b} \in \mathbb{F}_2^n`, ta nói **input differential** của :math:`S` là :math:`\delta = \bm{a} \oplus \bm{b}` và **output differential** của :math:`S` là :math:`\Delta = S(\bm{a}) \oplus S(\bm{b})`, trong đó :math:`\oplus` là phép XOR.

Trên thực tế, nếu trường được xét không phải :math:`\mathbb{F}_2` mà là một trường :math:`\mathbb{F}` bất kì thì input differential là :math:`\bm{b} - \bm{a}` và output differential là :math:`S(\bm{b}) - S(\bm{a})`. Trong mật mã chúng ta thường hay làm việc trên các không gian vector nhị phân nên phép trừ cũng chính là phép cộng (XOR) trên :math:`\mathbb{F}_2`.

Ánh xạ :math:`S` thường được sử dụng trong S-box là ánh xạ không tuyến tính, nghĩa là chúng ta không có tính chất :math:`S(\bm{a} \oplus \bm{b}) = S(\bm{a}) \oplus S(\bm{b})`. Tuy nhiên khi phân tích phân bố của :math:`\delta = \bm{a} \oplus \bm{b}` và :math:`\Delta = S(\bm{a}) \oplus S(\bm{b})` ta có thể trích ra các thông tin phục vụ tấn công. Do sử dụng các thông tin thống kê từ differential nên cách tấn công này được gọi là **differential attack** (hay **phá mã vi sai**).

Toy cipher
----------

1. Độ dài khối là :math:`4` bits.
2. Độ dài khóa là :math:`8` bits.

Mình gọi plaintext :math:`4` bits là :math:`P` và khóa :math:`8` bits là :math:`K = K_0 \Vert K_1`, trong đó :math:`K_0` và :math:`K_1` có :math:`4` bits và :math:`\Vert` là toán tử ghép chuỗi.

S-box của toy cipher là ánh xạ :math:`\mathbb{F}_2^4` tới :math:`\mathbb{F}_2^4` theo bảng sau.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: toycipher-sbox.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|

    .. include:: toycipher-sbox.rst.inc

Quá trình mã hóa mỗi khối plaintext :math:`4` bit :math:`P` thành ciphertext :math:`C` cũng :math:`4` bit là:

.. math:: 
    
    P \to P \oplus K_0 \to S(P \oplus K_0) \to S(P \oplus K_0) \oplus K_1 = C.

.. figure:: ../../figures/toycipher/toycipher.*

    Sơ đồ toy cipher

Phân tích vi sai
----------------

Tiếp theo chúng ta phân tích sự phân bố vi sai của S-box và biểu diễn thành bảng.

Trong bảng này, phần tử ở hàng :math:`i` và cột :math:`j` thể hiện số lượng cặp :math:`(\bm{a}, \bm{b}) \in \mathbb{F}_2^4 \times \mathbb{F}_2^4` sao cho :math:`\bm{a} \oplus \bm{b} = i` và :math:`S(\bm{a} \oplus \bm{b}) = j`.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: toycipher-ddt.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|

    .. include:: toycipher-ddt.rst.inc

Chúng ta quan tâm tới những hàng có nhiều giá trị :math:`0` và có một phần tử lớn nhất.

Cụ thể thì ở bảng này:

1. Nếu input differential là :math:`0` thì output differential là :math:`0` với xác suất :math:`16 / 16 = 1`.
2. Nếu input differential là :math:`1` thì output differential là :math:`13` với xác suất :math:`6 / 16`.
3. Nếu input differential là :math:`4` thì output differential là :math:`7` với xác suất :math:`6 / 16`.
4. Nếu input differential là :math:`8` thì output differential là :math:`5` với xác suất :math:`6 / 16`.
5. Nếu input differential là :math:`15` thì output differential là :math:`14` với xác suất :math:`6 / 16`.

Khi input differential là :math:`0`, nói cách khác là :math:`\bm{a} \oplus \bm{b} = 0`, tương đương với :math:`\bm{a} = \bm{b}`. Suy ra :math:`S(\bm{a}) = S(\bm{b})` nên output differential luôn là :math:`0 = S(\bm{a}) \oplus S(\bm{b})`. Tính chất này không hữu dụng.

Tiếp theo, giả sử ta mã hóa plaintext :math:`P_1` và nhận được ciphertext tương ứng là :math:`C_1`.

Tương tự ta mã hóa plaintext :math:`P_1'` và nhận được ciphertext tương ứng là :math:`C_1'`.

Theo cấu trúc cipher, :math:`P_1 \oplus K_0` và :math:`P_1' \oplus K_0` sẽ là các đầu vào của S-box. Do đó input differential là

.. math:: 
    
    \delta = (P_1 \oplus K_0) \oplus (P_1' \oplus K_0) = P_1 \oplus P_1'.

Điều này có nghĩa là input differential không phụ thuộc vào khóa và đây là tính chất quan trọng cho phá mã vi sai.

Theo quan sát số 2 về bảng phân bố vi sai ở trên, nếu input differential là :math:`1` thì output differential là :math:`13` với xác suất :math:`6 / 16`.

Giả sử ta chọn các plaintext :math:`P_1` và :math:`P_1'` sao cho :math:`P_1 \oplus P_1' = 1`.

Đặt :math:`I_1 = S(P_1 \oplus K_0)` và :math:`I_1' = S(P_1' \oplus K_0)`. Khi đó output differential của S-box là :math:`I_1 \oplus I_1'` và bằng :math:`13` với xác suất :math:`6 / 16`.

Để ý rằng :math:`C_1 = I_1 \oplus K_1` và :math:`C_1' = I_1' \oplus K_1` nên

.. math:: 
    
    C_1 \oplus C_1' = (I_1 \oplus K_1) \oplus (I_1' \oplus K_1) = I_1 \oplus I_1'

chính là output differential.

.. prf:remark:: 
    :label: rmk-differential-attack
    
    Nếu hai plaintext :math:`P_1` và :math:`P_1'` thỏa mãn :math:`P_1 \oplus P_1' = 1` thì hai ciphertext tương ứng :math:`C_1` và :math:`C_1'` sẽ cho giá trị :math:`C_1 \oplus C_1' = 13` với xác suất :math:`6 / 16`.

Nói cách khác, trung bình :math:`16` cặp plaintext mà :math:`P_1 \oplus P_1' = 16` thì sẽ có :math:`6` cặp cho kết quả :math:`C_1 \oplus C_1' = 13`.

Chosen plaintext
----------------

Dựa vào nhận xét trên, chiến thuật phá mã vi sai thực hiện như sau:

1. Chọn ngẫu nhiên plaintext :math:`P_1` và tính :math:`P_1' = P_1 \oplus 1`.
2. Mã hóa :math:`P_1` thu được :math:`C_1`, mã hóa :math:`P_1'` thu được :math:`C_1'`.
3. Nếu :math:`C_1 \oplus C_1' = 13` thì ta đã tìm được một cặp plaintext "tốt". Nếu không thì ta quay lại bước 1.

Xác suất :math:`6 / 16` đảm bảo rằng việc tìm kiếm sẽ không mất thời gian vì xác suất này khá lớn so với phần còn lại. :)))

Khi chúng ta đã tìm được cặp plaintext :math:`(P_1, P_1')` mà :math:`C_1 \oplus C_1' = 13`, chúng ta đã sẵn sàng khôi phục khóa con :math:`K_0`.

Đầu tiên, ta liệt kê tất cả cặp :math:`(\bm{a}, \bm{b}) \in \mathbb{F}_2^4 \times \mathbb{F}_2^4` sao cho :math:`\bm{a} \oplus \bm{b} = 1` và :math:`S(\bm{a}) \oplus S(\bm{b}) = 13`. Các cặp đó là

.. math:: 
    
    \mathcal{S}_0 = \{ (0, 1), (1, 0), (4, 5), (5, 4), (10, 11), (11, 10) \}.

Do phép XOR có tính đối xứng nên tập :math:`\mathcal{S}_0` cũng có những cặp đối xứng. Do đó ta chỉ cần lấy phần tử đầu của mỗi cặp và đặt

.. math:: 
    
    \mathcal{A} = \{ 0, 1, 4, 5, 10, 11 \}.

Mỗi phần tử :math:`\bm{a} \in \mathcal{A}` có tính chất :math:`S(\bm{a}) \oplus S(\bm{a} \oplus 1) = 13`.

Theo cấu trúc của toy cipher thì :math:`S(P_1 \oplus K_0) \oplus S(P_1' \oplus K_0) = 13`.

Như vậy :math:`\bm{a} = P_1 \oplus K_0` và :math:`\bm{a} \oplus 1 = P_1' \oplus K_0`. Từ đây ta tìm được các khả năng có thể có của khóa con :math:`K_0` ứng với mỗi giá trị :math:`\bm{a}`.

Với mỗi giá trị :math:`K_0`, ta tính được :math:`K_1 = C_1 \oplus S(P_1 \oplus K_0)`. Do :math:`\mathcal{A}` có :math:`6` phần tử nên ta sẽ có :math:`6` trường hợp khóa :math:`K = K_0 \Vert K_1`.

Để tìm ra khóa ta có thể thử mã hóa :math:`P_1` với từng khóa. Nếu kết quả là :math:`C_1` thì ta đã khôi phục đúng khóa.

Differential cryptanalysis ở toy cipher đã giảm số lượng khóa cần thử từ :math:`2^8 = 256` trường hợp xuống còn :math:`6` trường hợp.
