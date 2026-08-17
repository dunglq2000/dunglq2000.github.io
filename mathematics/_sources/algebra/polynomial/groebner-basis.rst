Cơ sở Gröbner
==============

Cơ sở Gröbner là công cụ biến bài toán trên ideal đa thức nhiều biến thành các
phép tính có quy tắc. Có thể xem nó như một phiên bản của phép khử Gauss dành
cho hệ phương trình đa thức: sau khi đưa các đa thức sinh về một cơ sở thích
hợp, bài toán kiểm tra một đa thức có thuộc ideal hay không trở thành bài toán
tính phần dư.

Trong bài này, :math:`R=\KK[x_1,\ldots,x_n]` và một thứ tự đơn thức được cố
định từ đầu. Với :math:`f\ne 0`, kí hiệu

* :math:`\LM(f)` là đơn thức dẫn đầu;
* :math:`\LC(f)` là hệ số dẫn đầu;
* :math:`\LT(f)=\LC(f)\LM(f)` là hạng tử dẫn đầu.

Thứ tự đơn thức
---------------

Việc chọn thứ tự đơn thức là một phần của bài toán, không phải một chi tiết
trình bày. Cùng một đa thức có thể có hạng tử dẫn đầu khác nhau khi đổi thứ tự,
và vì thế phép chia cũng như cơ sở Gröbner thu được có thể khác nhau.

Ba thứ tự thường gặp là:

* **lex**: so sánh vector số mũ từ biến đầu tiên;
* **grlex**: so sánh tổng bậc trước, rồi dùng lex khi tổng bậc bằng nhau;
* **grevlex**: so sánh tổng bậc trước, rồi xét vị trí khác nhau cuối cùng theo
  chiều ngược lại.

Ví dụ với :math:`x>y>z`, ta có
:math:`x^2z\succ_{\lex}y^2z^2`, nhưng
:math:`y^2z^2\succ_{\grlex}x^2z` vì đa thức thứ hai có tổng bậc lớn hơn.

Ideal hạng tử dẫn đầu
---------------------

Cho ideal :math:`I\subseteq R`. Ideal hạng tử dẫn đầu của :math:`I` là

.. math::

   \langle\LT(I)\rangle
   =\langle\LT(f)\mid f\in I,\ f\ne0\rangle.

.. prf:definition:: Cơ sở Gröbner
   :label: def-groebner-basis

   Một tập hữu hạn :math:`G=\{g_1,\ldots,g_t\}\subset I` là một cơ sở Gröbner
   của :math:`I` nếu

   .. math::

      \langle\LT(g_1),\ldots,\LT(g_t)\rangle
      =\langle\LT(I)\rangle.

Điểm quan trọng nằm ở vế phải: :math:`I` có vô hạn phần tử, nhưng các hạng tử
dẫn đầu của một tập hữu hạn :math:`G` đã mô tả được toàn bộ ideal hạng tử dẫn
đầu của nó.

Phép chia đa thức nhiều biến
----------------------------

Để chia :math:`f` cho danh sách :math:`G=(g_1,\ldots,g_t)`, đặt
:math:`p=f`, :math:`r=0`. Khi :math:`p\ne0`:

#. nếu có :math:`\LM(g_i)\mid\LM(p)`, khử hạng tử dẫn đầu bằng
   :math:`p\leftarrow p-\LT(p)g_i/\LT(g_i)`;
#. nếu không có phần tử nào chia được, chuyển :math:`\LT(p)` sang phần dư rồi
   bỏ nó khỏi :math:`p`.

Trong trường :math:`\FF_2`, phép trừ trùng với phép cộng. Đây là lý do mã nguồn
``CudaPolynomial`` dùng phép cộng khi tạo đa thức S và khi khử hạng tử.

Với một danh sách sinh tùy ý, phần dư có thể phụ thuộc thứ tự các phần tử. Nếu
:math:`G` là cơ sở Gröbner, phần dư chuẩn :math:`\operatorname{NF}_G(f)` là duy
nhất. Ta có tiêu chuẩn thành viên rất hữu ích:

.. math::

   f\in I \quad\Longleftrightarrow\quad \operatorname{NF}_G(f)=0.

Đa thức S và tiêu chuẩn Buchberger
----------------------------------

Đa thức S triệt tiêu hạng tử dẫn đầu của hai đa thức:

.. math::

   S(f,g)=
   \frac{\operatorname{lcm}(\LM(f),\LM(g))}{\LT(f)}f
   -\frac{\operatorname{lcm}(\LM(f),\LM(g))}{\LT(g)}g.

.. prf:theorem:: Tiêu chuẩn Buchberger
   :label: thm-buchberger-criterion

   Tập :math:`G` là cơ sở Gröbner khi và chỉ khi mọi đa thức S của các cặp phần
   tử trong :math:`G` đều có phần dư bằng không khi chia cho :math:`G`.

Tiêu chuẩn này vừa kiểm tra cơ sở, vừa dẫn trực tiếp tới thuật toán Buchberger.

Cơ sở Gröbner rút gọn
---------------------

Một cơ sở Gröbner là **rút gọn** nếu mọi đa thức có hệ số dẫn đầu bằng một và
không hạng tử nào của một phần tử bị hạng tử dẫn đầu của phần tử khác chia hết.
Với một ideal và một thứ tự đơn thức cố định, cơ sở Gröbner rút gọn là duy nhất.
Do đó Buchberger, F4 hay một hiện thực khác có thể sinh các cơ sở trung gian
khác nhau, nhưng sau bước rút gọn chúng phải cho cùng kết quả.

Ứng dụng vào hệ phương trình
----------------------------

Hệ :math:`f_1=\cdots=f_m=0` được biểu diễn bởi ideal
:math:`I=\langle f_1,\ldots,f_m\rangle`. Cơ sở Gröbner giữ nguyên tập nghiệm
nhưng thay tập sinh bằng một hệ thuận tiện hơn. Với thứ tự lex, cơ sở thường có
dạng gần tam giác, nhờ đó có thể giải một biến rồi thế ngược. Trong mật mã đại
số, các phương trình thường nằm trên :math:`\FF_2`; khi cần giới hạn nghiệm là
bit, ta thêm các phương trình trường :math:`x_i^2+x_i=0`.

