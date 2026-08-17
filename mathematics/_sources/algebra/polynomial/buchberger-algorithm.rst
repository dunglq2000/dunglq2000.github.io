Thuật toán Buchberger
=====================

Thuật toán Buchberger xây dựng cơ sở Gröbner bằng cách liên tục sửa những cặp
đa thức chưa thỏa tiêu chuẩn Buchberger. Đây là thuật toán nền tảng để hiểu các
phương pháp hiện đại như F4 và F5.

Thuật toán
----------

Đầu vào là :math:`F=\{f_1,\ldots,f_s\}`. Đặt :math:`G\leftarrow F` và tạo tập
:math:`P` chứa mọi cặp chỉ số của :math:`G`.

Khi :math:`P` chưa rỗng:

#. lấy một cặp :math:`(i,j)` khỏi :math:`P`;
#. tính :math:`r=\operatorname{NF}_G(S(g_i,g_j))`;
#. nếu :math:`r\ne0`, thêm :math:`r` vào :math:`G` và thêm vào :math:`P` mọi
   cặp giữa :math:`r` với các phần tử cũ.

Khi không còn cặp nào, mọi đa thức S đều rút gọn về không, nên theo tiêu chuẩn
Buchberger, :math:`G` là một cơ sở Gröbner.

.. code-block:: text

   G := F
   P := {(i, j) | 0 <= i < j < |G|}
   while P is not empty:
       (i, j) := select(P)
       r := normal_form(S(G[i], G[j]), G)
       if r != 0:
           append r to G
           add all pairs (old polynomial, r) to P
   return G

Ví dụ
-----

Xét :math:`F=\{f_1,f_2\}\subset\QQ[x,y]` theo thứ tự lex
:math:`x>y`, với

.. math::

   f_1=x^2-y,\qquad f_2=xy-1.

BCNN của :math:`\LM(f_1)=x^2` và :math:`\LM(f_2)=xy` là :math:`x^2y`.
Do đó

.. math::

   S(f_1,f_2)=y f_1-x f_2=x-y^2.

Phần dư khác không nên ta thêm :math:`f_3=x-y^2`. Cặp mới lại sinh ra quan hệ
:math:`y^3-1`. Sau khi xử lý hết các cặp và rút gọn, ta nhận được một hệ dạng
tam giác; có thể giải :math:`y` trước rồi suy ra :math:`x=y^2`.

Liên hệ với mã nguồn ``CudaPolynomial``
---------------------------------------

Hiện thực trong ``src/BuchbergerAlgorithm.cpp`` bám sát giả mã:

* ``pairs`` lưu các cặp tới hạn và chọn phần tử cuối, tức chiến lược ngăn xếp;
* ``SPoly`` lấy BCNN hai đơn thức dẫn đầu;
* ``PolynomialDivision`` trả phần dư ở phần tử đầu của vector kết quả;
* mỗi phần dư khác không được thêm vào ``G`` và ghép cặp với toàn bộ phần tử cũ.

Các đa thức của dự án nằm trên :math:`\FF_2`, vì vậy ``SPoly`` dùng phép cộng:
:math:`a-b=a+b` trong trường đặc số hai. Đơn thức được biểu diễn bằng vector số
mũ và được sắp theo graded lexicographic trong ``DeglexOrdering``.

Chi phí và điểm nghẽn
---------------------

Hai nguồn tăng chi phí là số cặp tới hạn và phép chia đa thức. Mỗi phần dư mới
làm cơ sở lớn hơn, đồng thời sinh thêm nhiều cặp. Hơn nữa, kết quả xử lý một cặp
có thể thay đổi cơ sở dùng để rút gọn cặp tiếp theo. Sự phụ thuộc này khiến vòng
lặp chính của Buchberger khó song song hóa trực tiếp.

Các hiện thực thực tế thường cải thiện bằng cách:

* dùng tiêu chuẩn để loại cặp chắc chắn cho phần dư bằng không;
* chọn cặp theo bậc BCNN thay vì thứ tự thêm vào;
* interreduce cơ sở trong quá trình tính;
* gom nhiều cặp và thay các phép chia riêng lẻ bằng đại số tuyến tính, chính là
  ý tưởng của F4.

