==================================
Phương pháp tọa độ trong mặt phẳng
==================================

Cuộc cách mạng trong hình học xảy ra khi nhà toán học lãng tử René Descartes phát minh ra hệ tọa độ và từ đó mọi đối tượng hình học có thể được biểu diễn bởi các phương pháp đại số như phương trình, đẳng thức.

.. figure:: ../../mathematicians/Descartes.jpg

	René Descartes (1596-1650)

-----------------------------
Danh mục thuật ngữ và kí hiệu
-----------------------------

Đầu tiên chúng ta thống nhất các thuật ngữ cũng như kí hiệu được sử dụng kể từ đây.

**Điểm** là đơn vị cơ bản của hình học. Bất kì đối tượng hình học nào cũng là một *tập hợp điểm*. Điểm được kí hiệu bởi chữ in hoa, ví dụ như :math:`A`, :math:`B_1`, :math:`B_2`.

**Đường thẳng** đi qua hai điểm phân biệt cho trước. Đường thẳng có thể kéo dài vô hạn về hai phía. Đường thẳng được kí hiệu bởi chữ in thường hoặc chữ Hy Lạp trong ngoặc đơn, ví dụ như :math:`(d)`, :math:`(\Delta)`.

**Đoạn thẳng** chỉ phần đường thẳng nằm giữa hai điểm và bản thân hai điểm đó.

**Nửa đường thẳng** chỉ phần đường thẳng nằm một phía của một điểm trên đường thẳng và chỉ kéo dài vô hạn về phía đó.

**Vector** là đoạn thẳng có hướng. Với điểm đầu là :math:`A` và điểm cuối là :math:`B` thì vector từ :math:`A` tới :math:`B` được kí hiệu là :math:`\overrightarrow{AB}`. Để chỉ một vector không cần biết điểm đầu và điểm cuối ta dùng chữ thường in đậm, ví dụ như :math:`\bm{a}`.

**Góc giữa hai vector** :math:`\overrightarrow{OA}` và :math:`\overrightarrow{OB}` là góc :math:`\angle AOB` và kí hiệu là :math:`(\overrightarrow{OA}, \overrightarrow{OB})`.

Tương tự đối với vector :math:`\bm{a}` và :math:`\bm{b}` thì góc giữa chúng kí hiệu là :math:`(\bm{a}, \bm{b})`.

----------------------
Vector trong mặt phẳng
----------------------

Trong hệ tọa độ :math:`Oxy` với tâm :math:`O` và hai trục :math:`Ox` (trục hoành) và :math:`Oy` (trục tung) vuông góc nhau, đặt :math:`O = (0, 0)` là tọa độ của tâm :math:`O`.

Tiếp theo, mọi điểm trong mặt phẳng Euclid đi liền với cặp số :math:`(x, y)` chỉ tọa độ của điểm đó. Ví dụ :math:`A = (1, 3)`, :math:`B = (4, 1)`.

.. _oxy1:

.. figure:: ../../figures/analytic_geometry/oxy-1.*

	Tọa độ của điểm trong mặt phẳng

Tọa độ của điểm cũng là tọa độ của vector từ :math:`O` tới điểm đó. Ở :numref:`oxy1` thì :math:`\overrightarrow{OA} = (1, 3)` và :math:`\overrightarrow{OB} = (4, 1)`. Tọa độ của vector :math:`\overrightarrow{AB}` khi đó sẽ là

.. math:: \overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = (4, 1) - (1, 3) = (3, -2).
	
Cũng theo :numref:`oxy1` thì ta thấy :math:`\overrightarrow{AB} = \overrightarrow{OC} = (3, -2)`.

Như vậy, nếu ta có hai điểm :math:`A = (x_A, y_A)` và :math:`B = (x_B, y_B)` thì tọa độ vector :math:`\overrightarrow{AB}` là

.. math:: \overrightarrow{AB} = (x_B - x_A, y_B - y_A).

**Tích vô hướng của hai vector** :math:`\bm{a} = (x_1, y_1)` và :math:`\bm{b} = (x_2, y_2)` được định nghĩa là

.. math:: \bm{a} \cdot \bm{b} = x_1 x_2 + y_1 y_2.

Ta cũng có thể kí hiệu tích vô hướng là :math:`\langle \bm{a}, \bm{b} \rangle` nhưng mình sẽ không dùng kí hiệu này.

