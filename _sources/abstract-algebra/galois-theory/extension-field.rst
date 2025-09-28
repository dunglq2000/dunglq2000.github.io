================
Extension Fields
================

----------------
Extension Fields
----------------

.. prf:definition:: Mở rộng trường
    :label: def-extension-field
    
    Trường :math:`E` được gọi là **mở rộng trường** (hay **extension field**) của trường :math:`F` nếu :math:`F` là trường con của :math:`E`. Khi đó :math:`F` được gọi là **trường cơ sở** (hay **base field**) và kí hiệu :math:`F \subset E`.

.. prf:example:: 
    :label: exp-q-sqrt2

    Trường nào nhỏ nhất chứa :math:`\mathbb{Q}` và :math:`\sqrt{2}`?

    Đáp án là trường
    
    .. math:: \mathbb{Q}(\sqrt{2}) = \{ a + b \sqrt{2} : a, b \in \mathbb{Q} \}.

    Việc chứng minh :math:`\mathbb{Q}(\sqrt{2})` là trường khá đơn giản, phần tử nghịch đảo đối với phép nhân của :math:`a + b \sqrt{2}` là

    .. math:: \frac{a}{a^2 - 2 b^2} + \frac{-2b}{a^2 - 2 b^2} \sqrt{2}.

.. prf:example:: 
    :label: exp-field-q-i
    
    Trường nào nhỏ nhất chứa :math:`\mathbb{Q}` và :math:`i` (ở đây :math:`i` là đơn vị ảo, :math:`i^2 = -1`)?

    Đáp án là trường
    
    .. math:: \mathbb{Q}(i) = \{ a + b i : a, b \in \mathbb{Q} \}.
        
    Tương tự, ở đây phần tử nghịch đảo đối với phép nhân của :math:`a + b i` là

    .. math:: \frac{a}{a^2 + b^2} + \frac{-b}{a^2 + b^2} i.

Ở đây :math:`\mathbb{Q}(\sqrt{2})` và :math:`\mathbb{Q}(i)` đều là mở rộng của :math:`\mathbb{Q}` và đều là tập con của :math:`\mathbb{C}`. Tuy nhiên hai trường này không phải tập con của nhau.

Như vậy, bằng việc mở rộng :math:`\mathbb{Q}` với :math:`\sqrt{2}` ta có trường :math:`\mathbb{Q}(\sqrt{2})`.

Tương tự, bằng việc mở rộng :math:`\mathbb{Q}` với :math:`i` ta có trường :math:`\mathbb{Q}(i)`.

Vậy trường nào chứa :math:`\mathbb{Q}`, :math:`\sqrt{2}` và :math:`i`?

.. prf:example:: 
    :label: exp-field-q-sqrt2-i
    
    Trường chứa cả :math:`\mathbb{Q}`, :math:`\sqrt{2}` và :math:`i` là tập hợp

    .. math:: \mathbb{Q}(\sqrt{2}, i) = \{ a + b\sqrt{2} + c i + d \sqrt{2} i : a, b, c, d \in \mathbb{Q} \}.

Trường trên có thể suy ra từ logic sau. Ta đã có :math:`\mathbb{Q}(i)` chứa :math:`\mathbb{Q}` và :math:`i`. Ta muốn thêm :math:`\sqrt{2}` vào trường :math:`\mathbb{Q}(i)` nên ta sẽ muốn mở rộng :math:`\mathbb{Q}(i)` lên :math:`\mathbb{Q}(i)(\sqrt{2})`.

Khi đó :math:`\mathbb{Q}(i)(\sqrt{2})` tương tự sẽ có dạng

.. math:: \mathbb{Q}(i)(\sqrt{2}) = \{ \alpha + \beta \sqrt{2} : \alpha, \beta \in \mathbb{Q}(i) \}.

Nói cách khác :math:`\alpha = a + b i` và :math:`\beta = c + d i`, :math:`a, b, c, d \in \mathbb{Q}`, nên ta có

.. math:: \alpha + \beta \sqrt{2} = a + b i + c \sqrt{2} + d \sqrt{2} i, \quad a, b, c, d \in \mathbb{Q}.

