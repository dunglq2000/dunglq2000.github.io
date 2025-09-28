Phép biến hình
==============

Trong thực tế chúng ta hay gặp các vấn đề về việc di dời một hình nào đó sang một vị trí khác trong mặt phẳng, không gian và phải đảm bảo giữ nguyên một số quan hệ nhất định. Trong đó cơ bản nhất và được ứng dụng rộng rãi là phép dời hình và phép đồng dạng.


Phép dời hình
-------------

.. prf:definition:: Phép dời hình
    :label: def-translation
    
    Phép dời hình từ hình :math:`\mathcal{H}` thành hình :math:`\mathcal{H}'` là một ánh xạ :math:`f` biến mỗi điểm thuộc hình :math:`\mathcal{H}` thành điểm thuộc hình :math:`\mathcal{H}'` sao cho khoảng cách giữa hai điểm bất kì trong :math:`\mathcal{H}` bảo toàn khi qua :math:`\mathcal{H}'`.

Nói cách khác, với mọi điểm :math:`A, B \in \mathcal{H}`, ánh xạ :math:`f` biến :math:`A` thành :math:`A'` và :math:`B` thành :math:`B'`, nghĩa là :math:`A', B' \in \mathcal{H}'`, thì :math:`A'B' = AB`.

Một số phép dời hình cơ bản là dời hình theo vector (dời theo một hướng nhất định), đối xứng qua trục, đối xứng qua tâm, quay quanh tâm hoặc quay quanh trục nào đó.


Phép dời hình theo vector
-------------------------

Phép dời hình theo vector :math:`\vec{v} \neq \vec{0}` (phép tịnh tiến) biến điểm :math:`A` thành điểm :math:`A'` sao cho :math:`\overrightarrow{AA'} = \vec{v}`.

Dễ thấy đây là phép dời hình vì với mọi :math:`A`, :math:`B` biến thành :math:`A'`, :math:`B'` ta có

.. math:: \overrightarrow{A'B'} = \overrightarrow{A'A} + \overrightarrow{AB} + \overrightarrow{BB'},
    
mà ta có

.. math:: \overrightarrow{A'A} = -\vec{v} = -\overrightarrow{BB'}
    
nên

.. math:: \overrightarrow{A'B'} = \overrightarrow{AB}.
    
Vector bằng nhau thì độ dài cũng bằng nhau. Ta có điều phải chứng minh.

.. figure:: ../../figures/geometric_transform/by_vector.*

    Tịnh tiến theo vector $\vec{a}$


Phép đối xứng qua đường thẳng cố định
-------------------------------------

Cho đường thẳng cố đinh :math:`(d)`.

Phép đối xứng qua đường thẳng :math:`(d)` biến điểm :math:`A` thành điểm :math:`A'` sao cho :math:`AA'` cắt :math:`(d)` tại trung điểm :math:`AA'` và đường thẳng đi qua :math:`AA'` vuông góc với :math:`(d)`.

.. figure:: ../../figures/geometric_transform/by_line.*

    Đối xứng qua đường thẳng :math:`(d)`


Phép đối xứng qua tâm cố định
-----------------------------

Cho điểm cố định :math:`O`.

Phép đối xứng tâm :math:`O` biến điểm :math:`A` thành điểm :math:`A'` sao cho :math:`\overrightarrow{OA} = -\overrightarrow{OA'}`. Nói cách khác :math:`O` là trung điểm đoạn thẳng :math:`AA'`.


Phép quay quanh tâm cố định
---------------------------

Cho điểm cố định :math:`O`.

Phép quay (mặc định là ngược chiều đồng hồ) quanh tâm :math:`O` theo một góc cố định :math:`\varphi` biến điểm :math:`A` thành điểm :math:`A'` sao cho

