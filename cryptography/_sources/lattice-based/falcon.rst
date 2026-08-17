======
FALCON
======

Falcon là lược đồ chữ ký hậu lượng tử theo mô hình hash-and-sign. Lược đồ
dùng NTRU lattice làm trapdoor và lấy mẫu Gaussian trong miền FFT để tìm
một vector ngắn thuộc lớp ghép xác định bởi thông điệp.

Không gian đại số
-----------------

Falcon làm việc với các phần tử thuộc vành 
:math:`\dfrac{\mathbb{Q}[x]}{\phi(x)}`, ở đây 
:math:`\phi(x) = x^n + 1` và :math:`n = 2^k`.

Ở đây :math:`\phi(x)` là đa thức cyclotomic nên ta có

.. math:: \phi(x) = \prod_{k \in \mathbb{Z}_m^{\times}} (x - \xi^k)

với :math:`m = 2n` và :math:`\xi` là nghiệm bậc 
:math:`m` của đơn vị.

:math:`\mathbb{Z}_m^{\times}` là nhóm các phần tử 
khả nghịch của :math:`\mathbb{Z}_m` đối với phép nhân.

Ta có quan hệ

.. math:: \mathbb{Q} \subseteq \mathbb{Q}[x] / (x^2 + 1) \subseteq \cdots \subseteq \mathbb{Q}[x] / (x^{n/2} + 1) \subseteq \mathbb{Q}[x] / (x^n + 1)

và chuỗi đẳng cấu

.. math:: \mathbb{Q}^n \cong (\mathbb{Q}[x] / (x^2 + 1))^{n / 2} \cong \cdots \cong (\mathbb{Q}[x] / (x^{n/2} + 1))^2 \cong \mathbb{Q}[x] / (x^n + 1).

Đặt

.. math:: a(x) = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1} \in \mathcal{Q}, b(x) = b_0 + b_1 x + \cdots + b_{n-1} x^{n-1} \in \mathcal{Q}

với :math:`\mathcal{Q}` là vành :math:`\mathbb{Q}[x] / (x^n + 1)`.

Kí hiệu :math:`a^*(\xi)` và gọi là Hermitian adjoint của 
:math:`a`, là phần tử duy nhất của :math:`\mathcal{Q}` sao 
cho mọi nghiệm :math:`\xi` của :math:`\phi(x)` ta đều có 
:math:`a^*(\xi) = \overline{a(\xi)}`, trong đó :math:`\overline{\cdot}` 
là liên hợp phức (complex conjugation) trên :math:`\mathbb{C}`.

Với :math:`\phi(x) = x^n + 1`, adjoint được tính bởi
:math:`a^*(x)=a(x^{-1}) \bmod (x^n+1)`, tức là

.. math::

   a^*(x)=a_0-a_{n-1}x-a_{n-2}x^2-\cdots-a_1x^{n-1}.

Ta mở rộng định nghĩa (Hermitian) adjoint lên vector và ma trận.

Adjoint :math:`B^*` của ma trận :math:`B \in \mathcal{Q}^{n \times m}`
là chuyển vị kết hợp với adjoint trên từng phần tử:

.. math:: 
    
    B = \begin{pmatrix}
        a & b \\ c & d
    \end{pmatrix} \Rightarrow B^* = \begin{pmatrix}
        a^* & c^* \\ b^* & d^*
    \end{pmatrix}.

Tích vô hướng (inner product) của hai đa thức :math:`a(x)` 
và :math:`b(x)` là

.. math:: \langle a, b \rangle = \dfrac{1}{n} \cdot \sum_{\phi(\xi) = 0} a(\xi) \cdot \overline{b(\xi)}

đây gọi là cách biểu diễn bằng fast fourier transform.

Ta mở rộng lên vector, với :math:`\bm{u} = (u_i)_i`
và :math:`\bm{v} = (v_i)_i` thuộc :math:`\mathcal{Q}^m` thì

.. math:: \langle \bm{u}, \bm{v} \rangle = \sum_{i} \langle u_i, v_i \rangle.

Cách chọn :math:`\phi(x)` ở trên cho chúng ta tích vô 
hướng giống thông thường