Khi đó ta viết

.. math:: \mathbb{Q}(i)(\sqrt{2}) = \mathbb{Q}(\sqrt{2}, i) = \{ a + b\sqrt{2} + c i + d \sqrt{2} i : a, b, c, d \in \mathbb{Q} \}.


.. prf:remark:: 
    :label: rmk-extension-field

    1. :math:`\mathbb{Q}(\sqrt{2})` là trường con của :math:`\mathbb{R}` nhưng :math:`\mathbb{Q}(i)` không phải.
    2. :math:`\mathbb{Q}(i)` nhỏ hơn :math:`\mathbb{C}` rất nhiều (không chứa :math:`\sqrt{2}`).
    3. :math:`\mathbb{Q}(\sqrt{2})` chứa tất cả nghiệm của đa thức :math:`f(x) = x^2 - 2` trên :math:`\mathbb{Q}`. Do đó :math:`\mathbb{Q}(\sqrt{2})` được gọi là **trường phân rã** của đa thức :math:`f(x)`.

---------------------------------------------
Biểu diễn quan hệ giữa các trường qua lattice
---------------------------------------------

Ở phần trước, :math:`\mathbb{Q}(\sqrt{2})` là mở rộng của :math:`\mathbb{Q}` và với hai phần tử :math:`a, b \in \mathbb{Q}` xác định một phần tử :math:`a + b \sqrt{2} \in \mathbb{Q}(\sqrt{2})`.

Do :math:`a + b \sqrt{2} = a \cdot 1 + b \cdot \sqrt{2}` nên :math:`\{ 1, \sqrt{2} \}` là **cơ sở** (hay **basis**) của :math:`\mathbb{Q}(\sqrt{2})`. Cơ sở chứa hai phần tử nên ta nói **bậc của mở rộng đơn** (hay **degree**) từ :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(\sqrt{2})` là :math:`2`.

Tương tự, mở rộng từ :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(i)` cũng có bậc là :math:`2` với cơ sở là :math:`\{ 1, i \}`.

Ta kí hiệu bậc của mở rộng đơn là

.. math:: \boxed{[E : F].}

Như vậy ta cũng các trường :math:`\mathbb{Q}(\sqrt{2})`, :math:`\mathbb{Q}(\sqrt{3})` và :math:`\mathbb{Q}(\sqrt{6})` là các mở rộng đơn bậc :math:`2` của :math:`\mathbb{Q}` (:numref:`extension_field-1`).

.. _extension_field-1:

.. figure:: ../../figures/extension_field/extension_field-1.*

    Mở rộng trường :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(\sqrt{2})`, :math:`\mathbb{Q}(\sqrt{3})` và :math:`\mathbb{Q}(\sqrt{6})`

Do :math:`\sqrt{6} = \sqrt{2} \cdot \sqrt{3}` dẫn ta tới câu hỏi, trường nào nhỏ nhất chứa cả :math:`\sqrt{2}` và :math:`\sqrt{3}`?

Thực hiện tương tự với :math:`\mathbb{Q}(\sqrt{2}, i)` ở trên ta có trường

.. math:: \mathbb{Q}(\sqrt{2}, \sqrt{3}) = \mathbb{Q}(\sqrt{2})(\sqrt{3}) = \{ a + b \sqrt{2} + c \sqrt{3} + d \sqrt{6} : a, b, c, d \in \mathbb{Q} \}

là trường nhỏ nhất chứa cả :math:`\sqrt{2}` và :math:`\sqrt{3}`.

Ở đây, :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` là mở rộng bậc :math:`4` của :math:`\mathbb{Q}` với cơ sở là :math:`\{ 1, \sqrt{2}, \sqrt{3}, \sqrt{6} \}`.

Bằng việc mở rộng từ :math:`\mathbb{Q}(\sqrt{2})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}) = \mathbb{Q}(\sqrt{2})(\sqrt{3})` ta cũng có đây là mở rộng bậc :math:`2` (tương tự chứng minh phía trên cho :math:`\mathbb{Q}(\sqrt{2}, i)`). Như vậy mở rộng từ :math:`\mathbb{Q}(\sqrt{3})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` cũng là mở rộng bậc :math:`2`.

