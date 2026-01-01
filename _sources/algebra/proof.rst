Phương pháp chứng minh toán học
*******************************

Chứng minh trực tiếp
====================

Giả sử chúng ta có điều kiện ban đầu là :math:`P` và ta cần chứng minh mệnh đề :math:`Q`.

Đối với chứng minh trực tiếp, từ :math:`P` chúng ta suy ra :math:`P_1` nào đó, rồi lại suy ra :math:`P_2` từ :math:`P_1`. Chúng ta làm vậy cho đến khi nhận được mệnh đề :math:`Q`.

Chứng minh trực tiếp hữu dụng đối với những lời giải tuần tự từng bước.

.. prf:example:: 
   :label: exp-direct-proof

   Cho tam giác :math:`ABC` với :math:`G`, :math:`H`, :math:`O` lần lượt là trọng tâm, trực tâm và tâm đường tròn ngoại tiếp tam giác :math:`ABC`. Chứng minh rằng ba điểm :math:`G`, :math:`H` và :math:`O` thẳng hàng.

Ở đây, với :math:`O` là tâm đường tròn ngoại tiếp tam giác, ta vẽ đường tròn đó trước (:numref:`euler-line`).

Tiếp theo, ta vẽ đường kính :math:`AD`.

Lúc này, vì góc :math:`\widehat{ACD}` chắn nửa đường tròn (:math:`AD` là đường kính) nên :math:`\widehat{ACD}` là **góc vuông**, hay :math:`CD` vuông góc :math:`AC`.

Tiếp theo, vì :math:`H` là trực tâm nên :math:`BH` vuông góc cạnh đối diện :math:`AC`.

Từ hai kết quả trên suy ra :math:`BH // CD` vì cùng vuông góc :math:`AC`.

Tương tự ta cũng có :math:`CH // BD`.

Tứ giác :math:`BHCD` có hai cặp cạnh song song là :math:`BH // CD` và :math:`CH // BD` nên :math:`BHCD` là hình bình hành.

Giao điểm hai đường chéo của hình bình hành là trung điểm mỗi đường chéo. Gọi :math:`I_1` là trung điểm :math:`BC` thì :math:`I_1` cũng là trung điểm :math:`HD`.

Vì :math:`O` là trung điểm :math:`AD`, :math:`I_1` là trung điểm :math:`HD` nên :math:`OI_1` là đường trung bình tam giác :math:`DHA`, hay :math:`\overrightarrow{OI_1} = \dfrac{1}{2}\overrightarrow{AH}`.

Do :math:`G` là trọng tâm :math:`\triangle ABC` và :math:`AI_1` là trung tuyến (:math:`I_1` là trung điểm :math:`BC`) nên :math:`G` chia đoạn thẳng :math:`AI_1` theo tỉ lệ :math:`2:1`, nghĩa là :math:`\overrightarrow{AG} = 2\overrightarrow{GI_1}`.

Tiếp theo chúng ta biến đổi

.. math::
   
   \overrightarrow{AH} & = 2 \overrightarrow{OI_1} \\
   \cancel{\overrightarrow{AG}} + \overrightarrow{GH} & = 2 (\overrightarrow{OG} + \overrightarrow{GI_1}) = 2\overrightarrow{OG} + \cancel{2\overrightarrow{GI_1}} \\
   \overrightarrow{GH} & = 2\overrightarrow{OG}.
   
Biểu thức cuối cùng chứng tỏ :math:`G`, :math:`H` và :math:`O` thẳng hàng, ngoài ra :math:`G` chia đoạn thẳng :math:`HO` theo tỉ lệ :math:`2:1`.

.. _euler-line:

.. figure:: ../figures/euler_line/euler_line.*

    Đường thẳng Euler

Quy nạp toán học (cơ bản)
=========================

Giả sử ta muốn chứng minh một mệnh đề :math:`P` đúng với mọi :math:`n \geqslant 1`. Phép quy nạp toán học hoạt động theo ba bước như sau:

1. Chứng minh mệnh đề :math:`P` đúng với :math:`n=1`. Đây gọi là *bước cơ sở*.
2. Giả sử mệnh đề :math:`P` đúng với :math:`n = k \geqslant 1`. Đây gọi là *giả thiết quy nạp*.
3. Chứng minh mệnh đề :math:`P` đúng với :math:`n = k+1` từ giả thiết quy nạp ở bước 2.

Như vậy phép **quy nạp toán học** (hay **mathematical induction**, **математическая индукция**) hoạt động theo bậc thang. Từ giả thiết quy nạp mệnh đề :math:`P` đúng với :math:`n = 1`, theo chứng minh ở bước 3 thì mệnh đề :math:`P` cũng đúng ở bước :math:`n = 1+1 = 2`. Do :math:`P` đúng với :math:`n = 2` nên cũng đúng ở :math:`n = 3`. Cứ tiếp tục như vậy :math:`P` sẽ đúng với mọi :math:`n \geqslant 1`. Đây là sự hiệu quả đáng kinh ngạc của phép quy nạp toán học.

