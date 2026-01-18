Kuznyechik
==========

Kuznyechik là một thuật toán mã hóa khối, đối xứng như AES. Kuznyechik tiếng Nga là Кузнечик, có nghĩa là châu chấu. Tuy nhiên trong văn bản quốc tế thì chúng ta giữ nguyên tên gọi
là hệ mã Kuznyechik.

Mã khối Kuznyechik biến đổi trên khối :math:`128` bit, độ dài khóa là :math:`256` bit, biến đổi trên :math:`9` vòng. Kuznyechik sử dụng mô hình SPN tương tự như AES, trở thành chuẩn mã hóa của Nga và được định nghĩa trong GOST R 34.12-2015.

Một điểm đặc biệt là quá trình biến đổi qua các vòng sử dụng mạng SPN, tuy nhiên thuật toán sinh khóa con cho các vòng sử dụng mô hình Feistel.

Phần này tham khảo chính từ :cite:`Losi2018`.

Mã hóa
------

Gọi :math:`k_i` là khóa con của vòng thứ :math:`i`, :math:`i = 0, 1, \ldots, 9`. Ta có các động tác biến đổi sau:

Phép biến đổi :math:`X`
^^^^^^^^^^^^^^^^^^^^^^^

Hàm :math:`X: \mathbb{F}_2^{128} \to \mathbb{F}_2^{128}` biến đổi trên block :math:`128` bits.

Ta chia block đầu vào thành :math:`16` cụm :math:`8` bit, kí hiệu

.. math:: 
    a = a_0 \Vert a_1 \Vert \ldots \Vert a_{14} \Vert a_{15}

với ký tự :math:`\Vert` chỉ việc nối các chuỗi bit (concatenate). Tương tự :math:`k_i` cũng được chia thành :math:`16` cụm :math:`8` bits. Khi đó, 

.. math:: 
    :label: kuz:1
    
    X(k_i, a) = k_{i, 0} \oplus a_0 \Vert 
    k_{i, 1} \oplus a_1 \Vert \ldots \Vert k_{i, 14} \oplus a_{14}
    \Vert k_{i, 15} \oplus a_{15}.

Nói cách khác, chúng ta xor :math:`128` bit của khối đầu vào và :math:`128` bit của khóa con :math:`k_i`.

Phép biến đổi :math:`S`
^^^^^^^^^^^^^^^^^^^^^^^^

Hàm :math:`S: \mathbb{F}_2^{128} \to \mathbb{F}_2^{128}`.

Block đầu vào tiếp tục được chia thành :math:`16` cụm :math:`8` bits. Mỗi cụm sẽ đi qua một bảng tra cứu SBox (gọi là bảng :math:`\pi`). Sau đó ta nối các kết quả với nhau.

.. math:: 
    :label: kuz:2

    S(a) = \pi(a_0) \Vert \pi(a_1) \Vert \ldots \Vert \pi(a_{14})
    \Vert \pi(a_{15}).

Bảng :math:`\pi` được định nghĩa sẵn và không tuyến tính, nên đây là bước không tuyến tính của thuật toán.

Phép biến đổi :math:`L`
^^^^^^^^^^^^^^^^^^^^^^^

Hàm :math:`L: \mathbb{F}_2^{128} \to \mathbb{F}_2^{128}`.

Block đầu vào vẫn được chia thành :math:`16` cụm :math:`8` bit. Tuy nhiên ở đây mỗi cụm :math:`8` bit biểu diễn một đa thức trong trường :math:`\mathrm{GF}(2^8)` với đa thức tối giản là :math:`g(x) = x^8 + x^7 + x^6 + x + 1`. Những phép tính cộng và nhân sau đây cũng được thực hiện trên trường :math:`\mathrm{GF}(2^8)` này.

.. math:: 
    :label: kuz:3

    
    \lambda(a) & = 148 a_{15} + 32 a_{14} + 133 a_{13} + 16 a_{12} \\
            & + 194 a_{11} + 192 a_{10} + a_9 + 251 a_8 \\
            & + a_7 + 192 a_6 + 194 a_5 + 16 a_4 \\
            & + 133 a_3 + 32 a_2 + 148 a_1 + a_0.
    

Tiếp theo, ta định nghĩa hàm :math:`\Lambda: \mathbb{F}_2^{128} \to \mathbb{F}_2^{128}` như sau

.. math:: 
    a = a_0 \Vert a_1 \Vert \ldots \Vert a_{14} \Vert a_{15}
    \to a_1 \Vert a_2 \Vert \ldots \Vert a_{15} \Vert \lambda(a)
    = \Lambda(a).

.. _kuzfic-1:

.. figure:: ../../figures/kuznyechik/funcLambda.*

    Hàm :math:`\lambda`

Lưu ý rằng sau khi tính toán trên hàm :math:`\lambda`, đa thức trên :math:`\mathrm{GF}(2^8)` được chuyển trở lại thành cụm :math:`8` bit sau đó mới nối vào dãy :math:`a_1`, :math:`a_2`, ..., :math:`a_{15}` như mô tả ở :numref:`kuzfic-1`.

