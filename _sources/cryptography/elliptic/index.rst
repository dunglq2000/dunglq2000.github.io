Đường cong elliptic
*******************

Đường cong elliptic (elliptic curve) rất nổi tiếng 
trong toán học. Đây là công cụ giúp các nhà toán học 
giải quyết bài toán lớn **Định lý cuối cùng của Fermat**. 

Trong mật mã học, đường cong elliptic là một trong 
những tiêu chuẩn bảo mật về mã hóa và chữ ký điện tử. 
Chương này khảo sát những đặc trưng cơ bản đường cong 
elliptic và ứng dụng trong mật mã học.


Mở đầu về đường cong elliptic
==============================

Đường cong elliptic là tập hợp các điểm :math:`(x, y)` trên mặt phẳng :math:`Oxy` thỏa mãn phương trình

.. math:: y^2 = x^3 + ax + b,

với :math:`a, b \in \mathbb{R}` và :math:`4a^3 + 27b^2 \neq 0`.

Ví dụ với phương trình :math:`y^2 = x^3 + 8`, đồ thị được biểu diễn ở :numref:`hình %s <ecc-1>`.

Ta thấy rằng, đường cong elliptic đối xứng qua trục hoành.

.. _ecc-1:

.. figure::  ../../figures/ecc/ecc1.jpg

    Elliptic :math:`y^2 = x^3 + 8`

Ví dụ với phương trình :math:`y^2 = x^3 - x`, đồ thị được biểu diễn ở :numref:`hình %s <ecc-2>`.

.. _ecc-2:

.. figure::  ../../figures/ecc/ecc2.jpg  

    Elliptic :math:`y^2 = x^3 - x`

Hoặc đối với phương trình :math:`y^2 = x^3 - 3x + 3` thì đồ thị được biểu diễn ở :numref:`hình %s <ecc-3>`.

.. _ecc-3:

.. figure::  ../../figures/ecc/ecc3.jpg  

    Elliptic :math:`y^2 = x^3 - 3x + 3`


Phép cộng các điểm trên elliptic
================================

Phương trình và đồ thị của đường cong elliptic đã 
được trình bày ở trên. Tuy nhiên chúng ta quan tâm 
tới mối liên hệ giữa các điểm trên elliptic, cụ thể 
là **phép cộng** hai điểm.

Ta thêm một điểm trừu tượng vào tập hợp các điểm 
trên đường cong elliptic và gọi là **điểm vô cực**. 
Điểm vô cực được kí hiệu là :math:`\mathcal{O}`. 
Khi đó mọi điểm :math:`P` thuộc đường cong elliptic 
sẽ có tính chất

.. math:: P + \mathcal{O} = \mathcal{O} + P = P.

Khi đó, với điểm :math:`P=(x, y)` bất kì trên elliptic, 
điểm đối xứng của nó qua trục hoàng là :math:`P' = (x, -y)`, 
và ta định nghĩa :math:`P + P' = \mathcal{O}`. 

Tiếp theo ta định nghĩa phép cộng hai điểm.

Giả sử :math:`P = (x_P, y_P)` và :math:`Q = (x_Q, y_Q)` 
là hai điểm trên elliptic. Ta có hai trường hợp:

1. Nếu :math:`P \neq Q`, ta vẽ đường thẳng đi qua 
   :math:`P` và :math:`Q`. Đường thẳng này cắt elliptic 
   tại điểm thứ ba là :math:`S`. Ta lấy :math:`R` đối xứng 
   với :math:`S` qua trục hoành. Khi đó :math:`R` cũng nằm 
   trên elliptic và :math:`P + Q = R`;
2. Nếu :math:`P \equiv Q`, ta vẽ tiếp tuyến với elliptic 
   tại điểm :math:`P`. Tiếp tuyến này cắt elliptic tại điểm 
   thứ hai là :math:`S`. Tương tự ta lấy :math:`R` đối xứng 
   với :math:`S` qua trục hoành. Khi đó :math:`P + Q = 2P = R`.

Khi đó, tập hợp các điểm trên elliptic cùng với 
điểm vô cực, và phép cộng hai điểm được định nghĩa 
như trên tạo thành một nhóm.

Để chứng minh đây là nhóm, ta cần chuyển các khái niệm 
hình học kia sang đại số để tính toán và chứng minh.


Phép cộng hai điểm khác nhau
-----------------------------

