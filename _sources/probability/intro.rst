Xác suất thống kê
*****************

Xác suất là gì?
===============

.. prf:definition:: Định nghĩa cổ điển của xác suất
    :label: def-classical-prob

    Định nghĩa thống kê của xác suất nói rằng, giả sử trong một phép thử có :math:`n` khả năng có thể xảy ra. Xét một biến cố :math:`A` xảy ra khi thực hiện phép thử có :math:`k` khả năng xảy ra. Khi đó xác suất của biến cố :math:`A` kí hiệu là :math:`P(A)` và được tính:

    .. math:: P(A) = \frac{k}{n}.

Dễ thấy, do biến cố :math:`A` là một trường hợp nhỏ trong tổng thể tất cả trường hợp khi thực hiện phép thử, nên :math:`0 \leqslant k \leqslant n`. Nghĩa là:

.. math:: 0 \leqslant P(A) \leqslant 1

với mọi biến cố :math:`A` bất kì.

.. prf:example:: 
    :label: exp-classical-prob-coin

    Xét phép thử tung hai đồng xu. Gọi :math:`A` là biến cố hai đồng xu cùng mặt.

    Ta kí hiệu :math:`S` là đồng xu sấp, :math:`N` là đồng xu ngửa. Khi đó các trường hợp có thể xảy ra của phép thử là :math:`S-S`, :math:`S-N`, :math:`N-S`, :math:`N-N` (:math:`4` trường hợp).

    Trong khi đó, các trường hợp có thể xảy ra của biến cố :math:`A` là :math:`S-S`, :math:`N-N` (:math:`2` trường hợp).

    Kết luận: :math:`P(A) = \dfrac{2}{4} = \dfrac{1}{2}`.

Chúng ta gọi tập hợp tất cả các trường hợp khi thực hiện phép thử là **không gian mẫu** và kí hiệu là :math:`\Omega`. Mỗi phần tử trong không gian mẫu được gọi là **biến cố sơ cấp**. Trong ví dụ trên:

.. math:: \Omega = \{ S-S, S-N, N-S, N-N \}.
    
Tập hợp các trường hợp có thể xảy ra của biến cố gọi là **không gian biến cố** và kí hiệu là :math:`\Omega_A`. Trong ví dụ trên, :math:`\Omega_A = \{ S-S, N-N \}`.
    
Như vậy, :math:`P(A) = \dfrac{\lvert\Omega_A\vert}{\lvert\Omega\rvert}`.

.. prf:example:: 
    :label: exp-classical-prob-dice

    Tung hai con súc sắc cân đối và đồng chất. Tính xác suất tổng số nút của hai con súc sắc bằng :math:`4`.

    Việc tung mỗi con súc sắc có :math:`6` trường hợp. Do đó :math:`\lvert\Omega\rvert = 6^2 = 36`.

    Gọi :math:`A` là biến cố tổng số nút của hai con súc sắc bằng :math:`4`. Ta có các trường hợp là :math:`4=1+3=3+1=2+2` (:math:`3` trường hợp).

    Như vậy :math:`\lvert\Omega_A\rvert = 3` và :math:`P(A) = \dfrac{3}{36} = \dfrac{1}{12}`.

Ba tiên đề về sự nhất quán của xác suất
---------------------------------------

**Tiên đề 1.** Nếu :math:`A` là một sự kiện và kí hiệu :math:`P(A)` là **xác suất của** :math:`A` thì:

.. math:: 0 \leqslant P(A) \leqslant 1.

**Tiên đề 2.** Nếu :math:`A` là một sự kiện và kí hiệu :math:`\bar{A}` là sự kiện phủ định của :math:`A` thì:

.. math:: P(A) + P(\bar{A}) = 1.

**Tiên đề 3.** Với hai sự kiện :math:`A` và :math:`B`, nếu hai sự kiện :math:`A` và :math:`B` không thể cùng xảy ra thì xác suất của sự kiện "xảy ra :math:`A` hoặc :math:`B`" bằng tổng các xác suất của :math:`A` và :math:`B`:

.. math:: P(A \cap B) = 0 \Rightarrow P(A \cup B) = P(A) + P(B).

Không gian xác suất
-------------------

.. prf:definition:: Không gian xác suất
    :label: def-prob-space

    Một **không gian xác suất** là một tập hợp :math:`\Omega` cùng với:

    1) Một họ :math:`\mathcal{S}` các tập con của :math:`\Omega`, thỏa mãn các tính chất sau:
    
       - :math:`\Omega \in \mathcal{S}`;
       - nếu :math:`A, B \in \mathcal{S}` thì :math:`A \cup B \in \mathcal{S}`, :math:`A \cap B \in \mathcal{S}` và :math:`\bar{A} = \Omega \setminus A \in \mathcal{S}`.

    Một họ như vậy được gọi là một **đại số** các tập con của :math:`\Omega`.

    Trong trường hợp :math:`\Omega` là tập có vô hạn phần tử thì ta cần thêm điều kiện sau: nếu :math:`A_i`, :math:`i = 1, 2, 3, \ldots` là một dãy vô hạn các phần tử của :math:`\mathcal{S}` thì hợp :math:`\bigcup\limits_{i=1}^\infty A_i` cũng thuộc họ :math:`\mathcal{S}`.

    Với điều kiện thêm này, :math:`\mathcal{S}` được gọi là một **sigma-đại số**. Các phần tử của :math:`\mathcal{S}` được gọi là tập hợp con **đo được** của không gian xác suất.

    2) Một hàm số thực :math:`P : \mathcal{S} \to \mathbb{R}`, được gọi là **phân bố xác suất** hay **độ đo xác suất** trên :math:`\Omega`, thỏa mãn các tính chất sau:

       i) với mọi :math:`A \in \mathcal{S}` ta có:

       .. math:: 0 \leqslant P(A) \leqslant 1

       ii)

       .. math:: P(\emptyset) = 0, P(\Omega) = 1

       iii) nếu :math:`A \cap B = \emptyset` thì:

       .. math:: P(A \cup B) = P(A) + P(B).

    Tổng quát hơn, nếu :math:`A_i`, với :math:`i = 1, 2, 3, \ldots` là một dãy các tập hợp con đo được và chúng đôi một không giao nhau thì:

    .. math:: P\left(\bigcup_i A_i\right) = \sum_{i} P(A_i).

