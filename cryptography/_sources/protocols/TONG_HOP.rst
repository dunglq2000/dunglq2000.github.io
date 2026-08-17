Tổng hợp bài tập môn Giao thức an toàn thông tin cho hệ thống cyber-physical
============================================================================


Tài liệu này tổng hợp nội dung từ hai nhóm ``ЛР`` (lab) và ``ДЗ`` (bài tập về nhà). Các file PDF, ``preamable.tex`` (tên file thực tế trong thư mục) và ``signature.png`` không được sử dụng.

Phần I — Lab (``ЛР``)
---------------------


Lab 1. DLP cho người lớn
~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Alice và Bob thiết lập khóa bí mật chung bằng giao thức DiffieHellman với các tham số công khai

.. math::

   g = 3810758074, \qquad p = 45507711121.


Các giá trị trao đổi trên kênh công khai là

.. math::

   A = 29309341614 = g^a \pmod p, B = 26699295561 = g^b \pmod p.


Hãy cài đặt thuật toán PohligHellman để tìm khóa bí mật chung của Alice và Bob.

Bài giải
^^^^^^^^


Ta phân tích bậc của nhóm:

.. math::

   p - 1 = 2^4 \cdot 3 \cdot 5 \cdot 149 \cdot 433 \cdot 2939.


Thuật toán được tổ chức thành ba tầng:

1. **Baby-step giant-step (BSGS):** giải :math:`g^x = h \pmod p` trong một nhóm có bậc đã biết :math:`n` với độ phức tạp xấp xỉ :math:`O(\sqrt n)`.
2. **DLP trong nhóm có bậc là lũy thừa nguyên tố:** với :math:`n = q^e`, tìm lần lượt các chữ số của :math:`x` trong cơ số :math:`q`; mỗi chữ số được giải bằng BSGS.
3. **PohligHellman:** chiếu bài toán vào từng nhóm con có bậc :math:`q_i^{e_i}`, giải các đồng dư :math:`x \equiv x_i \pmod{q_i^{e_i}}`, rồi ghép bằng định lý số dư Trung Hoa.

Sau khi tìm được :math:`a` hoặc :math:`b`, khóa chung được kiểm tra bởi

.. math::

   K = B^a = A^b = g^{a b} \pmod p.


Kết quả:

.. math::

   \boxed{K = 2862481617}.


Code đầy đủ (gồm lũy thừa nhanh, Euclid mở rộng, nghịch đảo modulo, CRT, căn bậc hai nguyên, BSGS và PohligHellman):

- `lab-1/lab_1.py <lab-1/lab_1.py>`_
- `lab-1/lab_1_test.py <lab-1/lab_1_test.py>`_


Lab 2. Hội đồng quản trị
~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Hội đồng quản trị có 7 người. Quyết định chiến lược cần đa số đồng thuận. Biết rằng Alice và Bob có 3 phiếu mỗi người, các thành viên còn lại có 1 phiếu. Mỗi phần khóa bí mật tương ứng với một phiếu.

Khóa công khai để kiểm tra chữ ký là

.. math::

   (y, g, p) = (189441003666576137454, 376380208497224504084, 835226855261605117963).


Thuật toán ký nhận ít nhất 6 phần khóa. Alice, Dave, Gaby và Hank đã ký digest

.. math::

   m = 14853270393159764412,


nhưng chữ ký sinh ra không vượt qua bước kiểm tra. Yêu cầu:

1. Mô tả hình thức giao thức sinh khóa và ký.
2. Tính chữ ký từ các phần khóa đã cho và chứng minh chữ ký sai.
3. Tìm lỗi trong chương trình.
4. Sửa lỗi, điều chỉnh các phần khóa nếu cần và chứng minh hệ thống mới hoạt động.

Bài giải
^^^^^^^^


**Mô hình giao thức.** Cho :math:`f(x)` là đa thức chia sẻ bí mật trên :math:`\mathbb F_p`. Bí mật chung là :math:`f(0)` và khóa công khai là

.. math::

   y = g^{f(0)} \pmod p.


Từ các cặp :math:`(x_i, f(x_i))` của những người tham gia, thuật toán nội suy Lagrange để khôi phục :math:`f(0)`. Sau đó chọn :math:`k` sao cho :math:`\gcd(k, p - 1) = 1` và tính chữ ký ElGamal

.. math::

   r = g^k \pmod p, s = (m - f(0) r) k^{-1} \pmod{p - 1}.


Chữ ký được kiểm tra bằng

