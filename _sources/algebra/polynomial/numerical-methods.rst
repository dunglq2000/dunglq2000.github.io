Phương pháp tính giá trị đa thức
================================

Cho đa thức

.. math:: p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0,

ta cần tìm giá trị :math:`p(x)` tại :math:`x = c`, tức là tính :math:`p(c)`.

Tính giá trị đa thức với phép thế trực tiếp
-------------------------------------------

Cách đơn giản nhất để tìm :math:`p(c)` là thế trực tiếp giá trị :math:`c` vào đa thức

.. math:: p(c) = a_n c^n + a_{n-1} c^{n-1} + \cdots + a_1 c + a_0.

Sau đó ta tính từng hạng tử

- :math:`a_1 c` cần một phép nhân;
- :math:`a_2 c^2` cần hai phép nhân :math:`a_2 \cdot c \cdot c`;
- tương tự, `a_i c^i` cần :math:`i` phép nhân.

Tổng cộng chúng ta cần

.. math:: 1 + 2 + \cdots + n = n (n+1) / 2

phép nhân. Sau đó ta cộng tất cả hạng tử lại với :math:`n+1` phép cộng.

Vấn đề là số lượng phép nhân cần để tính rất lớn nên chúng ta sẽ tìm hiểu những phương án tính toán khác hiệu quả hơn.

Tính giá trị đa thức với việc ghi nhớ lũy thừa
----------------------------------------------

Mình đề xuất một giải pháp đơn giản cho việc tính lũy thừa :math:`c^i`. Ở phần trên, mỗi hạng tử ta luôn phải tính lại :math:`c \cdot c \cdots c` nên mình sẽ dùng dãy :math:`c_i` cho lũy thừa và dãy :math:`p_i` cho tổng:

- khởi tạo :math:`c_0 = 1` và :math:`p_0 = a_0`;
- tính :math:`c_{i+1} = c_i \cdot c` với :math:`0 \leqslant i \leqslant n - 1`;
- tính :math:`p_{i+1} = p_i + a_{i+1} \cdot c_{i+1}` với :math:`0 \leqslant i \leqslant n - 1`.

Như vậy mình cần thực hiện :math:`n` phép cộng và :math:`2n` phép nhân (tính :math:`c_i` và :math:`a_{i+1} \cdot c_{i+1}`).

Tiếp theo mình sẽ nói về phương pháp phổ biến để tính giá trị đa thức gọi là **phương pháp Hoocner**.

Phương pháp Hoocner
-------------------

Để tính giá trị đa thức

.. math:: p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0

tại :math:`x = c`, ta thực hiện:

- khởi tạo :math:`p_0 = a_n`;
- tính :math:`p_1 = p_0 c + a_{n-1}`;
- tính :math:`p_2 = p_1 c + a_{n-2}`;
- tương tự, tính :math:`p_{i} = p_{i-1} c + a_{n-i}` với mọi :math:`1 \leqslant i \leqslant n`.

Cuối cùng, :math:`p_n` chính là kết quả :math:`p(c)`.

Phương pháp Hoocner tốn :math:`n` phép cộng và :math:`n` phép nhân (ở mỗi bước cần một phép cộng và một phép nhân).

Tuy nhiên, phương pháp Hoocner có hai ứng dụng quan trọng khác trong đại số là xác định đa thức khi thay :math:`x` thành :math:`y + c` (với :math:`c` là hằng số) và phân tích nhanh đa thức thành nhân tử khi biết một nghiệm.

Trước khi tìm hiểu phương pháp Hoocner tổng quát, mình sẽ trình bày phương pháp chia Hoocner trước.

Phương pháp chia Hoocner
------------------------

Giả sử ta có đa thức

.. math:: p(x) = a_n x^n + \cdots a_1 x + a_0

và ta biết một nghiệm của đa thức :math:`x = c`. Khi đó ta có thể phân tích đa thức :math:`p(x)` thành nhân tử dạng

.. math:: p(x) = (x - c) p_1(x)

với :math:`p_1(x)` là đa thức bậc :math:`n - 1`.

Đầu tiên ta viết các hệ số của đa thức theo bậc giảm dần :math:`a_n`, :math:`a_{n-1}`, ..., :math:`a_1`, :math:`a_0` và giá trị :math:`c` vào bảng.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-1.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|

    .. include:: tab-hoocner-1.rst.inc

Tiếp theo ta điền các giá trị vào dưới chân các ô :math:`a_i` bắt đầu từ :math:`a_n` theo quy tắc "đầu rơi - nhân ngang - cộng chéo", có nghĩa là:

- giữ nguyên :math:`a_n`;
- các ô kế tiếp là kết quả của phép nhân ô trước đó với :math:`c` rồi cộng cho ô bên trên.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-2.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|

    .. include:: tab-hoocner-2.rst.inc

Ví dụ, phân tích đa thức

.. math:: p(x) = x^3 - x^2 - x - 2

khi biết một nghiệm :math:`x = 2` của nó.

