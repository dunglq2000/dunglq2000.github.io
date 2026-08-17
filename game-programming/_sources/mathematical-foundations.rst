Nền tảng toán học của đồ họa 3D
===============================

Điểm, vector và hệ tọa độ
-------------------------

Cho :math:`\mathcal E` là một không gian affine liên kết với không gian vector
:math:`V`. Các phần tử của :math:`\mathcal E` gọi là **điểm** và được kí hiệu
bằng chữ hoa :math:`A,B,C,\ldots`. Với hai điểm :math:`A,B`, vector đi từ
:math:`A` tới :math:`B` được kí hiệu là :math:`\overrightarrow{AB}`.

Nói chính xác hơn, ta có một ánh xạ liên kết

.. math::

   \varphi:\mathcal E\times\mathcal E\longrightarrow V,
   \qquad
   (A,B)\longmapsto\varphi(A,B)=\overrightarrow{AB}.

Ánh xạ này được xác định bởi hai tính chất cơ sở. Trước hết,
với mỗi vector :math:`\bm{u}\in V` và mỗi điểm :math:`A\in\mathcal E`, tồn tại
duy nhất điểm :math:`B\in\mathcal E` sao cho

.. math:: \overrightarrow{AB}=\bm{u}.

Thứ hai, với mọi :math:`A,B,C\in\mathcal E`, ta có **hệ thức Chasles**:

.. math::

   \overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}.

Đặc biệt,

.. math::

   \overrightarrow{AA}=\bm{0},
   \qquad
   \overrightarrow{AB}=-\overrightarrow{BA}.

Như vậy điểm không phải là một bộ số hay một vector. Chỉ sau khi chọn hệ tọa
độ, điểm :math:`A` mới có tọa độ :math:`A(x_A,y_A,z_A)`.

Khi chọn gốc tọa độ :math:`O` và cơ sở
:math:`(\bm{e}_1,\bm{e}_2,\bm{e}_3)`, tọa độ của :math:`A` là bộ ba duy nhất
:math:`(x_A,y_A,z_A)` thỏa

.. math::

   \overrightarrow{OA}
   =x_A\bm{e}_1+y_A\bm{e}_2+z_A\bm{e}_3.

Do đó, với :math:`A(x_A,y_A,z_A)` và :math:`B(x_B,y_B,z_B)`, hệ thức Chasles
cho tọa độ

.. math::

   \overrightarrow{AB}
   =\overrightarrow{OB}-\overrightarrow{OA}
   =(x_B-x_A,\ y_B-y_A,\ z_B-z_A).

Cách viết này luôn giữ rõ đâu là điểm và đâu là vector.

Với :math:`\bm{u}, \bm{v} \in \mathbb{R}^3`, tích vô hướng

.. math:: \bm{u} \cdot \bm{v} = \|\bm{u}\|\, \|\bm{v}\|\cos \theta = u_x v_x + u_y v_y + u_z v_z

đo góc và phép chiếu. Hai vector trực giao khi tích vô hướng bằng :math:`0`. Tích có hướng

.. math::

   \bm{u} \times \bm{v}
   = \begin{bmatrix}
      u_yv_z - u_zv_y\\
      u_zv_x - u_xv_z\\
      u_xv_y - u_yv_x
    \end{bmatrix}

vuông góc với mặt phẳng sinh bởi :math:`\bm{u}, \bm{v}` và có độ dài bằng diện tích hình bình hành tương ứng. Chuẩn hóa vector khác không cho

.. math:: \widehat{\bm{v}} = \frac{\bm{v}}{\|\bm{v}\|}.

Phép chuẩn hóa cần ngưỡng :math:`\varepsilon` để tránh chia cho một độ dài gần :math:`0`.

Không gian affine
-----------------

Không gian vector :math:`V` trong định nghĩa được gọi là **không gian vector
liên kết**, hay **không gian nền**, của :math:`\mathcal E` và có thể kí hiệu
:math:`\overrightarrow{\mathcal E}`. Nếu :math:`V` có số chiều :math:`n` thì
:math:`\mathcal E` là không gian affine :math:`n` chiều:

.. math:: \dim\mathcal E=\dim V=n.

Không gian affine thực dùng trường :math:`\mathbb R`; không gian affine phức
dùng trường :math:`\mathbb C`. Trong đồ họa, ta chủ yếu làm việc với không gian
affine thực hai hoặc ba chiều.

Không gian vector :math:`V` tự nó có một cấu trúc affine chính tắc: xem các
phần tử của :math:`V` là điểm của không gian affine chính tắc và đặt ánh xạ
liên kết

.. math:: \varphi(\bm u,\bm v)=\bm v-\bm u.

Đây là lí do điểm và vector có thể cùng được lưu bằng một bộ số trong chương
trình. Tuy nhiên sự đồng nhất này phụ thuộc cấu trúc chính tắc hoặc hệ tọa độ;
trong hình học affine tổng quát, điểm và vector vẫn là hai loại đối tượng khác
nhau.

Từ hai tiên đề ở trên và hệ thức Chasles suy ra các tính chất cơ bản

.. math::

   \overrightarrow{AB}=\bm 0 &\Longleftrightarrow A=B,\\
   \overrightarrow{AB}&=-\overrightarrow{BA},\\
   \overrightarrow{AB}=\overrightarrow{CD}
   &\Longleftrightarrow
   \overrightarrow{AC}=\overrightarrow{BD},\\
   \overrightarrow{AB}&=\overrightarrow{OB}-\overrightarrow{OA},

trong đó :math:`O` là một điểm tùy ý ở đẳng thức cuối.

Phẳng affine
~~~~~~~~~~~~

Cho :math:`P_0\in\mathcal E` và :math:`W` là một không gian vector con của
:math:`V`. Tập hợp

.. math::

   \alpha
   =\{P\in\mathcal E:\overrightarrow{P_0P}\in W\}

được gọi là một **phẳng affine** đi qua :math:`P_0`, có không gian chỉ phương
:math:`W`. Nếu :math:`\dim W=m` thì :math:`\alpha` là một :math:`m`-phẳng và

.. math:: \dim\alpha=\dim W=m.

Điểm, đường thẳng và mặt phẳng lần lượt là :math:`0`-, :math:`1`- và
:math:`2`-phẳng. Trong không gian :math:`n` chiều, một :math:`(n-1)`-phẳng gọi
là **siêu phẳng**. Mọi điểm thuộc :math:`\alpha` đều có thể đóng vai trò
:math:`P_0`; không gian chỉ phương :math:`W` là duy nhất.

Nếu :math:`(\bm a_1,\ldots,\bm a_m)` là một cơ sở của :math:`W`, các điểm của
:math:`\alpha` được tham số hóa bởi

.. math::

   \overrightarrow{P_0P(t_1,\ldots,t_m)}
   = \sum_{i = 1}^{m} t_i \bm{a}_i.

Đường thẳng, mặt phẳng và không gian ba chiều lần lượt là các trường hợp
:math:`m = 1, 2, 3`. Biểu diễn này là cơ sở của ray, cạnh, mặt phẳng clipping và
các phép giao trong đồ họa. Một phẳng affine cũng là một không gian affine có
không gian nền :math:`W`, nên thường được gọi là không gian affine con.

Độc lập affine và bao affine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Các điểm :math:`P_0, \ldots, P_k` độc lập affine khi các vector
:math:`\overrightarrow{P_0P_1},\ldots,\overrightarrow{P_0P_k}` độc lập tuyến
tính. Định nghĩa không phụ thuộc điểm nào được chọn làm :math:`P_0`. Trong một
không gian affine :math:`n` chiều, một hệ có nhiều hơn :math:`n+1` điểm luôn
phụ thuộc affine.

**Bao affine** của một tập điểm là phẳng nhỏ nhất chứa tập đó. Sau khi chọn một
điểm :math:`O`, bao affine của :math:`P_0,\ldots,P_k` gồm các điểm :math:`P`
thỏa