.. math::

   g^m \stackrel{?}{\equiv} y^r r^s \pmod p.


Với các phần khóa ban đầu, thu được

.. math::

   Sig = (265673942823499415554, \ 331942928103462920994),


và hàm ``Verify`` trả về ``False``.
=

**Nguyên nhân.** ``KeyGen`` tạo đa thức bậc 6, trong khi quy tắc “ít nhất 6 phần khóa” chỉ cho phép nội suy duy nhất một đa thức có bậc không quá 5. Muốn khôi phục đa thức bậc 6 phải có ít nhất 7 điểm. Vì vậy các nhóm chỉ có 6 phiếu có thể khôi phục một giá trị tự do khác tại :math:`x = 0`, làm chữ ký không khớp với khóa công khai.

Từ toàn bộ các phần khóa cũ, bí mật chung được khôi phục là

.. math::

   f(0) = 28634772561323385792,


và đúng là :math:`y = g^{f(0)} \pmod p`. Để giữ nguyên khóa công khai nhưng hỗ trợ ngưỡng 6, chọn đa thức bậc 5 mới

.. math::

   F(x) = x^5 + 28634772561323385792


rồi phát lại các phần khóa dưới dạng :math:`F(x_i)`. Khi ký bằng các phần khóa mới, ``Verify`` trả về ``True``.

Code và script SageMath:

- `lab-2/main.py <lab-2/main.py>`_
- `lab-2/l3t1. KeyGen.sage <lab-2/l3t1.%20KeyGen.sage>`_
- `lab-2/l3t1. Sign.sage <lab-2/l3t1.%20Sign.sage>`_


Lab 3. Lược đồ cam kết của Alice và Bob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Trên đường cong elliptic :math:`E/\mathbb F_p`, điểm :math:`G` sinh nhóm con có bậc nguyên tố :math:`q`. Chuỗi bí mật :math:`S` được ánh xạ thành :math:`x \in \mathbb Z_q`. Hệ thống tạo điểm :math:`H = x_M G` từ dữ liệu liên quan đến thông điệp, rồi Alice chọn :math:`r \in \mathbb Z_q` và công bố cam kết

.. math::

   C = x G + r H.


Khi mở cam kết, Alice gửi :math:`(x, r)` và người kiểm tra xác nhận :math:`C \stackrel{?}{=} x G + r H`. Yêu cầu là thay chuỗi :math:`S` bằng chuỗi khác :math:`S'` vẫn vượt qua kiểm tra, sau đó đề xuất cách cải tiến.

Bài giải
^^^^^^^^


Điểm yếu cốt lõi là quan hệ logarit rời rạc giữa hai cơ sở đã biết:

.. math::

   H = x_M G.


Chọn tùy ý :math:`x_1 \ne x` và đặt

.. math::

   r_1 = r - (x_1 - x) x_M^{-1} \pmod q.


Khi đó

.. math::

   \begin{aligned} x_1 G + r_1 H & = x_1 G + \left(r - (x_1 - x) x_M^{-1}\right) x_M G \\ & = x G + r H = C. \end{aligned}


Do đó cùng một cam kết có thể được mở bằng hai cặp khác nhau :math:`(x, r)` và :math:`(x_1, r_1)`; tính *binding* bị phá vỡ.

**Cách cải tiến:** dùng cam kết Pedersen chuẩn

.. math::

   C = x G + r H,


nhưng :math:`H` phải được sinh độc lập sao cho không bên nào biết :math:`\alpha` thỏa :math:`H = \alpha G` (ví dụ áp dụng hash-to-curve với domain separation và tham số chung minh bạch). Khi không biết :math:`\log_G H`, việc tìm hai cách mở khác nhau sẽ suy ra cách giải DLP:

.. math::

   (x - x') G = (r' - r) H.


Demo sử dụng đường cong secp256k1:

- `lab-3/main_1.py <lab-3/main_1.py>`_
- `lab-3/main_final.py <lab-3/main_final.py>`_


Lab 4. Xác thực zero-knowledge dựa trên thặng dư bậc hai
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Các tham số công khai là :math:`(N, m)`, còn prover :math:`\mathfrak A` biết bí mật :math:`k` sao cho

.. math::

   k^2 \equiv m \pmod N.


Một vòng giao thức:

1. :math:`\mathfrak A` chọn ngẫu nhiên :math:`r < N`, gửi :math:`a = r^2 \bmod N`.
2. Verifier :math:`\mathfrak B` gửi thử thách :math:`b \in \{0, 1\}`.
3. :math:`\mathfrak A` gửi :math:`q = k^b r \bmod N`.
4. :math:`\mathfrak B` kiểm tra :math:`q^2 \stackrel{?}{\equiv} m^b a \pmod N`.