Một số lưu ý:

1. Không gian xác suất :math:`\Omega` còn được gọi là **không gian mẫu** (hay **sample space**) và nó là mô hình toán học trừu tượng cho vấn đề tính toán xác suất đang được quan tâm. Mỗi phần tử của :math:`\Omega` có thể được gọi là một **sự kiện thành phần** (hay **biến cố sơ cấp**, **elementary event**). Nếu :math:`A` là một phần tử trong :math:`\Omega` thì ta cũng có thể viết :math:`P(A)` và hiểu là :math:`P(\{ A \})`, trong đó :math:`\{ A \}` là tập con của :math:`\Omega` chứa duy nhất một phần tử :math:`A`. Mỗi sự kiện là một tập con của :math:`\Omega` nên có thể chứa nhiều (thậm chí vô hạn) sự kiện thành phần. Không nhất thiết tập con nào của :math:`\Omega` cũng đo được (nằm trong họ :math:`\mathcal{S}`) và chúng ta sẽ chỉ quan tâm đến các tập con đo được.
2. Trong toán học, một đại số là một tập hợp với các phép tính cộng, trừ và nhân (vành). Các tính chất của họ :math:`\mathcal{S}` trong định nghĩa không gian xác suất khiến nó là một đại số theo nghĩa:

   - phần tử :math:`0` trong :math:`\mathcal{S}` là tập rỗng;
   - phần tử đơn vị trong :math:`\mathcal{S}` là tập :math:`\Omega`;
   - phép nhân trong :math:`\mathcal{S}` là phép giao :math:`A \times B = A \cap B`;
   - phép cộng trong :math:`\mathcal{S}` là phép
 
   .. math:: A + B = (A \cup B) \setminus (A \cap B) = (A \setminus B) \cup (B \setminus A).

Đại số này có đặc số (số đặc trưng, characteristic) bằng :math:`2`, tức là :math:`2 A = A + A = 0` với mọi :math:`A`. Vì lý do này mà phép cộng và phép trừ là một. Chúng ta muốn :math:`\mathcal{S}` là một đại số để thuận tiện thực hiện tính toán số học.

1. Đẳng thức :math:`P\left(\bigcup\limits_i A_i\right) = \sum\limits_{i} P(A_i)` được gọi là **tính chất sigma** của xác suất. Tính chất sigma là **tính chất cộng vô hạn**: khi có một dãy vô hạn các tập con không giao nhau thì xác suất của hợp của chúng cũng bằng tổng vô hạn của các xác suất của các tập con. Tính chất sigma chính là tính chất cho phép chúng ta lấy giới hạn cho việc tính toán xác suất.

Ví dụ, nếu :math:`A_1 \subset A_2 \subset \ldots` là một dãy tăng các tập con của :math:`\Omega` và :math:`A = \lim\limits_{n \to \infty} A_n = \bigcup\limits_{n=1}^\infty A_n`, thì ta có thể viết :math:`P(A) = \lim\limits_{n \to \infty} P(A_n)` bởi vì:

.. math:: 
    
    P(A) & = P(A_1 \cup \bigcup_{n=1}^\infty (A_{n+1} \setminus A_n)) = P(A_1) + \sum_{n=1}^\infty P(A_{n+1} \setminus A_n) \\
    & = P(A_1) + \lim_{n \to \infty} P(A_{n+1} \setminus A_n) = P(A_1) + \lim_{n \to \infty}(P(A_{n+1}) - P(A_1)).

Đẳng thức :math:`P\left(\bigcup\limits_i A_i\right) = \sum\limits_{i} P(A_i)` không được suy ra từ :math:`P(A \cup B) = P(A) + P(B)` mà là một tiên đề trong xác suất. Tiên đề này được đưa ra bởi nhà toán học người Nga Andrei Nikolaievich Kolmogorov.

Phép cộng xác suất mở rộng
--------------------------

Ở tiên đề 3 bên trên, hai biến cố khi đó được gọi là **xung khắc**, nghĩa là nếu biến cố này xảy ra thì biến cố kia chắc chắn không xảy ra. Nói cách khác giao của chúng bằng rỗng.

Ta còn có thể kí hiệu giao hai biến cố :math:`P(A \cap B)` là :math:`P(AB)`.
    
