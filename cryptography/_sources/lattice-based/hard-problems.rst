Các bài toán khó
================


.. admonition:: Bài toán 1. (Bài toán nhóm con ẩn, Hidden Group Problem - HGP).

   Cho một nhóm :math:`G` và một hàm :math:`f` trên :math:`G` là hằng số và phân biệt trên các coset của nhóm con :math:`H` nào đó chưa biết của :math:`G`. Hãy tìm một tập các phần tử sinh của :math:`H`.


.. admonition:: Bài toán 2. (Bài toán vector ngắn nhất, Shortest Vector Problem - SVP)

   Cho một cơ sở tùy ý :math:`\bm{V}` của lattice :math:`\mathcal{L}`. Hãy tìm một vector :math:`\bm{x} \in \mathcal{L}` khác không với :math:`\lVert \bm{x} \rVert \leqslant \gamma(n) \cdot \lambda_1(\mathcal{L})`.


.. admonition:: Bài toán 3. (Bài toán Learning With Error, LWE Problem)

   Cho :math:`n, m, q > 0` là các số nguyên và :math:`\chi` là một phân bố lỗi trên :math:`\mathbb{Z}`. Với bí mật :math:`\bm{s} \xleftarrow{\$} \mathbb{Z}_q^n`, định nghĩa :math:`\mathcal{D}_{\bm{s}, \chi}` là phân bố lấy các mẫu :math:`\bm{a} \xleftarrow{\$} \mathbb{Z}_q^n` và :math:`e \xleftarrow{\chi} \mathbb{Z}`. Kết quả trả về :math:`(\bm{a}, \langle \bm{a}, \bm{s} \rangle + e \bmod q) \in \mathbb{Z}_q^n \times \mathbb{Z}_q`.

   1. Với :math:`n, q \geqslant 2` và :math:`m` mẫu độc lập từ phân bố :math:`\mathcal{D}_{\bm{s}, \chi}`, bài toán LWE tìm kiếm là tìm :math:`\bm{s}` (search LWE problem).

   2. Với :math:`n, q \geqslant 2` và :math:`m` mẫu độc lập :math:`(\bm{a}_i, b_i)`, bài toán LWE quyết định (decisional LWE problem) là phân biệt với :math:`i = 1, \ldots, m` thì :math:`(\bm{a}_i, b_i)` thuộc :math:`\mathbb{Z}_q^n \times \mathbb{Z}_q` hay thuộc :math:`\mathcal{D}_{\bm{s}, \chi}`. Nói cách khác là được lấy mẫu ngẫu nhiên theo :math:`\mathbb{Z}_q^n \times \mathbb{Z}_q` hay theo phân bố :math:`\mathcal{D}`.


Thông thường chúng ta coi vector :math:`\bm{s}` là secret và :math:`e` là lỗi (error) của LWE.

Chúng ta nói rằng bài toán LWE quyết định :math:`\text{LWE}_{n, m, q, \chi}` là :math:`(t, \varepsilon)`-hard nếu đối với bất kì thuật toán :math:`\mathcal{A}` nào chạy trong thời gian :math:`t`, nó đảm bảo rằng:

.. math::

   \left| \mathrm{Pr}\left[ \mathcal{A}^{\mathcal{D}_{\bm{s}, \chi}}(\cdot) = 1 \right] - \mathrm{Pr} \left[ \mathcal{A}^{\mathcal{U}(\mathbb{Z}_q^n \times \mathbb{Z}_q)} (\cdot) = 1 \right] \right| \leqslant \varepsilon


.. admonition:: Bài toán 4. (Bài toán Ring-LWE, R-LWE)

   Cho :math:`n, q > 0` là các số nguyên và :math:`\chi` là phân bố trên :math:`\mathcal{R}`. Với :math:`s \xleftarrow{\$} \mathcal{R}`, định nghĩa :math:`\mathcal{D}_{s, \chi}` là phân bố lấy các mẫu :math:`a \xleftarrow{\$} \mathcal{R}_q` và :math:`e \xleftarrow{\chi} \mathcal{R}`. Kết quả trả về :math:`(a, a s + e) \in \mathcal{R}_q \times \mathcal{R}_q`.

   Tương tự:

   1. Bài toán R-LWE tìm kiếm (search ring-LWE problem) là tìm :math:`s`.
   2. Bài toán R-LWE quyết định (decisional ring-LWE problem) là phân biệt :math:`(a_i, b_i) \xleftarrow{\$} \mathcal{R}_q \times \mathcal{R}_q` hay :math:`(a_i, b_i) \gets \mathcal{D}_{s, \chi}`.


Short vectors trong lattice
---------------------------


Các bài toán liên quan tới lattice mà chúng ta cần quan tâm để xây dựng các thuật toán mã hóa lattice-based.

1. **Shortest Vector Problem** (hay **SVP**): Tìm vector khác không có độ dài ngắn nhất trong lattice :math:`\mathcal{L}`, nghĩa là tìm :math:`\bm{v} \in \mathcal{L}` sao cho :math:`\lVert \bm{v} \rVert` nhỏ nhất;
2. **Closest Vector Problem** (hay **CVP**): Cho trước vector :math:`\bm{w} \in \mathbb{R}^n` mà không nằm trong :math:`\mathcal{L}`, tìm :math:`\bm{v} \in \mathcal{L}` gần với :math:`\bm{w}` nhất, nghĩa là cực tiểu hóa :math:`\lVert \bm{w} - \bm{v} \rVert`.

Thuật toán Babai
----------------


Thuật toán này giúp tìm một cơ sở "đủ tốt" để giải **apprCVP**.

.. prf:theorem:: Thuật toán Babai tìm vector gần nhất

   Gọi :math:`\mathcal{L} \subset \mathbb{R}^n` là lattice với cơ sở là :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_n` và gọi :math:`\bm{w} \in \mathbb{R}^n` là vector bất kỳ. 
   	
   Nếu các vector trong cơ sở trực giao nhau thì thuật toán Babai sẽ giải được **CVP**.
   	
   Nếu các vector trong cơ sở gần như trực giao thì thuật toán Babai sẽ giải được **apprCVP**.
   	
   Ngược lại, nếu các vector trong cơ sở không trực giao (nhiều) thì kết quả thuật toán trả về sẽ xa hơn vector gần với :math:`\bm{w}`.


.. prf:algorithm:: Thuật toán điểm gần nhất của Babai

   1. Biểu diễn :math:`\bm{w} = t_1 \bm{v}_1 + t_2 \bm{v}_2 + \ldots + t_n \bm{v}_n` với :math:`t_1, \ldots, t_n \in \mathbb{R}`.
   2. Đặt :math:`a_i = \lfloor t_i \rceil` với :math:`i = 1, \ldots, n`.
   3. Trả về vector :math:`\bm{v} = a_1 \bm{v}_1 + a_2 \bm{v}_2 + \ldots + a_n \bm{v}_n`.


Có thể thấy thuật toán Babai làm tròn các hệ số để trả về một vector lattice gần với :math:`\bm{w}`.
