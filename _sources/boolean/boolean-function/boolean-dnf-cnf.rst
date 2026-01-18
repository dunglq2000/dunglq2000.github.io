Disjunctive và Conjunctive Normal Form
======================================

Khi xử lý các mạch logic có ba toán tử chúng ta đặc biệt quan tâm là AND, OR, NOT. Điều này khác với đại số boolean ở phần trước chỉ quan tâm phép XOR và AND - phép cộng và nhân trong :math:`\mathbb{F}_2`.

Ở phần này kí hiệu:

- NOT của biến :math:`a` là :math:`\neg a`;
- AND của hai biến :math:`a` và :math:`b` là :math:`a \land b`. Chúng ta cũng có thể kí hiệu là :math:`a \cdot b` hoặc :math:`ab` như đại số boolean ở phần trước.
- OR của hai biến :math:`a` và :math:`b` là :math:`a \lor b`. Chúng ta **KHÔNG** dùng kí hiệu :math:`a + b` ở đây vì phép cộng đã được dùng ở phần ANF.

Phép AND và OR có tính giao hoán, kết hợp.

Một số luật logic
-----------------

Sau đây là một số "hằng đẳng thức đáng nhớ" trong logic:

1. Luật bù:

   - :math:`a \lor \neg a = 1`;
   - :math:`a \land \neg a = 0`.

2. Luật hấp thụ:

   - :math:`x \lor (x \land y) = x`;
   - :math:`x \land (x \lor y) = x`.

3. Luật đồng nhất:

   - :math:`x \lor 0 = x`;
   - :math:`x \land 1 = x`.

4. Luật giao hoán:

   - :math:`x \lor y = y \lor x`;
   - :math:`x \land y = y \land x`.

5. Luật kết hợp:

   - :math:`x \lor (y \lor z) = (x \lor y) \lor z`;
   - :math:`x \land (y \land z) = (x \land y) \land z`.

6. Luật phân phối:

   - :math:`x \lor (y \land z) = (x \lor y) \land (x \lor z)`;
   - :math:`x \land (y \lor z) = (x \land y) \lor (x \land z)`.

7. Luật De Morgan:

   - :math:`\neg (x \land y) = \neg x \lor \neg y`;
   - :math:`\neg (x \lor y) = \neg x \land \neg y`.

Tổng của tích
-------------

Nếu biểu thức boolean được biểu diễn ở dạng tổng của các tích thì ta gọi là **disjunctive normal form** (hay **DNF**).

.. prf:example:: 
    :label: exp-disjunctive-normal-form
    
    .. math:: (a \land \neg b \land \neg c) \lor (a \land b) \lor (b \land \neg c).

Ở đây, mỗi tích sẽ bao gồm các **literal** (hay **đơn tử**). Ví dụ với tích :math:`(a \land \neg b \land \neg c)` thì các literal sẽ là :math:`a`, :math:`\neg b` và :math:`\neg c`.

Mỗi tích sẽ được gọi là **term** (hay **hạng tử**). Trong ví dụ trên có ba term là :math:`(a \land \neg b \land \neg c)`, :math:`(a \land b)` và :math:`(b \land \neg c)`.

Biểu thức boolean với :math:`n` biến :math:`x_1`, ..., :math:`x_n` ở dạng **full disjunctive normal form** (hay **full DNF**) mỗi term của nó có đủ :math:`n` literal.

Ở ví dụ trên thì các term :math:`a \land b` và :math:`b \land \neg c` chỉ có hai literal nên không phải là full DNF.

.. prf:example:: Ví dụ về full DNF
    :label: exp-full-disjunctive-normal-form

    .. math:: (a \land b) \lor (a \land \neg b) \lor (\neg a \land b).

Để chuyển một hàm boolean về dạng full DNF chúng ta có thể dùng bảng chân trị.

Đặt :math:`f(x_1, \ldots, x_n)` là hàm boolean cần đưa về dạng full DNF.

1. Nếu :math:`f = 0` thì ta không xét.
2. Nếu :math:`f = 1`, với :math:`i = 1, \ldots, n` ta xây dựng term như sau:

   - nếu :math:`x_i = 0` thì literal là :math:`\neg x_i`;
   - nếu :math:`x_i = 1` thì literal là :math:`x_i`.

