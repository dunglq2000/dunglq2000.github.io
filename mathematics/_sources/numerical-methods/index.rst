Phương pháp tính toán
#####################

Tài liệu này giới thiệu các phương pháp số cơ bản để giải những bài toán thường gặp: tìm nghiệm, tối ưu, vi phân, tích phân, nội suy, hồi quy và giải phương trình vi phân. Mỗi phương pháp chỉ cho nghiệm gần đúng; vì vậy cần quan tâm đến giả thiết áp dụng, sai số và tiêu chuẩn dừng.

Sai số trong phương pháp tính
*****************************

Gọi :math:`x` là giá trị đúng của một đại lượng và :math:`\widetilde{x}` là giá trị gần đúng thu được bằng tính toán số.

Sai số tuyệt đối
================

Sai số tuyệt đối đo độ chênh lệch trực tiếp giữa giá trị gần đúng và giá trị đúng:

.. math::

   \Delta x = \left|x - \widetilde{x}\right|.

Nếu biết :math:`\Delta x \leqslant \varepsilon`, ta nói :math:`\widetilde{x}` xấp xỉ :math:`x` với sai số tuyệt đối không vượt quá :math:`\varepsilon`.

**Ví dụ.** Lấy :math:`x = \sqrt{2} \approx 1.41421356` và :math:`\widetilde{x} = 1.4142`. Khi đó

.. math::

   \Delta x \approx \left|1.41421356 - 1.4142\right| = 1.356 \times 10^{-5}.

Sai số tương đối
================

Khi :math:`x \ne 0`, sai số tương đối cho biết sai số tuyệt đối lớn đến đâu so với độ lớn của giá trị đúng:

.. math::

   \delta x = \frac{|x - \widetilde{x}|}{|x|}.

Thường biểu diễn dưới dạng phần trăm:

.. math::

   \delta_{\%}x = 100\, \delta x\%.

Với ví dụ trên,

.. math::

   \delta x \approx 9.59 \times 10^{-6}, \qquad
   \delta_{\%}x \approx 0.000959\%.

Sai số tương đối không phù hợp khi :math:`x = 0` hoặc rất gần :math:`0`; khi đó sai số tuyệt đối thường có ý nghĩa hơn.

Lan truyền sai số
=================

Giả sử đại lượng đầu ra

.. math::

   y = f(x_1, \ldots, x_n)

được tính từ các giá trị gần đúng :math:`x_i`, mỗi giá trị có chặn sai số
tuyệt đối :math:`\Delta x_i`. Nếu :math:`f` khả vi và các sai số đủ nhỏ,
khai triển bậc nhất cho chặn gần đúng

.. math::

   \Delta y
   \lesssim
   \sum_{i = 1}^{n}
   \left|\frac{\partial f}{\partial x_i}\right|\Delta x_i.

Khi :math:`f` khác :math:`0`, sai số tương đối có thể được ước lượng bằng

.. math::

   \delta y
   \lesssim
   \sum_{i = 1}^{n}
   \left|\frac{\partial \ln |f|}{\partial x_i}\right|\Delta x_i.

Đây là xấp xỉ bậc nhất: các số hạng chứa tích hoặc lũy thừa của
:math:`\Delta x_i` đã bị bỏ qua.

**Ví dụ.** Cho

.. math::

   y_1 = \frac{a^3}{b \sqrt{c}},
   \qquad
   y_2 = a^3 - b \sqrt{c}.

Đối với :math:`y_1`, ta có

.. math::

   \Delta y_1
   \lesssim
   \left|\frac{3 a^2}{b \sqrt{c}}\right| \Delta a
   + \left|\frac{a^3}{b^2 \sqrt{c}}\right| \Delta b
   + \left|\frac{a^3}{2 b c^{3/2}}\right| \Delta c,

và

.. math::

   \delta y_1
   \lesssim
   3 \delta a + \delta b + \frac{1}{2} \delta c.

Đối với hiệu :math:`y_2`, nên dùng sai số tuyệt đối:

.. math::

   \Delta y_2
   \lesssim
   3 |a|^2 \Delta a
   + \sqrt{c}\, \Delta b
   + \left|\frac{b}{2 \sqrt{c}}\right|\Delta c.

Ví dụ này cũng cho thấy phép trừ hai đại lượng gần nhau có thể tạo sai số
tương đối lớn, dù sai số tuyệt đối của từng đầu vào nhỏ.

Các nguồn sai số
================