.. math:: \widehat{(\overrightarrow{OA}, \overrightarrow{OA'})} = \varphi.

Trên mặt phẳng chúng ta có thể biểu diễn phép quay dưới hệ tọa độ như sau.

Giả sử vector :math:`\overrightarrow{OA}` có độ dài là :math:`r` và hợp với trục :math:`Ox` một góc :math:`\alpha`.

Khi đó, giả sử tọa độ của :math:`\overrightarrow{OA} = (x, y)` thì ta có

.. math:: 
    
    x & = r \cos \alpha, \\
    y & = r \sin \alpha.
    
Nếu ta quay vector này quanh gốc tọa độ, ngược chiều kim đồng hồ một góc :math:`\varphi` thì thực ra góc (mới) hợp bởi vector :math:`\overrightarrow{OA'}` và trục :math:`Ox` là :math:`\alpha + \varphi`.

Do đó

.. math:: 
    
    x' & = r \cos (\alpha + \varphi), \\
    y' & = r \sin (\alpha + \varphi).
    
Khi khai triển ra

.. math:: 
    
        x' & = r \cos \alpha \cos \varphi - r \sin \alpha \sin \varphi
    = x \cos \varphi - y \sin \varphi \\
        y' & = r \sin \alpha \cos \varphi + r \cos \alpha \sin \varphi 
    = y \cos \varphi + x \sin \varphi.
    
Dễ thấy, phép quay bảo toàn khoảng cách từ tâm :math:`O` tới điểm đó. Nghĩa là :math:`OA = OA'`.

.. figure:: ../../figures/geometric_transform/rotation.*


Phép biến hình trên mặt phẳng tọa độ
------------------------------------

Gọi :math:`A = (x, y)` là tọa độ ban đầu của điểm và :math:`A' = f(A) = (x', y')` là tọa độ điểm :math:`A'`, là kết quả của phép biến hình :math:`f` lên điểm :math:`A`.

Chúng ta lần lượt xét các phép biến hình đã liệt kê ở trên và chuyển về phép nhân ma trận.

Các phép nhân ma trận cho phép chúng ta hợp các phép biến đổi liên tiếp thành một biến đổi lớn.

Giả sử :math:`\bm{A}_T` là ma trận ứng với phép tịnh tiến, :math:`\bm{A}_R` là ma trận ứng với phép quay.

Khi đó với phép nhân ma trận, nếu ta muốn thực hiện liên tiếp phép tịnh tiến và phép quay thì ta có :math:`\bm{A}_T \cdot \bm{A}_R`.

Hợp các phép dời hình không có tính giao hoán, cũng như phép nhân ma trận. Do đó thứ tự thực hiện phép dời hình khác nhau thì thứ tự nhân ma trận cũng khác nhau.

Một yêu cầu về phép biến đổi tuyến tính là không có vector tự do, nghĩa là biến đổi có dạng

.. math:: 
    
    \begin{pmatrix}
    x' \\ y'
    \end{pmatrix} = \bm{A} \cdot \begin{pmatrix}
    x \\ y
    \end{pmatrix},

với :math:`\bm{A}` là ma trận :math:`n \times n`.


Phép dời hình theo vector
^^^^^^^^^^^^^^^^^^^^^^^^^

Đặt :math:`\vec{v} = (a, b)` là vector tịnh tiến. Khi đó :math:`\overrightarrow{AA'} = \vec{v}` sẽ tương đương với

.. math:: x' - x = a, \quad y' - y = b,

hay tương đương với :math:`x' = x + a` và :math:`y' = y + b`.

Dễ thấy rằng kết quả có thể viết ở dạng:

.. math:: 
    
    \begin{pmatrix}
        x' \\ y'
    \end{pmatrix} = \begin{pmatrix}
        1 & 0 \\ 0 & 1
    \end{pmatrix} \cdot \begin{pmatrix}
        x \\ y
    \end{pmatrix} + \begin{pmatrix}
        a \\ b
    \end{pmatrix}.

Tuy nhiên chúng ta cần một biến đổi tuyến tính không có vector :math:`\begin{pmatrix} a \\ b \end{pmatrix}`.

Lúc này, thay vì sử dụng ma trận :math:`2 \times 2` thì ta chuyển thành :math:`3 \times 3` và công thức trở thành:

.. math:: 

    \begin{pmatrix}
        x' \\ y' \\ 1
    \end{pmatrix} = \begin{pmatrix}
        1 & 0 & a \\
        0 & 1 & b \\
        0 & 0 & 1
    \end{pmatrix} \cdot \begin{pmatrix}
        x \\ y \\ 1
    \end{pmatrix}.

Ma trận :math:`\begin{pmatrix} 1 & 0 & a \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}` là ma trận tịnh tiến (translation vector) tương ứng với phép tịnh tiến điểm :math:`A = (x, y)` theo vector :math:`\vec{v} = (a, b)`.


Phép đối xứng qua đường thẳng cố định
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tương tự việc tìm tọa độ hình chiếu của một điểm lên một đường thẳng cho trước, ở đây chúng ta tìm hình chiếu rồi lấy đối xứng điểm ban đầu qua tâm là hình chiếu.

Gọi :math:`(d): ax + by + c = 0` là đường thẳng bất kì. Gọi :math:`M = (x_M, y_M)` là điểm cần lấy đối xứng và :math:`N = (x_N, y_N)` là điểm đối xứng của :math:`M` qua đường thẳng :math:`(d)`.

Gọi :math:`I = (x_I, y_I)` là hình chiếu của :math:`M` lên :math:`(d)`. Khi đó :math:`I` là trung điểm của đoạn thẳng :math:`MN` và :math:`MN \perp (d)`.

Do đường thẳng :math:`MN \perp (d)` và đường thẳng :math:`(d)` có vector pháp tuyến là :math:`\bm{v} = (a, b)` nên :math:`\bm{v}` là vector chỉ phương của đường thẳng :math:`MN`.

Như vậy đường thẳng :math:`MN` có phương trình tham số

.. math:: 

    \begin{cases}
        x & = x_M + at \\
        y & = y_M + bt
    \end{cases}, \quad t \in \mathbb{R}.

Do :math:`I \in MN` nên :math:`x_I = x_M + a t_0` và :math:`y_I = y_M + b t_0`. Vì :math:`I \in (d)` nên thay tọa độ điểm :math:`I` vào phương trình đường thẳng :math:`(d)` ta có

.. math:: a (x_M + a t_0) + b (y_M + b t_0) + c = 0 \Longleftrightarrow t_0 = -\dfrac{a x_M + b y_M + c}{a^2 + b^2}.

Như vậy tọa độ điểm :math:`I` là

.. math:: 

    x_I & = x_M + a t_0 = x_M - a \dfrac{a x_M + b y_M + c}{a^2 + b^2} = \dfrac{b^2 x_M - ab y_M - ac}{a^2 + b^2},

    y_I & = y_M + b t_0 = y_M - b \dfrac{a x_M + b y_M + c}{a^2 + b^2} = \dfrac{-ab x_M + a^2 y_M - bc}{a^2 + b^2}.

Vì :math:`I` là trung điểm :math:`MN` nên

.. math:: 

    x_N & = 2 x_I - x_M = \dfrac{2(b^2 x_M - ab y_M - ac)}{a^2 + b^2} - x_M  =  \dfrac{b^2 - a^2}{a^2 + b^2} x_M - \dfrac{2ab}{a^2 + b^2} y_M - \dfrac{2ac}{a^2 + b^2},

    y_N & = 2 y_I - y_M = \dfrac{2(-ab x_M + a^2 y_M - bc)}{a^2 + b^2} - y_M = -\dfrac{2ab}{a^2 + b^2} x_M + \dfrac{a^2 - b^2}{a^2 + b^2} y_M - \dfrac{2bc}{a^2 + b^2}.

Như vậy ta cũng có thể biểu diễn phép đối xứng trục bằng phép nhân ma trận

.. math:: 

    \begin{pmatrix} x_N \\ y_N \\ 1 \end{pmatrix} = 
    \begin{pmatrix}
        \dfrac{b^2 - a^2}{a^2 + b^2} & -\dfrac{2ab}{a^2 + b^2} & -\dfrac{2ac}{a^2 + b^2} \\
        -\dfrac{2ab}{a^2 + b^2} & \dfrac{a^2 - b^2}{a^2 + b^2} & -\dfrac{2bc}{a^2 + b^2} \\
        0 & 0 & 1
    \end{pmatrix} \cdot \begin{pmatrix} x_M \\ y_M \\ 1 \end{pmatrix}.



Phép đối xứng qua tâm cố định
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Theo định nghĩa ở trên, giả sử tâm :math:`O` có tọa độ :math:`(a, b)`. Điều kiện :math:`\overrightarrow{OA} = \overrightarrow{OA'}` tương đương với:

.. math:: x - a = -(x' - a), \quad y - a = -(y' - b),

hay tương đương với

.. math:: x' = -x + 2a, \quad y' = -y + 2b.

Tương tự bên trên, ta muốn một phép nhân ma trận mà không cộng thêm vector ngoài. Ta có phép nhân

.. math:: 

    \begin{pmatrix}
        x' \\ y' \\ 1
    \end{pmatrix} = \begin{pmatrix}
        -1 & 0 & 2a \\
        0 & -1 & 2b \\
        0 & 0 & 1
    \end{pmatrix} \cdot \begin{pmatrix}
        x \\ y \\ 1
    \end{pmatrix}

Như vậy, ma trận :math:`\begin{pmatrix} -1 & 0 & 2a \\ 0 & -1 & 2b \\ 0 & 0 & 1 \end{pmatrix}` là ma trận đối xứng qua tâm :math:`O = (a, b)`.


Phép quay quanh tâm cố định
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Từ công thức của phép quay quanh tâm là gốc tọa độ:

.. math:: 
    
    \begin{pmatrix}
        x' \\ y'
    \end{pmatrix} = \begin{pmatrix}
        \cos \varphi & -\sin \varphi \\
        \sin \varphi & \cos \varphi
    \end{pmatrix} \begin{pmatrix}
        x \\ y
    \end{pmatrix},

ta thấy rằng trong các phép biến đổi trên ta cần ma trận :math:`3 \times 3` thay vì :math:`2 \times 2` nên phép quay cũng cần ma trận :math:`3 \times 3` để có thể hợp với các phép biến hình khác.

.. math:: 

    \begin{pmatrix}
        x' \\ y' \\ 1
    \end{pmatrix} = \begin{pmatrix}
        \cos\phi & -\sin\phi & 0 \\
        \sin\phi & \cos\phi & 0 \\
        0 & 0 & 1
    \end{pmatrix} \cdot \begin{pmatrix}
        x \\ y \\ 1
    \end{pmatrix}.

Như vậy ma trận :math:`\begin{pmatrix} \cos\phi & -\sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{pmatrix}` thể hiện phép quay quanh tâm :math:`O` là gốc tọa độ.