.. prf:example:: 
   :label: exp-induction

   Chứng minh công thức tổng quát cho tổng :math:`1 + 2 + \ldots + n` là :math:`\dfrac{n(n+1)}{2}`.

Với :math:`n = 1` thì :math:`1 = \dfrac{1 (1 + 1)}{2}`. Như vậy công thức đúng cho :math:`n = 1`. Đây là bước cơ sở.

Giả sử mệnh đề đúng với :math:`n = k \geqslant 1`. Nghĩa là :math:`1 + 2 + \ldots + k = \dfrac{k(k+1)}{2}`. Đây là giả thiết quy nạp.

Bây giờ ta cần chứng minh mệnh đề đúng với :math:`n = k+1`, nghĩa là ta cần chứng minh 

.. math::

   1 + 2 + \ldots + k + (k+1) = \dfrac{(k+1)(k+2)}{2}.

Từ giả thiết quy nạp ta suy ra

.. math::

   1 + 2 + \ldots + k + (k+1) = & \dfrac{k(k+1)}{2} + (k+1) \\ = & \dfrac{k(k+1) + 2(k+1)}{2} \\ = & \dfrac{(k+1)(k+2)}{2}. 

Vậy là ta đã có điều cần chứng minh, và công thức đã được chứng minh đúng với mọi :math:`n \geqslant 1`.

.. prf:remark:: 
    :label: rmk-induction

    Tùy thuộc bài toán, bước cơ sở có thể không phải bắt đầu từ :math:`1` mà là một số nguyên dương nào đó khác.

Quy nạp toán học (mạnh)
=======================

Quy nạp toán học mạnh (strong induction) là một phiên bản mạnh hơn của phép quy nạp toán học ở trên.

Trong phép quy nạp toán học mạnh, *giả thiết quy nạp* sẽ được thay bằng: Giả sử mệnh đề :math:`P` ĐÚNG TỚI :math:`n = k \geqslant 1`.

Điểm khác biệt của quy nạp mạnh với quy nạp ban đầu là việc giả thiết quy nạp đúng với mọi :math:`n` nhỏ hơn hoặc bằng :math:`k` và chúng ta sẽ chứng minh mệnh đề đúng với :math:`n = k + 1`. Trong khi đó ở quy nạp ban đầu thì giả thiết quy nạp chỉ đúng với :math:`n = k` thôi.

Tính đúng đắn của quy nạp mạnh vẫn giống như quy nạp thông thường, nghĩa là vẫn hoạt động theo bậc thang. Khi mệnh đề đúng với :math:`n = 1` (bước cơ sở) thì chứng minh ở bước 3 cho kết quả mệnh đề :math:`P` đúng với :math:`n = 2`. Do mệnh đề :math:`P` đúng với :math:`n = 1, 2` nên sẽ đúng với :math:`n = 3`. Cứ tiếp tục như vậy thì :math:`P` sẽ đúng với mọi :math:`n \geqslant 1`.

Tại sao chúng ta cần dùng quy nạp toán học mạnh khi bản chất vẫn giống quy nạp thông thường?

Lý do là đôi khi chúng ta chứng minh :math:`n = k + 1` không dựa trên :math:`n = k`, mà là một điểm nào đó nhỏ hơn, nghĩa là trong khoảng :math:`[1, k]`.

.. prf:example::
   :label: exp-induction-strong

   Dãy số Fibonacci định nghĩa bởi :math:`F_1 = F_2 = 1` và :math:`F_{n+2} = F_{n+1} + F_n` với mọi :math:`n \geqslant 1`. Chứng minh rằng công thức tổng quát của dãy Fibonacci là

   .. math:: F_n = \frac{1}{\sqrt{5}} \left[ \left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n \right].

Khi :math:`n = 1` thì ta có :math:`F_1 = 1`, đúng với điều kiện ban đầu.

Khi :math:`n = 2` thì ta có :math:`F_2 = 1`, đúng với điều kiện ban đầu.

*Giả thiết quy nạp*: giả sử với mọi :math:`n = k \geqslant 1` ta đều có :math:`F_k = \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 + \sqrt{5}}{2}\right)^k - \left(\dfrac{1 - \sqrt{5}}{2}\right)^k \right]`.

Khi đó, với :math:`n = k+1`, ta có

.. math:: 

   F_{k+1} & = F_{k} + F_{k-1} \\
   & = \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 + \sqrt{5}}{2}\right)^k - \left(\dfrac{1 - \sqrt{5}}{2}\right)^k \right]
   + \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 + \sqrt{5}}{2}\right)^{k-1} - \left(\dfrac{1 - \sqrt{5}}{2}\right)^{k-1} \right] \\
   & = \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 + \sqrt{5}}{2}\right)^k + \left(\dfrac{1 + \sqrt{5}}{2}\right)^{k-1} \right]
   - \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 - \sqrt{5}}{2}\right)^k + \left(\dfrac{1 - \sqrt{5}}{2}\right)^{k-1} \right] \\
   & = \dfrac{1}{\sqrt{5}} \left(\dfrac{1 + \sqrt{5}}{2}\right)^{k-1} \left(\dfrac{1 + \sqrt{5}}{2} + 1\right)
   - \dfrac{1}{\sqrt{5}} \left(\dfrac{1 - \sqrt{5}}{2}\right)^{k-1} \left(\dfrac{1 - \sqrt{5}}{2} + 1\right).