- **Sai số dữ liệu** phát sinh khi số liệu đầu vào đã là số đo hoặc số gần đúng.
- **Sai số cắt cụt** xuất hiện khi thay một quá trình vô hạn bằng hữu hạn, chẳng hạn cắt chuỗi vô hạn hoặc thay đạo hàm bằng công thức sai phân với bước :math:`h`.
- **Sai số làm tròn** do máy tính chỉ lưu được hữu hạn chữ số có nghĩa. Phép trừ hai số gần nhau có thể làm mất nhiều chữ số chính xác.
- **Sai số phương pháp** là sai số do mô hình hoặc thuật toán xấp xỉ bài toán gốc.

Tổng sai số của kết quả thường là sự kết hợp của các nguồn trên. Giảm bước :math:`h` trong vi phân số có thể làm giảm sai số cắt cụt, nhưng đến một mức nào đó lại làm sai số làm tròn tăng lên; vì vậy không phải cứ chọn :math:`h` càng nhỏ càng tốt.

Sai số, phần dư và tiêu chuẩn dừng
==================================

Trong thực tế thường không biết nghiệm đúng :math:`x`, nên không thể tính trực tiếp :math:`\Delta x`. Thay vào đó, ta dùng một đại lượng có thể quan sát được để dừng thuật toán.

Với bài toán tìm nghiệm :math:`f(x) = 0`, phần dư là

.. math::

   r(\widetilde{x}) = f(\widetilde{x}).

Điều kiện :math:`|r(\widetilde{x})| \leqslant \varepsilon` cho thấy giá trị gần đúng gần thỏa phương trình, nhưng không luôn bảo đảm sai số nghiệm nhỏ: điều này còn phụ thuộc độ nhạy của bài toán. Với phương pháp chia đôi, độ rộng khoảng kẹp trực tiếp cho một chặn sai số:

.. math::

   |\alpha - m_k| \leqslant \frac{b_k - a_k}{2}.

Một tiêu chuẩn dừng phổ biến khác là so sánh hai nghiệm lặp liên tiếp:

.. math::

   \left|x_{k + 1} - x_k\right| \leqslant \varepsilon_{\mathrm{abs}}
    + \varepsilon_{\mathrm{rel}} \left|x_{k + 1}\right|.

Trong đó :math:`\varepsilon_{\mathrm{abs}}` kiểm soát độ chính xác gần :math:`0`, còn :math:`\varepsilon_{\mathrm{rel}}` giữ mức chính xác tỷ lệ với độ lớn nghiệm. Nên đặt dung sai phù hợp với độ chính xác thực sự cần thiết của bài toán, thay vì nhỏ hơn khả năng biểu diễn của dữ liệu đầu vào.

1. Tìm nghiệm phương trình một ẩn
*********************************

Cho hàm liên tục :math:`f(x)`, mục tiêu là tìm :math:`\alpha` sao cho

.. math::

   f(\alpha) = 0.

1.1. Phương pháp chia đôi
=========================

Giả sử :math:`f` liên tục trên :math:`[a, b]` và :math:`f(a)f(b) < 0`. Khi đó, theo định lý giá trị trung gian, đoạn này chứa ít nhất một nghiệm. Đặt

.. math::

   m_k = \frac{a_k + b_k}{2}.

Nếu :math:`f(a_k)f(m_k) < 0` thì chọn :math:`[a_{k + 1}, b_{k + 1}] = [a_k, m_k]`; ngược lại chọn :math:`[m_k, b_k]`. Dừng khi

.. math::

   b_k - a_k \leqslant \varepsilon.

Sau :math:`k` bước, sai số bị chặn bởi

.. math::

   |\alpha - m_k| \leqslant \frac{b - a}{2^{k + 1}}.

Phương pháp hội tụ chắc chắn nếu giả thiết đổi dấu được thỏa, nhưng tốc độ hội tụ tuyến tính.

**Ví dụ.** Tìm nghiệm của :math:`f(x) = x^2 - 2` trên :math:`[1, 2]`. Ta có :math:`f(1) = -1` và :math:`f(2) = 2`. Sau các bước chia đôi, trung điểm tiến đến

.. math::

   \alpha = \sqrt{2} \approx 1.41421356.

1.2. Phương pháp dây cung
=========================

Phương pháp dây cung thay đồ thị hàm số gần hai điểm :math:`a_k, b_k` bằng đường thẳng qua hai điểm đó. Hoành độ giao điểm với trục hoành là

.. math::

   c_k = b_k - \frac{f(b_k)(b_k - a_k)}{f(b_k) - f(a_k)}.

Trong biến thể kẹp nghiệm, giữ lại khoảng con mà tại đó hàm đổi dấu. Có thể dừng khi :math:`|f(c_k)| \leqslant \varepsilon` hoặc khi khoảng kẹp đủ nhỏ.

