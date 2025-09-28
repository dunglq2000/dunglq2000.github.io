Các nghịch lý về tập vô hạn
===========================

Tiếp theo chúng ta sẽ xem hết những bài toán hết sức thú vị 
cùng những lập luận cũng thú vị không kém để thấy rằng có 
nhiều điều bất ngờ sẽ xảy ra nếu vận dụng những lý luận chặt chẽ.


Nghịch lý Zeno
---------------

Zeno là nhà triết học cổ Hy Lạp nổi tiếng với bài toán *Achilles 
và rùa* (Achilles là anh hùng trong thần thoại Hy Lạp). Bài toán 
được phát biểu đơn giản như sau: 

    Nếu Achilles chạy đua và xuất phát sau con rùa thì 
    Achilles sẽ không bao giờ bắt kịp con rùa.

Bài toán nghe thật nực cười nhưng dưới lập luận của Zeno thì 
bài toán sẽ trở nên "có lý".

Zeno lập luận như sau: gọi :math:`d_1` là khoảng cách ban đầu giữa 
Achilles và con rùa. Achilles sẽ mất một khoảng thời gian :math:`t_1` 
để đi tới vị trí con rùa. Tuy nhiên trong khoảng thời gian :math:`t_1` 
đó con rùa cũng đã đi một đoạn :math:`d_2` nào đó rồi. Dĩ nhiên 
:math:`d_2` sẽ ngắn hơn :math:`d_1`. Nhưng nếu quá trình này lặp đi 
lặp lại, :math:`d_n` sẽ trở nên càng ngày càng nhỏ, tuy nhiên không 
bao giờ bằng :math:`0`. Nói cách khác, Achilles không bao giờ bắt 
kịp con rùa.

Dưới góc nhìn của toán học hiện đại, điều này chưa hẳn đúng. Vì thời 
Zeno chưa có nhiều khái niệm lẫn công cụ về vô cực, nên người ta đã 
công nhận tổng vô hạn sẽ là vô hạn. Học sinh lớp 11 hiện nay khi học 
tới cấp số nhân lùi vô hạn sẽ biết cách tính tổng 

.. math:: \frac{1}{10} + \frac{1}{100} + \cdots \frac{1}{10^n} = \frac{1}{9}

là hữu hạn.


So sánh :math:`\mathbb{N}` và :math:`\mathbb{Z}`
-------------------------------------------------

    Hai tập hợp :math:`\mathbb{N}` và :math:`\mathbb{Z}` là các tập vô hạn, như vậy lực lượng của tập hợp nào lớn hơn?

Câu hỏi tưởng chừng như vô vị vì nhìn vào mọi người đều thấy rằng 
:math:`\mathbb{Z}` "bao trọn" :math:`\mathbb{N}` (số nguyên kéo dài 
vô hạn về bên trái lẫn phải trong khi số tự nhiên chỉ kéo dài vô hạn 
về bên phải). Tuy nhiên, nhà toán học Cantor đã tìm ra một lý luận đầy 
*tính thuyết phục* để chứng minh rằng lực lượng của hai tập là bằng nhau.

Ta xét ánh xạ :math:`f: \mathbb{Z} \to \mathbb{N}` như sau:

- :math:`f(0) = 0`;
- các số âm của :math:`\mathbb{Z}` biến thành các số lẻ của :math:`\mathbb{N}`;
- các số dương của :math:`\mathbb{Z}` thì biến thành các số chẵn của :math:`\mathbb{N}`.

Ví dụ :math:`f(-1) = 1`, :math:`f(-2) = 3`, :math:`f(-3) = 5` và cứ như vậy tăng lên.

Tương tự với số dương :math:`f(1) = 2`, :math:`f(2) = 4`.

Ta có công thức

.. math:: 
    
    z = f(n) = \begin{cases} 2n, & \quad \text{nếu} \ n \geqslant 0 \\
    -1-2n, & \quad \text{nếu} \ n < 0.\end{cases}

Như vậy :math:`f` là đơn ánh vì hai phần tử khác nhau của :math:`\mathbb{Z}` 
sẽ cho ra hai phần tử khác nhau thuộc :math:`\mathbb{N}`. Tương tự :math:`f` 
cũng là toàn ánh vì mọi phần tử thuộc :math:`\mathbb{N}` đều có một phần tử 
từ :math:`\mathbb{Z}` biến thành. Như vậy :math:`f` là song ánh. Vậy lực 
lượng :math:`\mathbb{N}` và :math:`\mathbb{Z}` bằng nhau.

Bằng lập luận tương tự cũng có thể chứng minh số phần tử của :math:`\mathbb{Q}` 
bằng số phần tử của :math:`\mathbb{N}`. Những lập luận này đã gây ra tiếng vang 
lớn vào thời đó.

Ở :numref:`hình %s <meme-1>` cho thấy một cách xây dựng song ánh từ 
:math:`\mathbb{N}` tới :math:`\mathbb{Z}^2`, trong đó:

- điểm :math:`(0, 0)` tương ứng với :math:`1`;
- điểm :math:`(1, 0)` tương ứng với :math:`2`;
- điểm :math:`(1, 1)` tương ứng với :math:`3`;
- điểm :math:`(0, 1)` tương ứng với :math:`4`;
- cứ tiếp tục như vậy theo hình xoắn vuông.