Để ý rằng

.. math:: 
   
   \dfrac{1 + \sqrt{5}}{2} + 1 & = \dfrac{3 + \sqrt{5}}{2} = \dfrac{6 + 2\sqrt{5}}{4} = \dfrac{1 + 2\sqrt{5} + \left(\sqrt{5}\right)^2}{4} \\
   & = \dfrac{\left(1 + \sqrt{5}\right)^2}{2^2} = \left(\dfrac{1 + \sqrt{5}}{2}\right)^2,

tương tự ta cũng có :math:`\dfrac{1 - \sqrt{5}}{2} + 1 = \left(\dfrac{1 - \sqrt{5}}{2}\right)^2`, nên ở trên suy ra

.. math:: 

   F_{k+1} & = \dfrac{1}{\sqrt{5}} \left(\dfrac{1 + \sqrt{5}}{2}\right)^{k-1} \left(\dfrac{1 + \sqrt{5}}{2}\right)^2
   + \dfrac{1}{\sqrt{5}} \left(\dfrac{1 - \sqrt{5}}{2}\right)^{k-1} \left(\dfrac{1 - \sqrt{5}}{2}\right)^2 \\
   & = \dfrac{1}{\sqrt{5}} \left[ \left(\dfrac{1 + \sqrt{5}}{2}\right)^{k+1} - \left(\dfrac{1 - \sqrt{5}}{2}\right)^{k+1} \right].

Như vậy mệnh đề đúng với :math:`n = k+1` và ta có điều phải chứng minh.

Ở đây quy nạp mạnh thể hiện ở việc ta cần giả thiết đúng với :math:`n = k` và :math:`n = k-1` để chứng minh cho :math:`n = k+1`.

Chứng minh bằng phản chứng
==========================

Giả sử chúng ta có điều kiện :math:`P` và cần chứng minh kết quả :math:`Q`. Điều này tương đương với mệnh đề logic :math:`P \Rightarrow Q`. Chứng minh bằng phản chứng dựa trên sự tương đương của các mệnh đề logic, nghĩa là

.. math:: (P \Rightarrow Q) \Longleftrightarrow (\bar{Q} \Rightarrow \bar{P}).

Khi đó, từ kết quả :math:`Q` cần chứng minh, chúng ta giả sử rằng đang có :math:`\bar{Q}`, tức là phủ định của mệnh đề cần chứng minh. Bằng các lập luận logic chúng ta sẽ suy ra được điều trái với điều kiện ban đầu, tức là :math:`\bar{P}`. Đây là cơ sở của phép chứng minh bằng phản chứng.

.. prf:example:: 
   :label: exp-phan-chung

   Chứng minh rằng với mọi số tự nhiên :math:`n`, nếu :math:`n^3` chia hết cho :math:`3` thì :math:`n` chia hết cho :math:`3`.

Ở đây:

1. Điều kiện, tức mệnh đề :math:`P`, là ":math:`n^3` chia hết cho :math:`3`".
2. Mệnh đề cần chứng minh :math:`Q` là ":math:`n` chia hết cho :math:`3`".

Ta suy ra:

1. Phủ định của mệnh đề :math:`P` là ":math:`n^3` không chia hết cho :math:`3`", tức mệnh đề :math:`\bar{P}`.
2. Phủ định của mệnh đề :math:`Q` là ":math:`n` không chia hết cho :math:`3`", tức mệnh đề :math:`\bar{Q}`.

Như vậy phép phản chứng đưa ta tới việc chứng minh: nếu số tự nhiên :math:`n` không chia hết cho :math:`3` thì :math:`n^3` không chia hết cho :math:`3`.

Nếu :math:`n` không chia hết cho :math:`3` thì :math:`n` có dạng :math:`3k+1` hoặc :math:`3k+2` với :math:`k \in \mathbb{Z}`.

- nếu :math:`n = 3k+1` thì :math:`n^3 = 27k^3 + 27k^2 + 9k + 1`, khi chia :math:`3` sẽ dư :math:`1`. Khi đó :math:`n^3` không chia hết cho :math:`3`;
- nếu :math:`n = 3k+2` thì :math:`n^3 = 27k^3 + 54k^2 + 36k + 8`, khi chia :math:`3` sẽ dư :math:`2` (vì :math:`8` chia :math:`3` dư :math:`2`). Khi đó :math:`n^3` cũng không chia hết cho :math:`3`.

Như vậy khi :math:`n` không chia hết cho :math:`3` (mệnh đề :math:`\bar{Q}`) thì :math:`n^3` cũng không chia hết cho :math:`3` (mệnh đề :math:`\bar{P}`). Theo phản chứng ta có, nếu :math:`n^3` chia hết cho :math:`3` (mệnh đề :math:`P`) thì :math:`n` chia hết cho :math:`3` (mệnh đề :math:`Q`). Đây là điều phải chứng minh.