.. math:: \langle a, b \rangle = \sum_{i=0}^{n-1} a_i b_i

đây là cách biểu diễn bằng hệ số.

Ring lattice: với vành :math:`\mathcal{Q} = \mathbb{Q}[x] / \phi(x)` 
và :math:`\mathcal{Z} = \mathbb{Z}[x] / \phi(x)`, số nguyên dương 
:math:`m \geqslant n` và ma trận full-rank :math:`B \in \mathcal{Q}^{n \times m}`, 
ta kí hiệu :math:`\Lambda(B)` là module sinh bởi các hàng của :math:`B`:

.. math:: \Lambda(B) = \{ \bm{z} B : \bm{z} \in \mathcal{Z}^n \} \subseteq \mathcal{Q}^m.

Mở rộng ra, tập :math:`\Lambda` là lattice nếu tồn tại ma 
trận :math:`B` sao cho :math:`\Lambda = \Lambda(B)`.

Ta có thể nói :math:`\Lambda \subseteq \mathcal{Z}^m` là 
lattice :math:`q`-phân nếu :math:`q \mathcal{Z}^m \subseteq \Lambda`.

Phân phối Gaussian rời rạc
--------------------------

Với :math:`\sigma, mu \in \mathbb{R}` mà :math:`\sigma > 0`, 
ta định nghĩa hàm Gauss :math:`\rho_{\sigma, \mu}` là

.. math:: \rho_{\sigma, \mu} = \exp(-(x - \mu)^2 / (2 \sigma^2)),

và phân phối Gauss rời rạc :math:`D_{\mathbb{Z}, \sigma, \mu}` trên vành số nguyên là

.. math:: D_{\mathbb{Z}, \sigma, \mu}(x) = \frac{\rho_{\sigma, \mu}(x)}{\sum_{z \in \mathbb{Z}} \rho_{\sigma, \mu}(z)}.

Trực giao hóa Gram--Schmidt và cây Falcon
-----------------------------------------

Mỗi ma trận :math:`B \in \mathcal{Q}^{n \times m}` có thể phân tích thành :math:`B = L \times \tilde{B}` với :math:`L` là ma trận tam giác dưới (lower triangle) với các phần tử trên đường ché chính bằng :math:`1`.

Các hàng :math:`\tilde{b}_i` của :math:`\tilde{B}` thỏa
:math:`\langle \tilde b_i, \tilde b_j \rangle = 0` với :math:`i \neq j`.
Khi :math:`B` full-rank thì phân tích này là duy nhất và được gọi là
trực giao hóa Gram--Schmidt (GSO).

Ta gọi chuẩn Gram-Schmidt (norm) của :math:`B` là giá trị

.. math:: \lVert B \rVert_{GS} = \max_{\tilde{b}_i \in \tilde{B}} \lVert \tilde{b}_i \rVert

LDL:math:`^*` decomposition: LDL:math:`^*` decomposition viết mỗi ma trận Gram full-rank thành tích LDL:math:`^*` với:

1. :math:`L \in \mathcal{Q}^{n \times n}` là ma trận tam giác dưới với các phần tử :math:`1` trên đường chéo chính.

2. :math:`D \in \mathcal{Q}^{n \times n}` là ma trận chéo.

Nếu tồn tại GSO duy nhất :math:`B = L \cdot \tilde{B}` và với ma trận Gram :math:`G` full-rank thì tồn tại LDL:math:`^*` decomp duy nhất :math:`G = LDL^*`.

Nếu :math:`G = B \cdot B^*` thì :math:`G = L \cdot (\tilde{B} \tilde{B}^*) \cdot L^*` là LDL:math:`^*` decomp hợp lệ.

Khi đó, :math:`L \cdot \tilde{B}` là GSO của :math:`B` khi và chỉ khi :math:`L \cdot (\tilde{B} \cdot \tilde{B}^*) \cdot L^*` là LDL:math:`^*` decomp. của :math:`B \cdot B^*`.

Khóa và tham số
---------------

Tham số công khai
~~~~~~~~~~~~~~~~~

