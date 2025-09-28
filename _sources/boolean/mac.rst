Message Authentication Code
***************************

Điểm yếu của các hệ mật mã đối xứng là ở tính không từ chối. Bên nhận ciphertext không có cách nào xác minh được bên gửi, cũng như bên gửi hoàn toàn có thể chối bỏ rằng mình đã gửi ciphertext đi.

Để giải quyết vấn đề này người ta đã nghĩ ra một phương án là **Message Authentication Code** (viết tắt là **MAC**, tiếng Nga là **имитовставка**). Một số tài liệu tiếng Việt mình đọc thì MAC được dịch là *mã chứng thực thông điệp*.

Khi đó, MAC gồm ba thành phần:

1. Thuật toán tạo khóa bí mật :math:`K`.
2. Thuật toán tạo ra tag :math:`T` là thông tin chứng thực từ khóa bí mật :math:`K` và thông điệp :math:`M`, nói cách khác là :math:`T = \mathsf{MAC}(K, M)`.
3. Thuật toán kiểm tra: với :math:`T`, :math:`K` và :math:`M`, thuật toán trả về *chấp nhận* hoặc *bác bỏ*. Bên nhận sẽ tính toán :math:`T' = \mathsf{MAC}(K, M)` và so sánh với :math:`T`. Nếu :math:`T \equiv T'` thì chấp nhận thông tin không bị sửa đổi và được gửi từ một bên sở hữu khóa bí mật :math:`K`.

.. figure:: ../figures/mac/mac.*
    
    Sơ đồ tạo MAC

Nhìn chung, MAC giống với quy trình tạo chữ ký điện tử.

Hash-based Message Authentication Code (HMAC)
=============================================

HMAC là một cách tiếp cận để xây dựng MAC dựa trên hàm băm nên có tên gọi hash-based MAC.

.. figure:: ../figures/hmac/hmac.*

    Hash-based message authentication code

HMAC được định nghĩa trong RFC 2104 :cite:`rfc2104` bởi công thức

.. math:: \mathsf{HMAC}(K, M) = H\left(\left(K' \oplus opad\right) \Vert H\left(K' \oplus ipad\right) \Vert M\right),

trong đó:

- :math:`H` là một hàm băm mật mã;
- :math:`M` là thông điệp cần chứng thực;
- :math:`K` là khóa bí mật;
- :math:`K'` là khóa với độ dài cố định được tạo từ khóa bí mật :math:`K`;
- :math:`opad` là một dãy các byte ``0x5c``, viết tắt của outer padding;
- :math:`ipad` là một dãy các byte ``0x36``, viết tắt của inner padding.

Độ dài cố định (block-size) ở mô tả trên phụ thuộc vào hàm băm mật mã :math:`H`.

Mô hình HMAC cho phép chứng thực thông điệp nhưng không cho phép mã hóa (encrypt). Một ý tưởng cho việc này là chúng ta mã hóa trước rồi chứng thực bản mã nhận được. Đây là cách tiếp cận **Encrypt-then-MAC** và được ứng dụng khá rộng rãi, ví dụ như ở :cite:`rfc7366`. Chúng ta cũng có thể làm ngược lại, chứng thực bản rõ trước và sau đó mã hóa, gọi là **MAC-then-encrypt**. Tuy nhiên MAC-then-encrypt không được sử dụng nhiều.

Một ứng dụng tiêu biểu của Encrypt-then-MAC là cơ chế GCM (Galois/Counter Mode) được sử dụng rộng rãi khi đi kèm với thuật toán AES. Trước tiên chúng ta sẽ xem xét bài toán tổng quát hơn là Authentication Encryption (tạm dịch là *mã hóa có chứng thực*).

Authentication Encryption
=========================

Đầu tiên ta thống nhất các kí hiệu sau.