Phương pháp thường nhanh hơn chia đôi, song cần tránh :math:`f(b_k) - f(a_k)` quá gần :math:`0` và không có bảo đảm hội tụ chung mạnh bằng chia đôi.

**Ví dụ.** Với :math:`f(x) = x^2 - 2`, chọn :math:`a_0 = 1`, :math:`b_0 = 2`. Lần dây cung đầu tiên cho

.. math::

   c_0 = 2 - \frac{2(2 - 1)}{2 - (-1)} = \frac{4}{3}.

Tiếp tục lặp cho nghiệm gần đúng :math:`\sqrt{2} \approx 1.41421356`.

2. Tìm cực trị của hàm một biến
*******************************

Mục tiêu là tìm điểm :math:`x_*` sao cho :math:`f(x_*)` là cực tiểu hoặc cực đại trên đoạn :math:`[a, b]`. Các phương pháp sau thường giả sử hàm đơn đỉnh khi tìm cực đại, hoặc đơn đáy khi tìm cực tiểu.

2.1. Thu hẹp khoảng bằng ba điểm
================================

Từ khoảng hiện tại :math:`[a_k, b_k]`, đặt

.. math::

   c_k = \frac{a_k + b_k}{2}, \qquad
   d_{1, k} = \frac{a_k + c_k}{2}, \qquad
   d_{2, k} = \frac{c_k + b_k}{2}.

So sánh các giá trị tại :math:`d_{1, k}, c_k, d_{2, k}` và giữ khoảng bao quanh điểm có giá trị nhỏ nhất khi tìm cực tiểu, hoặc lớn nhất khi tìm cực đại. Dừng khi :math:`b_k - a_k \leqslant \varepsilon`.

**Ví dụ.** Tìm cực tiểu của :math:`f(x) = (x - 2)^2 + 1` trên :math:`[0, 4]`. Ở bước đầu, :math:`d_1 = 1`, :math:`c = 2`, :math:`d_2 = 3`; vì :math:`f(2) = 1` nhỏ nhất, khoảng mới là :math:`[1, 3]`. Quá trình thu hẹp về

.. math::

   x_* = 2, \qquad f(x_*) = 1.

2.2. Phương pháp tỉ lệ vàng
===========================

Đặt tỉ lệ vàng

.. math::

   \varphi = \frac{1 + \sqrt{5}}{2}.

Trong đoạn :math:`[a_k, b_k]`, chọn

.. math::

   x_{1, k} = b_k - \frac{b_k - a_k}{\varphi}, \qquad
   x_{2, k} = a_k + \frac{b_k - a_k}{\varphi}.

Khi tìm cực tiểu, nếu :math:`f(x_{1, k}) \geqslant f(x_{2, k})` thì bỏ phần bên trái; nếu không thì bỏ phần bên phải. Khi tìm cực đại, đảo chiều bất đẳng thức. Ưu điểm là một giá trị hàm được dùng lại sau mỗi bước.

**Ví dụ.** Tìm cực đại của :math:`f(x) = -(x - 3)^2 + 5` trên :math:`[0, 6]`. Các khoảng tỉ lệ vàng co dần quanh

.. math::

   x_* = 3, \qquad f(x_*) = 5.

3. Vi phân số
*************

Vi phân số xấp xỉ đạo hàm từ giá trị hàm tại các điểm gần :math:`x`. Bước :math:`h` cần đủ nhỏ để giảm sai số cắt cụt, nhưng không quá nhỏ để tránh sai số làm tròn.

3.1. Sai phân tiến
==================

.. math::

   f'(x) \approx \frac{f(x + h) - f(x)}{h},

với sai số cắt cụt bậc :math:`O(h)`.

**Ví dụ.** Với :math:`f(x) = x^2`, :math:`x = 1`, :math:`h = 0.01`:

.. math::

   f'(1) \approx \frac{1.01^2 - 1}{0.01} = 2.01.

Giá trị đúng là :math:`f'(1) = 2`.

3.2. Sai phân trung tâm cho đạo hàm cấp một
===========================================

.. math::

   f'(x) \approx \frac{f(x + h) - f(x - h)}{2 h},

với sai số cắt cụt :math:`O(h^2)`.

**Ví dụ.** Với :math:`f(x) = x^2`, :math:`x = 1`, :math:`h = 0.01`:

.. math::

   f'(1) \approx \frac{1.01^2 - 0.99^2}{0.02} = 2.

3.3. Sai phân trung tâm cho đạo hàm cấp hai
===========================================

.. math::

   f''(x) \approx \frac{f(x + h) - 2 f(x) + f(x - h)}{h^2},