Đầu tiên ta viết các hệ số thành bảng:

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-3.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|

    .. include:: tab-hoocner-3.rst.inc

Ta giữ lại hệ số bậc cao nhất :math:`a_n`:

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-4.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|

    .. include:: tab-hoocner-4.rst.inc

Tiếp theo, lấy kết quả vừa nhận được :math:`1`, nhân với :math:`x = 2` rồi cộng ô chéo bên phải

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-5.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|

    .. include:: tab-hoocner-5.rst.inc

Như vậy kết quả dưới :math:`-1` là :math:`1`, thực hiện tương tự ta có

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-6.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|

    .. include:: tab-hoocner-6.rst.inc

Hệ số cuối cùng chắc chắn bằng :math:`0`

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: tab-hoocner-7.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|

    .. include:: tab-hoocner-7.rst.inc

Như vậy :math:`(1, 1, 1)` là hệ số của đa thức :math:`p_1(x)` theo bậc giảm dần, tức là

.. math:: p_1(x) = x^2 + x + 1.

Phương pháp Hoocner tổng quát
-----------------------------

Cho đa thức

.. math:: p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0,

ta sẽ xác định các hệ số của đa thức :math:`p(y + c)` với :math:`y` là biến mới và :math:`c` là giá trị cho trước.

Giả sử

.. math:: p(y + c) = b_n y^n + b_{n-1} y^{n-1} + \cdots + b_1 y + b_0

với :math:`b_i` là các hệ số cần tìm.

Nếu :math:`y = 0` thì :math:`p(c) = b_0`. Ta tính được :math:`b_0` bằng phương pháp Hoocner bên trên.

Đặt

.. math:: p(x) = (x - c) p_1(x) + p(c)

với :math:`p_1(x)` là đa thức bậc :math:`n - 1`. Khi đó

.. math:: p(y + c) = y(b_n y^{n-1} + b_{n-1} y^{n-2} + \cdots + b_1) + b_0

và nếu ta đặt :math:`x = y + c` thì

.. math:: p(x) = (x - c) (b_n y^{n-1} + b_{n-1} y^{n-2} + \cdots b_1) + b_0

thì khi đồng nhất hai biểu thức :math:`p(x)` ta được

.. math:: p_1(x) = b_n y^{n-1} + b_{n-1} y^{n-2} + \cdots b_1 = p_1(y + c).

Lặp lại quá trình trên, cho :math:`y = 0` thì :math:`p_1(c) = b_1`, nói cách khác ta có thể tính :math:`b_1` từ phương pháp Hoocner ở trên.

Tương tự ta tính :math:`b_i = p_i(c)` với :math:`i = 1, 2, \ldots, n`, trong đó :math:`p_i(c)` là giá trị đa thức bậc :math:`n - i` tại :math:`x = c`.

.. prf:example:: Ví dụ phương pháp Hoocner tổng quát
    :label: exp-general-hoocner

    Cho

    .. math:: p(x) = 2 x^6 + 4 x^5 - x^2 + x + 2,

    tính :math:`p(y - 1)`.

    Ở đây :math:`c = -1`, ta sử dụng phương pháp chia Hoocner ở trên khi :math:`x = -1`.

    .. only:: html

      .. table:: 
          :class: centered-table

          .. include:: exp-hoocner-1.rst.inc

    .. only:: latex

        .. tabularcolumns:: |c|c|c|c|c|c|c|c|

        .. include:: exp-hoocner-1.rst.inc

    Lúc này, hệ số :math:`b_0` là giá trị ngoài cùng bên phải ở dòng thứ hai, nghĩa là :math:`b_0 = -2`.

    Tiếp tục sử dụng phương pháp chia Hoocner để tìm hàng thứ ba từ hàng thứ hai

    .. only:: html

      .. table:: 
          :class: centered-table

          .. include:: exp-hoocner-2.rst.inc

    .. only:: latex

        .. tabularcolumns:: |c|c|c|c|c|c|c|c|

        .. include:: exp-hoocner-2.rst.inc

    Hệ số :math:`b_1` là giá trị ngoài cùng bên phải ở dòng thứ ba, hay :math:`b_1 = 11`.

    Tương tự, từ hàng trên ta áp dụng phương pháp chia Hoocner để tìm hàng dưới với độ dài trừ đi :math:`1`. Khi độ dài hàng bằng :math:`1` thì ta kết thúc thuật toán.

    .. only:: html

      .. table:: 
          :class: centered-table

          .. include:: exp-hoocner-3.rst.inc

    .. only:: latex

        .. tabularcolumns:: |c|c|c|c|c|c|c|c|

        .. include:: exp-hoocner-3.rst.inc
    
    Như vậy, lấy kết quả ngoài cùng bên phải ở mỗi hàng ta có hệ số của đa thức :math:`p(y - 1)`, ở đây là

    .. math:: p(y - 1) = -2 + 11 x - 11 x^2 + 10 x^4 - 8 x^5 + 2 x^6.
    