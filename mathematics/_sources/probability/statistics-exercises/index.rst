###################################
Bài tập thực hành thống kê toán học
###################################

Các bài tập dưới đây được tổng hợp từ bảy báo cáo trong thư mục
``Math-Statistic``. Kết quả số của các thí nghiệm mô phỏng có thể thay đổi giữa
các lần chạy; nên đặt hạt giống cho bộ sinh số ngẫu nhiên nếu cần tái lập kết
quả.

Các chương trình Python gốc được giữ lại để đối chiếu. Phần lời giải bên dưới
trình bày phương pháp đã hiệu chỉnh ở những chỗ mã nguồn chưa hoàn toàn phù hợp
với đề bài.

Phân phối mẫu và các đặc trưng vị trí
=====================================

Đề bài
------

Xét bốn phân phối:

* phân phối chuẩn :math:`N(0, 1)`;
* phân phối Cauchy :math:`C(0, 1)`;
* phân phối Poisson với :math:`\lambda = 10`;
* phân phối đều trên :math:`[-\sqrt{3}, \sqrt{3}]`.

Với mỗi phân phối:

#. Sinh các mẫu có kích thước :math:`n = 10`, :math:`50` và :math:`1000`, rồi
   vẽ histogram cùng hàm mật độ hoặc hàm khối xác suất lý thuyết.
#. Với :math:`n = 10`, :math:`100` và :math:`1000`, lặp thí nghiệm 1000 lần và
   khảo sát trung bình mẫu, trung vị, trung bình khoảng biến thiên và trung bình
   tứ phân vị.

Cách giải
---------

Các đặc trưng vị trí được tính bởi

.. math::

   \bar{x} = \frac{1}{n} \sum_{i = 1}^{n} x_i,
   \qquad
   z_R = \frac{x_{(1)} + x_{(n)}}{2},
   \qquad
   z_Q = \frac{Q_1 + Q_3}{2}.

Với mỗi thống kê :math:`z`, từ 1000 giá trị mô phỏng
:math:`z_1, \ldots, z_{1000}`, ước lượng

.. math::

   \widehat{E z} = \frac{1}{1000} \sum_{j = 1}^{1000} z_j,
   \qquad
   \widehat{D z} = \frac{1}{999}
   \sum_{j = 1}^{1000} \left(z_j - \overline{z}\right)^2.

Histogram phải được chuẩn hoá để diện tích bằng 1. Với phân phối Poisson, nên
dùng các cột tại giá trị nguyên và chồng hàm khối xác suất thay vì hàm mật độ.

Thí nghiệm cho thấy trung bình mẫu hoạt động tốt với phân phối có moment hữu
hạn, nhưng không ổn định với phân phối Cauchy. Trung vị và :math:`z_Q` bền vững
hơn trước các giá trị cực đoan. Mã gốc chưa tính :math:`z_R`, vì vậy cần bổ sung
thống kê này nếu muốn tái hiện đầy đủ đề bài.

:download:`Mã demo cho bài 1 <code/lab1.py>`

Biểu đồ hộp và ngoại lệ
=======================

Đề bài
------

Với bốn phân phối ở bài trước và các kích thước mẫu :math:`20`, :math:`100`,
:math:`1000`:

#. vẽ biểu đồ hộp Tukey;
#. lặp thí nghiệm 1000 lần và ước lượng tỷ lệ phần tử ngoại lệ;
#. so sánh tỷ lệ thực nghiệm với xác suất ngoại lệ lý thuyết.

Cách giải
---------

Đặt khoảng tứ phân vị :math:`IQR = Q_3 - Q_1`. Hai hàng rào Tukey là

.. math::

   L = Q_1 - 1.5 IQR,
   \qquad
   U = Q_3 + 1.5 IQR.

Một quan sát là ngoại lệ nếu :math:`x < L` hoặc :math:`x > U`. Với :math:`m`
lần lặp, tỷ lệ ngoại lệ thực nghiệm là

