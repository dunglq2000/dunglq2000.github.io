===============
Plonk Protocol
===============

[TODO] Viết lại.

----------------------------
Elliptic curve và pairing
----------------------------

^^^^^^^^^^^^^^^^
Elliptic curve
^^^^^^^^^^^^^^^^

Đường cong elliptic trên trường :math:`\mathbb{F}` có dạng
:math:`y^2 = x^3 + ax + b` với :math:`x`, :math:`y`, :math:`a`, 
:math:`b` thuộc :math:`\mathbb{F}` và :math:`a, b` là các phần tử cho trước.

Khi đó đường cong elliptic là tập hợp các điểm :math:`(x, y)`
thỏa mãn phương trình trên và điểm vô cực :math:`\mathcal{O}`.

Để lấy ví dụ, xét :math:`\mathbb{F}_{101}` là trường modulo
:math:`101` và đường cong elliptic với phương trình
:math:`y^2 = x^3 + 3 \pmod{101}`.

^^^^^^^^^^^^^^^^
Pairing
^^^^^^^^^^^^^^^^

Gọi :math:`\mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_t` là các nhóm
có cùng order bằng :math:`r` và :math:`e` là một pairing. Khi
đó :math:`e` là ánh xạ sao cho

.. math:: \mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_t: \quad e(g_1, g_2) = g_t.

^^^^^^^^^^^^^^^^
Embedding degree
^^^^^^^^^^^^^^^^

Order của đường cong elliptic trên là :math:`102 = 2 \cdot 3 \cdot 17`.
Như vậy tồn tại các điểm trên đường cong có order là :math:`17`. Tuy
nhiên, chung ta cần nhiều điểm khác cũng có order là :math:`17` nhưng
không nằm trên đường cong :math:`\mathbb{F}_{101}`. Lúc này chúng
ta sẽ mở rộng trường lên :math:`\mathbb{F}_{101^k}`.

Bậc thấp nhất của mở rộng trường (với characteristic :math:`p`) chứa
tất cả điểm với order :math:`r` được gọi là **embedding degree**. Nói
đơn giản, embedding degree là số :math:`k` nhỏ nhất mà :math:`r \mid (p^k - 1)`.

Trong ví dụ này thì :math:`r = 17` là order của điểm và :math:`k = 2`.

Khi đó trường mở rộng :math:`\mathbb{F}_{101^2}` với đa thức tối
giản :math:`x^2 + 2` cho đường cong với các điểm order :math:`17`.

Mỗi phần tử trong :math:`\mathbb{F}_{101^2}` có dạng :math:`a + bx`
với :math:`a, b \in \mathbb{F}_{101}`.

------------
Mạch Plonk
------------

^^^^^^^^^^^^^^^^
Trusted setup
^^^^^^^^^^^^^^^^

Chúng ta cần một trusted setup gọi là **structured reference string**
(SRS, chuỗi liên kết cấu trúc).

SRS là một danh sách các điểm trên đường cong elliptic được tính toán
từ một số bí mật sinh ngẫu nhiên :math:`s`. Theo paper PLONK thì một
mạch :math:`n` cổng sẽ cần :math:`n+5` điểm sau:

.. math:: \mathrm{SRS}: \quad & 1 \cdot G_1, s \cdot G_1, \cdots, s^{n+2} \cdot G_1, \\ & 1 \cdot G_2, s \cdot G_2.

Trong ví dụ này, :math:`s` giúp sinh ra các điểm trong subgroup với
generator là :math:`G_1`. Do :math:`G_1` có order là :math:`17`,
:math:`s` không được vượt quá :math:`17`.

Chọn :math:`G_1 = (1, 2)` và :math:`G_2 = (36, 31x)` là hai generator
cho hai subgroup đều có order là :math:`17`.

Xét :math:`s = 2` (cho dễ tính) và :math:`n = 4` (có :math:`4` cổng).
Khi đó :math:`1 \cdot G_1, s \cdot G_1, \cdots, s^{n+2} \cdot G_1` là
các điểm sau:

.. math:: 
    
    \begin{array}{|c|c|c|c|}
        1 \cdot G_1 = (1, 2) & s \cdot G_1 = (68, 74) & s^2 \cdot G_1 = (65, 98) & s^3 \cdot G_1 = (18, 49) \\
        s^4 \cdot G_1 = (1, 99) & s^5 \cdot G_1 = (68, 27) & s^6 \cdot G_1 = (65, 3) &
    \end{array}

Tương tự, :math:`1 \cdot G_2` và :math:`s \cdot G_2` là các
điểm :math:`(36, 31x)` và :math:`(90, 82x)`.

Như vậy,

.. math:: \mathrm{SRS}: \quad & (1, 2), (68, 74), (65, 98), (18, 49), (1, 99), (68, 27), (65, 3) \\ & (36, 31x), (90, 82x).