Ta kí hiệu :math:`\lVert \bm{a} \rVert` là độ dài (chuẩn Euclid, Euclid norm) của vector :math:`\bm{a}`. Trong hệ tọa độ Descartes vuông góc, theo định lý Pythagoras, độ dài của vector là độ dài cạnh huyền tam giác vuông (:numref:`oxy1`). Như vậy, độ dài đoạn thẳng :math:`AB` với :math:`A = (x_A, y_A)` và :math:`B = (x_B, y_B)` là

.. math:: AB = \left\Vert \overrightarrow{AB} \right\Vert = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}.

Khi đó cosin góc giữa hai vector :math:`\bm{a}` và :math:`\bm{b}` là

.. math:: \cos (\bm{a}, \bm{b}) = \frac{\bm{a} \cdot \bm{b}}{\lVert \bm{a} \rVert \cdot \lVert \bm{b} \rVert} = \frac{x_1 x_2 + y_1 y_2}{\sqrt{x_1^2 + y_1^2} \cdot \sqrt{x_2^2 + y_2^2}}.

Nếu góc giữa hai vector bằng :math:`90` độ thì hai vector được gọi là vuông góc nhau. Khi đó tích vô hướng :math:`\bm{a} \cdot \bm{b} = 0`.

----------------------------------------
Phương trình đường thẳng trong mặt phẳng
----------------------------------------

Theo tiên đề Euclid, một đường thẳng được xác định khi biết hai điểm phân biệt thuộc đường thẳng đó. Trong hệ tọa độ, chúng ta có hai cách tìm phương trình đường thẳng.

**Sử dụng vector pháp tuyến.** Vector pháp tuyến của đường thẳng là vector vuông góc với mọi vector có phương là đường thẳng đó. Giả sử :math:`\bm{v} = (a, b)` là vector pháp tuyến của đường thẳng đi qua điểm :math:`M_0 = (x_0, y_0)`. Khi đó đường thẳng đi qua qua :math:`M_0` nhận :math:`\bm{v}` làm vector pháp tuyến là *tập hợp điểm* :math:`M = (x, y)` trên mặt phẳng sao cho :math:`\bm{v} \cdot \overrightarrow{M_0 M} = 0`. Điều này tương đương với

.. math:: \bm{v} \cdot \overrightarrow{M_0 M} = a \cdot (x - x_0) + b \cdot (y - y_0) = 0.

**Sử dụng vector chỉ phương.** Vector chỉ phương của đường thẳng là vector có phương song song với đường thẳng đó. Giả sử :math:`\bm{v}' = (a', b')` là vector chỉ phương của đường thẳng đi qua điểm :math:`M_0 = (x_0, y_0)`. Khi đó đường thẳng đi qua :math:`M_0` nhận :math:`\bm{v}'` làm vector chỉ phương là *tập hợp điểm* :math:`M = (x, y)` trên mặt phẳng sao cho :math:`\bm{v}'` cùng phương với :math:`\overrightarrow{M_0 M}`. Điều này tương đương với