Cuối cùng, hàm :math:`L` ban đầu là thực hiện hàm :math:`\Lambda` :math:`16` lần.

.. math:: 
    L(a) = \underbrace{\Lambda(\ldots\Lambda(a)\ldots)}_{\text{16 lần}}.

Như vậy, phép biến đổi trên vòng thứ :math:`i` với khóa con :math:`k_i` là

.. math:: 
    :label: kuz:4

    R(k_i, a) = L(S(X(a)))

với :math:`i = 0, 1, \ldots, 8`.

Ở vòng thứ :math:`10` ta XOR với khóa con :math:`k_9` nữa: :math:`X(k_9, a)`.

Thuật toán sinh khóa con
------------------------

Để sinh khóa con cho :math:`10` lần XOR, thuật toán Kuznyechik dùng mô hình Feistel. Đầu tiên ta định nghĩa hàm :math:`F(c, a)`. Với :math:`c` bất kì thuộc :math:`\mathbb{F}_2^{128}` và :math:`a = a_0 \Vert a_1` thuộc :math:`\mathbb{F}_2^{256}`. Hàm :math:`F(c, a)` biến phần tử thuộc :math:`\mathbb{F}_2^{128} \times \mathbb{F}_2^{256}` thành phần tử thuộc :math:`\mathbb{F}_2^{256}` bằng đẳng thức

.. math:: F(c, a) = a_1 \Vert a_0 \oplus R(c, a_1)

với hàm :math:`R` được định nghĩa ở phương trình :eq:`kuz:4`.

.. _kuzfic-2:

.. figure:: ../../figures/kuznyechik/funcF.*

    Biến đổi từ khóa :math:`k_0 \Vert k_1` thành :math:`k_2 \Vert k_3`

Với khóa đầu vào là :math:`k \in \mathbb{F}_2^{256}`, mình kí hiệu ở dạng ghép hai chuỗi :math:`128` bits :math:`k = k_0 \Vert k_1` với :math:`k_0, k_1 \in \mathbb{F}_2^{128}` là những khóa con mở đầu. Khi đó các khóa con cho :math:`10` phép XOR là :math:`k_0`, :math:`k_1`, ..., :math:`k_9`.

Thuật toán sinh khóa con được sử dụng như sau

.. math:: k_{2i+2} \Vert k_{2i+3} = F(c_{8i+7}, \ldots, F(c_{8i}, k_{2i} \Vert k_{2i+1})),

với :math:`i = 0, 1, 2, 3`. Thuật toán có thể mô tả ở :numref:`kuzfic-2`. 

Theo đó, các số :math:`c_0`, :math:`c_1`, ..., :math:`c_7` được sử dụng để sinh khóa :math:`k_2 \Vert k_3` từ :math:`k_0 \Vert k_1`. Tương tự, :math:`c_8`, :math:`c_9`, ..., :math:`c_{15}` được dùng để sinh khóa :math:`k_4 \Vert k_5` từ khóa :math:`k_2 \Vert k_3`. Các số :math:`c_0`, :math:`c_1`, ..., :math:`c_{31}` được định nghĩa trong tiêu chuẩn.

So sánh Kuznyechik với AES
--------------------------

Điểm giống nhau là cả hai thuật toán đều có phần tuyến tính và phần không tuyến tính. Về phần tuyến tính, đối với AES là các động tác Shift Rows, Mix Columns và Add Round Key, còn đối với Kuznyechik là hàm :math:`X` và :math:`L` bên trên. Về phần không tuyến tính đều là việc sử dụng một bảng tra cứu SBox của riêng thuật toán đó.

Điểm khác nhau đầu tiên là cách xây dựng ma trận tính toán. Nếu ta xem xét Shift Rows và Mix Columns dưới dạng phép nhân ma trận trên :math:`\mathrm{GF}(2^8)` thì ta thấy rằng ma trận chứa nhiều số :math:`0` nhất có thể. Điều này giúp tăng tốc độ tính toán. Về phần Kuznyechik, phép tính ở hàm :math:`\lambda` cũng thực hiện trên :math:`\mathrm{GF}(2^8)` nhưng không chứa bất kì số :math:`0` nào. Điều này làm tăng độ phức tạp tính toán nhưng cũng làm tăng tính an toàn.

Điểm khác nhau tiếp theo là việc sinh khóa con. AES sử dụng thuật toán sinh khóa con từng vòng từ toàn bộ :math:`256` bit ban đầu. Trong khi Kuznyechik sử dụng mô hình Feistel, theo đó với :math:`256` bit ban đầu được sử dụng cho hai vòng đầu, cứ mỗi hai khóa con sẽ sinh ra hai khóa con tiếp theo. Như vậy thuật toán sinh khóa con ít phức tạp hơn AES (Kuznyechik cần :math:`5` lần sinh khóa còn AES :math:`14` lần).
