Nền tảng toán học của đồ họa 3D
===============================

Điểm, vectơ và hệ tọa độ
------------------------

Một điểm :math:`\bm{p} \in \mathbb{R}^3` biểu diễn vị trí, còn vectơ :math:`\bm{v} \in \mathbb{R}^3` biểu diễn độ dời hoặc hướng. Về mặt tọa độ chúng đều là bộ ba số, nhưng có vai trò affine khác nhau:

.. math::

   \bm{p}_2 - \bm{p}_1\ \text{là vectơ},
   \qquad
   \bm{p} + \bm{v}\ \text{là điểm}.

Với :math:`\bm{u}, \bm{v} \in \mathbb{R}^3`, tích vô hướng

.. math:: \bm{u} \cdot \bm{v} = \|\bm{u}\|\, \|\bm{v}\|\cos \theta

đo góc và phép chiếu. Hai vectơ trực giao khi tích vô hướng bằng :math:`0`. Tích có hướng

.. math::

   \bm{u} \times \bm{v}
   = \begin{bmatrix}
      u_yv_z - u_zv_y\\
      u_zv_x - u_xv_z\\
      u_xv_y - u_yv_x
    \end{bmatrix}

vuông góc với mặt phẳng sinh bởi :math:`\bm{u}, \bm{v}` và có độ dài bằng diện tích hình bình hành tương ứng. Chuẩn hóa vectơ khác không cho

.. math:: \widehat{\bm{v}} = \frac{\bm{v}}{\|\bm{v}\|}.

Phép chuẩn hóa cần ngưỡng :math:`\varepsilon` để tránh chia cho một độ dài gần :math:`0`.

Không gian affine
-----------------

Không gian affine tách khái niệm **điểm** khỏi **vectơ**. Với hai điểm
:math:`P, Q`, hiệu :math:`Q - P` là một vectơ; với điểm :math:`P` và vectơ
:math:`\bm{v}`, tổng :math:`P + \bm{v}` là một điểm. Không có phép cộng hai
điểm mang ý nghĩa nội tại.

Một :math:`m`-phẳng đi qua :math:`P_0` và có các hướng độc lập
:math:`\bm{a}_1, \ldots, \bm{a}_m` được tham số hóa bởi

.. math::

   P(t_1, \ldots, t_m) = P_0 + \sum_{i = 1}^{m} t_i \bm{a}_i.

Đường thẳng, mặt phẳng và không gian ba chiều lần lượt là các trường hợp
:math:`m = 1, 2, 3`. Biểu diễn này là cơ sở của ray, cạnh, mặt phẳng clipping và
các phép giao trong đồ họa.

Các điểm :math:`P_0, \ldots, P_k` độc lập affine khi các vectơ
:math:`P_1 - P_0, \ldots, P_k - P_0` độc lập tuyến tính. Bao affine của chúng gồm
các tổ hợp

.. math::

   P = \sum_{i = 0}^{k} \lambda_i P_i,
   \qquad
   \sum_{i = 0}^{k} \lambda_i = 1.

Nếu thêm điều kiện :math:`\lambda_i \geqslant 0`, ta nhận được bao lồi. Với ba
đỉnh của tam giác, các :math:`\lambda_i` chính là tọa độ barycentric; chúng
vừa kiểm tra một điểm có nằm trong tam giác vừa nội suy thuộc tính đỉnh.

Mục tiêu affine và đổi hệ tọa độ
--------------------------------

Một mục tiêu affine gồm gốc :math:`O` và một cơ sở
:math:`(\bm{e}_1, \ldots, \bm{e}_n)`. Tọa độ :math:`\bm{x}` của điểm :math:`P`
được xác định bởi

.. math:: P = O + \sum_{i = 1}^{n} x_i \bm{e}_i.

Nếu mục tiêu mới có gốc :math:`O' = O + \bm{b}` và ma trận :math:`C` chứa các
vectơ cơ sở mới viết trong cơ sở cũ, thì hai bộ tọa độ liên hệ bởi

.. math:: \bm{x} = C \bm{x}' + \bm{b}.

Đây là dạng tổng quát của phép đổi model space sang world space hoặc world
space sang camera space. Một ánh xạ affine có dạng

.. math:: f(P) = A P + \bm{t}.

Nó bảo toàn đường thẳng, tính song song và tổ hợp affine, nhưng chỉ bảo toàn
độ dài và góc khi phần tuyến tính :math:`A` là một phép đẳng cự. Ánh xạ được
xác định hoàn toàn bởi :math:`A` và ảnh của một điểm; hợp hai ánh xạ affine
vẫn là ánh xạ affine.

Tọa độ thuần nhất
-----------------

Tịnh tiến không phải phép biến đổi tuyến tính trong :math:`\mathbb{R}^3`. Ta nhúng không gian affine vào tọa độ thuần nhất:

.. math::

   \bm{p} = (x, y, z) \longmapsto (x, y, z, 1),
   \qquad
   \bm{v} = (x, y, z) \longmapsto (x, y, z, 0).

Khi đó cả tịnh tiến, quay, co giãn và phép chiếu phối cảnh đều có thể biểu diễn bằng ma trận :math:`4 \times 4`. Với quy ước vectơ cột,

