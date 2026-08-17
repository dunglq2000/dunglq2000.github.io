Phép chiếu đa diện và khử đường khuất
=====================================

Bài toán
--------

Project trong thư mục ``polyhedron`` dựng hình chiếu trực giao của một đa diện lên mặt phẳng :math:`Oxy` và chỉ giữ những phần cạnh nhìn thấy. Hướng quan sát cố định là

.. math:: \bm{V} = (0, 0, 1).

Điểm có tọa độ :math:`z` lớn hơn nằm gần người quan sát hơn. Một mặt phía trên che phần cạnh phía dưới khi hình chiếu của cạnh nằm trong hình chiếu của mặt.

Khác depth buffer, thuật toán này không rasterize toàn bộ bề mặt. Nó biểu diễn chính xác mỗi cạnh bằng một tham số liên tục và trừ khỏi cạnh các khoảng bị từng mặt che. Kết quả phù hợp với wireframe và bản vẽ kỹ thuật.

Dữ liệu đa diện
---------------

Lớp ``R3`` trong ``polyhedron/common/r3.py`` lưu bộ ba tọa độ. Về mặt
hình học, tài liệu vẫn phân biệt điểm :math:`A, B, \ldots` với vector
:math:`\bm{u}, \bm{v}, \ldots`. Các phép toán vector mà lớp hỗ trợ gồm

.. math::

   \bm{u} + \bm{v}, \quad
   \bm{u} - \bm{v}, \quad
   k \bm{u}, \quad
   \bm{u} \cdot \bm{v}, \quad
   \bm{u} \times \bm{v}.

Khi nạp mô hình, mỗi đỉnh được co giãn và quay theo góc Euler :math:`z`--:math:`y`--:math:`z`:

.. math:: [P'] = c R_z(\gamma)R_y(\beta)R_z(\alpha) [P].

Ở đây :math:`[P]` là cột tọa độ của điểm :math:`P` trong hệ quy chiếu
đang dùng, không phải bản thân điểm.

Thứ tự phép quay là thiết yếu vì các ma trận quay không giao hoán.

Tệp ``.geom`` lưu số đỉnh :math:`n_v`, số mặt :math:`n_f` và số cạnh mô tả :math:`n_e`. Mỗi mặt được cho bởi một chu trình chỉ số

.. math:: i_1 \to i_2 \to \cdot s \to i_k \to i_1.

Các giả thiết hình học của hiện thực:

- mỗi mặt phẳng và lồi;
- các đỉnh mặt được sắp theo thứ tự đi quanh biên;
- hai mặt chung cạnh dùng cùng hai đỉnh, dù có thể ngược hướng;
- các cạnh trùng được hợp nhất trước khi xét che khuất.

Phép chiếu và tọa độ màn hình
-----------------------------

Phép chiếu trực giao là

.. math:: \Pi(x, y, z) = (x, y).

``TkDrawer`` đổi tọa độ phẳng sang pixel bằng

.. math::

   X = \frac{\mathrm{SIZE}}{2} + \mathrm{SCALE}\, x,
   \qquad
   Y = \frac{\mathrm{SIZE}}{2} - \mathrm{SCALE}\, y.

Dấu trừ ở :math:`Y` bù cho trục dọc của canvas hướng xuống.

.. figure:: figures/polyhedron-visibility-comparison.*
   :name: fig-polyhedron-hidden-line-removal
   :align: center
   :width: 82%

   Phép chiếu trực giao của ba mô hình ``box.geom``, ``ccc.geom`` và
   ``cube.geom``. Cột trái chứa toàn bộ cạnh sau phép chiếu; cột phải chỉ chứa
   các khoảng cạnh còn nhìn thấy sau khi khử đường khuất. Kí hiệu
   :math:`\odot` cho biết hướng :math:`\bm V=(0,0,1)` vuông góc và đi ra khỏi
   mặt phẳng hình vẽ.

Tham số hóa cạnh
----------------

Các hình tiếp theo dùng một phép tính cụ thể từ ``ccc.geom``. Ta xét cạnh
:math:`B=P_4` tới :math:`F=P_1` và mặt che
:math:`(P_5P_6P_7P_8)`. Ta chỉ áp dụng các góc quay Euler ghi trong tệp và bỏ
qua hệ số co giãn :math:`c=40`, vì hệ số này không thay đổi quan hệ che khuất.
Khi đó

.. math::

   B=(1.531,4.419,-1.768),
   \qquad F=(0,0,0).

Gọi :math:`B` và :math:`F` là hai đầu mút của một cạnh. Điểm :math:`E(t)`
trên cạnh được xác định bằng hệ thức

.. math::

   \overrightarrow{BE(t)} = t\,\overrightarrow{BF},
   \qquad 0 \leqslant t \leqslant 1.

.. figure:: figures/polyhedron-edge-parameterization.*
   :name: fig-polyhedron-edge-parameterization
   :align: center
   :width: 88%

   Tham số hóa cạnh :math:`P_4P_1`. Điểm cắt sẽ được tính ở dưới là
   :math:`E(0.555051)=(0.681,1.966,-0.787)`.

Mỗi cạnh ban đầu có tập khoảng nhìn thấy

.. math:: G = \{[0, 1]\}.

Nếu một mặt che khoảng :math:`S`, ta cập nhật

.. math:: G \leftarrow G \setminus S.

Hiệu hai đoạn có thể tách một đoạn thành hai. Vì vậy
``Segment.subtraction()`` sinh các phần bên trái và phải rồi loại đoạn suy
biến :math:`t_0 \geqslant t_1`. Cuối cùng mỗi khoảng :math:`[a, b]` còn
lại được đổi thành đoạn hình học từ :math:`E(a)` tới :math:`E(b)`.

Nửa không gian phía sau mặt
---------------------------

Với ba đỉnh đầu :math:`P_0, P_1, P_2` của mặt, pháp tuyến là

.. math::

   \bm{n}
   = \overrightarrow{P_0P_1} \times \overrightarrow{P_0P_2}.

Chọn dấu để :math:`\bm{n}_h \cdot \bm{V} \geqslant 0`. Nửa không gian nằm sau mặt đối với người quan sát là

.. math:: \bm{n}_h \cdot \overrightarrow{P_0X} < 0.

.. figure:: figures/polyhedron-behind-halfspace.*
   :name: fig-polyhedron-behind-halfspace
   :align: center
   :width: 76%

   Lát cắt vuông góc với mặt che. Với mặt :math:`(P_5P_6P_7P_8)`, pháp tuyến
   hướng về người quan sát là
   :math:`\bm n_h=(-6.25,10.825318,21.650635)`, tương ứng với pháp tuyến đơn
   vị :math:`\widehat{\bm n}_h=(-0.25,0.433013,0.866025)`. Cả :math:`B` và
   :math:`F` đều nằm phía sau mặt và :math:`h(B)=h(F)=-75`.

Mặt đứng thỏa :math:`\bm{n}_h \cdot \bm{V} = 0`; hình chiếu của nó có diện tích bằng :math:`0` nên không tạo miền che hai chiều.

Miền bên trong hình chiếu mặt
-----------------------------

Với cạnh biên từ :math:`P_{k - 1}` tới :math:`P_k`, mặt phẳng đứng đi qua cạnh và song song hướng nhìn có pháp tuyến

.. math::

   \bm{n}_{v, k}
   = \overrightarrow{P_{k-1}P_k} \times \bm{V}.

Dấu của mỗi pháp tuyến được chỉnh sao cho tâm mặt :math:`C`, xác định bởi

.. math::

   \overrightarrow{OC}
   = \frac{1}{m} \sum_{i = 0}^{m - 1} \overrightarrow{OP_i},

nằm trong nửa không gian được giữ; :math:`O` là gốc tọa độ. Vì mặt lồi,
hình chiếu của điểm :math:`X` nằm trong mặt khi và chỉ khi

.. math::

   \bm{n}_{v, k} \cdot \overrightarrow{P_{k-1}X} < 0,
   \qquad k = 0, \ldots, m - 1.

Đây là biểu diễn một đa giác lồi bằng giao các nửa không gian. Nếu mặt không lồi, giao này không còn mô tả đúng miền trong và cần triangulation hoặc một thuật toán point-in-polygon tổng quát.

.. figure:: figures/polyhedron-projected-interior.*
   :name: fig-polyhedron-projected-interior
   :align: center
   :width: 55%

   Hình chiếu mặt :math:`(P_5P_6P_7P_8)` là giao của bốn nửa không gian đứng.
   Phần đỏ của cạnh :math:`BF` nằm trong miền giao; phần xám đã đi ra ngoài
   qua biên chứa :math:`P_5P_6`.

Cắt cạnh bởi một nửa không gian
-------------------------------

Cho mặt phẳng biên đi qua điểm :math:`A` với pháp tuyến ngoài
:math:`\bm{n}`. Trên cạnh tại điểm :math:`E(t)`, đặt

.. math::

   h(t) = \bm{n} \cdot \overrightarrow{AE(t)}
       = (1 - t)h_0 + t h_1,

trong đó

.. math::

   h_0 = \bm{n} \cdot \overrightarrow{AB},
   \qquad
   h_1 = \bm{n} \cdot \overrightarrow{AF}.

Mã giữ nửa không gian :math:`h(t) < 0`. Nếu hai đầu nằm khác phía và :math:`h_1 \neq h_0`, tham số giao là

.. math:: t_* = -\frac{h_0}{h_1 - h_0}.

Tùy dấu :math:`h_0`, phần hợp lệ là :math:`[0, t_*]` hoặc :math:`[t_*, 1]`. Lặp phép cắt với các nửa không gian là một phiên bản một chiều của thuật toán clipping đa giác.

Trong ví dụ đang xét, biên đứng chứa :math:`P_5P_6` cho

.. math::

   h_0=-12.017207,
   \qquad h_1=9.633428,
   \qquad t_*=0.555051.

Do :math:`h_0<0`, khoảng thỏa nửa không gian này là :math:`[0,t_*]`.

.. figure:: figures/polyhedron-halfspace-clipping.*
   :name: fig-polyhedron-halfspace-clipping
   :align: center
   :width: 82%

   Hàm affine :math:`h(t)` đổi dấu tại :math:`t_*`. Phép cắt giữ phần màu đỏ
   nằm trong nửa không gian :math:`h_v<0`.

Khoảng cạnh bị che
------------------

Đoạn cạnh bị một mặt che là giao

.. math::

   S = [0, 1] \cap H_h \cap \bigcap_{k = 0}^{m - 1} H_{v, k},

trong đó :math:`H_h` là điều kiện nằm sau mặt và :math:`H_{v, k}` là các điều kiện nằm trong hình chiếu mặt. Nếu :math:`S` không suy biến, nó bị trừ khỏi tập ``gaps`` của cạnh.

Một cạnh có thể bị nhiều mặt che trên các khoảng khác nhau, nên kết quả cuối có thể gồm nhiều đoạn nhìn thấy rời nhau.

Đối với cạnh :math:`P_4P_1`, điều kiện phía sau mặt và ba trong bốn điều kiện
đứng đều cho toàn khoảng :math:`[0,1]`; chỉ biên :math:`P_5P_6` rút khoảng còn
:math:`[0,0.555051]`. Vì vậy

.. math::

   S=[0,0.555051],
   \qquad
   G\setminus S=[0.555051,1].

.. figure:: figures/polyhedron-hidden-interval.*
   :name: fig-polyhedron-hidden-interval
   :align: center
   :width: 94%

   Giao các điều kiện nửa không gian tạo khoảng bị che :math:`S` (đỏ). Phần
   bù trong khoảng cạnh ban đầu là đoạn còn nhìn thấy (xanh lá).

So sánh với back-face culling và depth buffer
----------------------------------------------

Ba khái niệm visibility này không giống nhau:

- **back-face culling** loại toàn bộ tam giác dựa trên orientation, không xét mặt khác có che nó hay không;
- **depth buffer** chọn fragment gần nhất tại mỗi sample sau rasterization;
- **khử đường khuất hình học** tính trực tiếp các khoảng cạnh bị mặt che trong không gian liên tục.

Với ảnh tô kín, depth buffer đơn giản và hiệu quả hơn. Với wireframe vector cần đường biên chính xác, thuật toán khoảng tham số tránh phụ thuộc độ phân giải raster.

Tối ưu bằng cấu trúc không gian
-------------------------------

Thuật toán cơ sở duyệt mọi cặp cạnh--mặt, có chi phí :math:`O(EF)`. ``optimize_7`` giảm số ứng viên bằng các bước:

1. loại cạnh trùng;
2. tiền tính tâm, pháp tuyến, cờ mặt đứng, :math:`z_{\max}` và bounding box;
3. bỏ mặt nếu cạnh chắc chắn nằm phía trước;
4. chia mặt phẳng chiếu thành lưới đều và chỉ xét các mặt thuộc ô mà cạnh đi qua.

Bounding box của mặt là

.. math:: [x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}].