.. math::

   \overrightarrow{OP} = \sum_{i = 0}^{k} \lambda_i \overrightarrow{OP_i},
   \qquad
   \sum_{i = 0}^{k} \lambda_i = 1.

Nếu thêm điều kiện :math:`\lambda_i \geqslant 0`, ta nhận được bao lồi. Với ba
đỉnh của tam giác, các :math:`\lambda_i` chính là tọa độ barycentric; chúng
vừa kiểm tra một điểm có nằm trong tam giác vừa nội suy thuộc tính đỉnh.

Tâm tỉ cự
~~~~~~~~~

Cho các điểm :math:`P_1,\ldots,P_k` và các hệ số
:math:`\lambda_1,\ldots,\lambda_k` có tổng
:math:`\lambda=\sum_i\lambda_i\ne0`. **Tâm tỉ cự** tương ứng là điểm duy nhất
:math:`G` thỏa

.. math::

   \overrightarrow{OG}
   =\frac{1}{\lambda}
    \sum_{i=1}^k\lambda_i\overrightarrow{OP_i}.

Điểm :math:`G` không phụ thuộc vào điểm :math:`O` đã chọn. Một đặc trưng tương
đương, hoàn toàn nội tại, là

.. math:: \sum_{i=1}^k\lambda_i\overrightarrow{GP_i}=\bm 0.

Khi mọi :math:`\lambda_i=1`, điểm :math:`G` là trọng tâm:

.. math::

   \overrightarrow{OG}=\frac1k\sum_{i=1}^k\overrightarrow{OP_i}.

Trọng tâm được dùng để tìm tâm tam giác, tâm một mặt đa giác và điểm đại diện
cho một cụm đỉnh.

Mục tiêu affine và đổi hệ tọa độ
--------------------------------

Một mục tiêu affine gồm gốc :math:`O` và một cơ sở
:math:`(\bm{e}_1, \ldots, \bm{e}_n)`. Tọa độ
:math:`(x_1,\ldots,x_n)` của điểm :math:`P` được xác định bởi

.. math:: \overrightarrow{OP} = \sum_{i = 1}^{n} x_i \bm{e}_i.

Nếu :math:`P(x_1,\ldots,x_n)` và :math:`Q(y_1,\ldots,y_n)` thì

.. math::

   \overrightarrow{PQ}
   =\sum_{i=1}^n(y_i-x_i)\bm e_i.

Nếu mục tiêu mới có gốc :math:`O'` với
:math:`\overrightarrow{OO'}=\bm{b}` và ma trận :math:`C` chứa các vector cơ sở
mới viết trong cơ sở cũ, thì hai cột tọa độ :math:`\bm{x}` và
:math:`\bm{x}'` của cùng điểm :math:`P` liên hệ bởi

.. math:: \bm{x} = C \bm{x}' + \bm{b}.

Đây là dạng tổng quát của phép đổi model space sang world space hoặc world
space sang camera space. Điều kiện :math:`\det C\ne0` bảo đảm hai họ vector cơ
sở đều là cơ sở và phép đổi tọa độ khả nghịch.

Ánh xạ affine
~~~~~~~~~~~~~

Cho :math:`\mathcal E,\mathcal E'` là hai không gian affine. Ánh xạ điểm
:math:`f:\mathcal E\to\mathcal E'` là **ánh xạ affine** nếu tồn tại một ánh xạ
tuyến tính :math:`\vec f:V\to V'` sao cho với mọi điểm :math:`P,Q`,

.. math::

   \overrightarrow{f(P)f(Q)}
   =\vec f\left(\overrightarrow{PQ}\right).

Ánh xạ :math:`\vec f` gọi là ánh xạ tuyến tính liên kết của :math:`f`. Một ánh
xạ affine được xác định duy nhất khi biết :math:`\vec f` và ảnh của một điểm;
hợp của hai ánh xạ affine vẫn là ánh xạ affine. Trong một mục tiêu tọa độ,
:math:`f` được mô tả bởi

