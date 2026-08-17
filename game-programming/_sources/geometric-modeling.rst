Mô hình hóa hình học
====================

Biểu diễn ẩn và tham số
-----------------------

Một đối tượng hình học thường được mô tả theo một trong hai cách:

- dạng ẩn :math:`F(x,y,z) = 0`, thuận tiện để phân loại phía, tính khoảng
  cách có dấu và tìm pháp tuyến;
- dạng tham số :math:`P=P(u,v)`, thuận tiện để sinh điểm, lấy mẫu bề mặt và
  gắn tọa độ texture.

Đường thẳng qua :math:`P_0` theo hướng :math:`\bm{d}` gồm các điểm :math:`P(t)`
thỏa

.. math:: \overrightarrow{P_0P(t)}=t\bm{d}.

Mặt phẳng qua :math:`P_0` với pháp tuyến :math:`\bm{n}` gồm các điểm :math:`P`
thỏa

.. math:: \bm{n} \cdot \overrightarrow{P_0P} = 0,

hay :math:`a x + b y + c z + d = 0`. Nếu :math:`Q(x_Q,y_Q,z_Q)`, khoảng cách
có dấu từ :math:`Q` tới mặt phẳng là

.. math::

   \delta(Q) = \frac{a x_Q+b y_Q+c z_Q+d}{\|\bm{n}\|}.

Dấu của :math:`\delta` cho biết điểm nằm ở nửa không gian nào. Công thức này
được dùng trong clipping, culling và phát hiện va chạm.

.. figure:: figures/oxy-01.*
   :name: fig-analytic-coordinate-system
   :align: center

   Điểm và vector trong một hệ tọa độ trực chuẩn hai chiều.

Giao và chiếu trực giao
-----------------------

Cho tia gốc :math:`O` theo hướng :math:`\bm{d}`, tức
:math:`\overrightarrow{OP(t)}=t\bm{d}`. Thay tọa độ của :math:`P(t)` vào
phương trình mặt phẳng cho

.. math::

   t = -\frac{a x_O+b y_O+c z_O+d}{\bm{n} \cdot \bm{d}}.

Mẫu số gần :math:`0` nghĩa là ray gần song song với mặt phẳng; thuật toán
phải dùng một ngưỡng số thay vì so sánh chính xác với :math:`0`.

Nếu :math:`\widehat{\bm{n}}` là pháp tuyến đơn vị, hình chiếu trực giao của
:math:`Q` lên mặt phẳng là điểm :math:`H` xác định bởi

.. math::

   \overrightarrow{QH}
   =-\bigl(\widehat{\bm{n}}\cdot\overrightarrow{P_0Q}\bigr)
   \widehat{\bm{n}}.

Trong hai chiều, đường :math:`a x + b y + c = 0` là trường hợp riêng và khoảng cách
từ :math:`(x_0, y_0)` tới đường bằng

.. math:: \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}.

.. figure:: figures/oxy-02.*
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

   * - .. image:: figures/ellipse.*
          :alt: Ellipse
     - .. image:: figures/hyperbola.*
          :alt: Hyperbol
     - .. image:: figures/parabola.*
          :alt: Parabol
   * - Ellipse
     - Hyperbol
     - Parabol

Trong không gian, nếu :math:`\bm{x}=(x,y,z)^{\mathsf T}` là cột tọa độ,
quadric mở rộng thành

.. math:: \bm{x}^{\mathsf T} Q \bm{x} + \bm{q}^{\mathsf T} \bm{x} + c = 0.

Mặt cầu, ellipsoid, trụ và nón đều thuộc lớp này. Khi thay phương trình ray
vào quadric, ta nhận một phương trình bậc hai theo :math:`t`; nghiệm dương
nhỏ nhất là giao nhìn thấy đầu tiên. Dạng ma trận còn cho phép biến đổi cả
quadric bằng một phép đổi tọa độ thống nhất.

Đường cong tham số
------------------

Đường cong gồm các điểm :math:`C(t)` và có vector tiếp tuyến
:math:`C'(t)`. Độ dài cung
trên :math:`[a, b]` là

.. math:: L = \int_a^b \|C'(t)\|\, dt.

Tham số không nhất thiết tỉ lệ với độ dài. Nếu cần vật chuyển động với tốc
độ đều, phải lập bảng độ dài cung rồi ánh xạ thời gian sang tham số.

Trong animation và mô phỏng, đại lượng cần tối ưu phải được viết thành một
phiếm hàm, chẳng hạn

.. math::

   T[C] = \int_a^b \frac{\|C'(t)\|}{v(C(t))}\, dt,

rồi mới rời rạc hóa đường cong để tối ưu số.

Tiếp tuyến, pháp tuyến và diện tích
-----------------------------------

Với bề mặt gồm các điểm :math:`S(u,v)`, hai vector tiếp xúc là
:math:`S_u` và :math:`S_v`; pháp tuyến được tính bởi

.. math::

   \bm{n} = \frac{S_u \times S_v}{\|S_u \times S_v\|}.

Phần tử diện tích là

.. math:: dA = \|S_u \times S_v\|\, du\, dv.

Đối với mặt ẩn :math:`F(x,y,z) = 0`, gradient :math:`\nabla F` là pháp
tuyến tại các điểm chính quy. Hai cách biểu diễn vì thế có thể cung cấp
pháp tuyến cho chiếu sáng mà không cần suy ra từ mesh đã rời rạc hóa.

.. figure:: figures/tangent-02.*
   :name: fig-curve-tangent-limit
   :align: center

   Tiếp tuyến xuất hiện như giới hạn của các cát tuyến trên đường cong.