Đầu tiên ta thiết lập công thức phép cộng giữa hai điểm 
cho trường hợp :math:`P \neq Q`. Giả sử 
:math:`P = (x_P, y_P)` và :math:`Q = (x_Q, y_Q)`.

Phương trình đường thẳng đi qua :math:`P` và :math:`Q` là

.. math:: 
    :label: eqecc-1

    y = \frac{y_Q - y_P}{x_Q - x_P} (x - x_P) + y_P.

Thay :math:`y` vào phương trình đường cong elliptic ta có

.. math:: 
    :label: eqecc-2

    \left[\frac{y_Q - y_P}{x_Q - x_P} (x - x_P) + y_P\right]^2 = x^3 + ax + b

Đặt :math:`k = \dfrac{y_Q - y_P}{x_Q - x_P}`. 
Khi đó phương trình tương đương với

.. math:: (k x - k x_P + y_P)^2 = x^3 + ax + b.

Khai triển và chuyển vế ta có

.. math:: x^3 - k^2 x^2 + \ldots = 0.

Ta chỉ cần quan tâm hệ số trước :math:`x^2`. 
Bởi vì ta biết rằng đường thẳng :math:`PQ` cắt elliptic 
tại ba điểm :math:`P`, :math:`Q`, :math:`S`, nên phương trình 
bậc 3 này có 3 nghiệm phân biệt là :math:`x_P`, :math:`x_Q` 
và :math:`x_S`. Theo theo định lý Viete ta có

.. math:: x_P + x_Q + x_S = k^2.

Như vậy ta có hoành độ điểm :math:`S`

.. math:: x_S = k^2 - x_P - x_Q,

thay :math:`x_S` vào :eq:`eqecc-1`, ta có tung độ điểm :math:`S`

.. math:: y_S = k(x_S - x_P) + y_P,

mà :math:`R` đối xứng với :math:`S` qua trục hoành, 
như vậy :math:`x_R = x_S` và :math:`y_R = -y_S`. 

Như vậy kết quả của phép cộng là

.. math:: 

    x_R & = k^2 - x_P - x_Q \\
    y_R & = k(x_P - x_R) - y_P

với :math:`k = \dfrac{y_Q - y_P}{x_Q - x_P}`.


Phép cộng hai điểm giống nhau
-----------------------------

Trong trường hợp hai điểm giống nhau, ta vẽ 
tiếp tuyến tiếp xúc với elliptic đi qua điểm đó. 

Giả sử ta muốn vẽ tiếp tuyến tại điểm :math:`P = (x_P, y_P)`, 
khi đó từ phương trình elliptic :math:`y^2 = x^3 + ax + b` 
ta vi phân hai vế thu được 

.. math:: 2y \,dy = (3x^2 + a) \, dx.

Ta biết rằng hệ số góc của đường tiếp tuyến là 
đạo hàm hàm số tại điểm đó, hay nói cách khác là 
:math:`dy/dx`. Như vậy hệ số góc tiếp tuyến tại 
điểm :math:`P` là

.. math:: k = \frac{dy}{dx} = \frac{3 x_P^2 + a}{2y_P}

và như vậy phương trình đường tiếp tuyến là

.. math:: y = k(x-x_P) + y_P.

Thực hiện tương tự như bên trên, ta có đường 
tiếp tuyến cắt elliptic tại hai điểm phân biệt, trong đó 
có một điểm tiếp xúc nên trong phương trình hoành độ 
giao điểm điểm tiếp xúc là nghiệm bội hai. Nói cách khác, 
theo định lý Viete thì

.. math:: x_P + x_P + x_S = k^2,

suy ra hoành độ điểm :math:`S` là

.. math:: x_S = k^2 - 2 x_P,

và tung độ điểm :math:`S` là

.. math:: y_S = k(x_S - x_P) + y_P

Cuối cùng, tọa độ điểm :math:`R = P + P` là

.. math:: x_R = k^2 - 2 x_P, \quad y_R = k(x_P - x_S) - y_P.


Tổng kết
--------

Để cộng hai điểm :math:`P=(x_P, y_P)` và 
:math:`Q = (x_Q, y_Q)` ta có ba trường hợp sau:

1. Nếu :math:`x_Q = x_P` và :math:`y_Q = -y_P`, 
   nói cách khác là đối xứng qua trục hoành, 
   thì ta có :math:`P + Q = \mathcal{O}`.