1. Đa thức cyclotomic :math:`\phi(x) = x^n + 1` với :math:`n = 2^k`.
2. Modulus là :math:`q \in \mathbb{N}^*` là số nguyên tố, :math:`\phi(x) \bmod q` sẽ split (phân rã) trên :math:`\mathbb{Z}_q[x]`.
3. Bound (chặn) :math:`\lfloor \beta^2 \rfloor > 0`.
4. Độ lệch chuẩn :math:`\sigma` và :math:`\sigma_{\text{min}} < \sigma_{\text{max}}`.
5. Chữ ký với độ dài (theo byte) là :math:`\mathtt{sbytelen}`.

Khóa bí mật
~~~~~~~~~~~

Private key gồm :math:`4` đa thức :math:`f`, :math:`g`, :math:`F`, :math:`G` thuộc :math:`\mathbb{Z}[x] / \phi(x)` với hệ số ngắn, thỏa phương trình

.. math:: f \cdot G - g \cdot F = q \bmod{\phi(x)}.

Đa thức :math:`f` cũng phải khả nghịch trong :math:`\mathbb{Z}_q[x] / \phi(x)`.

Cho trước :math:`f` và :math:`g`, ta có thể tính được :math:`F` và :math:`G` nhưng sẽ rất tốn sức. Do đó ta cần lưu thêm :math:`F` và từ :math:`f`, :math:`g` và :math:`F` ta sẽ tính lại :math:`G`.

FFT representation (biểu diễn FFT) của :math:`f`, :math:`g`, :math:`F` và :math:`G` là dạng ma trận

.. math:: 
    
    \hat{B} = \begin{pmatrix}
        FFT(g) & -FFT(f) \\ FFT(G) & -FFT(F)
    \end{pmatrix}.

Falcon trees. Falcon trees là cây nhị phân được định nghĩa đệ quy như sau:

1. Falcon tree với độ cao :math:`0` gồm một nút đơn với giá trị là :math:`\sigma > 0`.
2. Falcon tree với độ cao :math:`k` có tính chất:

* giá trị tại gốc, :math:`\mathtt{T}.\mathtt{value}`, là đa thức :math:`l \in \mathbb{Q}[x] / (x^n + 1)` với :math:`n = 2^k`;
* nút là trái và phải, :math:`\mathtt{T}.\mathtt{leftChild}` và :math:`\mathtt{T}.\mathtt{rightChild}`, là Falcon tree với độ cao :math:`k - 1`.

Nội dung của Falcon tree :math:`\mathtt{T}` được tính từ các thành phần :math:`f`, :math:`g`, :math:`F`, :math:`G` của private key và được mô tả bởi thuật toán ở sau.

Khóa công khai
~~~~~~~~~~~~~~

Falcon public key :math:`pk` tương ứng với private key :math:`sk = (f, g, F, G)` là đa thức :math:`h \in \mathbb{Z}_q[x] / \phi(x)` thỏa

.. math:: h = g f^{-1} \pmod{\phi(x), q}.

Sinh khóa
---------

Đặt :math:`R = \mathbb{Z}[x]/(x^n+1)` và
:math:`R_q = \mathbb{Z}_q[x]/(x^n+1)`. Thuật toán sinh khóa thực hiện:

1. Lấy mẫu hai đa thức ngắn :math:`f,g \in R` theo phân phối quy định.
2. Kiểm tra :math:`f` khả nghịch trong :math:`R_q` và chuẩn của
   :math:`(f,g)` nằm dưới ngưỡng cho phép; nếu không thì lấy mẫu lại.
3. Giải phương trình NTRU

   .. math::

      fG-gF=q

   để tìm hai đa thức ngắn :math:`F,G \in R`. Nếu không tìm được nghiệm
   đủ ngắn thì quay lại bước 1.
4. Tính :math:`h = g/f \bmod q`.
5. Từ cơ sở bí mật

   .. math::

      B = \begin{pmatrix} g & -f \\ G & -F \end{pmatrix}

   xây dựng biểu diễn FFT, ma trận Gram và cây Falcon dùng cho bộ lấy mẫu.
6. Trả về :math:`sk=(f,g,F,G)` và :math:`pk=h`.