.. math:: \bm{v}' \parallel \overrightarrow{M_0 M} \Leftrightarrow \frac{x - x_0}{a'} = \frac{y - y_0}{b'}.


1. Cả hai cách biểu diễn khi khai triển ra đều có dạng :math:`a x + by + c = 0` với :math:`c` là hằng số. Đây được gọi là dạng tổng quát của phương trình đường thẳng.
2. Cách viết :math:`\dfrac{x - x_0}{a'} = \dfrac{y - y_0}{b'}` được gọi là dạng chính tắc của phương trình đường thẳng.
3. Dạng chính tắc của phương trình đường thẳng còn có một tác dụng đặc biệt khác 

.. math:: \frac{x - x_0}{a'} = \frac{y - y_0}{b'} = t

với :math:`t \in \mathbb{R}`. Khi đó tọa độ :math:`M = (x, y)` có thể được biểu diễn dưới dạng

.. math:: 
    \begin{cases}
        x = x_0 + a' t \\ y = y_0 + b' t
    \end{cases}, \quad t \in \mathbb{R}.

Đây được gọi là phương trình dạng tham số.

Chúng ta chú ý rằng nếu đường thẳng song song với một trong hai trục tọa độ thì vector chỉ phương của nó sẽ cùng phương với vector đơn vị :math:`(1, 0)` hoặc :math:`(0, 1)`. Do đó không thể viết dưới dạng chính tắc được (không thể chia cho :math:`0`) nhưng có thể viết dưới dạng tổng quát hoặc dạng tham số.

------------------------------------
Khoảng cách giữa điểm và đường thẳng
------------------------------------

Nhắc lại một chút kiến thức cơ sở. **Khoảng cách** từ một điểm :math:`A` nằm ngoài đường thẳng :math:`(d)` là độ dài đoạn thẳng :math:`AH` với :math:`H \in (d)` sao cho :math:`AH` nhỏ nhất (:numref:`oxy2`).

Khi đó :math:`H` được gọi là **hình chiếu** của :math:`A` lên đường thẳng :math:`(d)` và :math:`AH` là **khoảng cách** từ :math:`A` tới :math:`(d)`. Do :math:`AH` là đoạn thẳng có độ dài ngắn nhất, điều này xảy ra khi :math:`AH \perp (d)`.

.. _oxy2:

.. figure:: ../../figures/analytic_geometry/oxy-2.*

	Hình chiếu và khoảng cách tới đường thẳng

Như vậy, để tìm hình chiếu của điểm :math:`A` lên đường thẳng :math:`(d)`, ta dựng đường thẳng đi qua điểm :math:`A` và vuông góc với :math:`(d)`.

Giả sử phương trình đường thẳng :math:`(d)` với vector pháp tuyến :math:`\bm{v} = (a, b)` là :math:`(d): ax + by + c = 0`.

Gọi :math:`(d')` là đường thẳng đi qua :math:`A = (x_0, y_0)` và vuông góc với :math:`d`. Do :math:`\bm{v}` là vector pháp tuyến của :math:`(d)` nên :math:`\bm{v}` là vector chỉ phương của :math:`(d')`. Khi đó phương trình dạng tham số của :math:`(d')` là

.. math:: 
	
	\begin{cases}
		x = x_0 + a t \\ y = y_0 + b t
	\end{cases}, \quad t \in \mathbb{R}.

Gọi :math:`H` là hình chiếu của :math:`A` lên :math:`(d)`. Khi đó :math:`H` là giao điểm của :math:`(d)` và :math:`(d')`. Vì :math:`H \in (d')` nên tọa độ của :math:`H` có dạng :math:`(x_0 + at, y_0 + bt)` với :math:`t` nào đó thuộc :math:`\mathbb{R}`. Chúng ta sẽ đi tìm :math:`t` này.

Vì :math:`H \in (d)` nên ta thay tọa độ của :math:`H` vừa tìm được vào phương trình của :math:`(d)` thu được

.. math:: a (x_0 + at) + b (y_0 + bt) + c = 0 \Leftrightarrow t = -\frac{a x_0 + b y_0 + c}{a^2 + b^2}.

Như vậy là ta đã tìm được :math:`t` từ đó xác định được tọa độ của :math:`H`.

Từ đây ta tính được khoảng cách từ :math:`A` tới :math:`(d)`, hay nói cách khác là độ dài đoạn thẳng :math:`AH`. Ta có :math:`A = (x_0, y_0)` và :math:`H = (x_0 + at, y_0 + bt)` nên :math:`\overrightarrow{AH} = (at, bt)`, suy ra

.. math:: 
	
	
		AH = & \left\Vert \overrightarrow{AH} \right\Vert = \sqrt{(at)^2 + (bt)^2} = \lvert t \rvert \sqrt{a^2 + b^2} \\ = & \left| -\frac{a x_0 + b y_0 + c}{a^2 + b^2} \right| \cdot \sqrt{a^2 + b^2} = \frac{\lvert a x_0 + b y_0 + c \rvert}{\sqrt{a^2 + b^2}}.
	

=======
Đạo hàm
=======

Phép tính vi tích phân đã được con người nghiên cứu từ lâu. Câu chuyện về ai là người phát minh ra phép tính vi tích phân: Newton hay Leibniz, được coi là một trong những vụ tranh cãi đáng xấu hổ nhất lịch sử toán học. Nhưng họ cũng đã để lại một mảnh đất màu mỡ cho toán học về sau.

-------------------------------
Cơ học và sự ra đời của đạo hàm
-------------------------------

Trường phái Newton sử dụng đạo hàm như công cụ khảo sát vận tốc từ quãng đường. Ở bậc trung học chúng ta biết rằng **vận tốc trung bình** bằng quãng đường chia thời gian. Tuy nhiên điều đó chỉ đúng cho **chuyển động thẳng đều**. Nếu quãng đường là một hàm số phụ thuộc thời gian (quãng đường là :math:`s(t)` với :math:`t` là thời gian) thì điều đó không đúng nữa.

Do quãng đường phụ thuộc thời gian nên có thể là vận tốc cũng phụ thuộc thời gian? Hợp lí đấy. Nhưng với mỗi một giá trị thời gian :math:`t` cho ta một vị trí :math:`s(t)` trên trục số, còn vận tốc thì không thể phụ thuộc một giá trị thời gian được. Rõ ràng vật phải di chuyển một quãng đường từ thời gian :math:`t_0` tới :math:`t_1` thì mới có vận tốc trên quãng đường đó chứ?

Cách tiếp cận ở đây là, chúng ta cho sự thay đổi thời gian, tức hiệu :math:`\Delta t = t_1 - t_0`, rất nhỏ. Khi đó vật đi từ :math:`s(t_0)` tới :math:`s(t_1)`, vậy là chúng ta có thể tính vận tốc với công thức :math:`v = \dfrac{s(t_1) - s(t_0)}{t_1 - t_0}`. Do :math:`\Delta t` rất nhỏ, hay **tiến về** :math:`0`, thì vận tốc gần như xảy ra vào đúng một thời điểm. Do đó vận tốc lúc này được gọi là **vận tốc tức thời**. Đó cũng chính là ý nghĩa cơ học và sự ra đời của đạo hàm theo trường phái Newton.

----------------------------
Ý nghĩa hình học của đạo hàm
----------------------------

Xét hàm số :math:`y = f(x)` liên tục trên khoảng :math:`(a, b)` chứa điểm :math:`x_0`.

Gọi :math:`M' = (x, y)` là một điểm thuộc hàm số :math:`y = f(x)`. Khi đó đạo hàm của :math:`f(x)` tại :math:`x_0` là giới hạn

.. math:: \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}.

