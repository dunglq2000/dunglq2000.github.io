Linear Feedback Shift Register
==============================

Linear Feedback Shift Register (LFSR) là một ứng dụng quan trọng của hàm boolean để sinh ra một chuỗi các giá trị (giả ngẫu nhiên, pseudorandom).

Linear Feedback Shift Register
------------------------------

Xét hàm boolean :math:`n` biến :math:`f(x_0, x_1, \ldots, x_{n-1})`. Khi đó với các giá trị (bit) khởi tạo :math:`x_0`, :math:`x_1`, ..., :math:`x_{n-1}` thuộc :math:`\mathbb{F}_2`, ta có thể sinh ra bit ở các vị trí tiếp theo

.. math:: x_{n} = f(x_0, x_1, \ldots, x_{n-1}).

Tương tự:

.. math:: x_{n+1} = f(x_1, x_2, \ldots, x_n), \ x_{n+2} = f(x_2, x_3, \ldots, x_{n+1}), \ x_{n+3} = f(x_3, x_4, \ldots, x_{n+2}), \ldots

Tổng quát, để sinh bit thứ :math:`n+i` thì đầu vào sẽ là các bit :math:`x_i`, :math:`x_{i+1}`, ..., :math:`x_{i+n-1}`.

.. math:: x_{n+i} = f(x_i, x_{i+1}, \ldots, x_{i+n-1}).

Theo :numref:`lfsr-im1`, kết quả của hàm :math:`f` sẽ được nối vào sau của dãy bit. Theo đó dãy bit sẽ luôn có dạng :math:`x_0`, :math:`x_1`, ..., :math:`x_n`, ...

.. _lfsr-im1:

.. figure:: ../../figures/lfsr/lfsr-1.*

	Feedback Shift Register

Thông qua hàm :math:`f`, các vector trong :math:`\mathbb{F}_2^n` sẽ chuyển trạng thái lẫn nhau theo công thức 

.. math:: (x_{n-1}, x_{n-2}, \ldots, x_1, x_0) \to (x_n, x_{n-1}, \ldots, x_2, x_1).

.. prf:example:: 
	:label: exp-chuyen-trang-thai

	Xét hàm boolean :math:`f(x_3, x_2, x_1, x_0) = x_3 x_2 \oplus x_0`. Bảng chân trị của hàm :math:`f` là

	.. math:: 
		f(x_3, x_2, x_1, x_0) = (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0).

	Ví dụ, với :math:`(0, 0, 0, 1)`, ta có :math:`f(0, 0, 0, 1) = 1` nên :math:`(0, 0, 0, 1)` biến đổi thành :math:`(1, 0, 0, 0)`. Như vậy chúng ta có các chuyển đổi đối với hàm :math:`f` được thể hiện thành :math:`4` chu trình ở các hình bên dưới.

.. figure:: ../../figures/lfsr/lfsr-2.*

	Chu trình thứ nhất của :math:`f`

.. figure:: ../../figures/lfsr/lfsr-3.*

	Chu trình thứ hai của :math:`f`

.. figure:: ../../figures/lfsr/lfsr-4.*

	Chu trình thứ ba của :math:`f`

.. figure:: ../../figures/lfsr/lfsr-5.*

	Chu trình thứ tư của :math:`f`

Ta thấy rằng tập các vector :math:`\bm{x} = (x_i, x_{i+1}, \ldots, x_{i+n-1})` có :math:`2^n` trường hợp. Do đó sẽ có một lúc nào đó (số :math:`i` nào đó) mà vector :math:`\bm{x}` trở lại đúng vector ban đầu. Như vậy tồn tại :math:`i` sao cho

.. math:: (x_0, x_1, \ldots, x_{n-1}) = (x_i, x_{i+1}, \ldots, x_{i+n-1}).

Từ đó dãy bit tiếp theo được sinh ra sẽ giống hệt trước đó nên số :math:`i` nhỏ nhất thỏa mãn đẳng thức được gọi là **chu kì** của Feedback Shift Register.

Trong các hàm boolean thì hàm boolean tuyến tính được quan tâm nhiều nhất để sinh ra chuỗi bit Feedback Shift Register. Do đó từ đây ta tập trung vào các hàm boolean tuyến tính và Linear Feedback Shift Register.

