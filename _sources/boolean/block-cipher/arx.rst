ARX
===

ARX là cách gọi chung của những mô hình mã hóa khối chỉ sử dụng 
ba toán tử Addition (A, phép cộng modulo :math:`2^n`), Rotation 
(R, dịch vòng bit), và XOR (X, toán tử xor).

Giả sử ta có hai số nguyên :math:`a` và :math:`b` có :math:`n` bit.

Khi đó, nếu ta biểu diễn :math:`a \in \mathbb{Z}_{2^n}` dưới dạng nhị phân

.. math:: a = a_0 + 2 a_1 + 2^2 a_2 + \cdots + 2^{n-1} a_{n-1}

thì số nguyên :math:`a` cũng tương ứng với vector

.. math:: (a_0, a_1, a_2, \ldots, a_{n-1}) \in \mathbb{F}_2^n.

Phép cộng modulo :math:`2^n` giữa hai số nguyên :math:`a` và :math:`b` được định nghĩa là

.. math:: \boxed{a \boxplus b = (a + b) \bmod 2^n.}

Thông thường :math:`n` cố định và là lũy thừa của :math:`2`. Ví dụ trong hệ mã Magma thì :math:`n = 32`.

Với số nguyên dương :math:`r` cố định, phép dịch vòng trái và phải :math:`r` bit lần lượt là

.. math:: 
    :nowrap:

    \begin{equation*}
        \boxed{
            \begin{split}
            a \lll r & = (a_r, a_{r+1}, \ldots, a_{n-1}, a_0, a_1, \ldots, a_{r-1}), \\
            a \ggg r & = (a_{n-r}, a_{n-r+1}, \ldots, a_{n-1}, a_0, a_1, \ldots, a_{n-r-1}).
            \end{split}
        }
    \end{equation*}

Đối với phép XOR thì ta thực hiện phép cộng modulo :math:`2` theo từng vị trí trong vector

.. math:: \boxed{a \oplus b = (a_0 \oplus b_0, a_1 \oplus b_1, \ldots, a_{n-1} \oplus b_{n-1}).}

Dưới góc độ phá mã vi sai, phép dịch vòng bit và phép XOR là hai biến đổi tuyến tính, và phép cộng modulo :math:`2^n` là biến đổi không tuyến tính. Do đó phép cộng modulo :math:`2^n` có thể loại bỏ sự có mặt của S-box trong thuật toán, phù hợp với các thiết bị lightweight vì không phải dùng bộ nhớ để lưu trữ S-box và các chip hiện này đều hỗ trợ thực hiện các phép tính ARX.

Nhược điểm của ARX là có nhiều phần chưa được nghiên cứu rộng rãi. Nói cách khác, có nhiều điểm chưa rõ ràng đối với các toán tử ARX ở thời điểm hiện tại (2025).

Một số thuật toán lightweight sử dụng ARX: họ SPECK/SIMON.