.. math::

   \widehat{p}_{\mathrm{out}}
   = \frac{\text{số quan sát nằm ngoài } [L, U]}{m n}.

Xác suất lý thuyết được tính từ các tứ phân vị tổng thể:

.. math::

   p_{\mathrm{out}} = F(L) + 1 - F(U).

Các giá trị xấp xỉ trong báo cáo lần lượt là :math:`0.007` cho phân phối chuẩn,
:math:`0.156` cho Cauchy, :math:`0.008` cho Poisson và :math:`0` cho phân phối
đều. Đuôi nặng của phân phối Cauchy làm tỷ lệ ngoại lệ lớn hơn rõ rệt.

Trong chương trình gốc, biến đếm ngoại lệ cần được đặt lại về 0 bên trong vòng
lặp theo kích thước mẫu; nếu không, kết quả của các kích thước sau sẽ cộng dồn
quan sát từ các thí nghiệm trước.

:download:`Mã demo cho bài 2 <code/lab2.py>`

Hệ số tương quan và phân phối chuẩn hai chiều
=============================================

Đề bài
------

#. Sinh mẫu từ phân phối chuẩn hai chiều với hệ số tương quan
   :math:`\rho = 0`, :math:`0.5`, :math:`0.9` và kích thước
   :math:`n = 20`, :math:`60`, :math:`100`.
#. Qua 1000 lần lặp, khảo sát hệ số tương quan Pearson, Spearman và tương quan
   góc phần tư.
#. Thực hiện tương tự với phân phối hỗn hợp

   .. math::

      0.9 N(0, 0, 1, 1, 0.9)
      + 0.1 N(0, 0, 10, 10, -0.9).

#. Vẽ đám mây điểm và ellipse xác suất bằng nhau.

Cách giải
---------

Với các cặp quan sát :math:`(x_i, y_i)`, hệ số Pearson là

.. math::

   r = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}
   {\sqrt{\sum_i (x_i - \bar{x})^2 \sum_i (y_i - \bar{y})^2}}.

Hệ số Spearman là hệ số Pearson của hai dãy hạng. Tương quan góc phần tư được
tính bởi

.. math::

   r_Q = \frac{n_1 + n_3 - n_2 - n_4}{n},

trong đó các góc phần tư được xác định quanh hai trung vị mẫu.

Với mỗi thống kê :math:`z`, cần báo cáo trung bình :math:`\widehat{E z}`, trung
bình bình phương :math:`\widehat{E z^2}` và

.. math::

   \widehat{D z} = \widehat{E z^2} - \left(\widehat{E z}\right)^2.

Để sinh đúng phân phối hỗn hợp, với mỗi điểm trước tiên lấy
:math:`B \sim \operatorname{Bernoulli}(0.1)`, rồi sinh điểm từ thành phần thứ
hai nếu :math:`B = 1`, ngược lại sinh từ thành phần thứ nhất. Không được lấy
tổng có trọng số của hai mẫu chuẩn độc lập, vì phép đó tạo ra một phân phối
chuẩn khác chứ không phải phân phối hỗn hợp. Ngoài ra, kỳ vọng mô phỏng phải dùng
trung bình, không dùng trung vị như trong hàm lập bảng của mã gốc.

:download:`Mã demo cho bài 3 <code/lab3.py>`

Hồi quy tuyến tính và tính bền vững
===================================

Đề bài
------

Tại 20 điểm :math:`x_i` cách đều từ :math:`-1.8` đến :math:`2`, sinh dữ liệu

.. math::

   y_i = 2 + 2 x_i + \varepsilon_i,
   \qquad
   \varepsilon_i \sim N(0, 1).

Ước lượng đường thẳng :math:`y = a + b x` bằng phương pháp bình phương tối
thiểu và phương pháp độ lệch tuyệt đối tối thiểu. Sau đó thay
:math:`y_1 \leftarrow y_1 + 10`, :math:`y_{20} \leftarrow y_{20} - 10` và so
sánh lại hai ước lượng.