.. math:: \bm{p}' = M \bm{p}.

Nếu dùng vectơ hàng thì thứ tự nhân ma trận phải đảo lại. Không được trộn hai quy ước trong cùng một phép tính.

Biến đổi affine cơ bản
----------------------

Ma trận tịnh tiến là

.. math::

   T(t_x, t_y, t_z) =
   \begin{bmatrix}
   1 & 0 & 0 & t_x\\
   0 & 1 & 0 & t_y\\
   0 & 0 & 1 & t_z\\
   0 & 0 & 0 & 1
   \end{bmatrix}.

Ma trận co giãn là

.. math::

   S(s_x, s_y, s_z) =
   \begin{bmatrix}
   s_x & 0 & 0 & 0\\
   0 & s_y & 0 & 0\\
   0 & 0 & s_z & 0\\
   0 & 0 & 0 & 1
   \end{bmatrix}.

Các phép quay quanh ba trục có dạng

.. math::

   R_x(\theta) =
   \begin{bmatrix}
   1 & 0 & 0 & 0\\
   0 & \cos \theta & - \sin \theta & 0\\
   0 & \sin \theta & \cos \theta & 0\\
   0 & 0 & 0 & 1
   \end{bmatrix},

.. math::

   R_y(\theta) =
   \begin{bmatrix}
   \cos \theta & 0 & \sin \theta & 0\\
   0 & 1 & 0 & 0\\
   -\sin \theta & 0 & \cos \theta & 0\\
   0 & 0 & 0 & 1
   \end{bmatrix},

.. math::

   R_z(\theta) =
   \begin{bmatrix}
   \cos \theta & - \sin \theta & 0 & 0\\
   \sin \theta & \cos \theta & 0 & 0\\
   0 & 0 & 1 & 0\\
   0 & 0 & 0 & 1
   \end{bmatrix}.

Một world transform thường là tích

.. math:: M_{\mathrm{world}} = T R S.

Với vectơ cột, phép ở bên phải tác động trước: mô hình được co giãn, quay rồi mới tịnh tiến. Nói chung :math:`RT \neq TR`, nên đổi thứ tự có thể biến một phép tự quay thành phép quay quanh một tâm bên ngoài. Quay quanh điểm :math:`\bm{c}` được thực hiện bởi

.. math:: M = T(\bm{c})R T(-\bm{c}).

Góc Euler và quaternion
-----------------------

Ba phép quay liên tiếp tạo một biểu diễn góc Euler. Chẳng hạn quy ước :math:`z`--:math:`y`--:math:`z` dùng

.. math:: R = R_z(\gamma)R_y(\beta)R_z(\alpha).

Biểu diễn này trực quan nhưng phụ thuộc thứ tự và có thể gặp gimbal lock. Quaternion đơn vị

.. math:: q = \left(\cos \frac{\theta}{2}, \ \widehat{\bm{u}} \sin \frac{\theta}{2} \right)

biểu diễn phép quay góc :math:`\theta` quanh trục :math:`\widehat{\bm{u}}`. Hai phép quay hợp thành bằng phép nhân quaternion; nội suy SLERP cho chuyển động quay đều hơn nội suy trực tiếp các góc Euler.

Biến đổi pháp tuyến
-------------------

Nếu vị trí được biến đổi bởi phần tuyến tính :math:`A` của world matrix, pháp tuyến không luôn biến đổi bởi chính :math:`A`. Để bảo toàn trực giao,

.. math:: \bm{n}' \propto (A^{ - 1})^{\mathsf T} \bm{n}.

Sau phép biến đổi phải chuẩn hóa lại. Chỉ khi :math:`A` là phép quay hoặc co giãn đồng đều mới có thể dùng trực tiếp :math:`A \bm{n}`.

Mesh tam giác
-------------

Một bề mặt cong được xấp xỉ bởi **triangle mesh**. Dữ liệu hình học thường gồm:

- vertex buffer chứa vị trí, pháp tuyến, màu, tọa độ texture hoặc tangent;
- index buffer mô tả các tam giác bằng chỉ số đỉnh;
- topology chỉ cách ghép các chỉ số thành điểm, đoạn hoặc tam giác.

.. figure:: rectangle.*
   :name: fig-mesh-rectangle

   Một hình chữ nhật được chia thành hai tam giác dùng chung hai đỉnh.

Thay vì lưu sáu đỉnh lặp, ta lưu :math:`(v_0, v_1, v_2, v_3)` và dãy chỉ số :math:`(0, 1, 2, 0, 2, 3)`. Thứ tự đỉnh, hay **winding order**, quyết định hướng pháp tuyến và mặt trước của tam giác.

Với tam giác :math:`(\bm{p}_0, \bm{p}_1, \bm{p}_2)`, một pháp tuyến chưa chuẩn hóa là

.. math:: \bm{n} = (\bm{p}_1 - \bm{p}_0) \times (\bm{p}_2 - \bm{p}_0).

Nếu :math:`\|\bm{n}\|` gần :math:`0`, tam giác suy biến và không nên đưa vào các phép tính hình học thông thường.