Một trường hợp đơn giản nhất của hai biến cố xung khắc là **biến cố đối**.

.. prf:example:: 
    :label: exp-expand-sum-prob

    Tung một đồng xu và gọi :math:`A` là biến cố đồng xu ra mặt ngửa. Khi đó biến cố đối của :math:`A`, kí hiệu là :math:`\bar{A}` là biến cố ra mặt sấp. Ở đây :math:`A \cup \bar{A} = \Omega` và :math:`A \cap \bar{A} = \emptyset`.

    Từ đó:

    .. math:: 1 = P(\Omega) = P(A \cup \bar{A}) = P(A) + P(\bar{A}),

    nói cách khác :math:`P(\bar{A}) = 1 - P(A)`.

Xét hai tập hợp :math:`A` và :math:`B`. Số phần tử của phép hợp hai tập hợp trong trường hợp tổng quát được tính như sau: 

.. math:: \lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert.
    
Tương tự, xác suất của phép cộng xác suất đối với hai biến cố có giao khác rỗng là: 

.. math:: P(A \cup B) = P(A) + P(B) - P(A B).

Xét các tập hợp :math:`A_1`, :math:`A_2`, ..., $A_n$. Khi đó, số phần tử khi hợp các tập hợp này là:

.. math:: |A_1 \cup A_2 \cup \cdots \cup A_n| & = |A_1| + |A_2| + \cdots + |A_n| - \sum_{i, j}|A_i \cap A_j| \\ & + \sum_{i, j, k} |A_i \cap A_j \cap A_k| + \cdots \\ & = \sum_{i=1}^n (-1)^{i+1} \sum_{j_1, j_2, \cdots, j_i} |A_{j_1} \cap A_{j_2} \cap \cdots \cap A_{j_i} |.

Tương tự, ta có phép cộng xác suất:

.. prf:theorem:: Phép cộng xác suất mở rộng
    :label: thm-expand-sum-prob

    .. math:: P(A_1 \cup A_2 \cup \cdots \cup A_n) = \sum_{i=1}^n (-1)^{i+1} \sum_{j_1, j_2, \cdots, j_i} P(A_{j_1} \cap A_{j_2} \cap \cdots \cap A_{j_i}).

Mô hình xác suất với vô hạn các sự kiện
---------------------------------------

.. prf:example:: Phân phối Poisson
    :label: exp-poisson-dist
    
    Giả sử tỉ lệ số khách hàng trung bình đến siêu thị trong một đơn vị thời gian cố định là :math:`\lambda`.
    
    Phân phối Poisson :math:`P(n) = e^{-\lambda} \cdot \dfrac{\lambda^n}{n!}` thể hiện xác suất có :math:`n` khách hàng đến siêu thị theo tỉ lệ thời gian :math:`\lambda`. 

Ở phân phối Poisson, :math:`n` nhận tất cả giá trị nguyên không âm :math:`0`, :math:`1`, ... cũng như thỏa điều kiện:

.. math:: \sum_{n=0}^{\infty} P(n) = \sum_{n=0}^\infty e^{-\lambda} \cdot \frac{\lambda^n}{n!} = e^{-\lambda} \sum_{n=0}^\infty \frac{\lambda^n}{n!} = e^{-\lambda} \cdot e^\lambda = 1.

Ở biến đổi trên, :math:`\sum\limits_{n=0}^\infty \frac{\lambda^n}{n!} = e^\lambda` là khai triển Taylor.

.. prf:example:: 
    :label: exp-eq-dist
    
    Giả sử ta biết rằng có một xe hơi :math:`X` đang đậu trên một khúc phố :math:`Z` và ta quan tâm đến vị trí của :math:`X` trên khúc phố đó. Ta có thể mô hình :math:`X` bằng một điểm và :math:`Z` là một đoạn thẳng và lấy đoạn thẳng đó làm không gian xác suất :math:`\Omega = [a; b]`, :math:`a, b \in \mathbb{R}`, :math:`a < b` (mô hình xác suất liên tục này có lực lượng continuum, không đếm được).
    
    Sự kiện "xe hơi đỗ chỗ nào đó trên khúc phố" chuyển thành sự kiện "điểm :math:`x` nằm trong một đoạn thẳng con nào đó trên đoạn thẳng :math:`\Omega = [a; b]`".
    
    Ta có thể chọn phân bố xác suất đều trên :math:`\Omega = [a; b]` theo nghĩa sau: xác suất mỗi đoạn thẳng con trên :math:`\Omega` tỷ lệ thuận với độ dài của đoạn thẳng con đó, hay :math:`P([c; d]) = (d - c) / (b - a)`.

Ánh xạ giữa các không gian xác suất
-----------------------------------

.. prf:definition:: Ánh xạ bảo toàn xác suất
    :label: def-ax-bao-toan-prob

    Một ánh xạ :math:`\phi : (\Omega_1, P_1) \to (\Omega_2, P_2)` từ một không gian xác suất :math:`(\Omega_1, P_1)` vào một không gian xác suất :math:`(\Omega_2, P_2)` được gọi là một **ánh xạ bảo toàn xác suất** nếu nó bảo toàn độ đo xác suất, nghĩa là với mọi tập con :math:`B \subset \Omega_2` đo được, ta có:

    .. math:: P_1(\phi^{-1}(B)) = P_2(B).