Định thức của :math:`B` bằng :math:`q`, nên các hàng của nó sinh NTRU
lattice

.. math::

   \Lambda_h^q = \{(u,v) \in R^2 : u+vh=0 \pmod q\}.

Tạo chữ ký
----------

Với thông điệp :math:`M`, khóa bí mật và nonce ngẫu nhiên :math:`r`, quá
trình ký gồm các bước:

1. Ánh xạ :math:`(r,M)` thành đa thức
   :math:`c=\mathsf{HashToPoint}(r\mathbin\Vert M) \in R_q`.
2. Xem :math:`\bm{t}=(c,0)` là mục tiêu. Dùng trapdoor :math:`B` và cây
   Falcon để lấy mẫu một điểm :math:`\bm{v}\in\Lambda_h^q` gần
   :math:`\bm{t}` theo phân phối Gaussian rời rạc.
3. Đặt :math:`\bm{s}=\bm{t}-\bm{v}=(s_1,s_2)`. Khi đó

   .. math::

      s_1+s_2h=c \pmod q.

4. Nếu :math:`\lVert(s_1,s_2)\rVert^2` vượt quá
   :math:`\lfloor\beta^2\rfloor`, hoặc :math:`s_2` không thể mã hóa trong
   giới hạn kích thước chữ ký, thì lấy nonce/mẫu mới.
5. Trả về chữ ký :math:`\sigma=(r,s_2)`. Thành phần :math:`s_1` không cần
   gửi vì verifier có thể khôi phục từ khóa công khai.

Việc lấy mẫu phải tuân đúng phân phối Gaussian và được triển khai chống
rò rỉ kênh kề. Thay bộ lấy mẫu bằng thao tác làm tròn gần đúng có thể làm
lộ thông tin về cơ sở bí mật qua nhiều chữ ký.

Kiểm tra chữ ký
---------------

Verifier nhận :math:`M`, :math:`\sigma=(r,s_2)` và :math:`h`:

1. Giải mã :math:`s_2`; từ chối nếu biểu diễn không hợp lệ.
2. Tính :math:`c=\mathsf{HashToPoint}(r\mathbin\Vert M)`.
3. Khôi phục

   .. math::

      s_1=c-s_2h \pmod q,

   với các hệ số được đưa về đại diện cân bằng quanh :math:`0`.
4. Chấp nhận khi và chỉ khi

   .. math::

      \lVert(s_1,s_2)\rVert^2 \leqslant \lfloor\beta^2\rfloor.

Tính đúng đắn
-------------

Trong quá trình ký, :math:`\bm{v}=\bm{t}-\bm{s}` thuộc
:math:`\Lambda_h^q`, vì vậy

.. math::

   (c-s_1)-s_2h=0 \pmod q.

Suy ra :math:`s_1+s_2h=c \pmod q`, đúng bằng quan hệ verifier dùng để
khôi phục :math:`s_1`. Bước rejection sampling của signer đồng thời bảo
đảm điều kiện chuẩn mà verifier kiểm tra.

Cơ sở an toàn và đặc điểm
-------------------------

Khả năng giả mạo được liên hệ với việc tìm nghiệm ngắn cho quan hệ
:math:`s_1+s_2h=c \pmod q`, tức một biến thể SIS trên NTRU lattice.
Cơ sở ngắn :math:`B` là trapdoor cho phép signer lấy mẫu hiệu quả, trong
khi khóa công khai :math:`h` chỉ mô tả lattice mà không công bố cơ sở
ngắn đó.

Falcon có chữ ký và khóa công khai gọn, phép ký/kiểm tra nhanh nhờ FFT,
nhưng việc triển khai khó hơn nhiều lược đồ lattice khác: số thực dấu
phẩy động, Gaussian sampling, kiểm tra chuẩn và mã hóa phải được thực
hiện chính xác và có khả năng chống side channel. Hai bộ tham số dùng
trong đặc tả Falcon là Falcon-512 (:math:`n=512`) và Falcon-1024
(:math:`n=1024`).

Tài liệu tham khảo
------------------

Phần mô tả thuật toán tuân theo `Falcon Specification v1.2
<https://falcon-sign.info/falcon.pdf>`_.
