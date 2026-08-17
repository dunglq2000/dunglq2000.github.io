Rasterization, nội suy và chiếu sáng
====================================

Tọa độ barycentric
------------------

Cho tam giác :math:`ABC` và chọn một gốc tọa độ :math:`O`. Mỗi điểm :math:`P`
trong mặt phẳng :math:`ABC` có thể được xác định bởi

.. math::

   \overrightarrow{OP}
   =\lambda_A\overrightarrow{OA}
   +\lambda_B\overrightarrow{OB}
   +\lambda_C\overrightarrow{OC},
   \qquad
   \lambda_A+\lambda_B+\lambda_C=1.

Điểm nằm trong tam giác kín khi :math:`\lambda_A,\lambda_B,\lambda_C`
không âm. Ba hệ số này là tọa độ barycentric và cũng là trọng số nội suy thuộc
tính theo đỉnh.

Trong hai chiều, đặt edge function

.. math::

   E_{AB}(P)
   =(x_P-x_A)(y_B-y_A)-(y_P-y_A)(x_B-x_A).

Sau khi thống nhất winding, dấu của ba giá trị

.. math::

   E_{AB}(P),\qquad E_{BC}(P),\qquad E_{CA}(P)

cho biết sample có nằm trong tam giác hay không. Edge function là affine theo :math:`x, y`, vì vậy có thể cập nhật tăng dần khi quét qua các pixel thay vì tính lại từ đầu.

Rasterization
-------------

Rasterizer không chỉ “vẽ đường viền” mà xác định tập sample được primitive phủ. Quy trình cơ bản:

1. tính bounding box của tam giác trong screen space;
2. giới hạn bounding box vào viewport;
3. đánh giá ba edge function tại tâm mỗi sample;
4. áp dụng quy tắc biên nhất quán, chẳng hạn top-left rule, để hai tam giác chung cạnh không tạo khe hoặc tô trùng;
5. sinh fragment và tọa độ barycentric cho các sample hợp lệ.

Multisample anti-aliasing đánh giá coverage tại nhiều sample trong mỗi pixel. Màu cuối là kết quả resolve các sample, giúp làm mượt biên hình học.

Nội suy thuộc tính
------------------

Một đại lượng affine :math:`a` như độ sâu sau projection có thể nội suy bằng

.. math:: a(P)=\lambda_Aa(A)+\lambda_Ba(B)+\lambda_Ca(C).

Tuy nhiên texture coordinate, vị trí camera-space và các varying khác không affine sau phép chia phối cảnh. Nếu clip coordinate của đỉnh :math:`i` có thành phần :math:`w_i`, nội suy đúng là

.. math::

   a(P)
   =\frac{\displaystyle\sum_{V\in\{A,B,C\}}\lambda_V\dfrac{a(V)}{w_V}}
          {\displaystyle\sum_{V\in\{A,B,C\}}\lambda_V\dfrac{1}{w_V}}.

Đây là **perspective-correct interpolation**. Nội suy tuyến tính trực tiếp tọa độ texture trong screen space làm texture trượt hoặc méo trên bề mặt nghiêng.

Depth buffer
------------

Depth buffer lưu độ sâu gần nhất tại mỗi sample. Fragment mới chỉ được giữ nếu vượt qua depth test. Đây là cách giải visibility theo từng pixel với chi phí gần tuyến tính theo số fragment, trái với thuật toán đường khuất hình học ở :doc:`polyhedron-visibility`.

Độ sâu sau projection không phân bố tuyến tính theo khoảng cách camera; phần lớn độ chính xác tập trung gần near plane. Các biện pháp cải thiện gồm:

- tăng near distance thay vì chỉ tăng far distance;
- dùng depth format có độ chính xác cao hơn;
- dùng reversed-Z với phép so sánh đảo và floating-point depth khi pipeline hỗ trợ;
- tránh hai bề mặt gần đồng phẳng gây z-fighting.

Màu và không gian màu
---------------------

Màu RGB tuyến tính là vector

.. math:: \bm{c} = (r, g, b), \qquad 0 \leqslant r, g, b \leqslant 1.

Phép modulation thực hiện theo từng thành phần:

.. math::

   \bm{c}_1 \odot \bm{c}_2
   = (r_1 r_2, g_1 g_2, b_1 b_2).

Các phép chiếu sáng phải thực hiện trong **linear color space**. Giá trị sRGB lưu trong texture hoặc framebuffer đã qua hàm truyền phi tuyến; phải decode trước khi cộng, nhân hoặc nội suy ánh sáng và encode lại khi xuất.

Alpha và blending
-----------------

