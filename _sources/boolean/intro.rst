Giới thiệu
**********

Giới thiệu
==========

Trung tâm của stream cipher và block cipher là các hàm boolean.

Ở những bài viết ở phần "Đại số boolean và mật mã học" này mình sẽ mô tả các đặc trưng khi xây dựng các hệ mật mã dạng dòng (stream cipher) và khối (block cipher) từ các hàm boolean.

Nhắc lại, hàm boolean :math:`n` biến là ánh xạ :math:`f` từ :math:`\{ 0, 1 \}^n` tới :math:`\{ 0, 1 \}`. Ở phần này mình sẽ sử dụng kí hiệu trường :math:`\mathbb{F}_2`. Như vậy hàm boolean trên :math:`n` biến là ánh xạ

.. math:: f: \mathbb{F}_2^n \to \mathbb{F}_2, \quad f(x_1, x_2, \ldots, x_n) = y.

Tiếp theo, khi "ghép" các hàm boolean lại ta có **hàm boolean vector** (hay **vectorial Boolean function**). Như vậy hàm boolean vector là ánh xạ

.. math:: F: \mathbb{F}_2^n \to \mathbb{F}_2^m, \quad f(x_1, x_2, \ldots, x_n) = (y_1, y_2, \ldots, y_m) \in \mathbb{F}_2^m.

Như vậy chúng ta có thể coi mỗi hàm :math:`y_i = f_i(x_1, \ldots, x_n)` là một hàm boolean nên khi ghép cạnh nhau chúng ta có hàm boolean vector.

+----------------+----------------+----------------+----------------+---------------------------+---------------------------+----------------+---------------------------+
| :math:`x_1`    | :math:`x_2`    | :math:`\cdots` | :math:`x_n`    | :math:`f_1(\bm{x})`       | :math:`f_2(\bm{x})`       | :math:`\cdots` | :math:`f_m(\bm{x})`       |
+================+================+================+================+===========================+===========================+================+===========================+
| :math:`0`      | :math:`0`      | :math:`\cdots` | :math:`0`      | :math:`f_1(0, \ldots, 0)` | :math:`f_2(0, \ldots, 0)` | :math:`\cdots` | :math:`f_m(0, \ldots, 0)` |
+----------------+----------------+----------------+----------------+---------------------------+---------------------------+----------------+---------------------------+
| :math:`\vdots` | :math:`\vdots` | :math:`\vdots` | :math:`\vdots` | :math:`\vdots`            | :math:`\vdots`            | :math:`\vdots` | :math:`\vdots`            |
+----------------+----------------+----------------+----------------+---------------------------+---------------------------+----------------+---------------------------+
| :math:`1`      | :math:`1`      | :math:`\cdots` | :math:`1`      | :math:`f_1(1, \ldots, 1)` | :math:`f_2(1, \ldots, 1)` | :math:`\cdots` | :math:`f_m(1, \ldots, 1)` |
+----------------+----------------+----------------+----------------+---------------------------+---------------------------+----------------+---------------------------+

Ở đây :math:`\bm{x} = (x_1, \ldots, x_n) \in \mathbb{F}_2^n`.

Bảng kí hiệu
============

+------------------------+-------------------------------------------------------------+
| Kí hiệu                | Ý nghĩa                                                     |
+========================+=============================================================+
| :math:`\mathcal{F}_n`  | Tập hợp tất cả hàm boolean :math:`n` biến                   |
+------------------------+-------------------------------------------------------------+
| :math:`\mathcal{A}_n`  | Tập hợp tất cả hàm boolean affine :math:`n` biến            |
+------------------------+-------------------------------------------------------------+
| :math:`\mathcal{L}_n`  | Tập hợp tất cả hàm boolean tuyến tính :math:`n` biến        |
+------------------------+-------------------------------------------------------------+
| :math:`\deg f`         | Bậc của hàm boolean :math:`f` ở dạng chuẩn tắc đại số (ANF) |
+------------------------+-------------------------------------------------------------+
| :math:`\mathrm{wt}(f)` | Trọng số của hàm boolean :math:`f`                          |
+------------------------+-------------------------------------------------------------+
| :math:`N_f`            | Nonlinearity của hàm boolean :math:`f`                      |
+------------------------+-------------------------------------------------------------+
| :math:`W_f(\bm{a})`    | Hệ số Walsh của hàm :math:`f` ứng với vector :math:`\bm{a}` |
+------------------------+-------------------------------------------------------------+