Hãy cài đặt giao thức, tìm các điều kiện cần thiết, tấn công khi verifier luôn chọn :math:`b = 1`, và xét biến thể :math:`b \in \{3, 5\}`.

Bài giải
^^^^^^^^


**Tính đúng đắn:**

.. math::

   q^2 = (k^b r)^2 = (k^2)^b r^2 \equiv m^b a \pmod N.


**Điều kiện bổ sung:** cần :math:`1 < m < N`, :math:`2 \le r \le N - 2`, :math:`\gcd(r, N) = 1` và :math:`\gcd(k, N) = 1`. Các giá trị :math:`r = 1` hoặc :math:`r = N - 1` làm :math:`a = 1` và có thể làm lộ :math:`\pm k` khi :math:`b = 1`.

**Tấn công khi** :math:`b` **luôn bằng 1.** Prover giả không cần biết :math:`k`: chọn :math:`\tilde q \in \mathbb Z_N^*` và gửi

.. math::

   \tilde a = \tilde q^2 m^{-1} \pmod N.


Với :math:`b = 1`, kiểm tra luôn đúng vì :math:`m \tilde a \equiv \tilde q^2 \pmod N`. Thử thách phải thực sự ngẫu nhiên và không dự đoán được.

**Biến thể** :math:`b \in \{3, 5\}` **cũng không an toàn.** Prover chọn :math:`r` và gửi

.. math::

   a = r^2 m^{-3} \pmod N.


Nếu :math:`b = 3`, trả lời :math:`q = r`; nếu :math:`b = 5`, trả lời :math:`q = r m`. Cả hai trường hợp đều thỏa:

.. math::

   m^3 a = r^2 = q^2,


.. math::

   m^5 a = r^2 m^2 = (r m)^2 = q^2.


Vì prover không hề dùng :math:`k`, biến thể không có tính soundness.

Code demo:

- `lab-4/main_2.py <lab-4/main_2.py>`_ — giao thức cơ bản
- `lab-4/main_3.py <lab-4/main_3.py>`_ — tấn công thử thách cố định
- `lab-4/main_4.py <lab-4/main_4.py>`_ — tấn công biến thể :math:`\{3, 5\}`

Phần II — Bài tập về nhà (``ДЗ``)
---------------------------------


Bài 1. Phân tích nhân tử cho trẻ em
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


1. Cho :math:`N = 293693171` và :math:`29550^2 \equiv 24073^2 \pmod N`. Hãy phân tích :math:`N` thành nhân tử.
2. Cho :math:`N = 1307 \cdot 95107`. Tìm :math:`x, y` sao cho :math:`x^2 \equiv y^2 \pmod N` nhưng :math:`x \not\equiv y \pmod N`.

Bài giải
^^^^^^^^


Từ hiệu hai bình phương:

.. math::

   N \mid (29550^2 - 24073^2) = (29550 - 24073) (29550 + 24073).


Ta có :math:`29550 - 24073 = 5477` và :math:`29550 + 24073 = 53623`, do đó

.. math::

   \boxed{293693171 = 5477 \cdot 53623}.


Với câu 2, chọn :math:`x - y = 1307` và :math:`x + y = 95107`. Giải hệ được

.. math::

   x = 48207, \qquad y = 46900.


Khi đó :math:`x^2 - y^2 = (x - y) (x + y) = N`, nên

.. math::

   \boxed{x = 48207, \quad y = 46900}.


.. note::

   Ghi chú biên tập: nguồn TeX có hai lỗi đánh máy ở câu 1 (``24073^3`` và ``53627``); các giá trị đúng là :math:`24073^2` và :math:`53623`.


Bài 2. Cấu hình RSA không an toàn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Yuri cấu hình RSA cho :math:`n` người dùng nhưng chỉ lưu :math:`k` số nguyên tố, với :math:`k < 2 n`. Mỗi modulus là tích của hai số nguyên tố khác nhau và các khóa công khai :math:`(e, N)` của người dùng đôi một khác nhau. Eve chọn ngẫu nhiên một người dùng :math:`u`. Tìm xác suất Eve có thể phân tích modulus của :math:`u`.

Bài giải
^^^^^^^^


Theo giả thiết được dùng trong lời giải nguồn, các modulus :math:`N_i` là đôi một khác nhau và được chọn đều từ :math:`\binom{k}{2}` tích có thể có. Eve phân tích được :math:`N_u` nếu một modulus khác dùng chung một thừa số nguyên tố với :math:`N_u`; khi đó