Vậy mở rộng từ :math:`\mathbb{Q}(\sqrt{6})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` là bậc mấy? Để xác định ta cần chứng minh nhận xét sau

.. prf:remark:: 
    :label: rmk-field-equiv
    
    :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}) \equiv \mathbb{Q}(\sqrt{2} + \sqrt{3})`, trong đó :math:`\mathbb{Q}(\sqrt{2} + \sqrt{3})` là trường nhỏ nhất chứa :math:`\mathbb{Q}` và :math:`\sqrt{2} + \sqrt{3}`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Ta chứng minh :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}) \subset \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Do :math:`\sqrt{2} + \sqrt{3}` nên nghịch đảo :math:`\dfrac{1}{\sqrt{2} + \sqrt{3}} = \sqrt{3} - \sqrt{2} \in \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Khi đó, :math:`\dfrac{1}{2} \cdot (\sqrt{2} + \sqrt{3}) \pm \dfrac{1}{2} \cdot (\sqrt{3} - \sqrt{2}) \in \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Vế trái sẽ bằng :math:`\sqrt{2}` hoặc :math:`\sqrt{3}`. Như vậy :math:`\sqrt{2}, \sqrt{3} \in \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Phép nhân trên trường cho ta :math:`\sqrt{2} \cdot \sqrt{3} = \sqrt{6} \in \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Như vậy với mọi :math:`a, b, c, d \in \mathbb{Q}` ta có :math:`a + b \sqrt{2} + c \sqrt{3} + d \sqrt{6} \in \mathbb{Q}(\sqrt{2} + \sqrt{3})`. Điều này tương đương với :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}) \subset \mathbb{Q}(\sqrt{2} + \sqrt{3})`.

    Nhưng mà :math:`\mathbb{Q}(\sqrt{2} + \sqrt{3})` là trường nhỏ nhất chứa :math:`\mathbb{Q}` và :math:`\sqrt{2} + \sqrt{3}`, và :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` là trường nhỏ nhất chứa :math:`\sqrt{2}` và :math:`\sqrt{3}`, kéo theo chứa cả :math:`\sqrt{2} + \sqrt{3}` nên :math:`\mathbb{Q}(\sqrt{2} + \sqrt{3}) \equiv \mathbb{Q}(\sqrt{2}, \sqrt{3})`.

Ta có :math:`\mathbb{Q}(\sqrt{6}) = \{ a + b \sqrt{6} : a, b \in \mathbb{Q} \}`. Khi đó

.. math:: 
    :label: QQ6_to_QQ2+3

    \mathbb{Q}(\sqrt{6})(\sqrt{2} + \sqrt{3}) = \{ \alpha + \beta (\sqrt{2} + \sqrt{3}) : \alpha, \beta \in \mathbb{Q}(\sqrt{6}) \}.

Đặt :math:`\alpha = a + b \sqrt{6}` và :math:`\beta = c + d \sqrt{6}`, như vậy mỗi phần tử trong :math:`\mathbb{Q}(\sqrt{6})(\sqrt{2} + \sqrt{3})` có dạng

.. math:: 
    
    a + b \sqrt{6} + (c + \sqrt{6})(\sqrt{2} + \sqrt{3}) = & a + (c + 3d) \sqrt{2} + (c + 2d) \sqrt{3} + b \sqrt{6} \\
        = & a' + b' \sqrt{2} + c' \sqrt{3} + d' \sqrt{6},
    
với :math:`a \to a'`, :math:`c+3d \to b'`, :math:`c + 2d \to c'` và :math:`b \to d'`.

Biến đổi này tương đương với hệ phương trình tuyến tính

.. math:: 

    \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 3 \\
        0 & 0 & 1 & 2 \\
        0 & 1 & 0 & 0
    \end{pmatrix} \begin{pmatrix}
        a \\ b \\ c \\ d
    \end{pmatrix} = \begin{pmatrix}
        a' \\ b' \\ c' \\ d'
    \end{pmatrix}

Ma trận trên khả nghịch trên :math:`\mathbb{Q}`, do đó :math:`\mathbb{Q}(\sqrt{6})(\sqrt{2} + \sqrt{3}) \equiv \mathbb{Q}(\sqrt{2}, \sqrt{3})`. Ở dạng biểu diễn :eq:`QQ6_to_QQ2+3` ta suy ra mở rộng từ :math:`\mathbb{Q}(\sqrt{6})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` là mở rộng bậc :math:`2`.

Sơ đồ mở rộng trường bây giờ như sau

.. figure:: ../../figures/extension_field/extension_field-2.*

---------------
Splitting Field
---------------

.. prf:definition:: Trường phân rã
    :label: def-splitting-field

    Xét trường :math:`F` và đa thức khác hằng
    
    .. math:: p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0
        
    trên :math:`F[x]`, ở đây :math:`a_i \in F` với mọi :math:`i = 1, 2, \ldots`

    Trường mở rộng :math:`E` của trường :math:`F` được gọi là **trường phân rã** (hay **splitting field**) của :math:`p(x)` nếu tồn tại các phần tử :math:`\alpha_1`, :math:`\alpha_2`, ..., :math:`\alpha_n` thuộc :math:`E` sao cho :math:`E = F(\alpha_1, \alpha_2, \ldots, \alpha_n)` và

    .. math:: p(x) = (x - \alpha_1) (x - \alpha_2) \cdots (x - \alpha_n).

Khi đó ta nói đa thức :math:`p(x) \in F[x]` phân rã (split) trong :math:`E` nếu nó phân tích thành các nhân tử bậc nhất (tuyến tính) trong :math:`E[x]`.

Nói nôm na, nếu đa thức có hệ số trong một trường :math:`F` nào đó (tức thuộc :math:`F[x]`) thì các nghiệm của nó nằm trong một trường lớn hơn chứa :math:`F`.

.. prf:example:: 
    :label: exp-splitting-field-1
    
    Đa thức :math:`f(x) = x^2 - 2` trên :math:`\mathbb{Q}[x]` không có nghiệm trên :math:`\mathbb{Q}`. Tuy nhiên :math:`\mathbb{Q}(\sqrt{2})` là trường chứa :math:`\mathbb{Q}` và các nghiệm của :math:`f(x)` là :math:`\pm \sqrt{2}`. Vì vậy :math:`\mathbb{Q}(\sqrt{2})` là trường phân rã của :math:`f(x)`.

.. prf:example:: 
    :label: exp-splitting-field-2
    
    Đa thức :math:`g(x) = x^2 + 1` trên :math:`\mathbb{Q}[x]` không có nghiệm trên :math:`\mathbb{Q}`. Tuy nhiên :math:`g(x)` có hai nghiệm là :math:`\pm i` và :math:`\mathbb{Q}(i)` chứa cả :math:`\mathbb{Q}` và :math:`\pm i` nên :math:`\mathbb{Q}(i)` là một trường phân rã của :math:`g(x)`.

Ở đây, bậc của đa thức :math:`f(x) = x^2 - 2` bằng với bậc của mở rộng trường từ :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(\sqrt{2})`.