Nhắc lại, hàm boolean tuyến tính là hàm boolean có dạng

.. math:: f(x_0, x_1, \ldots, x_{n-1}) = a_0 x_0 \oplus a_1 x_1 \oplus \ldots \oplus a_{n-1} x_{n-1}.

Trong đó :math:`a_i \in \mathbb{F}_2` là các hệ số cho trước. Ta định nghĩa đa thức đặc trưng cho hàm boolean tuyến tính như sau.

.. prf:definition:: Đa thức đặc trưng
	:label: def-char-poly
	
	Xét hàm boolean tuyến tính

	.. math:: f(x_0, x_1, \ldots, x_{n-1}) = a_0 x_0 \oplus a_1 x_1 \oplus \ldots \oplus a_{n-1} x_{n-1}.

	Khi đó đa thức đặc trưng tương ứng với hàm :math:`f` là đa thức có hệ số trong :math:`\mathbb{F}_2`

	.. math:: P(x) = a_0 + a_1 x + \ldots + a_{n-1} x^{n-1} + x^n.

Do hàm boolean tuyến tính có tính chất là $f(\bm{0}) = 0$ nên chu kì tối đa có thể đạt được là $2^n - 1$. Ta có một vài định nghĩa sau để một LFSR đạt được chu kì tối đa.

.. prf:definition:: Đa thức primitive
	:label: def-primitive-poly

	Xét đa thức

	.. math:: P(x) = a_0 + a_1 x + \ldots + a_{n-1} x^{n-1} + x^n

	thuộc :math:`\mathbb{F}_{2^n}`. Ta đã biết trường :math:`\mathbb{F}_{2^n}` có :math:`2^n - 1` phần tử khác không. Đặt :math:`p = 2^n - 1`. Đa thức :math:`P(x)` được gọi là **primitive** khi với mọi ước nguyên tố :math:`q` của :math:`p` thì:

	.. math:: x^s \not\equiv 1 \bmod{P(x)}, \quad \text{với} \ s = \frac{p}{q} = \frac{2^n - 1}{q}.

.. prf:definition:: Đa thức đặc trưng với chu kì cực đại
	:label: def-char-poly-with-max-period
	
	Đa thức

	.. math:: 
		P(x) = a_0 + a_1 x + \ldots + a_{n-1} x^{n-1} + x^n

	được gọi là **đa thức đặc trưng với chu kì cực đại** nếu đa thức đó tối giản và là đa thức primitive. 

.. prf:example:: 
	:label: exp-char-poly-with-max-period

	Xét đa thức :math:`f(x) = x^4 + x^3 + 1`. Ta có thể xác định xem đa thức này có sinh ra LFSR với chu kì tối đa hay không mà không cần tìm đồ thị chuyển trạng thái của LFSR.

	Đầu tiên ta chứng minh :math:`f(x)` là đa thức tối giản. Thật vậy, giả sử ngược lại, :math:`f(x)` là tích của hai đa thức bậc nhỏ hơn :math:`4`. Hai trường hợp có thể xảy ra là :math:`f(x)` chia hết cho đa thức tối giản bậc :math:`1` hoặc bậc :math:`2`.

	Các đa thức tối giản bậc :math:`1` là :math:`x` và :math:`x+1`. Ta có thể kiểm chứng rằng :math:`f(x)` không chia hết cho bất kì đa thức nào ở trên. Tương tự, đa thức tối giản bậc :math:`2` (trong :math:`\mathbb{F}_{2^4}`) là :math:`x^2 + x + 1` và :math:`f(x)` cũng không chia hết cho đa thức này. Như vậy ta có thể kết luận rằng :math:`f(x)` là đa thức tối giản.

	Trong :math:`\mathbb{F}_{2^4}` có :math:`2^4 - 1 = 15` phần tử khác :math:`0`. Các ước nguyên tố của :math:`15` là :math:`3` và :math:`5`. Ta thấy rằng

	.. math:: x^3 \not\equiv 1 \ \text{và} \ x^5 = x \cdot x^4 = x \cdot (x^3 + 1) = x^4 + x = x^3 + x + 1 \not\equiv 1.

	Như vậy :math:`f(x)` là đa thức primitive.

	Như vậy ta có thể kết luận rằng đa thức :math:`f(x)` sinh ra LFSR với chu kì tối đa.