2. Nếu :math:`x_P \neq x_Q`, đặt 
   :math:`k = \dfrac{y_Q - y_P}{x_Q - x_P}` 
   thì tọa độ điểm :math:`R = P + Q` là

.. math:: x_R = k^2 - x_P - x_Q, \quad y_R = k(x_P - x_R) - y_P.

3. Nếu :math:`x_P = x_Q` và :math:`y_P = y_Q`, 
   khi hai điểm trùng nhau, đặt 
   :math:`k = \dfrac{3x_P^2 + a}{2y_P}`, thì 
   tọa độ điểm :math:`R = 2P` là

.. math:: x_R = k^2 - 2x_P, \quad y_R = k(x_P - x_R) - y_P.

.. _duong-cong-elliptic-tren-Fp: 

Đường cong elliptic trên trường hữu hạn :math:`\mathbb{F}_p`
============================================================

Trong mật mã học đường cong elliptic được sử dụng 
nhiều nhất là trên trường hữu hạn :math:`\mathbb{F}_p` 
với :math:`p` là số nguyên tố.

Đường cong ellipitc lúc này là điểm vô cực 
:math:`\mathcal{O}` và tập hợp các điểm 
:math:`(x, y) \in \mathbb{F}_p^2` thỏa mãn

.. math:: y^2 \equiv x^3 + ax + b \bmod p,.

với :math:`4 a^3 + 27 b^2 \neq 0 \bmod p`.

Việc thực hiện phép cộng hai điểm cũng tương tự 
như trên :math:`\mathbb{R}` ở phần trên nhưng các 
phép tính được thực hiện trong modulo :math:`p`. 

Như vậy để cộng hai điểm :math:`P = (x_P, y_P)` 
và :math:`Q = (x_Q, y_Q)` thì:

1. Nếu :math:`x_Q \equiv x_P \pmod p` và 
   :math:`y_Q \equiv -y_P \pmod p` thì :math:`P + Q = \mathcal{O}`.
2. Nếu :math:`x_Q \not\equiv x_P \pmod p`, 
   đặt :math:`k \equiv \dfrac{y_Q - y_P}{x_Q - x_P} \pmod p` 
   thì tọa độ điểm :math:`R = P + Q` là

.. math:: x_R \equiv k^2 - x_P - x_Q \pmod p, \quad y_R = k(x_P - x_R) - y_P \pmod p.

3. Nếu :math:`x_Q \equiv x_P` và 
   :math:`y_Q \equiv y_P`, nói cách khác là hai điểm 
   trùng nhau, đặt :math:`k = \dfrac{3x_P^2 + a}{2y_P} \pmod p` 
   thì tọa độ điểm :math:`R = 2 P` là

.. math:: x_R = k^2 - 2x_P \pmod p, \quad y_R = k(x_P - x_R) - y_P \pmod p.

Một điểm đáng chú ý là :math:`\mathbb{F}_p` có hữu hạn phần tử, 
do đó số phần tử của đường cong elliptic với tọa độ trong 
:math:`\mathbb{F}_p` cũng là hữu hạn. Do tính chất này 
mà mật mã học có thể sử dụng đường cong elliptic.


Dạng Weierstrass tổng quát
==========================

Ở công thức cộng hai điểm giống nhau xuất hiện hai hằng số 
là :math:`2` và :math:`3`. Một vấn đề đặt ra là nếu trường 
có đặc số bằng :math:`2`, nghĩa là :math:`2 \equiv 0`, 
khi đó hàm hai biến

.. math:: f(x, y) = y^2 - x^3 - ax - b

sẽ có đạo hàm theo :math:`y` luôn bằng :math:`0` 
vì :math:`f_y = 2y \equiv 0`. Ta không thể tính tiếp tuyến 
như trên :math:`\mathbb{R}` để đưa ra công thức cho phép cộng 
hai điểm giống nhau. Tương tự đối với trường có đặc số 
bằng :math:`3`.

Trong trường hợp các trường :math:`K` có đặc số bằng 
:math:`2` thì chúng ta sử dụng dạng Weierstrass tổng quát 
(generalized Weierstrass) là

.. math:: y^2 + a_1 xy + a_3 y = x^3 + a_2 x^2 + a_4 x + a_6,

với :math:`a_1, a_2, a_3, a_4, a_6 \in K`.

[TODO] Phép cộng hai điểm trên đường cong elliptic dạng Weierstrass tổng quát.
