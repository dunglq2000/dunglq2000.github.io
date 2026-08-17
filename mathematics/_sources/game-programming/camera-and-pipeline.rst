Camera, phép chiếu và pipeline hình học
=======================================

Camera ảo
---------

Camera được xác định bởi vị trí mắt :math:`\bm{e}`, điểm ngắm :math:`\bm{t}` và một hướng lên tham chiếu :math:`\bm{u}_0`. Với hệ tọa độ tay phải và camera nhìn theo trục :math:`-z`, đặt

.. math::

   \bm{f} = \frac{\bm{t} - \bm{e}}{\|\bm{t} - \bm{e}\|},
   \qquad
   \bm{r} = \frac{\bm{f} \times \bm{u}_0}{\|\bm{f} \times \bm{u}_0\|},
   \qquad
   \bm{u} = \bm{r} \times \bm{f}.

Ba vectơ :math:`\bm{r}, \bm{u},-\bm{f}` tạo thành một cơ sở trực chuẩn của camera. Nếu :math:`\bm{f}` gần song song :math:`\bm{u}_0`, tích có hướng gần :math:`0` và phải chọn một up vector khác.

View matrix đổi tọa độ thế giới sang tọa độ camera:

.. math::

   M_{\mathrm{view}} =
   \begin{bmatrix}
   r_x & r_y & r_z & - \bm{r} \cdot \bm{e}\\
   u_x & u_y & u_z & - \bm{u} \cdot \bm{e}\\
   -f_x & - f_y & - f_z & \bm{f} \cdot \bm{e}\\
   0 & 0 & 0 & 1
   \end{bmatrix}.

Đây là nghịch đảo của world transform của camera. Thay vì di chuyển camera trong thế giới, ta biến đổi toàn bộ thế giới ngược lại quanh camera.

Frustum
-------

Phép chiếu phối cảnh chỉ giữ phần không gian nằm giữa near plane :math:`n` và far plane :math:`f`, đồng thời nằm trong góc nhìn. Miền này là một hình chóp cụt gọi là **view frustum**.

.. figure:: virtual_camera.*
   :name: fig-virtual-camera

   Frustum được giới hạn bởi near plane, far plane và bốn mặt phẳng bên.

Near plane phải dương. Tỉ số :math:`f/n` quá lớn làm giảm độ chính xác của depth buffer; vì vậy nên đẩy near plane ra xa camera ở mức ứng dụng cho phép thay vì chỉ tăng far plane.

Phép chiếu trực giao
--------------------

Phép chiếu trực giao bỏ một tọa độ theo hướng nhìn. Trong trường hợp đơn giản,

.. math:: \Pi(x, y, z) = (x, y).

Với hộp nhìn :math:`[l, r] \times [b, t] \times [-f,-n]`, một orthographic projection tay phải đưa hộp đó về normalized device coordinates:

.. math::

   M_{\mathrm{ortho}} =
   \begin{bmatrix}
   \dfrac{2}{r - l} & 0 & 0 & - \dfrac{r + l}{r - l}\\
   0 & \dfrac{2}{t - b} & 0 & - \dfrac{t + b}{t - b}\\
   0 & 0 & - \dfrac{2}{f - n} & - \dfrac{f + n}{f - n}\\
   0 & 0 & 0 & 1
   \end{bmatrix}.

Các đường song song vẫn song song và kích thước không phụ thuộc độ sâu. Phép chiếu này phù hợp cho bản vẽ kỹ thuật, UI và bài toán đa diện trong :doc:`polyhedron-visibility`.

Phép chiếu phối cảnh
--------------------

Từ các tam giác đồng dạng, điểm :math:`(x, y, z)` trong camera space có tọa độ ảnh tỉ lệ với

.. math:: x' \propto \frac{x}{ - z}, \qquad y' \propto \frac{y}{ - z}.

Đặt :math:`\theta` là field of view theo chiều dọc và :math:`a = w/h` là aspect ratio. Với NDC có độ sâu trong :math:`[-1, 1]`, một perspective matrix tay phải là