Thuật toán Berlekamp-Massey
---------------------------

Thuật toán Berlekamp-Massey là thuật toán tìm đa thức sinh có chu kì ngắn nhất sinh ra một dãy LFSR cho trước.

Bài toán ở đây là, giả sử chúng ta có một dãy bit

.. math:: u_0, u_1, \ldots, u_{l-1}

là một dãy bit được sinh giả ngẫu nhiêu (pseudorandom). Làm thế nào từ đoạn bit này ta xây dựng được đa thức đặc trưng của LFSR mà sinh ra tất cả các bit sau đó? Hơn nữa :math:`l` phải nhỏ nhất có thể.

Nhắc lại, đa thức đặc trưng là đa thức có dạng

.. math:: P(x) = a_0 + a_1 x + \ldots + a_{n-1} x^{n-1} + a_n x^n

thì hàm boolean tuyến tính sinh ra bit tiếp theo sẽ có dạng

.. math:: x_n = f(x_0, x_1, \ldots, x_{n-1}) = a_0 x_0 \oplus a_1 x_1 \oplus \ldots \oplus a_{n-1} x_{n-1}.

Tổng quát, công thức để sinh ra bit thứ :math:`n+i` sẽ là

.. math:: x_{n+i} = f(x_i, x_{i+1}, \ldots, x_{n+i-1}) = a_0 x_i \oplus a_1 x_{i+1} \oplus \ldots \oplus a_{n-1} x_{n+i-1}

với :math:`i = 0, 1, \ldots`

.. prf:algorithm:: Thuật toán Berlekamp-Massey
	:label: algo-berlekamp-massey

	Đầu vào là dãy bit :math:`u_0`, :math:`u_1`, ..., :math:`u_{l-1}`. 

	Đầu ra là đa thức đặc trưng bậc nhỏ nhất mà sinh ra toàn bộ dãy bit trên, bắt đầu từ các bit :math:`u_0`, :math:`u_1`, ... nhất định.

	**Bước -1.** Gọi :math:`n_0` là vị trí đầu tiên mà :math:`u_{n_0} = 1` (các bit được đánh số từ :math:`0`). Khi đó đặt :math:`P_{-1}(x) = 1` và :math:`k_{-1} = 1`. Nếu :math:`P_{-1}(x)` sinh ra toàn bộ dãy bit thì ta dừng thuật toán. Ngược lại thì tiếp tục bước 1.

	**Bước 0.** Đặt :math:`P_0(x) = x^{n_0 + 1} \oplus P_{-1}(x)` với :math:`n_0` là vị trí bit :math:`1` đầu tiên và đặt :math:`k_0 = \deg P_0(x) = n_0 + 1`.

	Ở mỗi bước từ đây trở đi, gọi :math:`m` là số sao cho 

	.. math:: k_{-1} = k_0 = \ldots = k_{m-1} < k_{m} = k_{s+2} = \ldots

	**Bước** :math:`n`. Để tìm :math:`P_n(x)` ta tính :math:`a = m - k_{m-1}` và :math:`b = n - k_{n-1}`.

	1. Nếu :math:`a \geqslant b` thì 

	.. math:: P_n(x) = P_{n-1}(x) \oplus x^{a-b} P_{m-1}(x).

	2. Nếu :math:`a < b` thì

	.. math:: P_n(x) = x^{b-a} P_{n-1}(x) \oplus P_{m-1}.

	Trong quá trình tìm :math:`P_n(x)`, khi nào bậc :math:`k_n` của :math:`P_n(x)` thỏa mãn điều kiện số :math:`m` thì ta cập nhật lại số :math:`m`.

	Ở mỗi bước, nếu :math:`P_n(x)` sinh ra toàn bộ dãy bit thì ta dừng thuật toán.

Để xem cách hoạt động của thuật toán Berlekamp-Massey ta sẽ giải ví dụ sau. 

Xét dãy bit :math:`111100100`.

Đặt :math:`n_0 = 0`, :math:`P_{-1}(x) = 1` và :math:`k_{-1} = 0`.

