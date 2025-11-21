Lý thuyết lập trình game
########################

Phần này mình sẽ trình bày các lý thuyết cơ bản trong lập trình game và sử dụng DirectX 11 để demo. Tài liệu tham khảo chính là :cite:`LunaDX11`.

Model presentation
******************

Mỗi object 3D được biểu diễn dưới dạng xấp xỉ các tam giác, gọi là tam giác mesh, liền kề nhau và tạo nên mô hình 3D.

Để tùy chỉnh độ mạnh yếu (intensity) của ánh sáng, ta sử dụng số thực từ :math:`0` tới :math:`1`.

Ví dụ, trong hệ màu RGB thì :math:`(0,25; 0,67; 1,00)` biểu diễn :math:`25\%` độ mạnh màu đỏ, :math:`67\%` độ mạnh màu xanh lá và :math:`100\%` độ mạnh màu xanh dương.

Như vậy, trong hệ màu RGB, màu sắc được biểu diễn bởi vector :math:`(r, g, b)` với :math:`0 \leqslant r, g, b \leqslant 1`.

Color Operations
================

Ta có thể cộng, trừ hai màu :math:`(r_1, g_1, r_1)` và :math:`(r_2, g_2, b_2)` thì được kết quả

.. math:: (r_1, g_1, b_1) \pm (r_2, g_2, b_2) = (r_1 \pm r_2, g_1 \pm g_2, b_1 \pm b_2).


Modulation hay componentwise multiplication (nhân đôi một) thực hiện phép nhân theo từng vị trí

.. math:: (r_1, g_1, b_1) \otimes (r_2, g_2, b_2) = (r_1 r_2, g_1 g_2, b_1 b_2).

128-bit color
=============

Một thành phần bổ sung ngoài R, G, B là A (alpha). Alpha xác định độ mờ (opacity) trong *blending*.

Khi đó, để xác định màu có alpha ta dùng vector bốn chiều :math:`(r, g, b, a)` với :math:`0 \leqslant r, g, b, a \leqslant 1`.

32-bit color
============

Để biểu diễn màu với :math:`32` bit, mỗi thành phần :math:`(r, g, b, a)` được biểu diễn bởi một byte. Tương tự, :math:`0` là độ mạnh thấp nhất (không có) và :math:`255` là độ mạnh lớn nhất.

.. note:: 

    Màu 32-bit có thể chuyển thành màu 128-bit bằng việc chia cho :math:`255` vì mỗi thành phần đều nằm thỏa :math:`0 \leqslant n \leqslant 255` nên :math:`0 \leqslant n / 255 \leqslant 1`.

    Ngược lại, màu 128-bit có thể chuyển thành màu 32-bit bằng phép nhân cho :math:`255` và làm tròn tới số nguyên gần nhất.

Trong DirectX, ``XMCOLOR`` biểu diễn alpha, red, green, blue theo thứ tự.

Rendering Pipeline
******************

Rendering Pipeline bao gồm các công đoạn được thể hiện ở :numref:`hình %s <fig-rendering-pipeline>`.

.. _fig-rendering-pipeline: 

.. figure:: rendering-pipeline.*
    
    Rendering Pipeline

Input Assembler Stage
*********************

Công đoạn Input Assembler (IA) đọc các dữ liệu hình học, bao gồm đỉnh (vertice) và chỉ số (indice), để thành lập các cơ chế (primitive) hình học như điểm, đường thẳng, tam giác.

Vertex
======

Đỉnh là một điểm trong không gian.

Primitive Topology
==================

Đỉnh được đóng gói (bound) và rendering pipeline bởi **vertex buffer**, là một cấu trúc dữ liệu trong DirectX.

Sử dụng **primitive topology** ta chỉ định liên kết giữa các đỉnh để hình thành các đối tượng hình học (đỉnh đơn, đoạn thẳng nối hai đỉnh, tam giác nối ba đỉnh, ...).

.. code-block:: C++

    void ID3D11DeviceContext::IASetPrimitiveTopology(...);

Khi ta có một danh sách các đỉnh thì có thể áp dụng một trong các topology sau để vẽ chúng.