.. math::

   M_{\mathrm{persp}} =
   \begin{bmatrix}
   \dfrac{1}{a \tan(\theta/2)} & 0 & 0 & 0\\
   0 & \dfrac{1}{\tan(\theta/2)} & 0 & 0\\
   0 & 0 & - \dfrac{f + n}{f - n} & - \dfrac{2 fn}{f - n}\\
   0 & 0 & - 1 & 0
   \end{bmatrix}.

Sau phép nhân, đỉnh có clip coordinates :math:`(x_c, y_c, z_c, w_c)`. Phép chia phối cảnh

.. math::

   (x_{ndc}, y_{ndc}, z_{ndc})
   = \left(\frac{x_c}{w_c}, \frac{y_c}{w_c}, \frac{z_c}{w_c} \right)

tạo hiệu ứng vật ở xa nhỏ hơn. Quy ước trục, khoảng NDC của :math:`z`, thứ tự ma trận và dấu trong projection matrix khác nhau giữa các API; các công thức chỉ đúng khi dùng nhất quán một quy ước.

Clipping trong tọa độ thuần nhất
--------------------------------

Clipping nên được thực hiện trước phép chia phối cảnh. Với NDC :math:`[-1, 1]^3`, một điểm nằm trong canonical view volume khi

.. math::

   -w_c \leqslant x_c \leqslant w_c,
   \qquad
   -w_c \leqslant y_c \leqslant w_c,
   \qquad
   -w_c \leqslant z_c \leqslant w_c.

Một primitive hoàn toàn ngoài cùng một mặt phẳng bị loại. Primitive cắt biên phải được tạo thêm đỉnh giao; thuộc tính tại đỉnh mới được nội suy cùng tham số giao.

Viewport transform
------------------

Với viewport có góc trái trên :math:`(x_0, y_0)`, chiều rộng :math:`W`, chiều cao :math:`H`, ánh xạ từ NDC sang pixel thường có dạng

.. math::

   X = x_0 + \frac{x_{ndc} + 1}{2} W,
   \qquad
   Y = y_0 + \frac{1 - y_{ndc}}{2} H.

Dấu trừ trong công thức :math:`Y` xuất hiện khi tọa độ màn hình hướng xuống. Tọa độ độ sâu được ánh xạ sang khoảng mà depth buffer sử dụng, thường là :math:`[0, 1]`.

Back-face culling
-----------------

Một mesh kín thường chỉ cần vẽ mặt hướng về camera. Trong screen space, diện tích có hướng của tam giác là

.. math::

   A_2 = (x_1 - x_0)(y_2 - y_0) - (y_1 - y_0)(x_2 - x_0).

Dấu của :math:`A_2` xác định winding order. Sau khi chọn chiều kim đồng hồ hoặc ngược chiều kim đồng hồ là mặt trước, tam giác có dấu ngược lại có thể bị loại. Culling chỉ đúng khi mesh có winding nhất quán và world transform không đảo orientation ngoài dự kiến.

Pipeline hình học hiện đại
--------------------------

Một pipeline rasterization có thể hiểu độc lập API qua các giai đoạn:

1. **Input assembly:** đọc vertex/index buffer và tạo primitive.
2. **Vertex processing:** áp dụng :math:`M_{\mathrm{proj}} M_{\mathrm{view}} M_{\mathrm{world}}` và tính các thuộc tính theo đỉnh.
3. **Tessellation/geometry processing tùy chọn:** sinh hoặc thay đổi primitive.
4. **Clipping và culling:** giới hạn primitive vào frustum và loại mặt sau.
5. **Rasterization:** tìm các sample được tam giác phủ và nội suy thuộc tính.
6. **Fragment/pixel shading:** tính màu, pháp tuyến hoặc dữ liệu render target.
7. **Per-sample operations:** depth/stencil test và blending.

Phần cố định của API có thể thay đổi, nhưng chuỗi toán học model--view--projection, clipping, nội suy và kiểm tra visibility vẫn giữ nguyên.