^^^^^^^^^^^^^^^^
Mạch PLONK
^^^^^^^^^^^^^^^^

Plonk circuit là mạch được biểu diễn ở dạng đa thức (gồm phép cộng
và nhân). Trong đó mỗi cổng, hay constrain, thực hiện một thao
tác (cộng hoặc nhân).

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ví dụ với định lý Pythagoras
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Giả sử chúng ta có bộ ba :math:`(3, 4, 5)` và chúng ta muốn kiểm tra
xem chúng có thỏa mãn phương trình Pythagoras :math:`a^2 + b^2 = c^2`
hay không.

Giả sử bộ ba :math:`(3, 4, 5)` sẽ đi vào ba đầu là :math:`x_1, x_3, x_5`.
Khi đó mạch tính

.. math:: 

    x_1 \cdot x_1 = x_2 \\
    x_3 \cdot x_3 = x_4 \\
    x_5 \cdot x_5 = x_6 \\
    x_2 + x_4 = x_6

Phương trình cuối cho kết quả :math:`x_1^2 + x_3^2 = x_5^2` là
điều kiện thỏa mãn phương trình Pythagoras. Mỗi :math:`x_i` được gọi
là "wire" (dây). Mạch này đi qua ba cổng nhân và một cổng cộng. Ta có
thể viết tất cả :math:`x_i` thành vector :math:`\mathbf{x} = (x_1, x_2, x_3, x_4, x_5, x_6)`.
Đối với ví dụ bộ ba :math:`(3, 4, 5)` thì

.. math:: \mathbf{x} = (3, 9, 4, 16, 5, 25).

Tương tự, đối với bộ ba :math:`(5, 12, 13)` thì 

.. math:: \mathbf{x} = (5, 25, 12, 144, 13, 169).

Mỗi cổng plonk sẽ gồm hai dây input trái và phải, và một dây
output. Ta gọi dây input trái và phải lần lượt là :math:`a` và
:math:`b`, còn dây output là :math:`c`.

Cổng plonk phức tạp hơn cổng cộng hoặc nhân để kiểm tra bộ
ba Pythagoras ở trên. Cổng plonk đầy đủ có dạng

.. math:: (q_L) \cdot a + (q_R) \cdot b + (q_O) \cdot c + (q_M) \cdot ab + q_C = 0.

Trong đó :math:`a, b` là hai dây input trái và phải, :math:`c`
là dây output, còn lại là các hệ số cho trước.

**Ví dụ**. Đối với đẳng thức :math:`a + b = c` thì ta
cho :math:`q_L = q_R = 1`, :math:`q_O = -1` và :math:`q_M = q_C = 0`.

Mạch kiểm tra bộ ba Pythagoras bên trên có thể được viết
lại dưới dạng mạch với các cổng plonk như sau

.. math:: 
    
    \begin{array}{ccccccccccc}
        0 \cdot a_1 & + & 0 \cdot b_1 & + & (-1) \cdot c_1 & + & 1 \cdot a_1 b_1 & + & 0 & = & 0 \\
        0 \cdot a_2 & + & 0 \cdot b_2 & + & (-1) \cdot c_2 & + & 1 \cdot a_2 b_2 & + & 0 & = & 0 \\
        0 \cdot a_3 & + & 0 \cdot b_3 & + & (-1) \cdot c_3 & + & 1 \cdot a_3 b_3 & + & 0 & = & 0 \\
        1 \cdot a_4 & + & 1 \cdot b_4 & + & (-1) \cdot c_4 & + & 0 \cdot a_3 b_3 & + & 0 & = & 0
    \end{array}

Bốn cổng plonk này tương đương bốn cổng kiểm tra bên trên.
Tương tự bên trên, nếu gọi :math:`\mathbf{a}` là vector các dây
input trái, :math:`\mathbf{b}` là vector các dây input phải và
:math:`\mathbf{c}` là các dây output thì

.. math:: \mathbf{a} = (3, 4, 5, 9), \, \mathbf{b} = (3, 4, 5, 16), \, \mathbf{c} = (9, 16, 25, 25).

Ta cũng viết hệ số cổng plonk dưới dạng vector, khi đó

.. math:: 

    \mathbf{q_L} & = (0, 0, 0, 1), \\
    \mathbf{q_R} & = (0, 0, 0, 1), \\
    \mathbf{q_O} & = (-1, -1, -1, -1), \\
    \mathbf{q_M} & = (1, 1, 1, 0), \\
    \mathbf{q_C} & = (0, 0, 0, 0)

Lúc này, các vector :math:`\mathbf{q}` được gọi là **selector** và sẽ giúp xây
dựng nên cấu trúc của mạch. Các vector :math:`\mathbf{a}, \mathbf{b}, \mathbf{c}`
thể hiện các biến của mạch và là private input của Prover (bên chứng minh ZKP).

