Topology
########

Nhập môn topology
*****************

Phần này mình sử dụng tài liệu :cite:`Verbitskiy2017` (phần II, bài 3).

.. prf:definition:: 
    :label: def-topo-space

    **Không gian topo** (hay **topological space**) là một cặp :math:`(X, \tau)`, trong đó:

    1. :math:`X` là một tập hợp khác rỗng.
    2. :math:`\tau` là một họ các tập con của :math:`X` thỏa ba tiên đề

       * :math:`\emptyset \in \tau` và :math:`X \in \tau`;
       * hợp bất kì một họ (hữu hạn hoặc vô hạn) các tập thuộc :math:`\tau` cũng là tập thuộc :math:`\tau`;
       * giao của một số hữu hạn các tập thuộc :math:`\tau` cũng là tập thuộc :math:`\tau`.

    Các phần tử thuộc :math:`\tau` được gọi là **tập mở** (hay **open set**, **открытое множество**).

    Như vậy:

    * :math:`\emptyset` và :math:`X` là các tập mở;
    * hợp của các tập mở cũng là tập mở;
    * giao của một số hữu hạn tập mở cũng là tập mở.

.. prf:example:: 
    :label: exp-topo-1

    Topo thô hay topo tầm thường (indiscrete/trivial) là tập :math:`\tau = \{ \emptyset, X \}`. Topo này chỉ gồm hai phần tử là tập rỗng và bản thân tập :math:`X`. Dễ thấy ba tiền đề được thỏa mãn.

.. prf:example:: 
    :label: exp-topo-2

    Khi :math:`\tau = P(X)` là tập hợp tất cả tập con của tập :math:`X`.

    Ví dụ, nếu :math:`X = \{ x_1, x_2 \}` thì

    .. math:: P(X) = \{ \emptyset, \{ x_1 \}, \{ x_2 \}, \{ x_1, x_2 \} \}.

    Một kết quả thông dụng là khi tập :math:`X` có :math:`n` phần tử thì :math:`P(X)` có :math:`2^n` phần tử. Lúc này :math:`\tau` cũng thỏa ba tiên đề trong định nghĩa.

.. prf:example:: 
    :label: exp-topo-3

    Topo chuẩn (standard) trên :math:`\mathbb{R}`: tập :math:`U \subseteq \mathbb{R}` được gọi là mở nếu với mọi điểm :math:`x \in U`, tồn tại một khoảng mở :math:`(a; b)` sao cho :math:`x \in (a; b) \subseteq U`.

Tập mở (open set, открытое множество) là định nghĩa các phần tử trong :math:`\tau`.

Tập đóng (closed set, замкнутое множество) nếu phần của nó trong :math:`X` là tập mở. Nói cách khác, nếu :math:`F \subseteq X` là tập đóng thì :math:`X \setminus F` là tập mở.

.. prf:remark:: 
    :label: rmk-topo-1

    Tập mở và tập đóng không phải hai khái niệm loại trừ nhau. Một tập thuộc :math:`\tau` có thể vừa mở và vừa đóng.

Ở :prf:ref:`exp-topo-2` thì :math:`\{ x_1 \}` và :math:`\{ x_2 \}` là các tập mở. Đồng thời, :math:`\{ x_1 \} = X \setminus \{ x_2 \}` nên :math:`\{ x_1 \}` cũng là tập đóng, tương tự cho :math:`\{ x_2 \}`.

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