.. math:: [f(P)] = A[P] + \bm{t},

trong đó :math:`[P]` và :math:`[f(P)]` lần lượt là cột tọa độ của hai điểm,
không phải chính các điểm đó.

Nó bảo toàn các phẳng, đường thẳng, tính song song, tâm tỉ cự và tổ hợp affine.
Độ dài và góc chỉ được bảo toàn khi phần tuyến tính :math:`A` là một phép đẳng
cự. Phép chiếu song song là một ví dụ quan trọng của ánh xạ affine; phép chiếu
phối cảnh nói chung không phải ánh xạ affine trong không gian Euclid ba chiều.

Tọa độ thuần nhất
-----------------

Tịnh tiến không phải phép biến đổi tuyến tính trên không gian vector tọa độ. Ta
biểu diễn tọa độ thuần nhất của điểm :math:`A(x_A,y_A,z_A)` và vector
:math:`\bm{v}=(v_x,v_y,v_z)` lần lượt bởi

.. math::

   [A]_h = (x_A, y_A, z_A, 1)^{\mathsf T},
   \qquad
   [\bm{v}]_h = (v_x, v_y, v_z, 0)^{\mathsf T}.

Khi đó cả tịnh tiến, quay, co giãn và phép chiếu phối cảnh đều có thể biểu diễn bằng ma trận :math:`4 \times 4`. Với quy ước vector cột,

.. math:: [A']_h = M[A]_h.

Nếu dùng vector hàng thì thứ tự nhân ma trận phải đảo lại. Không được trộn hai quy ước trong cùng một phép tính.

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

Với vector cột, phép ở bên phải tác động trước: mô hình được co giãn, quay rồi mới tịnh tiến. Nói chung :math:`RT \neq TR`, nên đổi thứ tự có thể biến một phép tự quay thành phép quay quanh một tâm bên ngoài. Nếu tâm quay là :math:`C(c_x,c_y,c_z)`, phép quay quanh :math:`C` được thực hiện bởi

.. math:: M = T(c_x,c_y,c_z)R T(-c_x,-c_y,-c_z).

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

Tổng Riemann và sự rời rạc hóa
------------------------------

Tích phân là một ví dụ cơ bản về cách xấp xỉ một đối tượng liên tục bằng các
đối tượng rời rạc dễ xử lý. Xét đường cong :math:`y=f(x)>0` trên đoạn
:math:`[a,b]`. Tích phân

.. math:: \int_a^b f(x)\,dx

là diện tích phần hình phẳng giới hạn bởi đường cong :math:`y=f(x)`, trục
hoành và hai đường thẳng :math:`x=a`, :math:`x=b`. Trong
:numref:`fig-riemann-area`, phần tô màu là diện tích dưới đồ thị
:math:`f(x)=-x^2+4` từ :math:`-2` tới :math:`2`.

.. figure:: figures/riemann_sum-01.*
   :name: fig-riemann-area
   :align: center

   Tích phân từ :math:`-2` tới :math:`2` của hàm số :math:`f(x)=-x^2+4`.

Ta có thể tính chính xác diện tích hình chữ nhật, hình vuông hoặc hình thang.
Để tính diện tích giới hạn bởi một đường cong bất kì, ta xấp xỉ nó bằng tổng
diện tích các hình chữ nhật. Chia đoạn :math:`[a,b]` thành :math:`n` phần bằng
nhau:

.. math::

   a=x_0<x_1<\cdots<x_{n-1}<x_n=b,
   \qquad x_i-x_{i-1}=\frac{b-a}{n}.

Trên đoạn :math:`[x_{i-1},x_i]`, chọn chiều cao hình chữ nhật là
:math:`f(x_i)`, tức dùng đầu mút bên phải. Tổng diện tích các hình chữ nhật là

.. math::

   S_n
   =\sum_{i=1}^n(x_i-x_{i-1})f(x_i)
   =\sum_{i=1}^n\frac{b-a}{n}f(x_i),
   \qquad
   x_i=a+\frac{b-a}{n}i.

Các hình sau lần lượt dùng :math:`8`, :math:`16` và :math:`32` hình chữ nhật.

.. figure:: figures/riemann_sum-02.*
   :name: fig-riemann-8
   :align: center

   Xấp xỉ diện tích bởi :math:`8` hình chữ nhật.

.. figure:: figures/riemann_sum-03.*
   :name: fig-riemann-16
   :align: center

   Xấp xỉ diện tích bởi :math:`16` hình chữ nhật.

.. figure:: figures/riemann_sum-04.*
   :name: fig-riemann-32
   :align: center

   Xấp xỉ diện tích bởi :math:`32` hình chữ nhật.

Khi số hình chữ nhật tăng, tổng diện tích tiến tới diện tích cần tìm:

.. math::

   \int_a^b f(x)\,dx
   =\lim_{n\to\infty}
    \sum_{i=1}^n\frac{b-a}{n}f\left(a+\frac{b-a}{n}i\right).

Ví dụ tính tích phân qua tổng Riemann
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Với :math:`f(x)=-x^2+4`, :math:`a=-2` và :math:`b=2`, ta có

.. math::

   \begin{aligned}
   \frac{b-a}{n}f(x_i)
   &=\frac{4}{n}\left[-\left(-2+\frac{4i}{n}\right)^2+4\right]\\
   &=\frac{64}{n}\left(\frac{i}{n}-\frac{i^2}{n^2}\right).
   \end{aligned}

Dùng hai công thức

.. math::

   \sum_{i=1}^n i=\frac{n(n+1)}{2},
   \qquad
   \sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}{6},

