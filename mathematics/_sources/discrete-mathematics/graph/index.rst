Lý thuyết đồ thị
****************

Phần này mình sử dụng các quyển sách dành cho học sinh chuyên Tin :cite:`TLCTin1`.

.. toctree:: 
   :maxdepth: 2

   definitions
   connection
   tree
   exercises

   application-1
   application-2
   application-3
   euler_hamilton

Đường đi ngắn nhất
==================

Đồ thị có trọng số là bộ ba :math:`G = (V, E, w)`, trong đó :math:`G = (V, E)` là đồ thị và :math:`w` là hàm trọng số:

.. math:: w: E \to \RR, e \mapsto w(e).

Hàm trọng số gán cho mỗi cạnh :math:`e` của đồ thị một số thực :math:`w(e)`, gọi là trọng số (weight) của cạnh.

Nếu cạnh :math:`e = (u, v)` thì ta cũng kí hiệu :math:`w(u, v) = w(e)`.

Đối với đồ thị :math:`n` đỉnh, ta có thể biểu diễn bằng ma trận trọng số :math:`W = \{ w_{uv} \}_{n \times n}`, trong đó :math:`w_{uv}` là trọng số của cạnh :math:`(u, v)`.

Khi :math:`(u, v) \notin E` thì :math:`w_{uv}` sẽ được gán giá trị đặc biệt để nhận biết đây không phải là cạnh, ví dụ là :math:`-\infty`, :math:`+\infty`, :math:`0`.

Đường đi, chu trình được định nghĩa giống trường hợp không có trọng số, chỉ khác là độ dài đường đi không tính bằng số cạnh đi qua mà là tổng trọng số của các cạnh đi qua. Độ dài của đường đi :math:`P` được kí hiệu là :math:`w(P)`.

Đường đi ngắn nhất xuất phát từ một đỉnh
----------------------------------------

(Single-source shortest path)

Cho đồ thị có trọng số :math:`G = (V, E, w)`. Hãy tìm các đường đi ngắn nhất xuất phát từ đỉnh :math:`s \in V` đến tất cả đỉnh còn lại của đồ thị.

Độ dài của đường đi từ :math:`s` tới :math:`t`, kí hiệu là :math:`\delta(s, t)`, gọi là **khoảng cách** (distance) từ :math:`s` tới :math:`t`.

Nếu không tồn tại đường đi từ :math:`s` tới :math:`t` thì ta đặt :math:`\delta(s, t) = +\infty`.

Cấu trúc bài toán con tối ưu
----------------------------

Định lí 1-1. Cho đồ thị có trọng số :math:`G = (V, E, w)`. Gọi :math:`P = (v_1, v_2, \ldots, v_k)` là đường đi ngắn nhất từ :math:`v_1` tới :math:`v_k`. Khi đó với mọi :math:`i`, :math:`j` sao cho :math:`1 \leqslant i \leqslant j \leqslant k`, đường đi :math:`P_{ij} = (v_i, v_{i+1}, \ldots, v_j)` là đường đi ngắn nhất từ :math:`v_i` tới :math:`v_j`.

Từ định lí 1-1 ta có thể thấy các thuật toán tìm đường đi ngắn nhất đều là thuật toán quy hoạch động hoặc tham lam (Floyd, Dijkstra).

Lưu ý, khi đồ thị có chu trình âm thì bài toán tìm đường đi ngắn nhất là bài toán NP đầy đủ.

Bài toán đo khoảng cách
-----------------------

Nếu đồ thị không có chu trình âm thì có thể chứng minh rằng một trong những đường đi ngắn nhất là đường đi đơn.

Khi đó, chỉ cần biết khoảng cách từ :math:`s` tới tất cả đỉnh khác thì đường đi ngắn nhất từ :math:`s` tới :math:`t` có thể tìm qua thuật toán sau.

Trước tiên, ta tìm đỉnh :math:`v_1 \neq t` sao cho :math:`\delta(s, t) = \delta(s, v_1) + c(v_1, t)`.

Dễ thấy rằng luôn tồn tại đỉnh :math:`v_1` như vậy, và đỉnh đó đứng liền trước :math:`t` trên đuòng đi từ :math:`s` tới :math:`t`.

Nếu :math:`v_1 = s` thì đường đi ngắn nhất là đường đi trực tiếp theo cung :math:`(s, t)`.

Nếu không thì vấn đề trở thành tìm đường đi ngắn nhất từ :math:`s` tới :math:`v_1`. Tương tự, ta tìm được đỉnh :math:`v_2 \notin \{ t, v_1 \}` sao cho

.. math:: \delta(s, v_1) = \delta(s, v_2) + c(v_2, t).

Tiếp tục tới khi ta có :math:`v_k = s`.

Nhãn và phép co
---------------

Với mỗi đỉnh :math:`v \in V`, nhãn khoảng cách :math:`d[v]` là độ dài của đường đi nào đó từ :math:`s` tới :math:`v`.

Nếu ta chưa xác định được đường đi nào từ :math:`s` tới :math:`v`, gán nhãn :math:`d[v] = +\infty`.

Khi đó ta khởi tạo vói mọi :math:`v \in V`:

.. math:: d[v] = \begin{cases} 0, \text{nếu} \ v = s \\ +\infty, \text{nếu} \ v \neq s \end{cases}

Do tính chất của nhãn khoảng cách, ta có :math:`d[v] \geqslant \delta(s, v)` với mọi :math:`v \in V`.