---------
Proof
---------

^^^^^^^^^^^^^^^^
Roots of unity
^^^^^^^^^^^^^^^^

Trong trường :math:`\mathbb{F}` có phần tử đơn vị là :math:`1`.
Nghiệm bậc :math:`n` của :math:`1` là các nghiệm :math:`x` thỏa
mãn phương trình :math:`x^n = 1`.

Ở ví dụ trên, mỗi subgroup đều có order là :math:`17`.
Bây giờ các tính toán của chúng ta sẽ nằm trong :math:`\mathbb{F}_{17}`.

Nhắc lại, các vector :math:`\mathbf{a}, \mathbf{b}, \mathbf{c}` cũng
như các vector hệ số :math:`\mathbf{q_L}, \mathbf{q_R}, \mathbf{q_O}, \mathbf{q_M}, \mathbf{q_C}`
đều có bốn phần tử. Chúng ta có cách xây dựng đa thức :math:`f(x)` từ các
cặp :math:`(x_i, f(x_i))` là **đa thức nội suy**.

Khi đó, mỗi vector ở trên sẽ tương ứng :math:`f(x_i)` với
:math:`1 \leqslant i \leqslant 4`. Đa thức sinh ra là đa thức bậc :math:`3`.

Ứng với mỗi vector :math:`\mathbf{a}, \mathbf{b}, \mathbf{c}` ta xây
dựng một đa thức bậc :math:`3`. Do có :math:`3 \cdot 4 = 12` giá
trị :math:`x_i` nên ta cần một "cơ chế" để tách trường :math:`\mathbb{F}_{17}`
thành :math:`3` tập rời nhau, mỗi tập :math:`4` phần tử.

Đầu tiên là cần một tập con của :math:`\mathbb{F}_{17}` có :math:`4` phần
tử. Tập con này là tập nghiệm của :math:`x^4 = 1 \pmod{17}`. Phương trình
này có nghiệm và may thay là có đủ :math:`4` nghiệm. Gọi :math:`H` là tập
các nghiệm của phương trình :math:`x^4 = 1 \pmod{17}` thì
:math:`H = \{ 1, 4, 16, 13 \}`.

Ta cần tìm thêm hai tập con khác của :math:`\mathbb{F}_{17}`, cũng
chứa :math:`4` phần tử và không giao nhau với :math:`H`. Chúng ta sẽ
dùng coset vì hai coset bất kì của nhóm hoặc là không giao nhau, hoặc
là trùng nhau.

Chọn :math:`k_1 = 2` và :math:`k_2 = 3` thì ta có các coset

.. math:: 1 H = \{ 1, 4, 16, 13 \}, \, k_1 H = \{ 2, 8, 15, 9 \}, \, k_2 H = \{ 3, 12, 14, 5 \}.

Với vector :math:`\mathbf{a} = \{ a_1, a_2, a_3, a_4 \}`, ta mong 
muốn :math:`f_{\mathbf{a}}(h_i) = a_i` với :math:`h_i \in H`, nghĩa 
là :math:`f_{\mathbf{a}}(1) = 3`, :math:`f_{\mathbf{a}}(4) = 4`, 
:math:`f_{\mathbf{a}}(16) = 5` và :math:`f_{\mathbf{a}}(13) = 9`. 
Sử dụng đa thức nội suy Lagrange có thể tìm được 
hàm :math:`f_{\mathbf{a}}(x) = 1 + 13x + 3x^2 + 3x^3`.

Tương tự ta cũng tìm được đa thức nội suy cho các vector
còn lại (tất cả đều dùng :math:`H`).

.. math:: 

    & f_{\mathbf{a}}(x) = 1 + 13x + 3x^2 + 3x^3 \\
    & f_{\mathbf{b}}(x) = 7 + 3x + 14x^2 + 13x^2 \\
    & f_{\mathbf{c}}(x) = 6 + 5x + 11x^2 + 4x^3 \\
    & f_{\mathbf{q_L}}(x) = 13 + x + 4x^2 + 16x^3 \\
    & f_{\mathbf{q_R}}(x) = 13 + x + 4x^2 + 16x^3 \\
    & f_{\mathbf{q_O}}(x) = 16 \\
    & f_{\mathbf{q_M}}(x) = 5 + 16x + 13x^3 + x^3 \\
    & f_{\mathbf{q_C}}(x) = 0 \\

Một vấn đề xảy ra là, bốn cổng plonk ở trên là rời nhau
và không liên quan gì nhau. Do đó chúng ta cần một phương
án để "nối" output từ cổng này thành input của cổng kia. 

Để làm việc này, ta đánh nhãn vector :math:`\mathbf{a}` bởi :math:`H`, 
vector :math:`\mathbf{b}` bởi :math:`k_1 H` và vector :math:`\mathbf{c}` 
bởi :math:`k_2 H`. Cụ thể ta có ánh xạ