ta nhận được

.. math::

   \begin{aligned}
   S_n
   &=\frac{64}{n^2}\sum_{i=1}^n i
     -\frac{64}{n^3}\sum_{i=1}^n i^2\\
   &=\frac{32(n+1)}{n}
     -\frac{32(n+1)(2n+1)}{3n^2}.
   \end{aligned}

Cho :math:`n` tiến tới vô cực, suy ra

.. math::

   \int_{-2}^{2}(-x^2+4)\,dx
   =32-\frac{64}{3}
   =\frac{32}{3}.

Nguyên lý này xuất hiện khắp đồ họa máy tính. Một đường cong được thay bằng
chuỗi đoạn thẳng; một mặt cong được chia thành các tam giác hoặc tứ giác; một
miền ảnh liên tục được lấy mẫu trên lưới pixel. Khi kích thước các phần tử giảm,
mô hình rời rạc mô tả hình liên tục chính xác hơn, nhưng số phép tính và lượng
bộ nhớ cũng tăng. Vì vậy tessellation và rasterization luôn phải cân bằng giữa
độ chính xác và chi phí tính toán.

Mesh tam giác
-------------

Một bề mặt cong được xấp xỉ bởi **triangle mesh**. Dữ liệu hình học thường gồm:

- vertex buffer chứa vị trí, pháp tuyến, màu, tọa độ texture hoặc tangent;
- index buffer mô tả các tam giác bằng chỉ số đỉnh;
- topology chỉ cách ghép các chỉ số thành điểm, đoạn hoặc tam giác.

.. figure:: figures/rectangle.*
   :name: fig-mesh-rectangle

   Một hình chữ nhật được chia thành hai tam giác dùng chung hai đỉnh.

Thay vì lưu sáu đỉnh lặp, ta lưu :math:`(v_0, v_1, v_2, v_3)` và dãy chỉ số :math:`(0, 1, 2, 0, 2, 3)`. Thứ tự đỉnh, hay **winding order**, quyết định hướng pháp tuyến và mặt trước của tam giác.

Với tam giác :math:`ABC`, một pháp tuyến chưa chuẩn hóa là

.. math:: \bm{n} = \overrightarrow{AB} \times \overrightarrow{AC}.

Nếu :math:`\|\bm{n}\|` gần :math:`0`, tam giác suy biến và không nên đưa vào các phép tính hình học thông thường.