.. prf:example:: 
    :label: exp-convert-to-full-DNF

    Sử dụng ví dụ ở trên

    .. math:: f(a, b, c) = (a \land \neg b \land \neg c) \lor (a \land b) \lor (b \land \neg c).

    Bảng chân trị của :math:`f` sẽ có dạng

    +-----------+-----------+-----------+-----------+
    | :math:`a` | :math:`b` | :math:`c` | :math:`f` |
    +===========+===========+===========+===========+
    | :math:`0` | :math:`0` | :math:`0` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`0` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`1` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`1` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`0` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`0` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`1` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`1` | :math:`1` | :math:`1` |
    +-----------+-----------+-----------+-----------+

    Ở đây :math:`f` nhận giá trị :math:`1` khi :math:`(a, b, c)` là các bộ :math:`(0, 1, 0)`, :math:`(1, 0, 0)`, :math:`(1, 1, 0)` và :math:`(1, 1, 1)`.

    - đối với :math:`(0, 1, 0)` thì term tương ứng là :math:`\neg a \land b \land \neg c`;
    - đối với :math:`(1, 0, 0)` thì term tương ứng là :math:`a \land \neg b \land \neg c`;
    - đối với :math:`(1, 1, 0)` thì term tương ứng là :math:`a \land b \land \neg c`;
    - đối với :math:`(1, 1, 1)` thì term tương ứng là :math:`a \land b \land c`.

    Như vậy hàm :math:`f` có thể viết lại là

    .. math:: f(a, b, c) = (\neg a \land b \land \neg c) \lor (a \land \neg b \land \neg c) \lor (a \land b \land \neg c) \lor (a \land b \land c).

Tích của các tổng
-----------------

Nếu biểu thức boolean được biểu diễn ở dạng tích của các tổng thì ta gọi là **conjunctive normal form** (hay **CNF**).

.. prf:example:: 
    :label: exp-conjunctive-normal-form
    
    .. math:: (a \lor \neg b \lor \neg c) \land (a \lor b) \land (b \lor \neg c).

Tương tự, mỗi tổng sẽ bao gồm các **literal** (hay **đơn tử**). Ví dụ với tổng :math:`(a \lor \neg b \lor \neg c)` thì các literal sẽ là :math:`a`, :math:`\neg b` và :math:`\neg c`.

Mỗi tích sẽ được gọi là **term** (hay **hạng tử**). Trong ví dụ trên có ba term là :math:`(a \lor \neg b \lor \neg c)`, :math:`(a \lor b)` và :math:`(b \lor \neg c)`.

Biểu thức boolean với :math:`n` biến :math:`x_1`, ..., :math:`x_n` ở dạng **full conjunctive normal form** (hay **full CNF**) mỗi term của nó có đủ :math:`n` literal.

Ở ví dụ trên thì các term :math:`a \lor b` và :math:`b \lor \neg c` chỉ có hai literal nên không phải là full CNF.

Tương tự, để chuyển một hàm boolean về dạng full CNF chúng ta có thể dùng bảng chân trị nhưng làm ngược lại so với DNF.

Đặt :math:`f(x_1, \ldots, x_n)` là hàm boolean cần đưa về dạng full CNF.

1. Nếu :math:`f = 1` thì ta không xét.
2. Nếu :math:`f = 0`, với :math:`i = 1, \ldots, n` ta xây dựng term như sau:

   - nếu :math:`x_i = 0` thì literal là :math:`x_i`;
   - nếu :math:`x_i = 1` thì literal là :math:`\neg x_i`.

.. prf:example:: 
    :label: exp-convert-to-full-CNF
    
    Sử dụng ví dụ ở trên

    .. math:: f(a, b, c) = (a \lor \neg b \lor \neg c) \land (a \lor b) \land (b \lor \neg c).

    Bảng chân trị của :math:`f` sẽ có dạng

    +-----------+-----------+-----------+-----------+
    | :math:`a` | :math:`b` | :math:`c` | :math:`f` |
    +===========+===========+===========+===========+
    | :math:`0` | :math:`0` | :math:`0` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`0` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`1` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`0` | :math:`1` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`0` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`0` | :math:`1` | :math:`0` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`1` | :math:`0` | :math:`1` |
    +-----------+-----------+-----------+-----------+
    | :math:`1` | :math:`1` | :math:`1` | :math:`1` |
    +-----------+-----------+-----------+-----------+

    Ở đây :math:`f` nhận giá trị :math:`0` khi :math:`(a, b, c)` là các bộ :math:`(0, 0, 0)`, :math:`(0, 0, 1)`, :math:`(0, 1, 1)`, và :math:`(1, 0, 1)`.

    - đối với :math:`(0, 0, 0)` thì term tương ứng là :math:`a \lor b \lor c`;
    - đối với :math:`(0, 0, 1)` thì term tương ứng là :math:`a \lor b \lor \neg c`;
    - đối với :math:`(0, 1, 1)` thì term tương ứng là :math:`a \lor \neg b \lor \neg c`;
    - đối với :math:`(1, 0, 1)` thì term tương ứng là :math:`\neg a \lor b \lor \neg c`.

    Như vậy hàm :math:`f` có thể viết lại là

    .. math:: f(a, b, c) = (a \lor b \lor c) \land (a \lor b \lor \neg c) \land (a \lor \neg b \lor \neg c) \land (\neg a \lor b \lor \neg c).