Cách giải
---------

Nghiệm bình phương tối thiểu là

.. math::

   \widehat{b}
   = \frac{\overline{x y} - \bar{x}\bar{y}}
   {\overline{x^2} - \bar{x}^2},
   \qquad
   \widehat{a} = \bar{y} - \widehat{b}\bar{x}.

Ước lượng độ lệch tuyệt đối tối thiểu giải bài toán lồi

.. math::

   (\widehat{a}, \widehat{b})
   = \mathop{\arg\min}_{a, b}
   \sum_{i = 1}^{n} \left|y_i - a - b x_i\right|.

Có thể giải bài toán thứ hai bằng một bộ tối ưu số hoặc quy hoạch tuyến tính.
Hai điểm ngoại lệ ở hai đầu miền :math:`x` có đòn bẩy lớn nên làm đường hồi quy
bình phương tối thiểu thay đổi đáng kể. Chuẩn :math:`L_1` của phương pháp độ
lệch tuyệt đối khiến nghiệm ít nhạy hơn với chúng.

:download:`Mã demo cho bài 4 <code/lab4.py>`

Kiểm định Pearson về luật phân phối
===================================

Đề bài
------

#. Sinh 100 quan sát từ :math:`N(0, 1)`, ước lượng các tham số bằng phương pháp
   hợp lý cực đại và kiểm định giả thuyết mẫu tuân theo phân phối chuẩn ở mức ý
   nghĩa :math:`\alpha = 0.05`.
#. Khảo sát độ nhạy của kiểm định bằng các mẫu cỡ 20 từ phân phối Laplace và
   phân phối đều.

Cách giải
---------

Ước lượng hợp lý cực đại của phân phối chuẩn là

.. math::

   \widehat{\mu} = \bar{x},
   \qquad
   \widehat{\sigma}^2
   = \frac{1}{n} \sum_{i = 1}^{n} (x_i - \bar{x})^2.

Chia trục số thành :math:`k = \lceil 1.72 n^{1/3} \rceil` khoảng. Với tần số
quan sát :math:`n_i` và xác suất lý thuyết theo phân phối chuẩn đã khớp

.. math::

   p_i = F_{\widehat{\mu}, \widehat{\sigma}}(b_i)
   - F_{\widehat{\mu}, \widehat{\sigma}}(a_i),

thống kê Pearson là

.. math::

   \chi^2 = \sum_{i = 1}^{k}
   \frac{(n_i - n p_i)^2}{n p_i}.

Bác bỏ :math:`H_0` nếu

.. math::

   \chi^2 > \chi^2_{1 - \alpha,\, k - 1 - r},

trong đó :math:`r = 2` vì :math:`\mu` và :math:`\sigma` được ước lượng từ chính
mẫu. Nên gộp các lớp lân cận nếu một tần số kỳ vọng :math:`n p_i` quá nhỏ,
thường lấy ngưỡng 5.

Mã gốc dùng phân phối chuẩn tắc để tính :math:`p_i` dù đã ước lượng tham số và
dùng :math:`k - 1` bậc tự do. Khi chạy lại, cần dùng hàm phân phối tích luỹ của
:math:`N(\widehat{\mu}, \widehat{\sigma}^2)` và hiệu chỉnh số bậc tự do như trên.
Với :math:`n = 20`, xấp xỉ chi bình phương còn yếu nên kết quả chỉ mang tính
minh hoạ.

:download:`Mã demo cho bài 5 <code/lab5.py>`

Khoảng tin cậy cho trung bình và độ lệch chuẩn
==============================================

Đề bài
------

Với mẫu cỡ :math:`n = 20` và :math:`n = 100`, hãy lập khoảng tin cậy cho trung
bình và độ lệch chuẩn:

* khi tổng thể có phân phối chuẩn;
* theo xấp xỉ tiệm cận mà không giả thiết dạng phân phối.

