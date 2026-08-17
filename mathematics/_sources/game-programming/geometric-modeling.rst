Mô hình hóa hình học
====================

Biểu diễn ẩn và tham số
-----------------------

Một đối tượng hình học thường được mô tả theo một trong hai cách:

- dạng ẩn :math:`F(\bm{x}) = 0`, thuận tiện để phân loại phía, tính khoảng
  cách có dấu và tìm pháp tuyến;
- dạng tham số :math:`\bm{x} = \bm{x}(u, v)`, thuận tiện để sinh đỉnh, lấy mẫu
  bề mặt và gắn tọa độ texture.

Đường thẳng qua :math:`\bm{p}_0` theo hướng :math:`\bm{d}` có dạng

.. math:: \bm{p}(t) = \bm{p}_0 + t \bm{d}.

Mặt phẳng qua :math:`\bm{p}_0` với pháp tuyến :math:`\bm{n}` có dạng

.. math:: \bm{n} \cdot (\bm{p} - \bm{p}_0) = 0,

hay :math:`a x + b y + c z + d = 0`. Khoảng cách có dấu từ :math:`\bm{q}` tới mặt
phẳng là

.. math::

   \delta(\bm{q}) = \frac{\bm{n} \cdot \bm{q} + d}{\|\bm{n}\|}.

Dấu của :math:`\delta` cho biết điểm nằm ở nửa không gian nào. Công thức này
được dùng trong clipping, culling và phát hiện va chạm.

.. figure:: ../figures/analytic_geometry/oxy-01.*
   :name: fig-analytic-coordinate-system
   :align: center

   Điểm và vectơ trong một hệ tọa độ trực chuẩn hai chiều.

Giao và chiếu trực giao
-----------------------

Thay ray :math:`\bm{r}(t) = \bm{o} + t \bm{d}` vào phương trình mặt phẳng cho

.. math::

   t = -\frac{\bm{n} \cdot \bm{o} + d}{\bm{n} \cdot \bm{d}}.

Mẫu số gần :math:`0` nghĩa là ray gần song song với mặt phẳng; thuật toán
phải dùng một ngưỡng số thay vì so sánh chính xác với :math:`0`.

Nếu :math:`\widehat{\bm{n}}` là pháp tuyến đơn vị, hình chiếu trực giao của
:math:`\bm{q}` lên mặt phẳng là

.. math::

   \bm{q}_{\Pi} = \bm{q}
   -\bigl(\widehat{\bm{n}} \cdot (\bm{q} - \bm{p}_0)\bigr) \widehat{\bm{n}}.

Trong hai chiều, đường :math:`a x + b y + c = 0` là trường hợp riêng và khoảng cách
từ :math:`(x_0, y_0)` tới đường bằng

.. math:: \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}.

.. figure:: ../figures/analytic_geometry/oxy-02.*
   :name: fig-point-line-projection
   :align: center

   Hình chiếu trực giao của một điểm lên đường thẳng.

Đường conic và quadric
----------------------

Conic là nghiệm của phương trình bậc hai trong mặt phẳng. Ba dạng chính tắc
thường gặp là

.. math::

   \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1,
   \qquad
   \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1,
   \qquad
   y^2 = 4 p x.

.. list-table:: Ba đường conic chính tắc
   :class: borderless
   :widths: 1 1 1

   * - .. image:: ../figures/conics/ellipse.*
          :alt: Ellipse
     - .. image:: ../figures/conics/hyperbola.*
          :alt: Hyperbol
     - .. image:: ../figures/conics/parabola.*
          :alt: Parabol
   * - Ellipse
     - Hyperbol
     - Parabol

Trong không gian, quadric mở rộng thành

.. math:: \bm{x}^{\mathsf T} Q \bm{x} + \bm{q}^{\mathsf T} \bm{x} + c = 0.

Mặt cầu, ellipsoid, trụ và nón đều thuộc lớp này. Khi thay phương trình ray
vào quadric, ta nhận một phương trình bậc hai theo :math:`t`; nghiệm dương
nhỏ nhất là giao nhìn thấy đầu tiên. Dạng ma trận còn cho phép biến đổi cả
quadric bằng một phép đổi tọa độ thống nhất.

Đường cong tham số
------------------

Đường cong :math:`\bm{c}(t)` có tiếp tuyến :math:`\bm{c}'(t)`. Độ dài cung
trên :math:`[a, b]` là

.. math:: L = \int_a^b \|\bm{c}'(t)\|\, dt.

Tham số không nhất thiết tỉ lệ với độ dài. Nếu cần vật chuyển động với tốc
độ đều, phải lập bảng độ dài cung rồi ánh xạ thời gian sang tham số.

Trong animation và mô phỏng, đại lượng cần tối ưu phải được viết thành một
phiếm hàm, chẳng hạn

.. math::

   T[\bm{c}] = \int_a^b \frac{\|\bm{c}'(t)\|}{v(\bm{c}(t))}\, dt,

rồi mới rời rạc hóa đường cong để tối ưu số.

Tiếp tuyến, pháp tuyến và diện tích
-----------------------------------

Với bề mặt tham số :math:`\bm{s}(u, v)`, hai vectơ tiếp xúc là
:math:`\bm{s}_u` và :math:`\bm{s}_v`; pháp tuyến được tính bởi

.. math::

   \bm{n} = \frac{\bm{s}_u \times \bm{s}_v}
                 {\|\bm{s}_u \times \bm{s}_v\|}.

Phần tử diện tích là

.. math:: dA = \|\bm{s}_u \times \bm{s}_v\|\, du\, dv.

Đối với mặt ẩn :math:`F(\bm{x}) = 0`, gradient :math:`\nabla F` là pháp
tuyến tại các điểm chính quy. Hai cách biểu diễn vì thế có thể cung cấp
pháp tuyến cho chiếu sáng mà không cần suy ra từ mesh đã rời rạc hóa.

.. figure:: ../figures/analytic_geometry/tangent-02.*
   :name: fig-curve-tangent-limit
   :align: center
   :width: 65%

   Tiếp tuyến xuất hiện như giới hạn của các cát tuyến trên đường cong.