Các tính chất mật mã của hàm boolean
====================================

Bậc đại số cao
--------------

Tham số :math:`\deg f` phải cao. Điều này đặc biệt quan trọng trong các stream cipher sử dụng LFSR.

Nonlinearity cao
----------------

Nonlinearity cực kì quan trọng trong việc chống phá mã tuyến tính (linear cryptanalysis). Nonlinearity càng cao, dấu vết tuyến tính càng thấp.

Hàm boolean có nonlinearity cực đại được gọi là **hàm bent** (hay **bent function**).

Theo phần đại số boolean ở trước thì

.. math:: N_f \leqslant 2^{n-1} - \dfrac{1}{2} \cdot 2^{n / 2 - 1}

khi :math:`n` chẵn.

Điều kiện cần và đủ để tồn tại hàm boolean :math:`n` biến là :math:`n` chẵn.

Nếu :math:`n` lẻ thì không tồn tại hàm bent :math:`n` biến. Tuy nhiên chúng ta vẫn có thể xem xét các hàm có nonlinearity :math:`N_f` lớn nhất và gọi chúng là **Almost Bent (AB)**.

Khi đó

.. math:: N_f \leqslant 2^{n-1} - 2^{(n-1) / 2}.

Bài tập
^^^^^^^

1. Chứng minh rằng khoảng cách từ hàm boolean :math:`f` với :math:`n` biến tới hàm boolean affine

.. math:: l_{\bm{a}, b}(\bm{x}) = a_1 x_1 \oplus \ldots \oplus a_n x_n \oplus b

với :math:`\bm{a} = (a_1, \ldots, a_n) \in \mathbb{F}_2^n` và :math:`b \in \mathbb{F}_2` được tính theo công thức:

.. math::

    d(f, l_{\bm{a}, 0} (\bm{x})) = 2^{n-1} - \frac{1}{2} W_f(\bm{a}),

    d(f, l_{\bm{a}, 1} (\bm{x})) = 2^{n-1} + \frac{1}{2} W_f (\bm{a}).

2. Chứng minh rằng nonlinearity của hàm boolean :math:`f` bất kì được tính bởi công thức

.. math:: N_f = 2^{n-1} - \frac{1}{2} \max_{\bm{y}} \lvert W_f (\bm{y}) \rvert.

3. Chứng minh rằng hàm boolean :math:`f` là hàm bent khi và chỉ khi :math:`W_f(\bm{y}) = \pm 2^{n/2}` với mọi vector :math:`\bm{y}`.

Balanced
--------

Hàm boolean được gọi là **balanced** (hay **cân bằng**, **сбалансированный**) nếu nhận giá trị :math:`0` và :math:`1` nhiều như nhau. Như vậy nếu hàm boolean :math:`f` trên :math:`n` biến cân bằng khi và chỉ khi

.. math:: \mathrm{wt}(f) = 2^{n-1}.

**Bài tập:** Xác định số lượng hàm boolean cân bằng có :math:`n` biến.

:math:`r`-resillient
--------------------

Đặt :math:`r` là số nguyên không âm nhỏ hơn :math:`n`. Hàm boolean :math:`f` với :math:`n` biến được gọi là :math:`r`-resillient (hay :math:`r`-устойчивой) nếu với mọi hàm con mà nhận được từ việc cố định :math:`r` biến thì đều là hàm cân bằng.

Hàm boolean này có độ an toàn cao hơn so với hàm cân bằng, giúp chống lại cách tấn công correlation cryptanalysis.

Correlation immune
------------------

Hàm boolean :math:`f` với :math:`n` biến được gọi là **correlation immune of order** :math:`r` (**корреляционно-иммунной порядка** :math:`r`, tạm dịch là *kháng tương quan bậc* :math:`r`) với :math:`1 \leqslant r \leqslant n` nếu với mọi hàm con :math:`f^{a_1, \ldots, a_r}_{i_1, \ldots, i_r}` nhận được từ việc cố định :math:`r` biến thì đều thỏa đẳng thức

.. math:: \mathrm{wt} (f^{a_1, \ldots, a_r}_{i_1, \ldots, i_r}) = \frac{\mathrm{wt}(f)}{2^r}.

Bài tập
^^^^^^^