Cách giải
---------

Đặt mức tin cậy là :math:`1 - \alpha`, trung bình mẫu là :math:`\bar{x}` và độ
lệch chuẩn mẫu hiệu chỉnh là :math:`s`. Nếu tổng thể chuẩn thì

.. math::

   \mu \in
   \left[
   \bar{x} - t_{1 - \alpha / 2,\, n - 1}\frac{s}{\sqrt{n}},
   \bar{x} + t_{1 - \alpha / 2,\, n - 1}\frac{s}{\sqrt{n}}
   \right]

và

.. math::

   \sigma \in
   \left[
   s \sqrt{\frac{n - 1}{\chi^2_{1 - \alpha / 2,\, n - 1}}},
   s \sqrt{\frac{n - 1}{\chi^2_{\alpha / 2,\, n - 1}}}
   \right].

Theo định lý giới hạn trung tâm, khoảng tiệm cận cho trung bình là

.. math::

   \mu \in
   \left[
   \bar{x} - z_{1 - \alpha / 2}\frac{s}{\sqrt{n}},
   \bar{x} + z_{1 - \alpha / 2}\frac{s}{\sqrt{n}}
   \right].

Đặt :math:`m_4 = n^{-1}\sum_i (x_i - \bar{x})^4`, hệ số nhọn dư
:math:`e = m_4 / s^4 - 3` và

.. math::

   U = z_{1 - \alpha / 2}\sqrt{\frac{e + 2}{n}}.

Một khoảng tiệm cận cho độ lệch chuẩn là

.. math::

   \sigma \in
   \left[
   \frac{s}{\sqrt{1 + U}},
   \frac{s}{\sqrt{1 - U}}
   \right],

với điều kiện :math:`U < 1`. Khi kích thước mẫu tăng, cả hai loại khoảng thường
hẹp hơn và xấp xỉ tiệm cận đáng tin cậy hơn.

:download:`Mã demo cho bài 6 <code/lab6.py>`

Độ đo Jaccard cho các khoảng ngẫu nhiên
=======================================

Đề bài
------

Sinh hai mẫu cỡ :math:`1000`:

.. math::

   X_1 \sim N(0, 0.95),
   \qquad
   X_2 \sim N(1, 1.05).

Với mỗi mẫu, xét khoảng trong :math:`[Q_1, Q_3]` và khoảng ngoài
:math:`[\min X, \max X]`. Tịnh tiến mẫu thứ nhất một lượng :math:`a`, rồi tìm
:math:`a \in [-2, 4]` làm độ đo Jaccard giữa hai khoảng lớn nhất.

Cách giải
---------

Với hai khoảng :math:`A = [a_1, a_2]` và :math:`B = [b_1, b_2]`, độ dài phần
giao và phần hợp là

.. math::

   |A \cap B|
   = \max\left(0, \min(a_2, b_2) - \max(a_1, b_1)\right),

.. math::

   |A \cup B| = \max(a_2, b_2) - \min(a_1, b_1).

Do đó

.. math::

   J(A, B) = \frac{|A \cap B|}{|A \cup B|}.

Quét một lưới đủ mịn trên :math:`[-2, 4]`, tính :math:`J` cho các khoảng trong
và ngoài sau khi cộng :math:`a` vào hai đầu khoảng của mẫu thứ nhất, rồi chọn
điểm cực đại. Trong lần chạy có hạt giống 42, mã gốc thu được xấp xỉ
:math:`a = 0.99` cho khoảng trong và :math:`a = 0.71` cho khoảng ngoài. Giá trị
từ khoảng trong gần độ lệch trung bình thực :math:`1` hơn vì các tứ phân vị ít
nhạy với giá trị cực đoan; khoảng ngoài phụ thuộc trực tiếp vào min và max nên
dao động mạnh giữa các mẫu.

:download:`Mã demo cho bài 7 <code/lab7.py>`