Tương tự, bậc của mở rộng trường từ :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(\sqrt{3})` bằng bậc đa thức :math:`g(x) = x^2 - 3`, và bậc của mở rộng trường từ :math:`\mathbb{Q}` lên :math:`\mathbb{Q}(\sqrt{6})` bằng với bậc đa thức :math:`h(x) = x^2 - 6`.

Ở trên ta đã chứng minh bậc của mở rộng trường từ :math:`\mathbb{Q}(\sqrt{2})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` là :math:`2`, điều này tương ứng với bậc của đa thức

.. math:: k(x) = (x^2 - 2)(x^2 - 3) = x^4 - 5 x + 6.

Tổng kết lại, nếu :math:`E` là trường phân rã của :math:`F` trên đa thức :math:`f(x) \in F[x]` thì bậc của mở rộng trường từ :math:`F` lên :math:`E` bằng với bậc của :math:`f(x)`.

Từ sơ đồ mở rộng trường bên trên ta có sơ đồ với đa thức tương ứng.

.. figure:: ../../figures/extension_field/extension_field-3.*

Vậy còn mở rộng từ :math:`\mathbb{Q}(\sqrt{6})` thành :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})`? Ở trên ta đã chứng minh rằng đây là mở rộng bậc :math:`2`. Vậy chúng ta cần tìm một đa thức bậc :math:`2` có hệ số trong :math:`\mathbb{Q}(\sqrt{6})` mà không có nghiệm trong :math:`\mathbb{Q}(\sqrt{6})`.