1. Chứng minh rằng hàm boolean :math:`f` là :math:`r`-resillient khi và chỉ khi nó cân bằng và correlation immune bậc :math:`r`.
2. (**Định lí Siegenthaler I**, 1984). Chứng minh rằng nếu hàm boolean :math:`f` là correlation immune bậc :math:`r` thì :math:`\deg f + r \leqslant n`.
3. (**Định lí Siegenthaler II**) Chứng minh rằng nếu hàm boolean :math:`f` là :math:`r`-resillient và :math:`r \leqslant n - 2` thì :math:`\deg f + r \leqslant n - 1`.

Chứng minh cho các định lí Siegenthaler có thể tìm ở :cite:`Agibalov`.

4. Chứng minh rằng hàm boolean :math:`f` là correlation immune bậc :math:`r` khi và chỉ khi :math:`W_f(\bm{y}) = 0` với mọi vector :math:`\bm{y}` thỏa :math:`1 \leqslant \mathrm{wt} (\bm{y}) \leqslant r`.

Năm 2007 Д. Г. Фон–Дер–Флаасс tìm được chặn trên cho correlation immune của hàm boolean không cân bằng.

5. (**Định lí Д. Г. Фон–Дер–Флаасс**, :cite:`Flaass`). Gọi :math:`f` là hàm boolean không cân bằng có correlation immune bậc :math:`r` khác :math:`0`. Chứng minh rằng :math:`r \leqslant (2n/3) - 1`.
6. Chứng minh rằng với hàm boolean :math:`r`-resillient :math:`f` sao cho :math:`r \leqslant n-2` thì ta có bất đẳng thức :math:`N_f \leqslant 2^{n-1} - 2^{r+1}` :cite:`Cusick`.

Algebraic immune
----------------

Tính chất này được giới thiệu vào năm 2004.

**Algebraic immune** (tạm dịch là *kháng đại số*) của hàm boolean :math:`f` là số :math:`d` nhỏ nhất sao cho tồn tại hàm boolean :math:`g` bậc :math:`d`, không đồng nhất với :math:`0`, thỏa mãn :math:`f g = 0` hoặc :math:`(f \oplus \bm{1}) g = 0`.

Algebraic immune của hàm :math:`f` được kí hiệu là :math:`\mathsf{AI}(f)`.

Ví dụ algebraic immune hàm :math:`f(\bm{x}) = x_1 x_2 x_3 \oplus x_1` bằng :math:`1`, vì ta có thể chọn :math:`g(\bm{x}) = x_1 \oplus 1`. Khi đó :math:`f g = (x_1 x_2 x_3 \oplus x_1) (x_1 \oplus 1) = 1`.

Bài tập
^^^^^^^

1. Chứng minh rằng algebraic immune của hàm boolean :math:`f` bất kì với :math:`n` biến không vượt quá giá trị :math:`\lceil n/2 \rceil`.
2. Chứng minh một số tính chất cơ bản của algebraic immune:
   
   - :math:`\mathsf{AI}(f) \leqslant \deg f`;
   - :math:`\mathsf{AI}(f \cdot g) \leqslant \mathsf{AI}(f) + \mathsf{AI}(g)`;
   - :math:`\mathsf{AI}(f \oplus g) \leqslant \mathsf{AI}(f) + \mathsf{AI}(g)`;
   - :math:`\mathsf{AI}(f) = \mathsf{AI}(g)` nếu :math:`g` nhận được từ :math:`f` qua một biến đổi affine trên các biến, nghĩa là :math:`g(\bm{x}) = f(\bm{A} \bm{x} \oplus \bm{b})` với :math:`\bm{A}` là ma trận khả nghịch bậc :math:`n` và :math:`\bm{b}` là vector.
 
3. Xác định giá trị của :math:`\mathsf{AI}(f)` với các hàm boolean sau và tìm hàm :math:`g` tương ứng:
    
   - :math:`f(\bm{x}) = x_1 x_2 x_4 \oplus x_1 x_2 \oplus 1`;
   - :math:`f(\bm{x}) = 0`;
   - :math:`f(\bm{x}) = 1`;
   - :math:`f(\bm{x}) = x_1 \cdots x_k` với :math:`k = 1, 2, \ldots, n`;
   - :math:`f(\bm{x}) = x_1 \oplus \ldots \oplus x_n`;
   - :math:`f(\bm{x}) = x_1 x_2 \oplus \ldots \oplus x_{n-1} x_n` (tổng tất cả cặp tích);
   - :math:`f(\bm{x}) = x_1 x_2 x_3 x_4 \oplus x_5 x_6`.

