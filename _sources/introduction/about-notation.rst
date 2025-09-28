======================================
Kí hiệu và công thức toán trong mật mã
======================================

Khi tham khảo các tài liệu về mật mã thì mình gặp chút khó 
khăn vì mỗi tác giả kí hiệu mỗi kiểu cho cùng khái niệm toán 
học. Hơn nữa, trong cộng đồng toxic CH mình cũng thấy được 
nhiều người kí hiệu mà không hiểu rõ nó là gì. Trong bài viết 
này mình sẽ nói về các kí hiệu toán học mà mình sẽ dùng trong 
các bài viết của mình, cũng như quan điểm về chúng.

----------------------------------------
Có nên sử dụng kí hiệu mọi lúc, mọi nơi?
----------------------------------------

Trong toán học, kí hiệu được sử dụng nhằm mô tả những định 
nghĩa, định lí. Thông qua kí hiệu, các nhà toán học của nhiều 
quốc gia khác nhau có thể "thấu hiểu" nhau bất chấp rào cản 
ngôn ngữ. Tuy nhiên trong các bài viết của mình thì mình sẽ 
không sử dụng kí hiệu mọi lúc, mọi nơi.

Ví dụ, định nghĩa giới hạn hàm số theo kiểu 
:math:`\delta-\varepsilon` được ghi như sau

.. math:: \forall \varepsilon > 0, \exists \delta > 0: \forall \left|x - x_0\right| < \delta \Rightarrow \left|f(x) - L\right| < \varepsilon.