Hơn nữa, nếu :math:`\phi` là một song ánh modulo những tập có xác suất bằng :math:`0`, nghĩa là tồn tại các tập con :math:`A \in \Omega_1`, :math:`B \in \Omega_2` sao cho :math:`P_1(A) = P_2(B) = 0` và :math:`\phi : \Omega_1 \setminus A \to \Omega_2 \setminus B` là song ánh bảo toàn xác suất, thì :math:`\phi` được gọi là **đẳng cấu xác suất**, và ta nói rằng :math:`(\Omega_1, P_1)` đẳng cấu xác suất với :math:`(\Omega_2, P_2)`.

.. prf:theorem:: 
    :label: thm-ax-bao-toan-prob

    Nếu :math:`(\Omega_1, P_1)` là một không gian xác suất và :math:`\phi : \Omega_1 \to \Omega_2` là một ánh xạ tùy ý thì tồn tại một độ đo xác suất :math:`P_2` sao cho ánh xạ :math:`\phi : (\Omega_1, P_1) \to (\Omega_2, P_2)` là ánh xạ bảo toàn xác suất.

Ta xây dựng :math:`P_2` theo công thức: với mỗi tập con :math:`B \subset \Omega_2`, nếu tồn tại :math:`P_1(\phi^{-1}(B))` thì ta đặt

.. math:: P_2(B) = P_1(\phi^{-1}(B)).

Độ đo xác suất :math:`P_2` như trên gọi là **push-forward** của :math:`P_1` qua ánh xạ :math:`\phi`, hay **phân bố xác suất cảm sinh** từ :math:`P_1` qua ánh xạ :math:`\phi`.

**Câu hỏi:** chứng minh rằng quan hệ đẳng cấu xác suất giữa các không gian xác suất là một quan hệ tương đương.

Giải: vì :math:`\phi` là song ánh, đối với tính phản xạ chúng ta lấy ánh xạ đồng nhất, tính đối xứng thì ánh xạ ngược của song ánh (vẫn là song ánh), bắc cầu thì ta hợp hai song ánh vẫn là song ánh.

Tích của các không gian xác suất
--------------------------------

Nếu :math:`(\Omega_1, P_1)` và :math:`(\Omega_2, P_2)` là hai không gian xác suất thì tích :math:`\Omega_1 \times \Omega_2` cũng có một độ đo xác suất :math:`P` được xác định bởi :math:`P_1` và :math:`P_2` bằng công thức: nếu :math:`A_1 \subset \Omega_1` và :math:`A_2 \subset \Omega_2` nằm trong các sigma-đại số tương ứng của :math:`P_1` và :math:`P_2` thì:

.. math:: P(A_1 \times A_2) = P_1(A_1) \times P_2(A_2).

Sigma-đại số của :math:`P` chính là sigma-đại số sinh bởi các tập con của :math:`\Omega_1 \times \Omega_2` có dạng :math:`A_1 \times A_2` như trên.

Tương tự ta có thể định nghĩa tích trực tiếp của :math:`n` không gian xác suất hay thập chí một dãy vô hạn các không gian xác suất.

.. prf:theorem:: 
    :label: thm-prod-of-prob-space

    Hai phép chiếu tự nhiên từ tích :math:`(\Omega_1, P_1) \times (\Omega_2, P_2)` của hai không gian xác suất xuống :math:`(\Omega_1, P_1)` và :math:`(\Omega_2, P_2)` là hai ánh xạ bảo toàn xác suất.

Xác suất có điều kiện
=====================

Xác suất có điều kiện
---------------------

.. prf:definition:: Xác suất có điều kiện
    :label: def-prob-conditional

    Xét hai biến cố :math:`A` và :math:`B`. Khi đó xác suất xảy ra của biến cố :math:`B` với điều kiện biến cố :math:`A` xảy ra là: 

    .. math:: P(A \vert B) = \frac{P(AB)}{P(B)}.
    
Ý nghĩa của công thức trên có thể hiểu là, việc biến cố :math:`A` xảy ra dựa trên cơ sở biến cố :math:`B` đã xảy ra, do đó không gian mẫu sẽ giảm xuống còn :math:`B` và biến cố giảm còn :math:`AB`.

Dựa trên định nghĩa của xác suất có điều kiện có thể đưa ra nhận xét sau.

.. prf:remark:: 
    :label: rmk-prob-conditional

    Từ công thức trên có thể thấy sự tương đương:

    .. math:: P(AB) = P(B) \cdot P(A \vert B) = P(A) \cdot P(B \vert A).

Nhận xét trên cho thấy sự liên hệ của hai biến cố. Nói cách khác việc xảy ra của biến cố này sẽ ảnh hưởng đến biến cố kia và ngược lại.

Tổng quát, nếu :math:`n` biến cố :math:`A_i`, :math:`i = 1, \ldots, n` không độc lập thì:

.. math:: P(A_1 A_2 \cdots A_n) = & P(A_1) \cdot P(A_2 \vert A_1) \cdot P(A_3 \vert A_2 A_1) \cdots \\ & P(A_n \vert A_1A_2 \cdots A_{n-1}).