Xét :numref:`int2a`, tỉ số :math:`\Delta y / \Delta x` là tangent của góc hợp bởi trục hoành :math:`Ox` và đường thẳng :math:`MM'`.

.. _int2a:

.. figure:: ../../figures/analytic_geometry/tangent-1.*

	Hệ số góc (trường hợp 1)

Tiếp theo, xét :numref:`int2b`, ta thấy đường thẳng :math:`MM'` ngày càng tiến sát lại với đường cong. Như vậy, khi :math:`\Delta x` tiến tới :math:`0` thì đường thẳng :math:`MM'` cắt đường cong tại hai điểm càng sát nhau. Đến khi hai điểm đó trùng nhau, đường thẳng :math:`MM'` chỉ đi qua đúng một điểm thuộc đường cong và khi đó :math:`MM'` trở thành tiếp tuyến của đường cong tại điểm :math:`M = (x_0, y_0)`.

.. _int2b:

.. figure:: ../../figures/analytic_geometry/tangent-2.*

	Hệ số góc (trường hợp 2)

Khi đó :math:`f'(x_0)` là tangent của góc hợp bởi :math:`MM'` và trục hoành :math:`Ox`, hay nói cách khác là **hệ số góc** (hay **угловой коэффициент**) của đường tiếp tuyến. Thêm nữa :math:`f'(x_0) = \dfrac{\Delta y}{\Delta x} = \dfrac{y - y_0}{x - x_0}` nên phương trình đường tiếp tuyến đi qua :math:`M = (x_0, y_0)` là

.. math:: y = f'(x_0) (x - x_0) + y_0.

=========
Tích phân
=========

Tích phân là khái niệm quan trọng trong giải tích. Sau đây sẽ trình bày cách tính tích phân theo tổng Riemann.

--------------------------------
Tích phân và phân chia diện tích
--------------------------------

Xét phương trình của một đường cong :math:`y = f(x) > 0` trên đoạn :math:`[a; b]`.

Theo định nghĩa, tích phân từ :math:`a` tới :math:`b` là diện tích phần hình phẳng giới hạn bởi đường cong :math:`y = f(x)`, trục hoành :math:`Ox` và hai trục đứng :math:`x = a`, :math:`x = b`.

Ờ :numref:`int1`, diện tích phần tô màu xám là tích phân từ :math:`-2` tới :math:`2` của hàm số :math:`f(x) = -x^2 + 4`.

.. _int1:

.. figure:: ../../figures/analytic_geometry/riemann_sum-1.*

	Tích phân từ :math:`-2` tới :math:`2` của :math:`f(x) = -x^2 + 4`

Chúng ta có thể tính diện tích hình chữ nhật, hình thang, hình vuông. Vậy có cách nào để tính diện tích một hình giới hạn bởi các đường cong bất kì không?

Có đấy! Chúng ta sẽ tính xấp xỉ bằng tổng diện tích các hình chữ nhật.

Ví dụ với hàm số :math:`f(x) = -x^2 + 4` ở trên, ta chia đoạn :math:`[a; b]` thành :math:`n` phần bằng nhau

.. math:: a = x_0 < x_1 < \ldots < x_{n-1} < x_n = b.