.. math:: 
    
    \begin{array}{c||c}
        a_1 = b_1 & 1 \to 2 \\
        a_2 = b_2 & 4 \to 8 \\
        a_3 = b_3 & 16 \to 15 \\
        a_4 = c_1 & 13 \to 3 \\
        b_1 = a_1 & 2 \to 1 \\
        b_2 = a_2 & 8 \to 4 \\
        b_3 = a_3 & 15 \to 16 \\
        b_4 = c_2 & 9 \to 12 \\
        c_1 = a_4 & 3 \to 13 \\
        c_2 = b_4 & 12 \to 8 \\
        c_3 = c_4 & 14 \to 5 \\
        c_4 = c_3 & 5 \to 14
    \end{array}

Gọi :math:`\sigma_1, \sigma_2, \sigma_3` lần lượt là
output khi ánh xạ tác động lên :math:`H, k_1 H, k_2 H`.
Theo bảng trên thì :math:`\sigma_1 = (2, 8, 15, 3), \sigma_2 = (1, 4, 16, 12), \sigma_3 = (13, 8, 5, 14)`.

Mỗi tác động như vậy thực chất tương ứng với một
đa thức bậc :math:`3`. 

Gọi :math:`S_{\sigma_1}` là đa thức từ :math:`H`
tới :math:`\sigma_1`. Sử dụng nội suy Lagrange ta
tính được :math:`S_{\sigma_1} = 7 + 13 x + 10 x^2 + 6x^3`.

Tương tự, gọi :math:`S_{\sigma_2}` là đa thức
từ :math:`k_1 H` tới :math:`\sigma_2` và :math:`S_{\sigma_3}`
là đa thức từ :math:`k_2 H` tới :math:`\sigma_3`. Ta tính 
được :math:`S_{\sigma_2} = 4 + 13x^2 + x^3` 
và :math:`S_{\sigma_3} = 6 + 7x + 3x^2 + 14x^3`.

Đến đây ta có đủ thành phần để tạo proof, gồm :math:`5` vòng.

^^^^^^^^^^^^^^^^
Round 1
^^^^^^^^^^^^^^^^

Round 1 bao gồm các bước:

- tạo random các phần tử :math:`b_1, \ldots, b_6 \in \mathbb{F}_{17}`;
- tính các đa thức :math:`a(x), b(x), c(x)` theo công thức

.. math:: 

    a(x) = (b_1 x + b_2) \cdot Z_H + f_{\mathbf{a}}(x) \\
    b(x) = (b_3 x + b_4) \cdot Z_H + f_{\mathbf{b}}(x) \\
    c(x) = (b_5 x + b_6) \cdot Z_H + f_{\mathbf{c}}(x).


Output là :math:`[a(s)], [b(s)], [c(s)]`, trong đó :math:`Z_H` là đa
thức sao cho mọi phần tử của subgroup :math:`H` là nghiệm của :math:`Z_H`.
Do các phần tử trong :math:`H` là nghiệm của :math:`x^4 = 1 \pmod{17}` 
nên :math:`Z_H = x^4 - 1`.

Giả sử ta chọn (ngẫu nhiên) các phần tử 
:math:`b_1 = 7, b_2 = 4, b_3 = 11, b_4 = 12, b_5 = 16, b_6 = 2`. 
Khi đó

.. math:: 

    Z_H(x) & = x^4 - 1 \\
    a(x) & = \cdots = 14 + 6x + 3x^2 + 3x^3 + 4x^4 + 7x^5 \\
    b(x) & = \cdots = 12 + 9x + 14x^2 + 13x^3 + 12x^4 + 11x^5 \\
    c(x) & = \cdots = 4 + 6x + 11x^2 + 4x^3 + 2x^4 + 16x^5.


Tiếp theo ta tính :math:`[a(s)], [b(s)], [c(s)]` là các điểm 
trên đường cong sử dụng SRS ban đầu và hệ số của các đa 
thức :math:`a(x), b(x), c(x)`. Cụ thể prover sẽ tính

.. math:: 

    [a(s)] & = 14 \cdot (1, 2) + 6 \cdot (68, 74) + 3 \cdot (65, 98) \\ & + 3 \cdot (18, 49) + 4 \cdot (1, 99) + 7 \cdot (68, 27) = (91, 66).

Tương tự cho :math:`[b(s)]` và :math:`[c(s)]`. Như vậy ta có

.. math:: [a(s)] = (91, 66), \ [b(s)] = (26, 45), \ [c(s)] = (91, 35).

^^^^^^^^^^^^^^^^
Round 2
^^^^^^^^^^^^^^^^

Round 2 được thực hiện qua các bước:

- random các phần tử :math:`b_7, b_8, b_9 \in \mathbb{F}_{17}`;
- nhận challenge từ verifier là :math:`\beta, \gamma \in \mathbb{F}_{17}`;
- tính :math:`z(x)` theo công thức:

.. math:: z(x) = (b_7 x^2 + b_8 x + b_9) \cdot Z_H(x) + \mathrm{acc}(x).

Ở round này, chúng ta *commit* một đa thức :math:`z(x)` để 
encode cho việc copy contrains (nối các dây của cổng) bên trên. 
Đa thức :math:`\mathrm{acc}(x)` sẽ được đề cập sau.

Các giá trị challenge :math:`\beta, \gamma` phụ thuộc vào 
protocol là interactive (tương tác) hay non-interactive.

- trong protocol interactive, verifier chọn các giá trị 
  này và gửi cho prover để prover tạo ra proof;
- trong protocol non-interactive, các giá trị này sinh ra 
  từ quá trình tính toán của prover và đi qua một hàm hash mật mã.

Trong cả hai trường hợp, giá trị này là không thể đoán trước 
và cần được tính giống nhau (về hàm hash, về trường) ở cả 
hai phía. Do đó quá trình này còn được gọi là **biến đổi Fiat-Shamir** 
có thể biến interactive thành non-interactive protocol.

Trước tiên ta cần tìm hiểu cơ chế interactive, ở đó verifier 
gửi các challenge cho prover.

Giả sử :math:`\beta = 12`, :math:`\gamma = 13`.

Hàm :math:`z(x)` ở trên được xây dựng từ các **accumulator** 
vector, định nghĩa như sau:

.. math:: 

    \mathrm{acc}_0 & = 1 \\
    \mathrm{acc}_i & = \mathrm{acc}_{i-1} \cdot \left(\dfrac{(a_i + \beta \cdot w^{i-1} + \gamma) \cdot (b_i + \beta k_1 w^{i-1} + \gamma) \cdot (c_i + \beta k_2 w^{i-1} + \gamma)}{(a_i + \beta S_{\sigma_1}(w^{i-1})+\gamma) \cdot (b_i + \beta k_1 S_{\sigma_2}(w^{i-1}) + \gamma) \cdot (c_i + \beta k_2 S_{\sigma_3}(w^{i-1}) + \gamma)}\right)


Do cách định nghĩa :math:`S_{\sigma}` ở trên mà sẽ có 
những phần ở tử và mẫu giản lược nhau, và tất nhiên là 
một số thì không.

Bằng tính toán trực tiếp thu được

.. math:: \mathrm{acc}_0 = 1, \ \mathrm{acc}_1 = 3, \ \mathrm{acc}_2 = 9, \ \mathrm{acc}_3 = 4.

Khi đó đa thức :math:`\mathrm{acc}(x)` tương ứng với đa thức 
nội suy từ nguồn là subgroup :math:`H = \{ 1, 4, 16, 13 \}` 
và ảnh tương ứng là vector :math:`\mathrm{acc} = (1, 3, 9, 4)`.

Nói cách khác là :math:`\mathrm{acc}(1) = 1`, :math:`\mathrm{acc}(4) = 3`, 
:math:`\mathrm{acc}(16) = 9` và :math:`\mathrm{acc}(13) = 4`. Từ đó ta có

.. math:: \mathrm{acc}(x) = 16x + 5x^2 + 14x^3.

Thay vào công thức tính :math:`z(x)` ta có

.. math:: 

    z(x) = & (14x^2 + 11x + 7) (x^4 - 1) + 16x + 5x^2 + 14x^3 \\
        = & 10 + 5x + 8x^2 + 14x^3 + 7x^4 + 11x^5 + 14x^6.

Cuối cùng thay giá trị secret :math:`s` vào :math:`z(x)` ta có 
:math:`z(s) = z(2) = 11` và tính :math:`[z(s)] = 11 (1, 2) = (32, 59)`.

^^^^^^^^^^^^^^^^
Round 3
^^^^^^^^^^^^^^^^

Round này chứa một lượng lớn tính toán. Chúng ta sẽ tính đa 
thức :math:`t(x)` bậc :math:`3n + 5` với :math:`n` là số lượng 
cổng. Đa thức :math:`t(x)` sẽ chứa mạch và tất cả assignment cùng lúc.

Quá trình ở round 3 gồm:

- tính quotient challenge :math:`\alpha \in \mathbb{F}_{17}`;
- tính quotient polynomial :math:`t(x)`