Màu RGBA thêm thành phần :math:`\alpha` mô tả opacity. Với alpha thẳng, phép source-over tổng quát là

.. math::

   \alpha_{out}
   = \alpha_s + (1 - \alpha_s)\alpha_d,

.. math::

   \bm{c}_{out}
   = \frac{
      \alpha_s \bm{c}_s + (1 - \alpha_s)\alpha_d \bm{c}_d
   }{\alpha_{out}}

khi :math:`\alpha_{out} > 0`. Nếu destination đục, :math:`\alpha_d = 1`, công thức màu rút gọn thành :math:`\alpha_s \bm{c}_s + (1 - \alpha_s) \bm{c}_d`.

Với premultiplied alpha, đặt :math:`\bm{c}' = \alpha \bm{c}`; khi đó

.. math:: \bm{c}'_{out} = \bm{c}'_s + (1 - \alpha_s) \bm{c}'_d.

Dạng này giúp phép tổng hợp ổn định hơn ở biên texture. Vật trong suốt thường cần sắp xếp từ xa tới gần nếu dùng blending thông thường, vì phép tổng hợp không giao hoán.

Texture và lấy mẫu
------------------

Tọa độ texture :math:`(u, v)` ánh xạ một điểm bề mặt vào ảnh. Nearest sampling chọn texel gần nhất; bilinear sampling nội suy bốn texel lân cận. Khi texture bị thu nhỏ mạnh, một pixel phủ nhiều texel và cần mipmap để lọc gần đúng trên footprint lớn hơn.

Đạo hàm screen-space của :math:`u, v` ước lượng mức mipmap. Anisotropic filtering cải thiện trường hợp footprint kéo dài mạnh, thường xảy ra khi nhìn bề mặt dưới góc xiên.

Mô hình chiếu sáng cục bộ
-------------------------

Đặt:

- :math:`\widehat{\bm{n}}` là pháp tuyến bề mặt;
- :math:`\widehat{\bm{l}}` là hướng từ điểm tới nguồn sáng;
- :math:`\widehat{\bm{v}}` là hướng từ điểm tới camera;
- :math:`\widehat{\bm{h}} = \dfrac{\widehat{\bm{l}} + \widehat{\bm{v}}}{\|\widehat{\bm{l}} + \widehat{\bm{v}}\|}` là half vector.

Thành phần khuếch tán Lambert là

.. math::

   \bm{c}_{diff}
   = \bm{c}_{light} \odot \bm{c}_{albedo}
    \max(0, \widehat{\bm{n}} \cdot \widehat{\bm{l}}).

Một mô hình specular đơn giản kiểu Blinn--Phong dùng

.. math::

   \bm{c}_{spec}
   = \bm{c}_{light}\, k_s
    \max(0, \widehat{\bm{n}} \cdot \widehat{\bm{h}})^q,

trong đó :math:`q` càng lớn thì highlight càng hẹp. Ambient term chỉ là xấp xỉ thô cho ánh sáng gián tiếp và không bảo toàn năng lượng.

Với point light ở khoảng cách :math:`d`, attenuation thường được xấp xỉ bởi

.. math:: A(d) = \frac{1}{k_c + k_l d + k_qd^2}.

Trong mô hình vật lý lý tưởng cường độ giảm theo :math:`1/d^2`; các hệ số tổng quát chủ yếu phục vụ điều khiển nghệ thuật.

Pháp tuyến theo mặt và theo đỉnh
--------------------------------

Flat shading dùng một pháp tuyến cho cả mặt. Smooth shading gán pháp tuyến tại đỉnh, thường bằng trung bình có trọng số của pháp tuyến các mặt kề, rồi nội suy và chuẩn hóa lại tại fragment.

Không nên trung bình qua cạnh sắc. Mesh thường tách vertex hoặc dùng smoothing group để một vị trí hình học có nhiều pháp tuyến khác nhau.

Vòng lặp mô phỏng và dựng hình
------------------------------

Một game loop tách **update** trạng thái khỏi **render**. Để mô phỏng ổn định, dùng bước thời gian cố định :math:`h`:

.. math::

   t_{acc} \leftarrow t_{acc} + \Delta t,
   \qquad
   \text{while } t_{acc} \geqslant h:
   \quad \operatorname{update}(h), \quad t_{acc} \leftarrow t_{acc} - h.

Render có thể nội suy giữa hai trạng thái mô phỏng với :math:`\alpha = t_{acc}/h`. Cách này tách tốc độ mô phỏng khỏi frame rate, giảm sai khác vật lý giữa máy nhanh và máy chậm. Đây là nguyên lý bền vững hơn vòng lặp cố ép một số frame cố định bằng cách bỏ qua thời gian dư.
