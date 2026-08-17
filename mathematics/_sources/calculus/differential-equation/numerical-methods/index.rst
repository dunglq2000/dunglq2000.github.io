Phương pháp số cho bài toán giá trị ban đầu
===========================================

Bài toán Cauchy bậc nhất có dạng

.. math:: y'(x) = f(x, y(x)), \qquad y(x_0) = y_0.

Khi không tìm được nghiệm đóng, ta chọn lưới
:math:`x_n = x_0 + n h` và xây dựng các giá trị :math:`y_n` xấp xỉ
:math:`y(x_n)`. Hai phương pháp cơ bản là Euler hiện và Runge--Kutta bậc
bốn (RK4).

Phương pháp Euler hiện
----------------------

Khai triển Taylor tại :math:`x_n` cho

.. math:: y(x_{n + 1}) = y(x_n) + h y'(x_n) + O(h^2).

Thay :math:`y' = f(x, y)` và bỏ số hạng dư, ta được

.. math:: y_{n + 1} = y_n + h f(x_n, y_n).

Đây là phép tiến một bước theo tiếp tuyến tại đầu đoạn. Sai số cục bộ có
cấp :math:`O(h^2)`, còn sai số toàn cục trên một khoảng cố định có cấp
:math:`O(h)`.

.. figure:: images/euler-method.png
   :name: fig-explicit-euler-method
   :align: center
   :width: 70%

   Mỗi bước Euler thay đường nghiệm bằng một đoạn tiếp tuyến.

Phương pháp Runge--Kutta bậc bốn
--------------------------------

RK4 lấy bốn ước lượng độ dốc trong một bước:

.. math::

   k_1 &= f(x_n, y_n), \\
   k_2 &= f\left(x_n + \frac{h}{2},
                 y_n + \frac{h k_1}{2}\right), \\
   k_3 &= f\left(x_n + \frac{h}{2},
                 y_n + \frac{h k_2}{2}\right), \\
   k_4 &= f(x_n + h, y_n + h k_3),

rồi kết hợp chúng theo công thức

.. math:: y_{n + 1} = y_n + \frac{h}{6}(k_1 + 2 k_2 + 2 k_3 + k_4).

Sai số cục bộ của RK4 có cấp :math:`O(h^5)` và sai số toàn cục có cấp
:math:`O(h^4)`, với giả thiết :math:`f` đủ trơn trên miền đang xét.

.. figure:: images/rk4-method.png
   :name: fig-rk4-method
   :align: center
   :width: 85%

   Bốn độ dốc được dùng để xây dựng một bước RK4.

Ví dụ so sánh
-------------

Xét bài toán

.. math::

   (x^2 - 1)y' + 2 x y^2 = 0,
   \qquad
   y(0) = 1.

Trên miền :math:`|x| < 1`, phương trình chuẩn là

.. math::

   y' = f(x, y) = \frac{-2 x y^2}{x^2 - 1}.

Tách biến cho

.. math::

   \frac{d y}{y^2} = \frac{-2 x\, d x}{x^2 - 1}.

Từ điều kiện đầu, nghiệm đúng là

.. math::

   y(x) = \frac{1}{1 + \ln(1 - x^2)}.

Mẫu số triệt tiêu tại
:math:`x = \sqrt{1 - e^{-1}} \approx 0.795`; vì vậy ví dụ số chỉ xét
:math:`0 \leqslant x \leqslant 0.7`.

.. figure:: images/euler-comparison-corrected.png
   :name: fig-euler-exact-comparison
   :align: center
   :width: 78%

   Nghiệm Euler tiến gần nghiệm đúng khi giảm bước :math:`h`.

.. figure:: images/rk4-comparison.png
   :name: fig-rk4-exact-comparison
   :align: center
   :width: 78%

   So sánh nghiệm RK4 ứng với nhiều kích thước bước.

Đo bậc hội tụ
-------------

Nếu sai số thỏa :math:`\varepsilon(h) \approx C h^p`, lấy logarithm cho

.. math::

   \ln \varepsilon
   \approx \ln C + p \ln h.

Vì vậy độ dốc của đường hồi quy giữa :math:`\ln h` và
:math:`\ln \varepsilon` xấp xỉ bậc :math:`p` của phương pháp. Khi giảm
:math:`h` một nửa, Euler thường giảm sai số khoảng :math:`2` lần, còn RK4
giảm khoảng :math:`2^4 = 16` lần trước khi sai số làm tròn chi phối.

.. list-table:: Đồ thị hội tụ từ báo cáo thực nghiệm
   :class: borderless
   :widths: 1 1

   * - .. image:: images/euler-regression.png
          :alt: Hồi quy sai số Euler
     - .. image:: images/rk4-error-corrected.png
          :alt: Quan hệ giữa bước và sai số RK4
   * - Euler: độ dốc xấp xỉ :math:`1`
     - RK4: độ dốc xấp xỉ :math:`4`

Code demo
---------

Chương trình sau cài đặt cả hai phương pháp chỉ với thư viện chuẩn:

.. literalinclude:: code/euler_rk4.py
   :language: python
   :linenos:

Các chương trình gốc dùng NumPy và Matplotlib vẫn được giữ để tái tạo bảng
và đồ thị:

- :download:`Phân tích Euler <code/legacy/euler-analysis.py>`;
- :download:`bộ giải RK4 <code/legacy/rk4-solver.py>`;
- :download:`chương trình vẽ đồ thị bổ sung <code/legacy/graph-53.py>`.

Ảnh kết quả bổ sung
-------------------

Các ảnh bảng kết quả theo từng bước được giữ lại để đối chiếu với code gốc.

.. list-table:: Kết quả Euler và RK4
   :class: borderless
   :widths: 1 1

   * - .. image:: images/euler-h-010-005.png
          :alt: Euler với bước 0.1 và 0.05
     - .. image:: images/rk4-h-010-005.png
          :alt: RK4 với bước 0.1 và 0.05
   * - .. image:: images/euler-h-0003125.png
          :alt: Euler với bước 0.003125
     - .. image:: images/rk4-h-00125.png
          :alt: RK4 với bước 0.0125
   * - .. image:: images/euler-correlation.png
          :alt: Tương quan bước và sai số Euler
     - .. image:: images/rk4-h-000625.png
          :alt: RK4 với bước 0.00625

Hai ảnh ``euler-comparison.png`` và ``rk4-error.png`` là các phiên bản thử
ban đầu; bản hiệu chỉnh được dùng trong nội dung chính. Tệp
``images/source-logo.png`` được lưu như một phần nguồn của báo cáo.
