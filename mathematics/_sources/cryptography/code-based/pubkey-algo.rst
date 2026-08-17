Các hệ mật mã khóa công khai dựa trên lý thuyết code
====================================================


Hệ mật mã McEliece
-------------------

Hệ mật mã McEliece được phát triển bởi R.J. Mceliece 
vào năm 1978 trong :cite:`McEliece1978APK`.


Ý tưởng xây dựng
^^^^^^^^^^^^^^^^

Đặt :math:`\bm{G}` là ma trận sinh của linear code 
:math:`[n, k]_q` :math:`\mathcal{C}` nào đó, sửa 
được :math:`t` lỗi.


Tham số
^^^^^^^

* :math:`\mathcal{C} = \{ \mathcal{C}_\lambda \}_{\lambda \in \Lambda}` 
  là một họ các linear code trên trường :math:`\mathbb{F}_q` 
  sao cho với mỗi code :math:`\bm{C} \in \mathcal{C}` có 
  một thuật toán decode hiệu quả là :math:`\mathsf{Decode}` 
  sửa được :math:`t` lỗi. Ở đây :math:`\Lambda \subseteq \{ 0, 1 \}^\star` 
  là tập các giá trị của tham số code trong họ.
* :math:`\mathsf{Sample}(1^\lambda)` là thuật toán xác suất 
  hiệu quả và детерминированный, sao cho với giá trị tham số 
  :math:`\lambda \in \Lambda` cho ra ma trận sinh :math:`\bm{G}` 
  của code :math:`\mathcal{C}_\lambda`, số lượng lỗi :math:`t` 
  và thuật toán :math:`\mathsf{Decode}`, giải được bài toán 
  decode trên linear code :math:`[n, k]_q` với ma trận sinh 
  :math:`\bm{G}` và kênh truyền có :math:`t` lỗi. Kí hiệu 
  :math:`\mathcal{G} = \{ \bm{G}_\lambda \}_{\lambda \in \Lambda}` 
  là tập tất cả ma trận sinh cho ra thuật toán 
  :math:`\mathsf{Sample}(1^\lambda)` cho mọi trường hợp 
  tham số :math:`\lambda \in \Lambda`.


Thuật toán sinh khóa (Gen)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Private key gồm:

1. Ma trận :math:`\bm{M} \in \mathrm{GL}_q(k)` 
   không suy biến cỡ :math:`k \times k` trên :math:`\mathbb{F}_q`.
2. :math:`\bm{G} \in V_{k \times n}(q)` là 
   ma trận sinh của :math:`[n, k]_q` code :math:`\mathcal{C}_\lambda`.
3. :math:`\bm{P} \in \mathcal{S}_n` là hoán vị 
   trên tập :math:`\{ 1, \ldots, n \}`.
4. :math:`\mathsf{Decode}` là thuật toán decode 
   trên mã :math:`\mathcal{C}_\lambda`.

Public key gồm:

1. :math:`\bm{G}_{pub} = \bm{M} \cdot \bm{G} \cdot \bm{P} \in V_{k \times n}(q)` 
   là ma trận sinh của code tương đương với code 
   :math:`\mathcal{C}_\lambda`.
2. :math:`t \in \mathbb{N}` là số lỗi được decode 
   bởi :math:`\mathsf{Decode}`.


Thuật toán mã hóa (Enc)
^^^^^^^^^^^^^^^^^^^^^^^

Thuật toán mã hóa nhận đầu vào là thông điệp 
:math:`\bm{m} \in V_k(q)` và trả về ciphertext 
:math:`\bm{c} \in V_n(q)`.

Để mã hóa, chọn ngẫu nhiên vector :math:`\bm{e} \in V_n(q)` 
độ dài :math:`n` và có trọng số Hamming bằng :math:`t`. 
Khi đó ta tính ciphertext:

.. math:: \bm{c} = \bm{m} \cdot \bm{G}_{pub} + \bm{e}.


Thuật toán giải mã (Dec)
^^^^^^^^^^^^^^^^^^^^^^^^

1. Tính :math:`\bm{b} \gets \bm{c} \cdot \bm{P}^{-1}`.
2. Tính :math:`\bm{u} \gets \mathsf{Decode}(\bm{b})`.
3. Tính :math:`\bm{m} \gets \bm{u} \cdot \bm{M}^{-1}`.

Khi đó :math:`\bm{m}` là plaintext ban đầu.


Hệ mật mã Niederreiter
-----------------------