Theo :math:`P_{-1}(x) = 1` thì :math:`1 \to 1 \to 1 \to 1`, nghĩa là bit đầu thành bit thứ hai, bit thứ hai thành bit thứ ba và thứ ba thành thứ tư. Từ đó suy ra

.. math:: 
	P_0 (x) = P_1 (x) = P_2 (x) = P_3 (x) = x^{0+1} \oplus 1 = x \oplus 1.

Do :math:`k_{-1} < k_0 = k_1 = k_2 = k_3` (:math:`0 < 1`) nên :math:`m = 0`.

Để tìm :math:`P_4(x)`, ta có :math:`a =  m- k_{m-1} = 0 - 0 = 0` và :math:`b = n - k_{n-1} = 4 - 1 = 3`. Do :math:`a < b` nên

.. math:: 
	P_4(x) = x^3 P_3(x) \oplus P_{-1}(x) = x^3 \cdot (x \oplus 1) \oplus 1 = x^4 \oplus x^3 \oplus 1.

Do :math:`k_4 > k_3` (:math:`4 > 1`) nên :math:`m = 4`.

.. figure:: ../../figures/berlekamp_massey/berlekamp_massey-1.*

	LFSR tương ứng :math:`P_4(x)`

Trong hình trên, hàng đầu từ trái sang phải là :math:`u_0, u_1, u_2, u_3`. Hàng thứ hai từ trái sang phải là :math:`u_1, u_2, u_3, u_4`. Hàng thứ ba là :math:`u_2, u_3, u_4, u_5`, nhưng :math:`u_5 = 0` theo dãy ban đầu nên LFSR sinh ra :math:`1` là chưa đúng, thuật toán chuyển sang bước tiếp theo.

Để tìm :math:`P_5(x)`, ta có :math:`a = m - k_{m-1} = 4 - 1 = 3` và :math:`b = n - k_{n-1} = 5 - 4 = 1`. Suy ra

.. math:: P_5(x) = P_4(x) \oplus x^2 P_3 (x) = x^4 \oplus x^3 \oplus 1 \oplus x^2 \cdot (x \oplus 1) = x^4 \oplus x^2 \oplus 1.

Theo :math:`P_5(x) = x^4 \oplus x^2 \oplus 1` thì LFSR sẽ hoạt động như hình dưới đây. Cũng theo hình dưới thì :math:`P_6(x) = P_5(x) = x^4 \oplus x^2 \oplus 1`.
	
.. figure:: ../../figures/berlekamp_massey/berlekamp_massey-2.*

	LFSR tương ứng :math:`P_5(x)` và :math:`P_6(x)`

Để tìm :math:`P_7(x)`, ta có :math:`a = m - k_{m-1} = 3` và :math:`b = n - k_{n-1} = 7 - 4 = 3`. Do :math:`a \geqslant b` nên

.. math:: 
	P_7(x) = P_6(x) \oplus P_3(x) = x^4 \oplus x^2 \oplus 1 \oplus x \oplus 1 = x^4 \oplus x^2 \oplus x.

Khi đó LFSR sẽ được sinh như hình.

.. figure:: ../../figures/berlekamp_massey/berlekamp_massey-3.*

	LFSR tương ứng :math:`P_7(x)`

Để tìm :math:`P_8(x)`, :math:`a = 3` và :math:`b = 8 - 4 = 4`. Do :math:`a < b` nên

.. math:: 
	P_8(x) = x P_7(x) \oplus P_3(x) = x^5 \oplus x^3 \oplus x^2 \oplus x \oplus 1.

Lúc này LFSR sẽ là

.. figure:: ../../figures/berlekamp_massey/berlekamp_massey-4.*

	LFSR tương ứng :math:`P_8(x)`

Như vậy đa thức sinh ra dãy bit ban đầu là :math:`x^5 \oplus x^3 \oplus x^2 \oplus x \oplus 1`. Thuật toán Berlekamp-Massey tìm ra đa thức đặc trưng với độ phức tạp là :math:`8` (tìm tới :math:`P_8(x)`).

Ví dụ trên có thể được kiểm tra bởi chương trình Python ở `đây <https://github.com/dunglq2000/lfsr-berlekamp-massey>`_.