+---------------------------+---------------------------------------------------------------------------+
| Kí hiệu                   | Ý nghĩa                                                                   |
+===========================+===========================================================================+
| :math:`P`                 | bản rõ (plaintext)                                                        |
+---------------------------+---------------------------------------------------------------------------+
| :math:`K`                 | khóa cho thuật toán mã hóa đối xứng                                       |
+---------------------------+---------------------------------------------------------------------------+
| :math:`K'`                | khóa dùng để tạo MAC                                                      |
+---------------------------+---------------------------------------------------------------------------+
| :math:`\mathsf{Enc}_K(P)` | hàm mã hóa đối xứng bản rõ :math:`P` với khóa bí mật :math:`K`            |
+---------------------------+---------------------------------------------------------------------------+
| :math:`C`                 | bản mã (ciphertext) khi mã hóa bản rõ :math:`P` với khóa bí mật :math:`K` |
+---------------------------+---------------------------------------------------------------------------+
|                           | :math:`C = \mathtt{Enc}_K(P)`                                             |
+---------------------------+---------------------------------------------------------------------------+
| :math:`A`                 | thông tin để chứng thực (Authentication Data)                             |
+---------------------------+---------------------------------------------------------------------------+

Authentication Encryption (AE)
------------------------------

**Authentication Encryption** (hay **AE**) có thể biểu diễn bởi hàm