4. Cho ví dụ hàm boolean :math:`f` với giá trị algebraic immune nhỏ nhất, nghĩa là :math:`\mathsf{AI}(f) = d` với :math:`d = 1, 2, \ldots, k`.

Differentially :math:`\delta`-uniform
--------------------------------------

Differential :math:`\delta`-uniform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Khái niệm này lần đầu được định nghĩa trong :cite:`eurocrypt-1993-2628`.

Hàm boolean vector :math:`F : \mathbb{F}_2^n \to \mathbb{F}_2^n` gọi là **differentially** :math:`\delta`- **uniform** nếu với mọi vector :math:`\bm{a}` khác không và vector :math:`\bm{b}` bất kì thì phương trình

.. math:: F(\bm{x}) \oplus F(\bm{x} \oplus \bm{a}) = \bm{b}

có không quá :math:`\delta` nghiệm với :math:`\delta` là số nguyên dương.

Để ý rằng nếu phương trình có nghiệm là :math:`\bm{x}` thì cũng có nghiệm :math:`\bm{x} \oplus \bm{a}`. Số :math:`\delta` càng nhỏ thì phép biến đổi của thuật toán mã hóa càng ít có dấu hiệu vi sai, tăng khả năng kháng phá mã vi sai.

Một cách tổng quát ta có định nghĩa sau.

.. prf:definition:: Differential :math:`\delta`-uniform
    :label: def-delta-uniform

    Hàm boolean vector từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là **differential** :math:`\delta`- **uniform** nếu với mọi :math:`\bm{a} \in \mathbb{F}_p^n` khác không và với mọi :math:`\mathbb{F}_p^m` thì phương trình

    .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

    có không quá :math:`\delta` nghiệm.

Trong mật mã học thường dùng :math:`p = 2`. Thông thường các hàm boolean tập trung vào việc xây dựng các S-box nên :math:`n` thường là :math:`4` hoặc :math:`8`.

Perfect Nonlinear và Almost Perfect Nonlinear
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prf:definition:: Hàm Perfect Nonlinear
    :label: def-PN

    Hàm boolean vector :math:`F` từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là hàm **Perfect Nonlinear (PN)** nếu phương trình

    .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

    có đúng :math:`p^{n-m}` nghiệm với mọi vector :math:`\bm{a} \in \mathbb{F}_p^n` khác không và :math:`\bm{b} \in \mathbb{F}_p^m`.

Số lượng hàm PN rất ít. Đối với các giá trị :math:`n` và :math:`p` thường được sử dụng trong mật mã thậm chí không tồn tại hàm PN. Do đó chúng ta sẽ nới lỏng điều kiện thành hàm Almost Perfect Nonlinear (APN).

.. prf:definition:: Hàm Almost Perfect Nonlinear
    :label: def-APN

    Hàm boolean vector :math:`F` từ :math:`\mathbb{F}_p^n` tới :math:`\mathbb{F}_p^m` được gọi là hàm **Almost Perfect Nonlinear (APN)** nếu phương trình

    .. math:: F(\bm{x} + \bm{a}) - F(\bm{x}) = \bm{b}

    có không quá hai nghiệm với mọi :math:`\bm{a} \in \mathbb{F}_p^n` khác không và với mọi :math:`\bm{b} \in \mathbb{F}_p^m`.

Bài toán khó hiện nay là xây dựng hàm APN là song ánh với số biến :math:`n` chẵn. Đặc biệt là :math:`n` có dạng lũy thừa của :math:`2`.

Như vậy, theo định nghĩa có thể thấy điều tương đương sau

- APN là differential :math:`2`-uniform.
- PN là differential :math:`1`-uniform khi :math:`n = m`.

Hoán vị APN
^^^^^^^^^^^

Từ trước tới nay có ba phương pháp xây dựng hoán vị APN trên :math:`\mathbb{F}_2^n`. Tuy nhiên cả ba phương pháp chỉ hoạt động trên :math:`n` lẻ. Câu hỏi về việc xây dựng hoán vị APN tới giờ vẫn là vấn đề mở với :math:`n` chẵn, dặc biệt là :math:`n` có dạng lũy thừa của :math:`2` như đã nói ở trên.

Bài tập
^^^^^^^

Chứng minh hàm :math:`S : \mathbb{F}_2^8 \to \mathbb{F}_2^8` của S-box trong thuật toán AES là differentially :math:`4`-uniform.

Bài tập này cho thấy rằng S-box tốt thì :math:`\delta` sẽ nhỏ nhất có thể nhằm kháng phá mã vi sai.