.. math::

   \gcd(N_u, N_i)


cho ta thừa số đó.

Sau khi cố định :math:`N_u`, có :math:`\binom{k - 2}{2}` modulus không dùng một trong hai thừa số của nó. Xác suất không có modulus nào trong :math:`n - 1` modulus còn lại dùng chung thừa số là

.. math::

   P(\overline A) = \frac{ \left(\binom{k - 2}{2}\right)_{n - 1}}
   { \left(\binom{k}{2} - 1\right)_{n - 1}},


trong đó :math:`(t)_j = t (t - 1) \cdots (t - j + 1)` là giai thừa giảm. Vì vậy

.. math::

   \boxed{
   P(A) = 1 - \frac{ \left(\binom{k - 2}{2}\right)_{n - 1}}
   { \left(\binom{k}{2} - 1\right)_{n - 1}}
   }.


Nếu :math:`n - 1 > \binom{k - 2}{2}` thì tử số bằng 0 và :math:`P(A) = 1`.

.. note::

   Lưu ý: điều kiện “các cặp :math:`(e, N)` khác nhau” tự nó vẫn cho phép hai người dùng có cùng :math:`N` nhưng khác :math:`e`. Công thức trên cần giả thiết mạnh hơn rằng các modulus đôi một khác nhau (thường hợp lý khi cùng dùng một public exponent chuẩn). Nếu cho phép lặp modulus, phân bố chọn khóa phải được chỉ rõ thì xác suất mới xác định duy nhất.


Bài 3. Đồng cấu nguy hiểm
~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Cho ElGamal với khóa công khai

.. math::

   (y, g, p) = (785, 1706, 2441).


Biết

.. math::

   c = Enc(97) = (1669, 239),


.. math::

   c_1 = Enc(2230) = (564, 1040).


Tìm :math:`m'` nếu :math:`c' = (1732, 1567) = Enc(m')`.

Bài giải
^^^^^^^^


Mã hóa ElGamal có dạng

.. math::

   Enc(m; r) = (g^r, m y^r).


Tọa độ thứ nhất cho thấy

.. math::

   1669^{-1} \cdot 564 \equiv 1732 \pmod{2441},


nên :math:`r' \equiv r_1 - r` theo bậc của nhóm. Từ tọa độ thứ hai của hai bản mã đã biết:

.. math::

   y^r \equiv 239 \cdot 97^{-1} \equiv 1915 \pmod{2441},


.. math::

   y^{r_1} \equiv 1040 \cdot 2230^{-1} \equiv 909 \pmod{2441}.


Do :math:`1567 \equiv m' (y^r)^{-1} y^{r_1} \pmod{2441}`,

.. math::

   m' \equiv 1567 \cdot 1915 \cdot 909^{-1} \equiv 2313 \pmod{2441}.


Vậy

.. math::

   \boxed{m' = 2313}.


Bài 4. Giao thức trên đường cong elliptic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Đề bài
^^^^^^


Cho :math:`G` sinh nhóm con bậc nguyên tố :math:`q` trên đường cong elliptic. Người dùng :math:`i` có khóa bí mật :math:`sk_i \in \mathbb Z_q` và khóa công khai :math:`PK_i = sk_i G`. Khi liên lạc với Bob, người dùng chọn :math:`r_1, r_2`, tính

.. math::

   R_1 = r_1 G, \qquad R_2 = r_2 G,


lấy hoành độ :math:`x` của điểm :math:`r_2 PK_b`, rồi tính

.. math::

   s = sk_i + r_1 + x \pmod q.


Người dùng gửi :math:`(R_1, R_2, s)`. Hãy chỉ ra cách Bob xác định người gửi.

Bài giải
^^^^^^^^


Bob dùng khóa bí mật của mình để tính

.. math::

   sk_b R_2 = sk_b (r_2 G) = r_2 (sk_b G) = r_2 PK_b.


Vì thế Bob lấy được đúng hoành độ :math:`x` mà người gửi đã dùng. Tiếp theo,

.. math::

   s G = (sk_i + r_1 + x) G = PK_i + R_1 + x G.


Suy ra

.. math::

   \boxed{PK_i = s G - R_1 - x G}.


Bob tra :math:`PK_i` trong cơ sở dữ liệu công khai ánh xạ :math:`(U_i, PK_i)` và xác định được danh tính :math:`U_i` của người gửi.