Sử dụng nhận xét trên có thể chứng minh công thức này bằng quy nạp. Về mặt ý nghĩa, biến cố :math:`A_1` xảy ra đầu tiên. Tiếp theo đó :math:`A_2` xảy ra với điều kiện :math:`A_1` đã xảy ra. Tiếp theo nữa, :math:`A_3` xảy ra khi cả :math:`A_1` và :math:`A_2` xảy ra, chính là :math:`A_1 A_2`.

Tương tự như vậy, :math:`A_i` xảy ra với điều kiện tất cả :math:`A_1`, ..., :math:`A_{i-1}` đều đã xảy ra, là biến cố giao :math:`A_1 \ldots A_{i_1}`.

Cũng từ nhận xét trên, các biến cố có vai trò như nhau nên việc đổi vị trí không thay đổi kết quả :math:`P(A_1 \ldots A_n)`.

Sự độc lập và phụ thuộc của các sự kiện
---------------------------------------

Nếu hai biến cố không ảnh hưởng việc xảy ra của nhau thì ta gọi là biến cố độc lập.

.. prf:definition:: Biến cố độc lập
    :label: def-independent-event

    Hai biến cố được gọi là **độc lập** nếu việc xảy ra của biến cố này không ảnh hưởng đến việc xảy ra của biến cố kia, hay:

    .. math:: P(A) = P(A \vert B) = P(AB) / P(B).

Viết cách khác là:

.. math:: P(AB) = P(A) \cdot P(B).

Khi đó, giả sử ta có một họ :math:`\mathcal{M}` các sự kiện.

.. prf:definition:: Họ các sự kiện độc lập
    :label: def-set-of-ind-event

    Họ :math:`\mathcal{M}` được gọi là một **họ các sự kiện độc lập** nếu như với bất kì số tự nhiên :math:`k` nào và bất kì sự kiện :math:`A_i`, ..., :math:`A_k` khác nhau nào trong họ :math:`\mathcal{M}` ta cũng có:

    .. math:: P(A_1 \cdots A_k) = P(A_1) \cdot P(A_2) \cdots P(A_k).

.. prf:remark:: 
    :label: rmk-set-of-ind-event
    
    Nếu ta có một họ các sự kiện độc lập thì các sự kiện trong họ độc lập đôi một với nhau. Nhưng ngược lại chưa chắc: có những họ không độc lập mà trong đó các sự kiện độc lập từng đôi một với nhau!

Công thức xác suất toàn phần
----------------------------

.. prf:definition:: Hệ biến cố đầy đủ
    :label: def-full-set-event

    Xét phép thử có không gian mẫu là :math:`\Omega`. Một hệ các biến cố :math:`A_1`, :math:`A_2`, ..., :math:`A_n` là một **hệ biến cố đầy đủ** (hoặc **phân hoạch**) của :math:`\Omega` nếu chúng thỏa các điều kiện:

    - :math:`A_1 \cup A_2 \cup \cdots \cup A_n = \Omega`;
    - :math:`A_i \cap A_j = \emptyset` với mọi :math:`i \neq j`.

.. prf:example:: 
    :label: exp-full-set-event

    Một hệ biến cố đầy đủ đơn giản là :math:`\Omega = \{ A, \bar{A} \}` gồm biến cố :math:`A` và biến cố đối của :math:`A` là :math:`\bar{A}`.

Khi có một hệ biến cố đầy đủ, ta có thể tính xác suất của một biến cố bất kì nếu biết xác suất của các biến cố trong hệ biến cố đầy đủ và xác suất có điều kiện tương ứng.

.. prf:theorem:: Công thức xác suất toàn phần
    :label: thm-full-set-event

    Gọi :math:`A_1`, :math:`A_2`, ..., :math:`A_n` là một hệ biến cố đầy đủ của :math:`\Omega`. Khi đó, với biến cố :math:`B` bất kì trong phép thử:

    .. math:: P(B) = P(A_1) \cdot P(B \vert A_1) + \cdots + P(A_n) \cdot P(B \vert A_n).
    
.. prf:example:: 
    :label: exp-full-set-event-sol

    **Đề bài.** Trong một lớp học có :math:`15` bạn nam và :math:`10` bạn nữ. Trong đó có :math:`5` bạn nam biết chơi bóng chuyền và :math:`2` bạn nữ biết chơi bóng chuyền. Chọn ngẫu nhiên một bạn trong lớp, tính xác suất bạn đó biết chơi bóng chuyền.

    **Giải.** Bài này có thể giải đơn giản bằng việc xác định số bạn biết chơi bóng chuyền là :math:`5 + 2 = 7` (:math:`5` nam và :math:`2` nữ), trong khi không gian mẫu là :math:`15 + 10 = 25` nên kết quả là :math:`\dfrac{7}{25}`.

    Bài này nhằm đưa ra cái nhìn đơn giản về việc xác định điều kiện để thành lập hệ biến cố đầy đủ và giải bài toán. 

    Ở đây chúng ta cần tìm một hệ biến cố đầy đủ. Gọi :math:`A_1` là biến cố bạn được chọn là nam và :math:`A_2` là biến cố bạn được chọn là nữ.
    
    Như vậy :math:`\Omega = \{ A_1, A_2 \}` thỏa định nghĩa về hệ biến cố đầy đủ.
    
    Dễ thấy :math:`P(A_1) = \dfrac{15}{25} = \dfrac{3}{5}` và :math:`P(A_2) = \dfrac{10}{25} = \dfrac{2}{5}`.

    Tiếp theo, gọi :math:`B` là biến cố bạn được chọn biết chơi bóng chuyền.

    Khi đó, xác suất một bạn biết chơi bóng chuyền với điều kiện bạn đó là nam bằng :math:`P(B \vert A_1) = \dfrac{5}{15} = \dfrac{1}{3}`.

    Tương tự, xác suất một bạn biết chơi bóng chuyền với điều kiện bạn đó là nữ bằng :math:`P(B \vert A_2) = \dfrac{2}{10} = \dfrac{1}{5}`.

    Theo công thức xác suất toàn phần, xác suất bạn được chọn ngẫu nhiên biết chơi bóng chuyền là :math:`P(B)` và ta tính được

    .. math:: P(B) = P(A_1) \cdot P(B \vert A_1) + P(A_2) \cdot P(B \vert A_2) = \frac{3}{5} \cdot \frac{1}{3} + \frac{2}{5} \cdot \frac{1}{5} = \frac{7}{25}.