.. math:: T = \mathsf{MAC}(K', C),

khi đó MAC được tạo bởi khóa :math:`K'`, bản mã :math:`C`.

Thông thường, :math:`K'` sẽ được sinh ra từ :math:`K` hoặc cả hai đều được sinh từ một mật khẩu (password) hoặc passphrase nào đó.

Authentication Encryption with Associated Data (AEAD)
-----------------------------------------------------

Tương tự với AE nhưng lúc này chúng ta thêm một đoạn thông tin gọi là **Associated Data** hoặc **Authentication Data**. Lúc này MAC sẽ được tính bởi công thức

.. math:: T = \mathsf{MAC}(K', C, A),

với :math:`A` là thông tin chứng thực (authentication data).

Hiện nay trong các giao thức mật mã thì AEAD là bắt buộc đi kèm với thuật toán mã hóa đối xứng.

Ở TLS v1.3 thì đối với thuật toán AES có hai phương án AEAD là **GCM** (Galois/Counter Mode) và **CCM** (CBC-MAC). Đối với các cipher suites sử dụng các thuật toán tiêu chuẩn GOST (Liên bang Nga) sử dụng phương án AEAD là **MGM** (Multilinear Galois Mode). Chúng ta cần lưu ý rằng các AEAD được định nghĩa trong các *khuyến nghị* (*recommendation*) chứ không phải trong các *tiêu chuẩn* :cite:`9256, 9171, R:1323565:1:026-2019`. Nói cách khác, khi phát triển sản phẩm mật mã thì đây không phải quy định bắt buộc nhưng về mặt an toàn thì chúng ta nên áp dụng vì những mode khác luôn có khuyết điểm (ECB, CBC, v.v.).

Phần sau mình sẽ trình bày cách tính MAC dựa trên GCM, CCM và MGM.

Các loại AEAD
=============

Sơ lược về mã hóa với bộ đếm (counter)
--------------------------------------

Cả ba phương án AEAD sau đây đều sử dụng CTR (Counter Mode) để mã hóa. Sau đó việc việc tính toán MAC được thực hiện theo những cách khác nhau.

Cơ chế mã hóa với bộ đếm như hình sau.

.. figure:: ../figures/CTR_encryption/CTR_encryption.*

    Mã hóa theo mode CTR

Bắt đầu với giá trị :math:`\mathrm{Counter}_1`, các counter sau đó được tạo ra khi tăng dần bộ đếm với hàm :math:`\mathsf{incr}` nào đó:

.. math:: \mathrm{Counter}_{i+1} = \mathsf{incr}(\mathrm{Counter}_i)

với :math:`i = 1, 2, \ldots`

Khi đó, nếu :math:`P_1`, :math:`P_2`, ..., :math:`P_n` là các khối bản rõ thì các khối bản mã tương ứng :math:`C_1`, :math:`C_2`, ..., :math:`C_n` được tính bởi

.. math:: C_i = P_i \oplus \mathsf{Enc}_K(\mathrm{Counter}_i).

Hàm :math:`\mathsf{incr}` là một hàm tăng nào đó, không nhất thiết là cộng :math:`1`.

Điều quan trọng khi chúng ta sử dụng CTR là không được sử dụng lại :math:`\mathrm{Counter}_1`, các bạn có thể tìm về lỗ hổng *reuse nonce*. Nếu sử dụng lại counter thì chúng ta sẽ bị tấn công dạng known-plaintext.

Galois/Counter Mode (GCM)
-------------------------

Đây là dạng AEAD được sử dụng rộng rãi nhất hiện nay (ít ra là mình thấy vậy :v).

GCM sử dụng CTR để mã hóa và sử dụng các phép tính trên trường Galois để tạo MAC nên có tên gọi là Galois/Counter Mode.

.. figure:: ../figures/GCM_encryption/GCM_encryption.*

Bắt đầu với :math:`\mathrm{Counter}_0`, hay còn gọi là **nonce**, các giá trị bộ đếm tiếp theo được tính bởi việc tăng giá trị trước đó bởi hàm :math:`\mathsf{incr}`. Việc mã hóa sử dụng CTR giống như đã trình bày ở trên.

Để tính MAC, giả sử chúng ta có :math:`m` khối associated data là :math:`A_1`, :math:`A_2`, ..., :math:`A_m` và :math:`n` khối bản mã :math:`C_1`, :math:`C_2`, ..., :math:`C_n`. Khi đó các khối :math:`A_i` và :math:`C_j` có :math:`128` bit được biểu diễn thành các đa thức trong :math:`\mathrm{GF}(2^{128})` với đa thức tối giản là :math:`x^{128} + x^7 + x^2 + x + 1`.

Đặt

.. math:: A = A_1 \Vert A_2 \Vert \cdots \Vert A_m, \quad C = C_1 \Vert C_2 \Vert \cdots \Vert C_n.

Đặt :math:`H = \mathsf{Enc}_K(0^{128})`. Đây là phần tử trường Galois dùng để tạo MAC nên có thể nói :math:`H` chính là :math:`K'` ở phần mô tả MAC bên trên.

MAC :math:`T` sẽ được tính bởi công thức

.. math::
    
    T & = A_1 H^{n+m+2} \oplus A_2 H^{n+m+1} \oplus \cdots A_m H^{n+3} \\
    & \oplus C_1 H^{n+2} \oplus C_2 H^{n+1} \oplus \cdots \oplus C_n H^2 \\
    & \oplus L H \oplus \mathsf{Enc}_K(\mathrm{Counter}_0),

với :math:`L = \mathsf{len}(A) \Vert \mathsf{len}(C)`, nghĩa là độ dài cả đoạn :math:`A` là :math:`\mathsf{len}(A)` sẽ được biểu diễn bằng dãy :math:`64` bit và tương tự, độ dài cả đoạn :math:`C` là :math:`\mathsf{len}(C)` sẽ được biểu diễn bằng dãy :math:`64` bit. Khi nối hai đoạn đó lại ta có khối :math:`L` có :math:`128` bit.

Ở hình minh họa ở trên thì :math:`m = 1` và :math:`n = 2` (có một khối AD và hai khối bản mã).

CBC-MAC
-------

.. figure:: ../figures/CCM_encryption/CCM_encryption.*

    Mã hóa theo CCM

Việc mã hóa cũng sử dụng bộ đếm CTR, ở đây là :math:`\mathrm{ctr} + i` với :math:`i = 1, 2, \ldots` còn :math:`\mathrm{ctr}` thì dùng để tính MAC sau.

Tương tự, ta giả sử có :math:`m` khối AD và :math:`n` khối bản mã. Khi đó với một :math:`\mathrm{IV}` (có công thức tạo nhưng mình không nói ở đây) thì đầu tiên ta đặt :math:`B_0 = \mathsf{Enc}_K(\mathrm{IV})`, ta tính

.. math:: B_i = \mathsf{Enc}_K(A_i \oplus B_{i-1})

với :math:`i = 1, 2, \ldots, m`. Phần này là CBC dành cho AD.

Ta tiếp tục tính CBC cho các bản rõ :math:`P_1`, :math:`P_2`, ..., :math:`P_n` bằng

.. math:: B_{i+m} = \mathsf{Enc}_K(P_i \oplus B_{i+m-1})

với :math:`i = 1, 2, \ldots, n`.

Tag :math:`T` sẽ là :math:`B_{n+m}` và MAC là :math:`64` bit cao nhất (MSB) của :math:`\mathsf{Enc}_K(\mathrm{ctr}) \oplus T`, nghĩa là

.. math:: U = \mathsf{MSB}_{64}(\mathsf{Enc}_K(\mathrm{ctr}) \oplus T).

Ở đây MAC được tạo bởi CBC nên có tên gọi là CBC-MAC.

Multilinear Galois Mode (MGM)
-----------------------------

Đây là AEAD sử dụng cho các GOST cipher suite cho TLS v1.3 và là mở rộng của GCM. Ở đây thay vì chúng ta chỉ nhân với một phần tử :math:`H` như GCM mà là một dãy :math:`H_1`, :math:`H_2`, ... nên có tên gọi là multilinear Galois.

.. figure:: ../figures/MGM_encryption/MGM_encryption-1.*

    Mã hóa theo MGM

Đối với MGM chúng ta cần một đoạn :math:`127` bit gọi là :math:`\mathrm{nonce}` và sẽ sử dụng để mã hóa lẫn tính MAC.

Để mã hóa, đặt :math:`Y_1 = \mathsf{Enc}_K(0 \Vert \mathrm{nonce})`. Đây là điểm khởi đầu của bộ đếm. Khi đó các phần tử bộ đếm được được sinh bởi quy tắc

.. math:: Y_{i+1} = \mathsf{incr}_r(Y_i), \quad i = 1, 2, \ldots, n.

Bản mã sẽ là

.. math:: C_i = \mathsf{Enc}_K(Y_i) \oplus P_i, \quad i = 1, 2, \ldots, n.

Tiếp theo, đặt :math:`Z_1 = \mathsf{Enc}_K(1 \Vert \mathrm{nonce})` và

.. math:: Z_{i+1} = \mathsf{incr}_l(Z_i), \quad i = 1, 2, \ldots, n+m+1.

.. _MGM:

.. figure:: ../figures/MGM_encryption/MGM_encryption-2.*
    
    Quá trình sinh dãy :math:`(H_i)`

Chúng ta tính một dãy :math:`H_1`, :math:`H_2`, ... theo quy tắc sau (:numref:`MGM`)

.. math:: H_i = \mathsf{Enc}_K(Z_i), \quad i = 1, 2, \ldots, n + m + 1.

Dãy :math:`H_i` sẽ được dùng dùng để tính MAC. Gọi

.. math:: \mathcal{T} = A_1 H_1 \oplus A_2 H_2 \oplus \cdots \oplus A_m H_m \oplus C_1 H_{m+1} \oplus \cdots C_n H_{n+m} \oplus L H_{n+m+1},

với :math:`L = \mathsf{len}(A) \Vert \mathsf{len}(C)` như GCM. Một điều lưu ý ở đây là MGM có thể sử dụng cho thuật toán với độ dài khối là :math:`64` bit (Magma) và :math:`128` bit (Kuznyechik). Khi đó, nếu độ dài khối là :math:`64` bit thì đa thức tối giản là :math:`x^{64} + x^4 + x^3 + x + 1` và nếu độ dài khối là :math:`128` bit thì đa thức tối giản là :math:`x^{128} + x^7 + x^2 + x + 1`.

Khi đó, MAC là :math:`64` bit cao (MSB) của kết quả :math:`\mathsf{Enc}_K(\mathcal{T})`, nghĩa là

.. math:: T = \mathsf{MSB}_{64}(\mathsf{Enc}_K(\mathcal{T})).

Hàm :math:`\mathsf{incr}_l` và :math:`\mathsf{incr}_r` hoạt động theo nguyên tắc, giả sử chúng ta có một số :math:`128` bit là :math:`L \Vert R`, trong đó :math:`L` và :math:`R` đều có :math:`64` bit. Khi đó

- :math:`\mathsf{incr}_l(L \Vert R) = L' \Vert R` với :math:`L' = (L + 1) \bmod 2^{64}`;
- :math:`\mathsf{incr}_r(L \Vert R) = L \Vert R'` với :math:`R' = (R + 1) \bmod 2^{64}`.

Ở đây :math:`L'` (hoặc :math:`R'`) được biểu diễn bởi dãy :math:`64` bit và gắn vào :math:`R` (hoặc :math:`L`) ban đầu để có một dãy :math:`128` bit.