Vietsub cho :numref:`hình %s <meme-1>`: Không có chuyện :math:`\mathbb{N}` và 
:math:`\mathbb{Z}^2` có cùng số phần tử. Ở đây thuật ngữ "số phần tử" không 
thực sự chính xác mà nên gọi là "lực lượng" vì khi nói đến các tập vô hạn (tức 
tập có vô hạn phần tử) thì vô hạn không thể so sánh với vô hạn. Hai tập hợp 
vô hạn chỉ có thể có cùng lực lượng.

.. _meme-1:

.. figure:: https://sun9-41.userapi.com/impg/zmz_1-_MamZ7dwVLXKooNar7f1hC5crUItC2YA/sCWd3BmHVqc.jpg?size=640x550&quality=95&sign=53e3e82934396255a586fb2e39f0c82e&type=album 

    Song ánh giữa :math:`\mathbb{N}` và :math:`\mathbb{Z}^2`. Nguồn: https://vk.com/wall-91031095_82482.

Từ đây tập hợp vô hạn có thể chia ra **đếm được** (countable) 
và **không đếm được** (uncountable). Tiếp theo ta định nghĩa hai 
dạng tập hợp này.

1. Tập hợp được gọi là **đếm được** khi tồn tại song ánh từ nó tới :math:`\mathbb{N}`.
2. Tập hợp được gọi là **không đếm được** khi nó không phải là tập đếm được.


Định lý về :math:`\mathbb{R}`
-----------------------------

.. prf:theorem:: 
    :label: thr-about-R

    Tập hợp số thực :math:`\mathbb{R}` là tập không đếm được.

Chúng ta cần một nhận xét sau:

    Khoảng :math:`(0; 1)` là tương đương với tập :math:`\mathbb{R}`.

Chúng ta có thể xây dựng một song ánh từ :math:`\mathbb{R}` tới :math:`(0, 1)`, 
ví dụ :math:`f(x) = \dfrac{e^x}{e^x+1}`.

Khi đó, thay vì chứng minh :math:`\mathbb{R}` không đếm được, ta chỉ 
cần chứng minh đoạn :math:`(0; 1)` không đếm được.

.. admonition:: Chứng minh
    :class: danger

    Cantor đưa ra hai phương pháp chứng minh và cả hai đều độc đáo. 

    **Phương án 1:** Phương pháp chéo hóa (diagonalization).

    Xét ánh xạ

    .. math::   
        
        & 0 \to 0,a_{0, 0}a_{0, 1}a_{0, 2} \cdots \\
        & 1 \to 0,a_{1, 0}a_{1, 1}a_{1, 2} \cdots \\
        & 2 \to 0,a_{2, 0}a_{2, 1}a_{2, 2} \cdots \\
        & \cdots

    Ta chứng minh ánh xạ này không phải toàn ánh.

    Xét số :math:`y = 0,b_0 b_1 b_2 \ldots` với :math:`b_i \neq a_{i, i}` 
    với mọi :math:`i`, tức là trên đường chéo của các số trên ta chọn số 
    :math:`b_i` khác với số trên đường chéo. Như vậy số :math:`y` này có 
    chữ số ở vị trí :math:`0` khác :math:`f(0)`, chữ số ở vị trí :math:`1` 
    khác :math:`f(1)`, vân vân và mây mây, nên không tìm được số :math:`n` 
    nào mà :math:`f(n) = y`. Ta suy ra :math:`f` không phải toàn ánh và 
    từ đó không phải song ánh.

    **Phương án 2.** Phương pháp dãy các đoạn thẳng đóng bị chặn lồng vào 
    nhau (sequence of closed bounded nested).

    Giả sử đoạn :math:`(0; 1)` đếm được. Khi đó ta có thể liệt kê các 
    phần tử của đoạn là :math:`I = \{ x_1, x_2, \ldots \}`.

    Từ tập :math:`I` ta lấy ra một đoạn con :math:`I_1` sao cho :math:`x_1 \not\in I_1`.

    Tiếp theo, từ tập :math:`I_1` ta lấy ra một đoạn con :math:`I_2` 
    sao cho :math:`x_2 \not\in I_2`.

    Tiếp tục như vậy, ta lấy ra các đoạn con

    .. math:: \cdots \subset I_n \subset \cdots \subset I_2 \subset I_1 \subset I

    với :math:`x_n \not\in I_n` với mọi :math:`n \in \mathbb{N}`.

    Theo định lý về các đoạn thẳng đóng bị chặn lồng vào nhau thì giao của 
    chúng không rỗng, tức là tồn tại số :math:`x` thuộc giao giao của các tập 
    :math:`I_1`, ..., :math:`I_n`. Phần tử :math:`x \in I_n` với mọi :math:`n`. 
    Do :math:`x_n \not\in I_n` và :math:`x \in I_n` nên :math:`x \neq x_n` với 
    mọi :math:`n`, tức là không nằm trong tập :math:`I`. Điều này mâu thuẫn 
    với giả sử đoạn :math:`(0; 1)` đếm được, suy ra đoạn :math:`(0; 1)` là tập 
    không đếm được.