Ở đây, nếu chúng ta đảo điều kiện đề bài, ví dụ như bạn được chọn ngẫu nhiên là nữ *với điều kiện bạn đó biết chơi bóng chuyền* thì sao? Đề bài lúc này tương đương việc tính :math:`P(A_2 \vert B)`.

Để trả lời câu hỏi này chúng ta sử dụng công thức Bayes.

Công thức Bayes
---------------

.. prf:theorem:: Công thức Bayes
    :label: thm-bayes

    Xét hệ biến cố đầy đủ :math:`\{ A_1, A_2, \ldots, A_n \}` của không gian xác suất. Với biến cố :math:`B` bất kì ta có **công thức Bayes**:

    .. math:: P(A_i | B) = \frac{P(A_i) P(B | A_i)}{\displaystyle{\sum_{j=1}^n P(A_j) P(B | A_j)}}

    với mọi :math:`1 \leqslant i \leqslant n`.

Công thức Bayes thực ra là công thức xác suất có điều kiện :math:`P(B) \cdot P(A \vert B) = P(A) \cdot P(B \vert A)`, trong đó ta thay :math:`P(B)` bởi công thức xác suất toàn phần.

Như vậy, để trả lời cho câu hỏi trên, ta có

.. math:: P(A_2 \vert B) = \dfrac{P(A_2) \cdot P(B \vert A_2)}{P(B)} = \dfrac{\dfrac{2}{5} \cdot \dfrac{1}{5}}{\dfrac{7}{25}} = \dfrac{2}{7}.

Biến ngẫu nhiên
===============

Biến ngẫu nhiên
---------------

Xét phép thử với không gian mẫu :math:`\Omega`. Với mỗi biến cố sơ cấp :math:`\omega \in \Omega` ta liên kết với một số thực :math:`\xi(\omega) \in \mathbb{R}` thì :math:`\xi` được gọi là **biến ngẫu nhiên** (hay **random variable**, BNN).

.. prf:definition:: Biến ngẫu nhiên
    :label: def-random-var

    **Biến ngẫu nhiên** :math:`\xi` của một phép thử với không gian mẫu :math:`\Omega` là ánh xạ: 

    .. math:: \xi = \xi (\omega), \quad \omega \in \Omega.

Giá trị :math:`\xi(\omega)` được gọi là một giá trị của biến ngẫu nhiên :math:`\xi`.

- Nếu :math:`\xi(\omega)` là một tập hữu hạn :math:`\{ \xi_1, \xi_2, \ldots, \xi_n \}` hay tập vô hạn đếm được thì :math:`\xi` được gọi là **biến ngẫu nhiên rời rạc**.
- Nếu :math:`\xi(\omega)` là một khoảng của :math:`\mathbb{R}` hay toàn bộ :math:`\mathbb{R}` thì :math:`\xi` được gọi là **biến ngẫu nhiên liên tục**.

Phân bố xác suất của biến ngẫu nhiên
------------------------------------

.. prf:definition:: Hàm phân phối xác suất
    :label: def-func-dist

    **Hàm phân phối** của biến ngẫu nhiên :math:`\xi` là hàm số :math:`F(x)`, xác định bởi:

    .. math:: F(x) = P(\xi \leqslant x), \quad x \in \mathbb{R}.
    
Ở đây ta viết gọn :math:`P(\xi \leqslant x)` từ :math:`P(\{ \omega: \xi(\omega) \leqslant x \})`. Tập hợp :math:`\{ \omega: \xi(\omega) \leqslant x \}` có thể không thuộc một biến cố nào, do đó có thể là tập rỗng (ứng với xác suất là :math:`0`).

Tính chất của hàm phân phối
---------------------------

**Tính chất 1.** Hàm phân phối :math:`F(x)` không giảm trên mọi đoạn thẳng.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`x_2 > x_1`. Ta thấy rằng

    .. math:: \{ \xi \leqslant x_2 \} = \{ \xi \leqslant x_1 \} + \{ x_1 < \xi \leqslant x_2 \}.

    Do đó nếu ta lấy xác suất thì cũng có

    .. math:: P(\xi \leqslant x_2) = P(\xi \leqslant x_1) + P(x_1 < \xi \leqslant x_2).

    Xác suất luôn không âm, hay :math:`P(x_1 < \xi \leqslant x_2) \geqslant 0`, suy ra :math:`P(\xi \leqslant x_2) \geqslant P(\xi \leqslant x_1)`, hay :math:`F(x_2) \geqslant F(x_1)`.