1. Point List: mỗi đỉnh được vẽ như một đỉnh độc lập.
2. Line Strip: các đỉnh thành lập các đoạn thẳng nối liền nhau. Giả sử ta có :math:`n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_n` thì ta vẽ :math:`n-1` cạnh là :math:`v_1 v_2`, :math:`v_2 v_3`, ..., :math:`v_{n-1} v_n`.
3. Line List: cứ hai đỉnh sẽ vẽ một cạnh. Giả sử ta có :math:`2n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_{2n}` thì ta vẽ :math:`n` cạnh :math:`v_1 v_2`, :math:`v_3 v_4`, ..., :math:`v_{2n-1} v_{2n}`.
4. Triangle Strip: các đỉnh thành lập các tam giác nối liền nhau. Giả sử ta có :math:`n` đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_n` thì ta vẽ :math:`n-2` tam giác :math:`v_1 v_2 v_3`, :math:`v_2 v_3 v_4`, ..., :math:`v_{n-2} v_{n-1} v_n`.
5. Triangle List: cứ ba đỉnh ta vẽ một tam giác. Khi đó với :math:`3n` đỉnh ta có :math:`n` tam giác.
6. Primitives with Adjacency: một triangle list được gọi là adjacency nếu một tam giác kề với một tam giác khác.
7. Control Point Patch List: optional cho tessellation stage.

Index
=====

Ta sử dụng chỉ số (index) thay vì đỉnh (vertex) nhằm giảm bộ nhớ lưu trữ và xử lý.

Xét :numref:`hình %s <fig-rectangle>`. Hình chữ nhật được tạo từ bốn đỉnh :math:`v_0`, :math:`v_1`, :math:`v_2` và :math:`v_3`.

.. _fig-rectangle: 

.. figure:: rectangle.*

    Hình chữ nhật ghép từ hai hình tam giác

Ta có thể lưu mảng các đỉnh và sau đó là mảng các chỉ số tương ứng với từng tam giác.

.. code-block:: C++

    Vertex v[4] = { v0, v1, v2, v3 };

    UINT indice[6] = {
        0, 1, 2, // tam giác v0 -> v1 -> v2
        0, 2, 3, // tam giác v0 -> v2 -> v3
    };

Một điều cần lưu ý là thứ tự đỉnh trong các tam giác phải giống nhau (cùng chiều hoặc ngược chiều kim đồng hồ). Lý do cho việc này là để xác định mặt trước và sau, và sẽ được giải thích rõ hơn trong công đoạn *culling*.

Vertex Shader Stage
*******************

Sau khi chỉ định primitives để assembler, các đỉnh sẽ được chuyển tới vertex shader stage.

Có thể hiểu rằng, vertex shader stage lấy đầu vào là từng đỉnh và đầu ra cũng là đỉnh.

Hàm ``VertexShader`` chúng ta cài đặt để chỉ dẫn cho GPU xử lý.

Các công dụng của vertex shader gồm:

- transformation: là các phép biến hình, bao gồm tịnh tiến (translation), quay (rotation) và co dãn (scale);
- lighting: ánh sáng;
- displacement mapping (?).

Chúng ta không những có thể truy cập dữ liệu của input vertex mà còn truy cập được texture, ma trận của phép biến hình, scene light.

Local Space và World Space
==========================

World Space là hệ tọa độ toàn cục (global) chứa tất cả object trong không gian 3D.

Đôi khi một object sẽ có vị trí tương đối so với object khác thay vì gốc tọa độ. Ví dụ cánh tay gắn với cơ thể thì local space sẽ dễ dùng hơn.

Local Space là hệ tọa độ gắn với một object nào đó và xác định vị trí của một số object khác theo vị trí tương đối đối với object làm gốc.

Câu hỏi là: làm sao dời tất cả object từ local space tới world space? Chúng ta sẽ sử dụng phép biến đổi world transform và tính toán trên world matrix.

Thuận lợi khi dùng world transform là:

1. Đơn giản: thông thường trong local space thì object nằm ở tâm nên sẽ dễ dàng tính theo world space.
2. Một object có thể dùng trong nhiều scene khác nhau nên không cần thiết phải chỉ định tọa độ cố định world space (không phải chỉ định tọa độ cho từng scene).
3. Đôi khi ta vẽ cùng object nhiều lần trên scene nhưng khác tọa độ, hướng, kích cỡ. Mỗi lần vẽ ta gọi là một *instance*.

Giả sử:

- :math:`\bm{Q}_w = (Q_x, Q_y, Q_z)` là tọa độ của object ban đầu;
- :math:`\bm{u}_w = (u_x, u_y, u_z)` là trục :math:`x` của local space;
- :math:`\bm{v}_w = (v_x, v_y, v_z)` là trục :math:`y` của local space;
- :math:`\bm{w}_w = (w_x, w_y, w_z)` là trục :math:`z` của local space;

Khi đó ma trận chuyển từ local space sang world space là

.. math:: 

    \bm{W} = \begin{pmatrix}
        u_x & u_y & u_z & 0 \\
        v_x & v_y & v_z & 0 \\
        w_x & w_y & w_z & 0 \\
        Q_x & Q_y & Q_z & 1
    \end{pmatrix}.

Thông thường :math:`\bm{W}` là một dãy các biến đôi liên tiếp, ví dụ :math:`\bm{W} = \bm{S} \bm{R} \bm{T}`, trong đó:

- :math:`\bm{S}` là ma trận co dãn (scale matrix);
- :math:`\bm{R}` là ma trận xoay (rotation matrix);
- :math:`\bm{T}` là ma trận tịnh tiến (translation matrix).

Ví dụ:

.. math:: 

    \bm{S} = \begin{pmatrix}
        2 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 2 & 1 \\
        0 & 0 & 0 & 1 \\
    \end{pmatrix}, \ \bm{R} = \begin{pmatrix}
        \sqrt{2} / 2 & 0 & -\sqrt{2} / 2 & 0 \\
        0 & 1 & 0 & 0 \\
        \sqrt{2} / 2 & 0 & \sqrt{2} / 2 & 0 \\
        0 & 0 & 0 & 1
    \end{pmatrix}, \ \bm{T} = \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        10 & 0 & 10 & 1
    \end{pmatrix}.

Khi đó

.. math:: 
    
    \bm{W} = \bm{S} \bm{R} \bm{T} = \begin{pmatrix}
        \sqrt{2} & 0 & -\sqrt{2} & 0 \\
        0 & 1 & 0 & 0 \\
        \sqrt{2} & 0 & \sqrt{2} & 0 \\
        10 & 0 & 10 & 1
    \end{pmatrix}