Tham số
^^^^^^^

* :math:`\mathcal{C} = \{ \mathcal{C}_\lambda \}_{\lambda \in \Lambda}` 
  là một họ các linear code trên trường :math:`\mathbb{F}_q` 
  sao cho với mỗi code :math:`C \in \mathcal{C}` 
  có một thuật toán decode hiệu quả là 
  :math:`\mathsf{Decode}` sửa được :math:`t` lỗi. 
  Ở đây :math:`\Lambda \subseteq \{ 0, 1 \}^\star` 
  là tập các giá trị của tham số code trong họ.
* :math:`\mathsf{Sample}(1^\lambda)` là thuật toán 
  xác suất hiệu quả và детерминированный, sao cho 
  với giá trị tham số :math:`\lambda \in \Lambda` cho ra 
  ma trận parity-check :math:`\bm{H}` của code 
  :math:`\mathcal{C}_\lambda`, số lượng lỗi :math:`t` 
  và thuật toán :math:`\mathsf{SDecode}`, giải được 
  bài toán syndrome decode trên linear code 
  :math:`[n, k]_q` với ma trận parity-check :math:`\bm{H}` 
  và kênh truyền có :math:`t` lỗi. Kí hiệu 
  :math:`\mathcal{H} = \{ \bm{H}_\lambda \}_{\lambda \in \Lambda}` 
  là tập tất cả ma trận parity-check cho ra 
  thuật toán :math:`\mathsf{Sample}(1^\lambda)` cho mọi 
  trường hợp tham số :math:`\lambda \in \Lambda`.


Thuật toán sinh khóa (Gen)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Private key gồm:

1. Ma trận :math:`\bm{M} \in \mathrm{GL}_q(r)` 
   cỡ :math:`r \times r` trên :math:`\mathbb{F}_q`, 
   với :math:`r = n - k` là số kí tự kiểm tra của 
   :math:`[n, k]_q` code :math:`\mathcal{C}_\lambda`.
2. :math:`\bm{H} \in V_{r \times n}(q)` là ma trận 
   parity-check của :math:`[n, k]_q` code 
   :math:`\mathcal{C}_\lambda`.
3. :math:`\bm{P} \in \mathcal{S}_n` là hoán vị 
   trên :math:`\{ 1, \ldots, n \}`.
4. :math:`\mathsf{SDecode}` là thuật toán 
   syndrome decode trên code :math:`\mathcal{C}_\lambda`.

Public key gồm:

1. :math:`\bm{H}_{pub} = \bm{M} \cdot \bm{H} \cdot \bm{P} \in V_{k \times n}(q)` 
   là ma trận parity-check của code mới tương đương 
   với code :math:`\mathcal{C}_\lambda`.
2. :math:`t \in \mathbb{N}` là số lượng lỗi 
   có thể sửa bởi :math:`\mathsf{SDecode}`.


Thuật toán mã hóa (Enc)
^^^^^^^^^^^^^^^^^^^^^^^

Plaintext được biểu diễn thành vector :math:`\bm{m} \in V_l(q)` 
với :math:`l = \lfloor \log_q ((q - 1)^t \binom{n}{t}) \rfloor`. 
Ciphertext là vector :math:`\bm{c} \in V_r(q)`.

Ta cần ánh xạ :math:`\varphi_{n, t, q} : V_l(q) \to V_n(q)` là 
đơn ánh, với mỗi :math:`\bm{m} \in V_l(q)` cho ra vector 
:math:`\bm{e} \in V_n(q)` có trọng số Hamming là :math:`t`.

1. :math:`\bm{e} \gets \varphi_{n, t, q}(\bm{m})`
2. :math:`\bm{c} \gets \bm{e} \cdot \bm{H}_{pub}^\top`


Thuật toán giải mã (Dec)
^^^^^^^^^^^^^^^^^^^^^^^^

Đẻ giải mã ta cần ánh xạ :math:`\varphi_{n, t, q}^{-1}` 
là ánh xạ ngược của :math:`\varphi_{n, t, q}`.

1. :math:`\bm{s} \gets \bm{M}^{-1} \bm{c}^\top`.
2. :math:`\bm{e} \gets \mathsf{SDecode}(\bm{c})`.
3. :math:`\bm{e} \gets \bm{e} \cdot \bm{P}`.
4. :math:`\bm{m} \gets \varphi^{-1}_{n, t, q}(\bm{e})`.