**Tính chất 2.** :math:`\lim\limits_{x \to -\infty} F(x) = 0`.

**Tính chất 3.** :math:`\lim\limits_{x \to +\infty} F(x) = 1`.

**Tính chất 4.** Hàm phân phối :math:`F(x)` liên tục phải trên toàn trục số.

Để chứng minh các tính chất 2, 3, 4 chúng ta cần các tiên đề của sự liên tục (continunity axioms) và sẽ không đề cập ở đây.

Biến ngẫu nhiên rời rạc
-----------------------

Cho BNN rời rạc

.. math:: \xi = \xi(\omega), \xi = \{ a_1, a_2, \ldots, a_n, \ldots \}.
    
Giả sử :math:`a_1 < a_2 < \cdots < a_n < \cdots` với xác suất tương ứng là :math:`P(\xi = a_i) = p_i`, :math:`i = 1, 2, \ldots`

Ta có thể biểu diễn biến ngẫu nhiên và xác suất tương ứng của nó bằng bảng phân phối xác suất của :math:`\xi`.

+-------------+-------------+-------------+-----+-------------+-----+
| :math:`\xi` | :math:`a_1` | :math:`a_2` | ... | :math:`a_n` | ... |
+=============+=============+=============+=====+=============+=====+
| :math:`P`   | :math:`p_1` | :math:`p_2` | ... | :math:`p_n` | ... |
+-------------+-------------+-------------+-----+-------------+-----+

Rõ ràng rằng :math:`p_n \geqslant 0` với mọi :math:`n`. Hơn nữa:

.. math:: \sum_{n=1}^\infty p_n = 1.

Không gian mẫu lúc này là hợp của các tập biến ngẫu nhiên rời rạc:

.. math:: \Omega = \{ \xi = a_1 \} \cup \{ \xi = a_2 \} \cup \cdots

Các biến ngẫu nhiên xung khắc nhau (vì :math:`\xi` không thể nhận hai giá trị khác nhau cùng lúc), do đó xác suất cả không gian mẫu là

.. math:: 1 = P(\Omega) = P(\xi = a_1) + P(\xi = a_2) + \cdots = p_1 + p_2 + \cdots

.. prf:definition:: Phân bố Bernoulli
    :label: def-bernoulli-dist
    
    Phân bố xác suất cho không gian sinh bởi đúng một sự kiện :math:`A` và phủ định của nó :math:`\bar{A}`, hay :math:`\Omega = \{ A, \bar{A} \}`. Nếu xác suất xảy ra sự kiện :math:`A` là :math:`p` thì xác suất xảy ra :math:`\bar{A}` là :math:`1-p`.

Phân bố Bernoulli được đặt tên theo nhà toán học Jacob Bernoulli (1654-1705).

.. prf:definition:: Phân phối nhị thức
    :label: def-binom-dist

    Biến ngẫu nhiên :math:`\xi` được gọi là có **phân phối nhị thức** với tham số :math:`p`, :math:`n`, với :math:`p \in [0; 1]` và :math:`n` là số tự nhiên, nếu :math:`\xi` nhận các giá trị :math:`0`, :math:`1`, ..., :math:`n` và

    .. math:: P(\xi = k) = C^k_n p^k q^{n-k}, \quad k = 0, 1, \ldots, n,  

    ở đây :math:`q = 1 - p`.

.. prf:example:: 
    :label: exp-binom-dist

    Một bài kiểm tra có :math:`100` câu hỏi trắc nghiệm bốn đáp án. Xác suất chọn ngẫu nhiên đúng đáp án của mỗi câu hỏi thì giống nhau và bằng :math:`\dfrac{1}{4}`.

    Ở đây xác suất chọn ngẫu nhiên đúng đáp án của một câu hỏi bất kì là :math:`p = \dfrac{1}{4}`, và số lượng câu hỏi là :math:`n = 100`.

    Gọi :math:`\xi` là biến ngẫu nhiên số câu hỏi trả lời đúng. Khi đó :math:`\xi` nhận các giá trị :math:`0`, :math:`1`, ..., :math:`100`.

    Do đó bài toán này có phân phối nhị nhức và

    .. math:: P(\xi = k) = C^k_{100} \left(\dfrac{1}{4}\right)^k \left(\dfrac{3}{4}\right)^{100-k}.

.. prf:definition:: Phân bố xác suất đều
    :label: def-eq-dist

    Phân bố xác suất :math:`P` trên không gian xác suất hữu hạn với :math:`N` phần tử :math:`\Omega = \{ A_1, \ldots, A_n \}` được gọi là **phân bố xác suất đều** nếu như

    .. math:: P(A_1) = \cdots = P(A_n) = 1 / N.

Khái niệm phân bố đều không mở rộng được lên các không gian xác suất có số phần tử là vô hạn và đếm được vì :math:`1` chia vô cùng bằng :math:`0` mà tổng của chuỗi vô hạn số :math:`0` vẫn bằng :math:`0` chứ không bằng :math:`1`.