với sai số cắt cụt :math:`O(h^2)`.

**Ví dụ.** Với :math:`f(x) = x^2`, :math:`x = 1`, :math:`h = 0.01`:

.. math::

   f''(1) \approx \frac{1.01^2 - 2 + 0.99^2}{0.01^2} = 2,

trùng với giá trị đúng :math:`f''(1) = 2`.

4. Tích phân Simpson thích nghi
*******************************

Ta cần xấp xỉ

.. math::

   I = \int_a^b f(x)\, dx.

Trên đoạn :math:`[x, x + h]`, quy tắc Simpson một panel là

.. math::

   I_1 = \frac{h}{6} \left[f(x) + 4 f\!\left(x + \frac{h}{2}\right) + f(x + h)\right].

Chia đôi đoạn để có xấp xỉ tinh hơn :math:`I_2`. Một ước lượng sai số là

.. math::

   \Delta = \frac{I_2 - I_1}{15}.

Đoạn được chấp nhận khi :math:`|\Delta| \leqslant \varepsilon`; nếu không, tiếp tục giảm bước. Vì Simpson có sai số bậc bốn, kích thước bước thường được điều chỉnh theo lũy thừa :math:`1/5` của tỷ số sai số.

**Ví dụ.** Tính

.. math::

   \int_0^1 x^2\, dx.

Simpson với :math:`h = 1` cho

.. math::

   \frac{1}{6} \left[0 + 4 \left(\frac{1}{2}\right)^2 + 1\right] = \frac{1}{3},

đúng bằng giá trị tích phân chính xác.

5. Nội suy đa thức Lagrange
***************************

Với :math:`n` điểm có hoành độ phân biệt :math:`(X_i, Y_i)`, đa thức nội suy Lagrange là

.. math::

   P_{n - 1}(x) = \sum_{i = 0}^{n - 1} Y_i L_i(x), \qquad
   L_i(x) = \prod_{\substack{0 \leqslant j \leqslant n - 1\\j \ne i}} \frac{x - X_j}{X_i - X_j}.

Đa thức có bậc không quá :math:`n - 1` và thỏa :math:`P_{n - 1}(X_i) = Y_i`. Khi số điểm lớn, dạng Lagrange trực tiếp có thể kém ổn định về số.

**Ví dụ.** Nội suy các điểm :math:`(0, 1)` và :math:`(2, 5)`. Khi đó

.. math::

   P_1(x) = 1 \cdot \frac{x - 2}{0 - 2} + 5 \cdot \frac{x - 0}{2 - 0} = 1 + 2 x.

Vì vậy :math:`P_1(1) = 3`.

6. Hồi quy tuyến tính theo bình phương tối thiểu
************************************************

Ta tìm đường thẳng

.. math::

   y = ax + b

sao cho tổng bình phương sai số :math:`\sum_i(Y_i - a X_i - b)^2` nhỏ nhất. Đặt

.. math::

   S_x = \sum_i X_i, \quad S_y = \sum_i Y_i, \quad S_{xx} = \sum_i X_i^2, \quad S_{xy} = \sum_i X_i Y_i.

Nếu :math:`n S_{xx} - S_x^2 \ne 0`, các hệ số là

.. math::

   a = \frac{n S_{xy} - S_x S_y}{n S_{xx} - S_x^2}, \qquad
   b = \frac{S_y - a S_x}{n}.

**Ví dụ.** Với ba điểm :math:`(1, 2)`, :math:`(2, 3)`, :math:`(3, 5)`, ta có :math:`S_x = 6`, :math:`S_y = 10`, :math:`S_{xx} = 14`, :math:`S_{xy} = 23`. Suy ra

.. math::

   a = \frac{3}{2}, \qquad b = \frac{1}{3}.

Đường hồi quy là :math:`y = \frac{3}{2}x + \frac{1}{3}`.

7. Giải hệ phương trình tuyến tính bằng khử Gauss
*************************************************

Xét hệ

.. math::

   A \boldsymbol{x} = \boldsymbol{y}.

Khử Gauss dùng các phép biến đổi sơ cấp trên hàng để đưa ma trận về dạng tam giác trên. Sau đó thế ngược:

.. math::

   x_i = \frac{y_i - \sum_{j = i + 1}^{n - 1} A_{ij}x_j}{A_{ii}}.

Trong thực hành nên dùng pivot từng phần để tránh chia cho pivot quá nhỏ và tăng ổn định số.

**Ví dụ.** Giải hệ

.. math::

   \begin{cases}
   2 x + y = 5, \\
   x - y = 1.
   \end{cases}