Trong đó :math:`x_{i+1} - x_i` cố định và bằng :math:`\dfrac{b-a}{n}`.

Đối với :numref:`int2` ta xấp xỉ bằng :math:`7` hình chữ nhật. Đối với :numref:`int3` ta xấp xỉ bằng :math:`15` hình chữ nhật. Đối với :numref:`int4` ta xấp xỉ bằng :math:`31` hình chữ nhật. 

.. _int2:

.. figure:: ../../figures/analytic_geometry/riemann_sum-2.*

	Xấp xỉ diện tích bởi :math:`7` hình chữ nhật

.. _int3:

.. figure:: ../../figures/analytic_geometry/riemann_sum-3.*

	Xấp xỉ diện tích bởi :math:`15` hình chữ nhật

.. _int4:

.. figure:: ../../figures/analytic_geometry/riemann_sum-4.*

	Xấp xỉ diện tích bởi :math:`31` hình chữ nhật

Càng dùng nhiều hình chữ nhật, tổng diện tích của chúng càng gần với diện tích cần tìm, hay là tích phân cần tìm.

Ở ba hình trên, mỗi hình chữ nhật trong đó có chiều rộng bằng nhau là :math:`\dfrac{b-a}{n}` với :math:`n` là số đoạn. Chiều dài là :math:`f(x_i)` với :math:`x_i = a + \dfrac{b-a}{n} i`, :math:`i = 1, 2, \ldots, n` (biên sau).

Cụ thể hơn, hình chữ nhật từ :math:`x_{i-1}` tới :math:`x_i` sẽ có chiều dài là :math:`f(x_i)` và chiều rộng là :math:`\dfrac{b-a}{n}`. Ở đây lưu ý rằng việc chọn chiều dài không bắt buộc phải chọn biên sau. Chúng ta hoàn toàn có thể chọn chiều dài là :math:`f(x_{i-1})`, hoặc :math:`\max f(x)`, :math:`\min f(x)` trên đoạn :math:`[x_{i-1}; x_i]`.

Khi đó, tổng diện tích của các hình chữ nhật là

.. math:: \sum_{i=1}^n (x_{i} - x_{i-1}) \cdot f(x_i) = \sum_{i=1}^n \frac{b-a}{n} f(x_i).

Khi số lượng hình chữ nhật tăng lên tới vô hạn thì tổng diện tích sẽ tiến tới diện tích chính xác của hình cần tìm, hay nói cách khác là tích phân. Do đó kết quả sẽ là

.. math:: \int\limits_{a}^{b} f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} \frac{b-a}{n} f(x_i), \quad x_i = a + \frac{b-a}{n} i.

-------------------------------------
Ví dụ tính tích phân qua tổng Riemann
-------------------------------------

Ví dụ, tính tích phân từ :math:`-2` tới :math:`2` của hàm số :math:`f(x) = -x^2 + 4` ở trên.

Ta có :math:`b = 2` và :math:`a = -2` nên

.. math:: 
	
	
		\frac{b-a}{n} f(x_i) = & \frac{4}{n} \left(-\left(-2+\frac{4}{n} i\right)^2 + 4\right) \\ = & \frac{4}{n}\left( -4 + \frac{16}{n} i - \frac{16}{n^2} i^2 + 4\right) \\ = & \frac{64}{n} \left( \frac{i}{n} - \frac{i^2}{n^2} \right).
	

Tính tổng :math:`i` từ :math:`1` tới :math:`n` ta có :math:`\displaystyle{\sum_{i=1}^{n} i = \frac{n(n+1)}{2}}`.

Tính tổng :math:`i^2` từ :math:`1` tới :math:`n` ta có :math:`\displaystyle{\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}}`.

Từ đây ta suy ra

.. math:: 
	
	
		\sum_{i=1}^n \frac{64}{n} \left(\frac{i}{n} - \frac{i^2}{n^2}\right) = & \frac{64}{n^2} \sum_{i=1}^n i - \frac{64}{n^3} \sum_{i=1}^{n} i^2 \\ & = -\frac{64}{n^2} \cdot \frac{n(n+1)}{2} - \frac{64}{n^3} \cdot \frac{n(n+1)(2n+1)}{6}.
	

Khi :math:`n` tiến tới vô cực thì biểu thức trên tiến tới :math:`\dfrac{64}{2} - \dfrac{64 \cdot 2}{6} = \dfrac{32}{3}`. Đây chính là giá trị của tích phân :math:`\displaystyle{\int\limits_{-2}^2 (-x^2 + 4) \, dx}`.