Đây là định nghĩa giới hạn hữu hạn của hàm số, nói rằng hàm 
số :math:`f(x)` tiến tới :math:`L` khi :math:`x` tiến tới 
:math:`x_0`. Mình thấy việc kí hiệu đôi khi khiến mình bị 
rối khi theo dõi các phần (có lẽ do mình không giỏi toán). =(((

Do đó định nghĩa giới hạn hàm số ở trên được viết lại theo 
tiếng Việt như sau:

- với mọi :math:`\varepsilon > 0`
- tồn tại :math:`\delta > 0` sao cho:

  * với mọi :math:`x` mà :math:`\left|x - x_0\right| < \delta`
  * ta sẽ có :math:`\left|f(x) - L\right| < \varepsilon`.

Khi này, việc chứng minh giới hạn hàm số theo định nghĩa sẽ 
"thông" hơn. Mình sẽ theo từng câu chữ ở trên:

- lấy :math:`\varepsilon > 0` bất kì (tương ứng lượng từ *với mọi*)
- tìm :math:`\delta > 0` (chứng minh tồn tại, thường sẽ liên 
  hệ với :math:`\varepsilon` ở trên) thỏa mãn:

  * nếu với mọi :math:`x` thỏa mãn :math:`\left|x - x_0\right| < \delta`
  * mình sẽ suy ra được :math:`\left|f(x) - L\right| < \varepsilon`.

Kết luận: việc viết ra đầy đủ giúp mình biết được các bước 
cần thực hiện theo định nghĩa, định lí nào đó.

.. _Zn-or-Z-nZ:

:math:`\mathbb{Z}_n` hay :math:`\mathbb{Z} / n \mathbb{Z}`?
-----------------------------------------------------------

Thông thường, việc kí hiệu :math:`\mathbb{Z}_n` được hiểu 
là tập hợp các số dư có thể có khi chia một số nguyên bất 
kì cho :math:`n`, nói cách khác

.. math:: \mathbb{Z}_n = \{ 0, 1, 2, \ldots, n - 1 \}.

Đối với :math:`\mathbb{Z} / n \mathbb{Z}`, chúng ta có thể 
dùng hai cách lí giải: bằng lý thuyết nhóm và bằng quan hệ 
tương đương (quan hệ hai ngôi).

Nếu sử dụng lý thuyết nhóm, nếu ta nhân mỗi phần tử trong 
:math:`\mathbb{Z}` với :math:`n` thì

.. math:: n\mathbb{Z} = \{ \ldots, -2n, -n, 0, n, 2n, \ldots \}.

Ta lần lượt cộng :math:`i` cho các phần tử của 
:math:`n\mathbb{Z}` với :math:`i = 0, 1, \ldots, n - 1`. 
Khi đó ta sẽ có

.. math:: 

  \begin{array}{ccc}
    0 + n\mathbb{Z} & = & \{ \ldots, -2n, -n, {\color{red}0}, n, 2n, \ldots, \}, \\
    1 + n\mathbb{Z} & = & \{ \ldots, -2n + 1, -n + 1, {\color{red}1}, n + 1, 2n + 1 \ldots \}, \\
    \vdots & \\
    (n - 1) + n\mathbb{Z} & = & \{ \ldots, -n + 1, -1, {\color{red}n - 1}, 2n-1, 3n-1, \ldots \}.
  \end{array}

Các tập :math:`0 + n\mathbb{Z}`, :math:`1 + n\mathbb{Z}`, 
..., :math:`(n - 1) + n\mathbb{Z}` rời nhau nên chúng ta có 
đúng :math:`n` coset. Hơn nữa phép cộng số nguyên có tính 
giao hoán nên :math:`i + n\mathbb{Z} = n\mathbb{Z} + i`. 
Như vậy tập :math:`n\mathbb{Z}` là **nhóm con chuẩn tắc** 
(hay **normal subgroup**) của :math:`\mathbb{Z}`. Khi đó 
:math:`\mathbb{Z} / n\mathbb{Z}` được gọi là **nhóm thương** 
(hay **quotient group**) và kí hiệu

.. math:: \mathbb{Z} / n\mathbb{Z} = \{ 0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n-1) + n\mathbb{Z} \}.

Đối với cách giải thích sử dụng quan hệ tương đương, 
chúng ta kí hiệu

.. math:: \overline{x} = \{ y \in \mathbb{Z} : x \equiv y \bmod n \}.

Nói cách khác, :math:`x` và :math:`y` có quan hệ nếu 
:math:`x` và :math:`y` có cùng số dư khi chia cho 
:math:`n`.

Dễ thấy

.. math:: 
    
  \begin{array}{ccc}
    \overline{0} & = & \{ \ldots, -2n, -n, {\color{red}0}, n, 2n, \ldots, \}, \\
    \overline{1} & = & \{ \ldots, -2n + 1, -n + 1, {\color{red}1}, n + 1, 2n + 1 \ldots \}, \\
    \vdots & \\
    \overline{n-1} & = & \{ \ldots, -n + 1, -1, {\color{red}n - 1}, 2n-1, 3n-1, \ldots \}.
  \end{array}

Đây là ví dụ hoặc bài tập phổ biến trong các bài giảng 
về quan hệ tương đương. Ở đây, quan hệ tương đương chia 
(phân hoạch) tập :math:`\mathbb{Z}` thành :math:`n` tập 
con không giao nhau, gọi là các **lớp tương đương**. 
Chúng ta lấy số nguyên không âm nhỏ nhất của mỗi lớp 
làm đại diện cho lớp đó, tức là :math:`0`, :math:`1`, 
..., :math:`n-1` như trên.

Khi đó, **tập thương** là tập hợp các lớp tương đương

.. math:: \mathbb{Z} / n\mathbb{Z} = \{ \overline{0}, \overline{1}, \ldots, \overline{n-1} \}.

Như vậy, dù giải thích theo lý thuyết nhóm hay quan hệ 
tương đương đều chỉ ra rằng :math:`n\mathbb{Z}` chia tập 
:math:`\mathbb{Z}` thành :math:`n` tập con không giao 
nhau, và chúng ta lấy số nguyên không âm nhỏ nhất của mỗi 
tập làm đại diện cho tập đó. Lúc này, các phép cộng, trừ 
và nhân (không có chia) trên tập :math:`\mathbb{Z} / n\mathbb{Z}` 
sẽ cho các phần tử vẫn thuộc :math:`\mathbb{Z} / n\mathbb{Z}`.

Tuy nhiên phép tính trên :math:`\mathbb{Z}_n` phải chỉ 
định phép modulo :math:`n`, chẳng hạn là :math:`a + b \bmod n` 
với :math:`a, b \in \mathbb{Z}_n`.

Lý do hai tập này có thể dùng như nhau là tính đẳng cấu, 
kí hiệu là :math:`\mathbb{Z}_n \cong \mathbb{Z} / n\mathbb{Z}`. 
Trong nhiều tài liệu, tập :math:`\mathbb{Z}_n` được định nghĩa là

.. math:: \mathbb{Z}_n = \{ \overline{0}, \overline{1}, \ldots, \overline{n-1} \}

chỉ vành các số dư (resuide ring, кольцо вычётов). Ý 
nghĩa vẫn giống :math:`\mathbb{Z} / n\mathbb{Z}`, ta 
xét tất cả phần tử của :math:`\mathbb{Z}` dưới :math:`n` 
lớp rời nhau. Do đó mình nghĩ rằng cần hiểu rõ ý nghĩa 
của :math:`\mathbb{Z} / n\mathbb{Z}` trước khi phán 
:math:`\mathbb{Z}_n` ở bất cứ đâu.

.. _Zp-or-Fp:

:math:`\mathbb{Z}_p` hay :math:`\mathbb{F}_p`?
----------------------------------------------

Khi :math:`p` là số nguyên tố thì chúng ta có thể 
thực hiện phép chia khác :math:`0` (nhân nghịch đảo) 
trong modulo :math:`p`. Khi đó tập :math:`\mathbb{Z}_p` 
trở thành trường và chúng ta có thể dùng :math:`\mathbb{F}_p` 
để thể hiện rõ ý này (F = Field). Cách kí hiệu :math:`\mathbb{Z}_p` 
không sai nhưng mình nghĩ sẽ khó theo dõi xem đâu là trường, 
đâu không phải là trường (mới chỉ là vành).

.. _GF-28-or-GF-258:

:math:`\mathrm{GF}(2^8)` hay :math:`\mathrm{GF}(256)`?
------------------------------------------------------

Rõ ràng :math:`2^8 = 256`, và hai cách kí hiệu là một. 
Tuy nhiên mình chọn viết cách đầu.

Đầu tiên, việc kí hiệu :math:`2^8` sẽ dễ liên hệ tới 
phần tử của trường, tức là các đa thức bậc :math:`8` và 
có dạng

.. math:: a_0 + a_1 x + \cdots + a_7 x^7

với :math:`a_i \in \mathrm{GF}(2)`.

Nếu viết :math:`\mathrm{GF}(256)`, chúng ta phải nhớ 
xem :math:`256` phân tích thành thừa số nguyên tố ra 
sao. Điều này đơn giản nếu chúng ta làm việc với các 
số quen thuộc như :math:`2^8 = 256`. Tuy nhiên nếu 
chúng ta nghiên cứu trên số nguyên tố khác, chẳng hạn

.. math:: \mathrm{GF}(6561), \mathrm{GF}(625), \ldots

thì không phải ai cũng nhớ. Chúng ta phải mất công phân 
tích số :math:`6561` thành :math:`3^8`, hay :math:`625` 
thành :math:`5^3`, rồi mới làm tiếp.

Một ví dụ khác là

.. math:: \mathrm{GF}(340282366920938463463374607431768211456),

thì cũng là :math:`\mathrm{GF}(2^{128})` thôi, được dùng 
khi tính message authentication code (MAC) của thuật toán 
mã hóa đối xứng. Ở đây chắc chắn mình sẽ chọn viết 
:math:`\mathrm{GF}(2^{128})` thay vì con số dài ngoằn kia.

Như vậy, việc viết :math:`\mathrm{GF}(256)` không sai, 
nhưng mình nghĩ viết :math:`\mathrm{GF}(2^8)` có nhiều 
ưu điểm hơn và sẽ giúp tạo thói quen tốt.

.. _F-28-or-F2-8:

:math:`\mathbb{F}_{2^8}` hay :math:`\mathbb{F}_2^8`?
----------------------------------------------------

Hai tập hợp này có cùng số phần tử là :math:`2^8 = 256`. 
Tuy nhiên ý nghĩa của chúng khác nhau hoàn toàn.

Đầu tiên, :math:`\mathbb{F}_{2^8}` chỉ trường các đa thức 

.. math:: a_0 + a_1 x + \cdots + a_7 x^7,

với :math:`a_i \in \mathbb{F}_2`. Các phép tính cộng, trừ, 
nhân, chia hai đa thức được thực hiện trong modulo :math:`m(x)` - 
là một đa thức tối giản bậc :math:`8` với hệ số trong :math:`\mathbb{F}_2`.

Trong khi đó, :math:`\mathbb{F}_2^8` chỉ các vector

.. math:: \bm{a} = (a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7) \in \mathbb{F}_2^8

với :math:`a_i \in \mathbb{F}_2`. Ta xem :math:`\mathbb{F}_2^8` 
là một không gian vector. Khi đó chúng ta chỉ có hai phép tính 
trên tập :math:`\mathbb{F}_2^8` là cộng hai vector và nhân 
vector với một phần tử thuộc :math:`\mathbb{F}_2`. Nếu các 
bạn mở rộng lên không gian Euclid hay gì đó thì vẫn không 
giống :math:`\mathbb{F}_{2^8}`.

.. _GF-pn-or-F-pn:

:math:`\mathrm{GF}(p^n)` hay :math:`\mathbb{F}_{p^n}`?
------------------------------------------------------

Hai cách kí hiệu đều có ý nghĩa như nhau.

Khi :math:`n = 1` thì mình thấy dùng :math:`\mathrm{GF}(p)` 
hay :math:`\mathbb{F}_p` đều được.

Khi :math:`n \geqslant 2` thì mỗi cách kí hiệu đều có 
ưu điểm và nhược điểm riêng. Cả hai cách đều chỉ trường 
số với các phần tử là đa thức

.. math:: a_0 + a_1 x + a_2 x^2 + \cdots + a_{n-1} x^{n-1},

với :math:`a_i \in \mathbb{F}_p`, hay cũng có thể 
viết :math:`a_i \in \mathrm{GF}(p)`.

Việc viết :math:`\mathbb{F}_{p^n}` có nhược điểm là 
làm đại lượng :math:`p^n` hơi nhỏ, khó nhìn nên sử 
dụng :math:`\mathrm{GF}(p^n)` sẽ tốt hơn. Tuy nhiên 
một ưu điểm của :math:`\mathbb{F}_{p^n}` là có thể 
chỉ tập các vector mà mỗi vị trí là một phần tử 
trong :math:`\mathbb{F}_{p^n}`. Ví dụ

.. math:: \bm{f} = (f_1(x), f_2(x), \ldots, f_m(x)) \in \mathbb{F}_{p^n}^m

với :math:`f_i(x)` là các phần tử thuộc :math:`\mathbb{F}_{p^n}`. 
Nếu sử dụng :math:`\mathrm{GF}(p^n)` thì phải viết 
:math:`\mathrm{GF}(p^n)^m` khá rối. Khi chúng ta xét 
tới ma trận có phần tử trong :math:`\mathbb{F}_{p^n}` 
thì còn rối hơn nữa. Thay vào đó ta có thể viết

.. math:: 
    
    \bm{A} = \begin{pmatrix}
        a_{1, 1}(x) & a_{1, 2}(x) & \cdots & a_{1, d}(x) \\
        a_{2, 1}(x) & a_{2, 2}(x) & \cdots & a_{2, d}(x) \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m, 1}(x) & a_{m, 2}(x) & \cdots & a_{m, d}(x)
    \end{pmatrix} \in \mathbb{F}_{p^n}^{m \times d}

với :math:`a_{i, j}(x)` là phần tử thuộc 
:math:`\mathbb{F}_{p^n}`.

Từ các lý do trên có thể thấy :math:`\mathbb{F}_{p^n}` 
đa dụng hơn nên mình sẽ dùng cách kí hiệu này.