.. prf:remark:: 
    :label: rmk-properties-eq-dist

    Phân bố xác suất đều có **tính đối xứng**, **cân bằng** hay **hoán vị được** của các sự kiện thành phần.

.. prf:definition:: Phân phối Poisson
    :label: def-poisson-dist

    Biến ngẫu nhiên :math:`\xi` được gọi là có **phân phối Poisson** với tham số :math:`\lambda`, nếu :math:`\xi` nhận các giá trị :math:`0`, :math:`1`, ..., :math:`n` và

    .. math:: P(\xi = k) = \dfrac{\lambda^k \cdot e^{-\lambda}}{k!}, \quad k = 0, 1, \ldots, n.
    
Tham số :math:`\lambda` thể hiện số lần trung bình mà một sự kiện xảy ra trong một khoảng thời gian nhất định. Khi đó, nếu một biến ngẫu nhiên có số lần xuất hiện trung bình của một sự kiện trong thời gian :math:`t` thì nó có phân phối Poisson với tham số :math:`\lambda t`, với :math:`\lambda` là số lần trung bình trong một đơn vị thời gian.

Biến ngẫu nhiên liên tục
------------------------

.. prf:definition:: Biến ngẫu nhiên liên tục
    :label: def-cont-random-var

    Biến ngẫu nhiên :math:`\xi` được gọi là **liên tục**, nếu nó nhận giá trị tại mọi điểm thuộc một đoạn liên tục nào đó trên trục số, và tồn tại một hàm số không âm :math:`p(x)` sao cho với mọi đoạn $[a ,b]$ (hữu hạn hoặc vô hạn) ta có

    .. math:: P(a \leqslant \xi \leqslant b) = \int\limits_{a}^{b} p(x)\, dx
    
    Hàm :math:`p(x)` được gọi là **hàm mật độ** của biến ngẫu nhiên :math:`\xi`.

Tương tự biến ngẫu nhiên rời rạc, :math:`p(x) \geqslant 0` với mọi :math:`x \in \mathbb{R}` và khi hai cận là vô cực thì biến ngẫu nhiên bao quát toàn bộ không gian mẫu, nghĩa là

.. math:: \int\limits_{-\infty}^{+\infty} p(x)\, dx = 1.

Từ định nghĩa của hàm phân phối $F(x) = P(\xi \leqslant x)$ ta có hai tính chất của hàm mật độ:

1. :math:`\displaystyle{F(x) = \int\limits_{-\infty}^{x} p(x)\, dx}`.
2. :math:`p(x) = F'(x)`.

Tính chất thứ nhất là từ định nghĩa hàm phân phối. Tính chất thứ hai suy ra từ việc cận trên của tích phân là hữu hạn.

Hàm mật độ của biến ngẫu nhiên rời rạc
--------------------------------------

Biến ngẫu nhiên rời rạc có bảng xác suất sau:

+-----------+-------------+-------------+-----+-------------+-----+
| :math:`x` | :math:`x_1` | :math:`x_2` | ... | :math:`x_n` | ... |
+===========+=============+=============+=====+=============+=====+
| :math:`P` | :math:`p_1` | :math:`p_2` | ... | :math:`p_n` | ... |
+-----------+-------------+-------------+-----+-------------+-----+

Khi đó hàm mật độ của :math:`X` là:

.. math:: 
    
    f(x) = \begin{cases}
        p_i & \text{khi} \ x = x_i, \\
        0 & \text{khi} \ x \neq x_i, \ \text{với mọi} \ i.
    \end{cases}

.. prf:remark:: 
    :label: rmk-density-disc

    Ta có các lưu ý sau:

    - :math:`p_i \geqslant 0`, :math:`\sum p_i = 1`, :math:`i = 1, 2, \ldots`
    - :math:`\displaystyle{P(a < X \leqslant b) = \sum_{a < x_i \leqslant b} p_i}`.

Hàm mật độ của biến ngẫu nhiên liên tục
---------------------------------------

.. prf:definition:: 
    :label: def-density-cont

    Hàm số $f: \mathbb{R} \mapsto \mathbb{R}$ được gọi là **hàm mật độ** của biến ngẫu nhiên liên tục :math:`X` nếu:

    .. math:: P(a \leqslant X \leqslant b) = \displaystyle{\int\limits_a^b f(x)\,dx}, \forall a, b \in \mathbb{R}.

.. prf:remark:: 
    :label: rmk-density-cont

    Với mọi :math:`x \in \mathbb{R}`, :math:`f(x) \geqslant 0` và :math:`\displaystyle{\int\limits_{-\infty}^{+\infty}f(x)\,dx = 1}`.

**Ý nghĩa hình học.** Xác suất của biến ngẫu nhiên :math:`X` nhận giá trị trong :math:`[a; b]` bằng diện tích hình thang cong giới hạn bởi :math:`x = a`, :math:`x = b`, :math:`y=f(x)` và :math:`Ox`.

.. raw:: html

   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2343650775986433"
     crossorigin="anonymous"></script>
   <!-- First Ads -->
   <ins class="adsbygoogle"
      style="display:block"
      data-ad-client="ca-pub-2343650775986433"
      data-ad-slot="4417625951"
      data-ad-format="auto"
      data-full-width-responsive="true"></ins>
   <script>
      (adsbygoogle = window.adsbygoogle || []).push({});
   </script>