Quay lại một chút, ta đã mở rộng :math:`\mathbb{Q}(\sqrt{6})` lên :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` với sự trợ giúp của phần tử :math:`\sqrt{2} + \sqrt{3}`. Từ đây ta có thể xây dựng đa thức

.. math:: m(x) = x^2 - (\sqrt{2} + \sqrt{3})^2 = x^2 - 5 - 2 \sqrt{6}.

Đa thức :math:`m(x)` có hệ số trong :math:`\mathbb{Q}(\sqrt{6})` nhưng không có nghiệm trong :math:`\mathbb{Q}(\sqrt{6})`, mà trong :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})`. Ta có điều phải chứng minh.

------------------
Field automorphism
------------------

.. prf:remark:: 
    :label: rmk-automorphism
    
    Tập hợp tất cả tự đẳng cấu (automorphism) trên trường :math:`F` là nhóm với toán tử là hợp của các hàm. Kí hiệu là :math:`Aut(F)`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Dễ thấy nếu :math:`\sigma` và :math:`\tau` là tự đẳng cấu trên :math:`F` thì :math:`\sigma \tau` và :math:`\sigma^{-1}` cũng là tự đẳng cấu trên :math:`F` (đều là song ánh). Ánh xạ đồng nhất hiển nhiên là tự đẳng cấu nên sẽ là phần tử đơn vị của nhóm.

.. prf:remark:: 
    :label: rmk-group-automorphisms
    
    Gọi :math:`E` là mở rộng trường của :math:`F`. Khi đó tập hợp tất cả tự đẳng cấu trên :math:`E` mà cố định phần tử của :math:`F` tạo thành một nhóm, nghĩa là tập hợp tất cả các tự đẳng cấu :math:`\sigma : E \to E` sao cho :math:`\sigma(\alpha) = \alpha` với mọi :math:`\alpha \in F` tạo thành một nhóm.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Từ nhận xét ở trên thì tập hợp tất cả tự đẳng cấu trên :math:`E` tạo thành một nhóm :math:`Aut(E)`. Như vậy để chứng minh nhận xét này thì chúng ta chỉ cần chỉ ra tập hợp tất cả tự đẳng cấu của :math:`E` mà cố định phần tử trong :math:`F` là một nhóm con của :math:`Aut(E)`.

    Gọi :math:`\sigma` và :math:`\tau` là hai tự đẳng cấu của :math:`E` sao cho :math:`\sigma(\alpha) = \alpha` và :math:`\tau(\alpha) = \alpha` với mọi :math:`\alpha \in F`.

    Khi đó :math:`\sigma(\tau(\alpha)) = \sigma(\alpha) = \alpha` nên ánh xạ hợp :math:`\sigma \tau` cũng nằm trong tập các tự đẳng cấu trên :math:`E` mà cố định phần tử trên :math:`F`.

    Ngoài ra, :math:`\sigma^{-1}(\alpha) = \alpha` và ánh xạ đồng nhất cố định mọi phần tử trên :math:`E`. Như vậy tập tất cả tự đẳng cấu trên :math:`E` mà cố định mọi phần tử trong :math:`F` là nhóm con của :math:`Aut(E)`.

Ở trên ta kí hiệu nhóm tất cả các tự đẳng cấu trên :math:`E` là :math:`Aut(E)`. Bây giờ ta sẽ định nghĩa nhóm Galois.

.. prf:definition:: Nhóm Galois
    :label: def-galois-group

    Gọi :math:`E` là mở rộng trường của :math:`F`.  Ta nói **nhóm Galois** (hay **Galois group**) của :math:`E` trên :math:`F` là nhóm tất cả tự đẳng cấu của :math:`E` mà cố định phần tử trên :math:`F`, nghĩa là

    .. math:: G(E / F) = \{ \sigma \in Aut(E) : \sigma(\alpha) = \alpha \ \text{với mọi} \ \sigma \in F \}.