Mỗi mặt được đưa vào các ô giao bounding box. Khi xử lý một cạnh, tập ``processed`` ngăn cùng một mặt bị xét nhiều lần qua nhiều ô. Lưới không thay đổi tiêu chuẩn che khuất; nó chỉ giảm số phép cắt thực tế.

Các cấu trúc thay thế cho lưới đều gồm quadtree, BVH và k-d tree. Chúng hữu ích khi mật độ hình học phân bố không đều.

Độ ổn định số
--------------

So sánh số thực chính xác như :math:`h = 0` hoặc :math:`\bm{n} \cdot \bm{V} = 0` không ổn định với dữ liệu gần đồng phẳng. Nên dùng ngưỡng tỉ lệ theo dữ liệu, chẳng hạn

.. math:: |h| \leqslant \varepsilon.

Các trường hợp cần xử lý riêng:

- cạnh có hình chiếu gần một điểm;
- tam giác hoặc mặt có diện tích gần :math:`0`;
- mẫu số :math:`h_1 - h_0` gần :math:`0`;
- khoảng giao chỉ chạm tại một đầu mút;
- kích thước ô lưới bằng hoặc gần :math:`0`.

Ánh xạ lý thuyết sang mã
------------------------

.. list-table::
   :header-rows: 1

   * - Khái niệm
     - Hiện thực
   * - Vector, tích vô hướng, tích có hướng và phép quay
     - ``polyhedron/common/r3.py``
   * - Đổi tọa độ sang canvas
     - ``polyhedron/common/tk_drawer.py``
   * - Khoảng tham số và phép hiệu
     - ``Segment`` trong các file ``polyedr.py``
   * - Nội suy cạnh và cắt nửa không gian
     - ``Edge``
   * - Pháp tuyến, tâm và bounding box
     - ``Facet``
   * - Đọc mô hình và điều phối
     - ``Polyedr``
   * - Lưới không gian và lọc ứng viên
     - ``polyhedron/optimize_7/polyedr.py``

Các bước phát triển nằm trong ``noshadow/``, ``shadow/``, ``preoptimize/`` và ``optimize_1/`` tới ``optimize_7/``. Bộ kiểm thử trong ``polyhedron/tests`` kiểm tra vector, đoạn tham số, giao nửa không gian, pháp tuyến và quá trình nạp mô hình.
