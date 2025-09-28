==========
Giới thiệu
==========

Zero Knowledge Proof (ZKP) là một protocol mật mã cho phép
một bên thuyết phục bên còn lại rằng họ sở hữu những thông
tin quan trọng mà không để lộ bất cứ gì về chính thông tin
quan trọng đó.

Khi đó, bên thuyết phục được gọi là **prover**, bên đưa ra
thử thách để prover chứng minh bản thân gọi là **challenger**
hoặc **verifier**.

.. admonition:: Tính chất của zero knowledge proof

    Mỗi protocol zero-knowledge phải đảm bảo ba tính chất sau:

    1. Completeness (tính đầy đủ): nếu mệnh đề đúng thì
       verifier có thể xác nhận và bị thuyết phục bởi prover.
    2. Soundness: nếu mệnh đề sai thì prover không thể thuyết
       phục verifier rằng nó đúng.
    3. Zero-knowlegde: verifier không biết gì về tính đúng sai
       của mệnh đề.

Lấy một ví dụ đơn giản để xem cách hoạt động của ZKP là protocol
QR [#first]_.

.. [#first] https://www.cs.princeton.edu/courses/archive/fall07/cos433/lec15.pdf

------------
Protocol PQ
------------

Mệnh đề cần kiểm tra: :math:`x` là một thặng dư chính phương modulo
:math:`n`. Prover muốn chứng minh với verifier rằng mình biết căn
bậc hai của :math:`x` trong modulo :math:`n`.

^^^^^^^^^^^^
Public input
^^^^^^^^^^^^

Số :math:`x` và modulo :math:`n`, với :math:`0 \leqslant x < n`.

^^^^^^^^^^^^^^^^^^^^^^^^
Quá trình tạo proof
^^^^^^^^^^^^^^^^^^^^^^^^

Quá trình tạo proof (thuyết phục) diễn ra như sau:

+----------------------------------+--------------------------+
| Prover (Alice)                   | Verifier (Bob)           |
+==================================+==========================+
| Public input: :math:`x \pmod n`  |                          |
+----------------------------------+--------------------------+
| Private input: :math:`w \pmod n` |                          |
| thỏa :math:`x = w^2 \pmod n`     |                          |
+----------------------------------+--------------------------+
| Chọn ngẫu nhiên số :math:`u`     |                          |
| từ :math:`\mathbb{Z}_n^*`        |                          |
+----------------------------------+--------------------------+
| Gửi Bob :math:`y = u^2 \pmod n`  |                          |
+----------------------------------+--------------------------+
|                                  | Chọn ngẫu nhiên          |
|                                  | :math:`b \in \{ 0, 1 \}` |
+----------------------------------+--------------------------+
|                                  | Gửi :math:`b` cho Alice  |
+----------------------------------+--------------------------+
| Gửi :math:`z = w^b \cdot u`      |                          |
| cho Bob                          |                          |
+----------------------------------+--------------------------+

^^^^^^^^^^^^^^^^^^^^^^^^
Quá trình verification
^^^^^^^^^^^^^^^^^^^^^^^^

Gọi :math:`z` là số được gửi bởi Alice. Bob kiểm tra

.. math:: z^2 \stackrel{?}{=} x^b \cdot y.

Như vậy:

1. Nếu :math:`b = 0` thì :math:`z^2 = y = u^2\pmod n`.
2. Nếu :math:`b = 1` thì :math:`z^2 = xy = (wu)^2 \pmod n`.

^^^^^^^^^^^^^^^^^^^^^^^^
Nguyên lí hoạt động
^^^^^^^^^^^^^^^^^^^^^^^^

Bob chỉ biết :math:`x` và :math:`n` trong khi Alice biết căn bậc hai của
:math:`x` modulo :math:`n`.

Ở đây Alice muốn thuyết phục Bob rằng mình biết căn bậc hai của :math:`x`
trong modulo :math:`n`.

Nếu Alice thật sự biết căn bậc hai của :math:`x` là :math:`w`, hay
:math:`x = w^2 \pmod n`, thì Alice cần chứng minh cho Bob thấy.

1. Alice chọn số random :math:`u \in \mathbb{Z}_n^*` và gửi
   :math:`y = u^2 \pmod n` cho Bob.
2. Bob chọn ngẫu nhiên :math:`b \in \{ 0, 1 \}` và gửi cho Alice.

Với mỗi trường hợp của :math:`b`:

* nếu :math:`b = 0` thì Alice cần tính căn bậc hai của :math:`y`
  modulo :math:`n` và gửi cho Bob. Đó chính là :math:`u`;
   
* nếu :math:`b = 1` thì Alice cần tính căn bậc hai của :math:`xy`
  (:math:`x` public và :math:`y` được gửi trước đó). Ta có
  :math:`xy = w^2 u^2 \pmod n` nên Alice cần gửi :math:`wu`.
  Nếu Alice thật sự biết căn bậc hai của :math:`x` thì có thể
  tính được :math:`wu`;

Bob có thể kiểm tra số :math:`z` được gửi tới có thỏa mãn
:math:`z^2 = y \pmod n` (nếu :math:`b = 0`) hoặc thỏa mãn
:math:`z^2 = xy \pmod n` (nếu :math:`b = 1`) hay không.

Trong ví dụ trên, ta thấy các tính chất của ZKP:

1. Completeness: khi :math:`x` thực sự là số chính phương modulo
   :math:`n` và Alice có thể đưa số :math:`w` sao cho
   :math:`x = w^2 \pmod n` thì Bob sẽ chấp nhận với xác suất
   bằng :math:`1`. Điều này khá dễ thấy;
2. Soundness: nếu :math:`x` không là số chính phương modulo :math:`n`
   thì Bob có thể bác bỏ chứng minh của Alice với xác suất ít nhất
   :math:`1/2` (trong trường hợp :math:`b=1`). Trong khi đó
   :math:`b = 0` thì vẫn có "cơ may" đúng;
3. Zero knowledge: Bob không biết bất cứ thông tin nào liên quan
   đến Alice nhưng Alice có thể thuyết phục Bob tin rằng mình
   biết căn bậc hai của :math:`x`. Zero knowledge có nghĩa là
   trong suốt quá trình Bob không biết thêm thông tin gì hơn
   từ Alice.

-----------------------------
Mô hình Zero Knowledge Proof
-----------------------------

Phần tiếp theo được tổng hợp từ một số nguồn dành cho newbie [#second]_.

.. [#second] What is a zk-SNARK? URL - https://blog.thirdweb.com/what-is-a-zk-snark/

ZKP bao gồm ba bước là: key generation, proof generation và verification.

^^^^^^^^^^^^^^^^^^
1. Key generation
^^^^^^^^^^^^^^^^^^

Bước này tạo các tham số để một bên proof và để bên còn lại verification.

Thông thường, ở bước này có một hàm :math:`C(x, w)` nhận hai tham số là
:math:`x` (public input) và :math:`w` (private input, witness).

Một tham số private là :math:`\lambda` giúp việc sinh ra các tham số gồm
public key :math:`pk` và private key :math:`vk`.

Ký hiệu: :math:`\text{Setup}(C, \lambda) \rightarrow (pk, vk)`.

Trong đó :math:`pk` được gửi cho prover để họ chứng minh bản thân
(thuyết phục verifier rằng họ sở hữu thông tin).

Ngược lại, :math:`vk` được gửi cho verifier để họ kiểm tra mệnh đề từ prover.

^^^^^^^^^^^^^^^^^^^^
2. Proof generation
^^^^^^^^^^^^^^^^^^^^

Bước này thực hiện bởi prover để sinh ra giá trị gửi cho bên verifier kiểm tra.

Với đầu vào gồm private input là :math:`w`, public input là :math:`x` và public
key là :math:`pk`, prover sẽ tính toán prf rồi gửi cho verifier.

Ký hiệu: :math:`\text{Prove}(w, x, pk) \rightarrow \text{prf}`.

^^^^^^^^^^^^^^^^^^
3. Verification
^^^^^^^^^^^^^^^^^^

Bước này thực hiện bởi verifier để kiểm tra mệnh đề prf được gửi từ prover.

Với đầu vào gồm public input :math:`x`, proof là prf và private key là :math:`vk`,
verifier kiểm tra tính đúng đắn của prf.

Ký hiệu: :math:`\text{Verify}(x, \text{prf}, vk) \rightarrow` đúng
(nếu hợp lệ) hoặc sai (ngược lại).