Nếu :math:`f(x)` là đa thức trong :math:`F[x]` và :math:`E` là trường phân rã của :math:`f(x)` theo :math:`F` thì ta định nghĩa nhóm Galois của :math:`f(x)` theo :math:`G(E / F)`.

.. prf:example:: 
    :label: exp-automorphism-1

    Liên hợp của số phức xác định bởi ánh xạ quen thuộc

    .. math:: \sigma : a + bi \to a - bi

    là một tự đẳng cấu trên tập các số phức :math:`\mathbb{C}`. Vì :math:`\mathbb{R} \subset \mathbb{C}` và

    .. math:: \sigma(a) = \sigma(a + 0i) = a - 0i = a

    nên ánh xạ :math:`\sigma` thuộc :math:`G(\mathbb{C} / \mathbb{R})`.

.. prf:example:: 
    :label: exp-automorphism-2

    Xét các trường :math:`\mathbb{Q} \subset \mathbb{Q}(\sqrt{5}) \subset \mathbb{Q}(\sqrt{3}, \sqrt{5})`. Khi đó với :math:`a, b \in \mathbb{Q}(\sqrt{5})` thì ánh xạ

    .. math:: \sigma(a + b\sqrt{3}) = a - b\sqrt{3}

    là tự đẳng cấu trên :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})` mà cố định :math:`\mathbb{Q}(\sqrt{5})`.

    Thật vậy, giả sử :math:`a = s + t \sqrt{5}` và :math:`b = u + v \sqrt{5}` với :math:`s, t, u, v \in \mathbb{Q}`. Khi đó

    .. math:: \sigma(a + b\sqrt{3}) = a - b\sqrt{3} = s + t\sqrt{5} - (u + v\sqrt{5}) \sqrt{3} = (s - u\sqrt{3}) + (t - v\sqrt{3}) \sqrt{5}.

    Ta có

    .. math:: a + b\sqrt{3} = (s + u\sqrt{3}) + (t + v\sqrt{3}) \sqrt{5} \in \mathbb{Q}(\sqrt{5})

    khi và chỉ khi :math:`s + u\sqrt{3} \in \mathbb{Q}` và :math:`t + v\sqrt{3} \in \mathbb{Q}`. Nói cách khác :math:`u = v = 0`. Như vậy

    .. math:: \sigma(a + b\sqrt{3}) = \sigma(s + t\sqrt{5}) = s + t\sqrt{5}.

    Phần tử :math:`s + t\sqrt{5} \in \mathbb{Q}(\sqrt{5})` nên :math:`\sigma` cố định các phần tử trên :math:`\mathbb{Q}(\sqrt{5})`.

Tương tự ta cũng có ánh xạ

.. math:: \tau(a + b\sqrt{5}) = a - b\sqrt{5}

là tự đẳng cấu trên :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})` mà cố định :math:`\mathbb{Q}(\sqrt{3})`.

Tuy nhiên ánh xạ hợp :math:`\mu = \sigma \tau` không cố định cả :math:`\mathbb{Q}(\sqrt{3})` lẫn :math:`\mathbb{Q}(\sqrt{5})`.

Chúng ta cũng chứng minh được rằng :math:`\{ id, \sigma, \tau, \mu \}` là nhóm Galois của :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})` trên :math:`\mathbb{Q}` vì các ánh xạ đó cố định phần tử thuộc :math:`\mathbb{Q}` (không chứa căn).

Như vậy nhóm Galois của :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})` có :math:`4` phần tử, tức là :math:`\lvert G(\mathbb{Q}(\sqrt{3}, \sqrt{5}) / \mathbb{Q}) \rvert = 4`. Ở trên phần trường phân rã mình cũng đã chỉ ra rằng :math:`[ \mathbb{Q}(\sqrt{3}, \sqrt{5}) : \mathbb{Q} ] = 4` nên ở đây