Chúng ta có thể sử dụng đoạn code sau của SageMath để tìm full CNF (các bạn có thể xem ở `đây <https://doc.sagemath.org/html/en/reference/logic/sage/logic/boolformula.html>`_):

.. code-block:: python

    import sage.logic.propcalc as propcalc
    s = propcalc.formula("(a | ~b | ~c) & (a | b) & (b | ~c)")
    s.convert_cnf()
    print(s)

Phương pháp bìa Karnaugh tìm biểu thức tối tiểu
-----------------------------------------------

Chúng ta đã thấy rằng từ một biểu thức DNF hoặc CNF thì tìm được biểu thức full DNF hoặc full CNF.

Tuy nhiên trong thực tế chúng ta quan tâm đến biểu thức ít term, và mỗi term có ít literal nhất có thể. Do đó chúng ta cần một phương án rút gọn biểu thức boolean.

Đối với hàm ba hoặc bốn biến chúng ta có thể sử dụng **bìa Karnaugh** (hay **Karnaugh map**, **карта Карно**).

Ở phần sau mình sẽ trình bày cách tìm tất cả biểu thức tối tiểu đối với DNF. Đối với CNF làm ngược lại.

Trường hợp ba biến
^^^^^^^^^^^^^^^^^^

Giả sử ta có biểu thức boolean :math:`f(x_1, x_2, x_3)`.

Ta viết bảng gồm :math:`2` hàng (ứng với :math:`2` giá trị của :math:`x_1` thuộc :math:`\{0 ,1 \}`) và :math:`4` cột (ứng với :math:`4` giá trị :math:`x_2 x_3` thuộc :math:`\{ 00, 01, 10, 11 \}`).

.. important:: 

    Hai ô kề nhau khác nhau đúng **MỘT** bit.

.. _kn-map: 

.. figure:: ../../figures/karnaugh/karnaugh-1.*

    Bìa Karnaugh

Ở :numref:`kn-map`, :math:`x_2 x_3` được viết theo thứ tự :math:`00`, :math:`01`, :math:`11` rồi mới tới :math:`10`. Điều này đảm bảo với lưu ý ở trên là hai ô kề nhau khác nhau đúng một bit.

Tiếp theo, ta điền giá trị của hàm :math:`f` vào bảng. Ở đây, ô ở hàng :math:`x_1` và ở cột :math:`x_2 x_3` sẽ là giá trị :math:`f(x_1, x_2, x_3)`.

.. figure:: ../../figures/karnaugh/karnaugh-2.*

    Điền giá trị vào bìa Karnaugh

Lấy ví dụ DNF ở trên với bảng chân trị tương ứng:

.. math:: f(x_1, x_2, x_3) = (x_1 \land \neg x_2 \land \neg x_3) \lor (x_1 \land x_2) \lor (x_2 \land \neg x_3).

+-------------+-------------+-------------+-----------+
| :math:`x_1` | :math:`x_2` | :math:`x_3` | :math:`f` |
+=============+=============+=============+===========+
| :math:`0`   | :math:`0`   | :math:`0`   | :math:`0` |
+-------------+-------------+-------------+-----------+
| :math:`0`   | :math:`0`   | :math:`1`   | :math:`0` |
+-------------+-------------+-------------+-----------+
| :math:`0`   | :math:`1`   | :math:`0`   | :math:`1` |
+-------------+-------------+-------------+-----------+
| :math:`0`   | :math:`1`   | :math:`1`   | :math:`0` |
+-------------+-------------+-------------+-----------+
| :math:`1`   | :math:`0`   | :math:`0`   | :math:`1` |
+-------------+-------------+-------------+-----------+
| :math:`1`   | :math:`0`   | :math:`1`   | :math:`0` |
+-------------+-------------+-------------+-----------+
| :math:`1`   | :math:`1`   | :math:`0`   | :math:`1` |
+-------------+-------------+-------------+-----------+
| :math:`1`   | :math:`1`   | :math:`1`   | :math:`1` |
+-------------+-------------+-------------+-----------+