.. math:: 

    t(x) = & \left(a(x) b(x) q_M(x) + a(x) q_L(x) + b(x) q_R(x) + c(x) q_O(x) + \mathrm{PI} (x) + q_C(x)\right) \dfrac{1}{Z_H(x)} \\
    + & \left((a(x) + \beta x  + \gamma) (b(x) + \beta k_1 x + \gamma) (c(x) + \beta k_2 x + \gamma) z(x) \right) \dfrac{\alpha}{Z_H(x)} \\
    - & \left( (a(x) + \beta S_{\sigma_1}(x) + \gamma) (b(x) + \beta S_{\sigma_2}(x) + \gamma) (c(x) + \beta S_{\sigma_3}(x) + \gamma) z(xw) \right) \dfrac{\alpha}{Z_H(x)} \\
    + & (z(x) - 1) L_1(x) \dfrac{\alpha^2}{Z_H(x)} 


- tách :math:`t(x)` thành các đa thức bậc nhỏ hơn :math:`n+2` là 
  :math:`t_{10}(x)`, :math:`t_{\text{mid}}(x)` và :math:`t_{\text{ni}}(x)` sao cho

.. math:: t(x) = t_{10}(x) + x^{n+2} t_{\text{mid}}(x) + x^{2n+4} t_{\text{ni}}(x).

Đầu ra của round :math:`3` là :math:`[t_{10}(s)]`, :math:`[t_{\text{mid}}(x)]` và
:math:`[t_{\text{ni}}(x)]`.

Dòng cuối có :math:`L_1(x)` sẽ được định nghĩa dưới đây.

:math:`L_1(x)` là cơ sở của đa thức nội suy từ :math:`H`. 
Với :math:`L_1(1) = 1`, các giá trị còn lại cho ảnh bằng :math:`0`. 
Khi đó :math:`L_1(x)` tương ứng vector :math:`(1, 0, 0, 0)` 
nên :math:`L_1(x) = 13 + 13 x + 13 x^3 + 13 x^3`.

Verifier chọn số :math:`\alpha` (ngẫu nhiên) và gửi cho prover.

^^^^^^^^^^^^^^^^
Round 4
^^^^^^^^^^^^^^^^

- verifier chọn một số :math:`\mathfrak{z}` và gửi cho prover;
- prover khi đó cần tính

.. math:: 
    
    \begin{array}{ccc}
        \bar{a} = a(\mathfrak{z}) & \bar{b} = b(\mathfrak{z}) & \bar{c} = c(\mathfrak{z}) \\
        \bar{S}_{\sigma_1} = S_{\sigma_1}(\mathfrak{z}) & \bar{S}_{\sigma_2} = S_{\sigma_2}(\mathfrak{z}) & \\
        \bar{t} = t(\mathfrak{z}) & & \\
        \bar{z}_w = z(\mathfrak{z} w)
    \end{array}

- tính đa thức linearization

.. math:: 

    r(x) = & \bar{a} \bar{b} q_M(x) + \bar{a} q_L(x) + \bar{b} q_R(x) + \bar{c} q_O(x) + q_C(x) \\
    + & ((\bar{a} + \beta \mathfrak{z} + \gamma) (\bar{b} + \beta k_1 \mathfrak{z} + \gamma) (\bar{c} + \beta k_2 \mathfrak{z} + \gamma) \cdot z(x)) \alpha \\
    - & ((\bar{a} + \beta \bar{S}_{\sigma_1} + \gamma) (\bar{b} + \beta \bar{S}_{\sigma_2} + \gamma) \beta \bar{z}_w \cdot S_{\sigma_3}(s)) \alpha \\
    + & z(x) L_1(\mathfrak{z}) \alpha^2


- tính linearization evaluation :math:`\bar{r} = r(\mathfrak{z})`.

Output của round 5 là các giá trị

.. math:: (\bar{a}, \bar{b}, \bar{c}, \bar{S}_{\sigma_1}, \bar{S}_{\sigma_2}, \bar{z}_w, \bar{t}, \bar{z}).

^^^^^^^^^^^^^^^^
Round 5
^^^^^^^^^^^^^^^^

Verifier chọn số ngẫu nhiên :math:`v \in \mathbb{F}_{17}` và 
gửi cho prover.

- tính đa thức đầu cho proof là :math:`W_{\mathfrak{z}}(x)` như sau

.. math:: 
    
    W_\mathfrak{z}(x) = \dfrac{1}{x-\mathfrak{z}} \left(\begin{split}
        & t_{10}(x) + \mathfrak{z}^{n+2} t_\text{mid}(x) + \mathfrak{z}^{2n+4} t_\text{ni}(x) - \bar{t} \\
        + & v(r(x) - \bar{r}) \\
        + & v^2 (a(x) - \bar{a}) \\
        + & v^3 (b(x) - \bar{b}) \\
        + & v^4 (c(x) - \bar{c}) \\
        + & v^5 (S_{\sigma_1}(x) - \bar{S}_{\sigma_1}) \\
        + & v^6 (S_{\sigma_2}(x) - \bar{S}_{\sigma_2})
    \end{split}\right)

- tính đa thức tiếp theo cho proof là :math:`W_{\mathfrak{z} w}(x)`:

.. math:: W_{\mathfrak{z} w}(x) = \dfrac{z(x) - \bar{z}_w}{x - \mathfrak{z} w}.

Output của round 5 là :math:`[w_\mathfrak{z}], [w_{\mathfrak{z} w}]`.

^^^^^^^^^^^^^^^^
Proof
^^^^^^^^^^^^^^^^

Proof thu được là vector :math:`\pi_{\text{SNARK}}` như sau

.. math:: \pi_{\text{SNARK}} = ([a], [b], [c], [z], [t_{10}], [t_{\text{mid}}], [t_{\text{ni}}], [W_\mathfrak{z}], [W_{\mathfrak{z} w}], \bar{a}, \bar{b}, \bar{c}, \bar{S}_{\sigma_1}, \bar{S}_{\sigma_2}, \bar{r}, \bar{z}_w).

-------------------------
Code mẫu với SageMath
-------------------------

.. code-block:: python

    from sage.all import *

    F101 = GF(101)['xn']; xn = F101.gen()
    F101_2 = GF(101**2, name='yn', modulus=xn**2 + 2)

    Ec = EllipticCurve(F101_2, [0, 3])

    G1 = Ec(1, 2)
    G2 = Ec(36, 31*xn)

    s = 2
    n = 4
    SRS = []
    for i in range(n+3):
        SRS.append(s**i * G1)
    for i in range(2):
        SRS.append(s**i * G2)

    print([srs.xy() for srs in SRS])

    F17 = GF(17)
    Pol = PolynomialRing(F17, 'x')
    x = Pol.gen()

    Z_H = x**4 - 1

    k1, k2 = 2, 3
    H = [F17(i) for i in [1, 4, 16, 13]]
    assert set(H) == set([z[0] for z in Z_H.roots()])
    k1_H = [F17(k1 * h) for h in H]
    k2_H = [F17(k2 * h) for h in H]

    print(f"k1 H = {k1_H}, k2 H = {k2_H}")

    ai = [3, 4, 5, 9]
    bi = [3, 4, 5, 16]
    ci = [9, 16, 25, 25]
    qLi = [0, 0, 0, 1]
    qRi = [0, 0, 0, 1]
    qOi = [-1, -1, -1, -1]
    qMi = [1, 1, 1, 0]
    qCi = [0, 0, 0, 0]

    fa = Pol.lagrange_polynomial(list(zip(H, ai)))
    fb = Pol.lagrange_polynomial(list(zip(H, bi)))
    fc = Pol.lagrange_polynomial(list(zip(H, ci)))
    fqL = Pol.lagrange_polynomial(list(zip(H, qLi)))
    fqR = Pol.lagrange_polynomial(list(zip(H, qRi)))
    fqO = Pol.lagrange_polynomial(list(zip(H, qOi)))
    fqM = Pol.lagrange_polynomial(list(zip(H, qMi)))
    fqC = Pol.lagrange_polynomial(list(zip(H, qCi)))

    sigma_1 = list(map(F17, [2, 8, 15, 3]))
    sigma_2 = list(map(F17, [1, 4, 16, 12]))
    sigma_3 = list(map(F17, [13, 8, 5, 14]))

    S_sig_1 = Pol.lagrange_polynomial(list(zip(H, sigma_1)))
    S_sig_2 = Pol.lagrange_polynomial(list(zip(k1_H, sigma_2)))
    S_sig_3 = Pol.lagrange_polynomial(list(zip(k2_H, sigma_3)))

    # Dưới đây là kết quả tính theo ví dụ, khác phần trên
    S_sig_2 = x**3 + 13*x**2 + 4
    S_sig_3 = 14*x**3 + 3*x**2 + 7*x + 6

    # Round 1

    b_coeffs = [7, 4, 11, 12, 16, 2]

    ax = (b_coeffs[0] * x + b_coeffs[1]) * Z_H + fa
    bx = (b_coeffs[2] * x + b_coeffs[3]) * Z_H + fb
    cx = (b_coeffs[4] * x + b_coeffs[5]) * Z_H + fc

    ass = sum(i * j for i, j in zip(ax.coefficients(), SRS))
    bss = sum(i * j for i, j in zip(bx.coefficients(), SRS))
    css = sum(i * j for i, j in zip(cx.coefficients(), SRS))

    print(ass.xy(), bss.xy(), css.xy())

    # Round 2

    b_coeffs.extend([14, 11, 7])

    beta_, gamma_ = 12, 13

    w = 4 # Choose from H
    acc = [1]
    for i in range(1, len(H)):
        numerator_  = (ai[i-1] + beta_ * w**(i-1) + gamma_)
        numerator_ *= (bi[i-1] + beta_ * k1 * w**(i-1) + gamma_)
        numerator_ *= (ci[i-1] + beta_ * k2 * w**(i-1) + gamma_)

        denominator_  = (ai[i-1] + beta_ * S_sig_1(w**(i-1)) + gamma_)
        denominator_ *= (bi[i-1] + beta_ * S_sig_2(w**(i-1)) + gamma_)
        denominator_ *= (ci[i-1] + beta_ * S_sig_3(w**(i-1)) + gamma_)

        acc.append(acc[-1] * F17(numerator_) / F17(denominator_))

    accx = Pol.lagrange_polynomial(list(zip(H, acc)))
    print(accx)

    zx = (b_coeffs[6] * x**2 + b_coeffs[7] * x + b_coeffs[8]) * Z_H + accx
    zs = zx(s) * G1
    print(f"[z(s)] = {zs.xy()}")

    alpha = 15

    L1x = Pol.lagrange_polynomial(list(zip(H, [1, 0, 0, 0])))

    tx = (ax * bx * fqM + ax * fqL + bx * fqR + cx * fqO + 0 + fqC)
    tx += (ax + beta_ * x + gamma_) * (bx + beta_ * k1 * x + gamma_) * (cx + beta_ * k2 * x + gamma_) * zx * alpha
    tx -= (ax + beta_ * S_sig_1 + gamma_) * (bx + beta_ * S_sig_2 + gamma_) * (cx + beta_ * S_sig_3 + gamma_) * zx(w * x) * alpha
    tx += (zx - 1) * L1x * alpha * alpha

    #print(tx.coefficients(sparse=False))

    print(tx % Z_H)

    tx //= (x**4 - 1)

    tx_c = tx.coefficients(sparse=False)

    #print(tx_c)

    t10 = Pol(tx_c[0:6])
    tmid = Pol(tx_c[6:12])
    tni = Pol(tx_c[12:18])

    t10s = t10(s) * G1
    tmids = tmid(s) * G1
    tnis = tni(s) * G1

    zz = 5

    abar = ax(zz)
    bbar = bx(zz)
    cbar = cx(zz)
    S_sig_1_bar = S_sig_1(zz)
    S_sig_2_bar = S_sig_2(zz)
    tbar = tx(zz)
    zwbar = zx(w * zz)

    rx = abar * bbar * fqM + abar * fqL + bbar * fqR + cbar * fqO + fqC
    rx += (abar + beta_ * zz + gamma_) * (bbar + beta_ * k1 * zz + gamma_) * (cbar + beta_ * k2 * zz + gamma_) * zx * alpha
    rx -= (abar + beta_ * S_sig_1_bar + gamma_) * (bbar + beta_ * S_sig_2_bar + gamma_) * beta_ * zwbar * S_sig_3 * alpha
    rx += zx * L1x(zz) * alpha**2

    rbar = rx(zz)

    print(abar, bbar, cbar, S_sig_1_bar, S_sig_2_bar, zwbar, tbar, rbar)

    v = F17(12)

    wzx = t10 + zz**(n+2) * tmid + zz**(2*n+4) * tni - tbar
    wzx += v * (rx - rbar)
    wzx += v**2 * (ax - abar)
    wzx += v**3 * (bx - bbar)
    wzx += v**4 * (cx - cbar)
    wzx += v**5 * (S_sig_1 - S_sig_1_bar)
    wzx += v**6 * (S_sig_2 - S_sig_2_bar)
    wzx //= (x - zz)

    wzwx = (zx - zwbar) // (x - zz * w)

    f__ = lambda fx, srs: sum(i * j for i, j in zip(fx.coefficients(sparse=False), srs))


    a__ = f__(ax, SRS)
    b__ = f__(bx, SRS)
    c__ = f__(cx, SRS)
    z__ = f__(zx, SRS)
    t10__ = f__(t10, SRS)
    tmid__ = f__(tmid, SRS)
    tni__ = f__(tni, SRS)
    wz__ = f__(wzx, SRS)
    wzw__ = f__(wzwx, SRS)

    pi_snark = [a__, b__, c__, z__, t10__, tmid__, tni__, wz__, wzw__, abar, bbar, cbar, S_sig_1_bar, S_sig_2_bar, rbar, zwbar]
    print(pi_snark)

--------------------
Tài liệu tham khảo
--------------------

[1] *Under the hood of zkSNARKs — PLONK protocol: Part 1*, URL - https://medium.com/coinmonks/under-the-hood-of-zksnarks-plonk-protocol-part-1-34bc406d8303

[2] *Under the hood of zkSNARKs — PLONK protocol: Part 2*, URL - https://medium.com/coinmonks/under-the-hood-of-zksnarks-plonk-protocol-part-2-ee00d6accb4d

[3] *Under the hood of zkSNARKs — PLONK protocol: Part 3*, URL - https://medium.com/@cryptofairy/under-the-hood-of-zksnarks-plonk-protocol-part3-821855e49ce6

[4] https://github.com/tarassh/zkSNARK-under-the-hood