.. math:: \lvert G(\mathbb{Q}(\sqrt{3}, \sqrt{5}) / \mathbb{Q}) \rvert = [\mathbb{Q}(\sqrt{3}, \sqrt{5}) : \mathbb{Q}] = 4.

Một điều nữa là trường :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})` cũng chính là không gian vector trên :math:`\mathbb{Q}` với cơ sở là tập :math:`\{ 1, \sqrt{3}, \sqrt{5}, \sqrt{15} \}`. Tập này cũng có :math:`4` phần tử.

Một câu hỏi tự nhiên được đặt ra ở đây: việc số lượng phần tử của các tập hợp ở đây bằng nhau là ngẫu nhiên hay có lý do?

.. prf:remark:: 
    :label: rmk-roots-perm
    
    Cho :math:`E` là một mở rộng trường của :math:`F` và :math:`f(x)` là đa thức trên :math:`F[x]`. Khi đó mỗi tự đẳng cấu trong :math:`G(E / F)` xác định một hoán vị các nghiệm của :math:`f(x)` trên :math:`E`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt

    .. math:: f(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n

    và giả sử :math:`\alpha \in E` là một nghiệm của :math:`f(x)`. Khi đó với tự đẳng cấu :math:`\sigma \in G(E/F)` ta có

    .. math::
        
        0 & = \sigma(0) \\
        & = \sigma(f(\alpha)) \\
        & = \sigma(a_0 + a_1 \alpha + a_2 \alpha^2 + \cdots + a_n \alpha^n) \\
        & = \sigma(a_0) + \sigma(a_1 \alpha) + \sigma(a_2 \alpha^2) + \cdots + \sigma(a_n \alpha^n) \\
        & = \sigma(a_0) + \sigma(a_1) \sigma(\alpha) + \sigma(a_2) \sigma(\alpha^2) + \cdots + \sigma(a_n) \sigma(\alpha^n).
        
    Trong đó hai dòng cuối là từ định nghĩa của tự đẳng cấu. Thêm nữa :math:`\sigma(\alpha^k) = \sigma(\alpha)^k` và do :math:`\sigma \in G(E/F)` nên :math:`\sigma(a_i) = a_i` với mọi :math:`0 \leqslant i \leqslant n`. Như vậy có thể suy ra

    .. math:: 0 = a_0 + a_1 \sigma(\alpha) + a_2 \sigma(\alpha)^2 + \cdots + a_n \sigma(\alpha)^n,

    nói cách khác :math:`\sigma(\alpha)` cũng là nghiệm của :math:`f(x)`.

Cho :math:`E` là mở rộng trường của trường :math:`F`. Hai phần tử :math:`\alpha, \beta \in E` được gọi là **liên hợp** trên :math:`F` nếu chúng có cùng đa thức tối tiểu. Ở đây, đa thức tối tiểu được hiểu là đa thức có bậc nhỏ nhất nhận :math:`\alpha` và :math:`\beta` làm nghiệm.

Ví dụ, trên trường :math:`\mathbb{Q}(\sqrt{2})` thì hai phần tử :math:`\sqrt{2}` và :math:`-\sqrt{2}` là liên hợp trên :math:`\mathbb{Q}` vì chúng đều là nghiệm của đa thức tối giản :math:`x^2 - 2`.

.. prf:remark:: 
    :label: rmk-conj-aut
    
    Nếu :math:`\alpha` và :math:`\beta` liên hợp trên :math:`F` thì tồn tại đẳng cấu :math:`\sigma : F(\alpha) \to F(\beta)` sao cho :math:`\sigma` đồng nhất các phần tử trên :math:`F`.

Khi đó ta có định lí quan trọng sau về số phần tử của nhóm Galois. Phần chứng minh hiện tại mình bỏ qua vì cần một vài bổ đề khá dài.

.. prf:theorem:: 
    :label: thm-galois-group-extension

    Đặt :math:`f(x)` là đa thức trên :math:`F[x]` và giả sử :math:`E` là trường phân rã của :math:`f(x)` trên :math:`F`. Nếu :math:`f(x)` không có nghiệm bội thì

    .. math:: \lvert G(E/F) \rvert = [E : F].