Khi đó bìa Karnaugh sẽ là

.. figure:: ../../figures/karnaugh/karnaugh-dnf-1.*

Tiếp theo chúng ta xác định các tế bào, là các term với số lượng literal nhỏ nhất có thể.

Đối với dạng DNF, chúng ta quan tâm các ô có giá trị :math:`1`. Ta gom các ô có giá trị :math:`1` kề nhau tạo thành hình chữ nhật có :math:`2^i` ô với :math:`i = 0, 1, \ldots`

Ở hình trên có ba tế bào theo thứ tự là :math:`x_1`, :math:`x_2` và :math:`x_3` (:numref:`kn-dnf`):

- :math:`001` và :math:`011`;
- :math:`011` và :math:`010`;
- :math:`011` và :math:`111`.

.. _kn-dnf:

.. figure:: ../../figures/karnaugh/karnaugh-dnf-1.* 

    Các tế bào của biểu thức :math:`f`

Mỗi tế bào sẽ tương ứng với term ở các vị trí giống nhau. Nói cách khác:

- tế bào màu đỏ :math:`001` và :math:`011` giống nhau ở bit đầu và bit thứ ba, tương ứng :math:`x_1` và :math:`x_3` nên term là :math:`\neg x_1 \land x_3`. Ta đặt :math:`T_1 = \neg x_1 \land x_3`;
- tế bào màu xanh lá :math:`011` và :math:`010` giống nhau ở bit đầu và bit thứ hai, tương ứng :math:`x_1` và :math:`x_2` nên term là :math:`\neg x_1 \land x_2`. Ta đặt :math:`T_2 = \neg x_1 \land x_2`;
- tế bào màu vàng :math:`011` và :math:`111` giống nhau ở bit thứ hai và thứ ba, tương ứng :math:`x_2` và :math:`x_3` nên term là :math:`x_2 \land x_3`. Ta đặt :math:`T_3 = x_2 \land x_3`.

Luôn nhớ rằng trong DNF thì giá trị :math:`1` ta giữ nguyên (ví dụ :math:`x_3`) còn giá trị :math:`0` thì ta đảo (ví dụ $\neg x_1$).

Tiếp theo, ta xét các tế bào có số ô nhiều nhất trước. Ở đây cả ba tế bào đều có hai ô nên tương đương nhau.

1. Chọn tế bào :math:`T_1`. Ta gạch bỏ tất cả ô của tế bào :math:`T_1`.

.. figure:: ../../figures/karnaugh/karnaugh-dnf-2.*

    Bìa Karnaugh sau khi gạch bỏ :math:`T_1`

2. Trong các tế bào còn lại, ta chọn tế bào chưa bị gạch hết và có số ô cao nhất. Ở đây chúng ta có hai phương án:

   - chọn :math:`T_2`, ta gạch bỏ :math:`T_2`. Tiếp tục quá trình với :math:`T_3`, ta gạch bỏ :math:`T_3`. Khi đó công thức tối tiểu là :math:`T_1 \to T_2 \to T_3`;
   - chọn :math:`T_3`, ta gạch bỏ :math:`T_3`. Tiếp tục quá trình với :math:`T_2`, ta gạch bỏ :math:`T_2`. Khi đó công thức tối tiểu là :math:`T_1 \to T_3 \to T_2`.

Như vậy ta có hai công thức tối tiểu là :math:`T_1 \to T_2 \to T_3` và :math:`T_1 \to T_3 \to T_2`, nghĩa là:

.. math:: 
    
    f(x_1, x_2, x_3) & = (\neg x_1 \land x_3) \lor (\neg x_1 \land x_2) \lor (x_2 \land x_3) \\
    & = (\neg x_1 \land x_3) \lor (x_2 \land x_3) \lor (\neg x_1 \land x_2).
    
Hai công thức hóa ra ... giống nhau. Đó là do biểu thức ban đầu chứ không phải tất cả trường hợp đều như vậy.