Từ phương trình thứ hai, :math:`x = 1 + y`. Thế vào phương trình đầu được :math:`3 y = 3`, nên

.. math::

   x = 2, \qquad y = 1.

8. Newton cho hệ phương trình phi tuyến
***************************************

Với hệ :math:`F(\boldsymbol{x}) = \boldsymbol{0}`, tại nghiệm gần đúng :math:`\boldsymbol{x}_k`, phương pháp Newton giải hệ tuyến tính

.. math::

   J_F(\boldsymbol{x}_k)\boldsymbol{s}_k = -F(\boldsymbol{x}_k),

rồi cập nhật

.. math::

   \boldsymbol{x}_{k + 1} = \boldsymbol{x}_k + \boldsymbol{s}_k.

Jacobian có thể được xấp xỉ bằng sai phân tiến:

.. math::

   \frac{\partial F_j}{\partial x_i}(\boldsymbol{x}) \approx
   \frac{F_j(\boldsymbol{x} + \delta \boldsymbol{e}_i) - F_j(\boldsymbol{x})}{\delta}.

Phương pháp hội tụ nhanh gần nghiệm nếu Jacobian không suy biến, nhưng phụ thuộc mạnh vào giá trị khởi tạo.

**Ví dụ.** Giải :math:`F(x) = x^2 - 2 = 0` bằng Newton, bắt đầu từ :math:`x_0 = 1.5`:

.. math::

   x_{k + 1} = x_k - \frac{x_k^2 - 2}{2 x_k}.

Ta được :math:`x_1 \approx 1.41666667`, :math:`x_2 \approx 1.41421569`, tiến nhanh đến :math:`\sqrt{2}`.

9. Phương trình vi phân thường: Dormand-Prince 4(5)
***************************************************

Xét bài toán Cauchy

.. math::

   y' = f(x, y), \qquad y(x_0) = y_0.

Dormand-Prince là một cặp Runge-Kutta nhúng: trong mỗi bước, nó dùng các độ dốc trung gian :math:`k_1, \ldots, k_7` để tạo một nghiệm bậc năm :math:`y^{(5)}` và một nghiệm bậc bốn :math:`y^{(4)}`. Sai số cục bộ được ước lượng bởi

.. math::

   \mathrm{err} = \left|y^{(5)} - y^{(4)}\right|.

Nếu sai số đạt dung sai, bước được chấp nhận. Kích thước bước mới có dạng

.. math::

   h_{\mathrm{new}} = h \cdot \min \left(s_{\max}, \max \left(s_{\min}, 0.8 \left(\frac{\mathrm{tol}}{\mathrm{err}}\right)^{1/5}\right)\right).

**Ví dụ.** Với :math:`y' = y`, :math:`y(0) = 1`, nghiệm đúng là :math:`y(1) = e \approx 2.71828183`. Dormand-Prince tự giảm hoặc tăng bước để đạt dung sai đặt trước và cho xấp xỉ của :math:`e` tại :math:`x = 1`.

10. Hàm gamma dưới không đầy đủ
*******************************

Hàm gamma dưới không đầy đủ không chuẩn hoá được định nghĩa bởi

.. math::

   \gamma(a, x) = \int_0^x t^{a - 1}e^{-t}\, dt.

Một biểu diễn chuỗi là

.. math::

   \gamma(a, x) = x^ae^{-x} \sum_{n = 0}^{\infty} \frac{x^n}{a(a + 1)\cdots(a + n)}.

Ta cộng các hạng liên tiếp cho đến khi độ lớn hạng mới nhỏ hơn dung sai. Chuỗi đặc biệt hiệu quả khi các hạng giảm nhanh.

**Ví dụ.** Với :math:`a = 1`, ta có

.. math::

   \gamma(1, x) = \int_0^x e^{-t}\, dt = 1 - e^{-x}.

Do đó

.. math::

   \gamma(1, 1) = 1 - e^{-1} \approx 0.63212056.

Ghi nhớ khi áp dụng phương pháp số
**********************************

- Kiểm tra giả thiết của phương pháp trước khi tính: liên tục và đổi dấu cho chia đôi; đơn đỉnh hoặc đơn đáy cho tìm kiếm cực trị; hoành độ phân biệt cho nội suy Lagrange.
- Chọn dung sai phù hợp với độ chính xác cần thiết và thang đo của bài toán.
- Đối chiếu nghiệm bằng cách thay ngược vào phương trình, kiểm tra phần dư hoặc so sánh với nghiệm giải tích khi có thể.
- Với bài toán kém điều kiện, sai số dữ liệu đầu vào và sai số làm tròn có thể bị khuếch đại đáng kể.
