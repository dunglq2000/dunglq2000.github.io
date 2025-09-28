Tập hợp
=======


Mở đầu về tập hợp
-----------------

Một **tập hợp** (**set**) bao gồm các phần tử khác nhau. Tập hợp là khái niệm cơ sở cho nhiều vấn đề của toán học. Tuy nhiên chúng ta lại không có một định nghĩa chặt chẽ về tập hợp mà chỉ có thể biểu diễn nó. Để biểu diễn tập hợp ta có hai cách.

1. Liệt kê. Ví dụ :math:`A = \{ 1, 2, 3, 4 \}`, :math:`B = \{ a, b , c \}`.
2. Sử dụng tính chất đặc trưng. Ví dụ :math:`A = \{ a \in \mathbb{N}^* : a < 5 \}`.

Ở đây hai cách biểu diễn tập hợp :math:`A` là giống nhau.

.. prf:definition:: Tập hợp rỗng
    :label: def-empty-set

    Tập hợp rỗng không chứa phần tử nào, kí hiệu là :math:`\emptyset`.

.. prf:definition:: Tập hợp con
    :label: def-subset

    Xét tập hợp :math:`A`. Tập hợp :math:`B` được gọi là **tập hợp con** của tập :math:`A` nếu mọi phần tử của :math:`B` đều nằm trong :math:`A`. Nói cách khác với mọi :math:`b \in B` thì :math:`b \in A`. Ta kí hiệu :math:`B \subset A`.

.. prf:remark:: 
    :label: rmk-subset
    
    Tập hợp rỗng là con của mọi tập hợp.

Dễ thấy rằng mọi tập hợp là tập hợp con của chính nó. Do đó tập con này được gọi là tập con tầm thường (trivial subset). Để kí hiệu một tập con có thể bằng tập chứa nó ta viết :math:`B \subseteq A`. Trong trường hợp :math:`B` là tập con của :math:`A` nhưng không bằng :math:`A` ta có thể viết :math:`B \subsetneq A`.


Toán tử trên tập hợp
--------------------

Chúng ta xem xét ba toán tử cơ bản trên tập hợp là **giao**, **hợp** và **hiệu** của hai tập hợp. Để biểu diễn các toán tử này ta có thể dùng biểu đồ Venn.

.. prf:definition:: Giao của hai tập hợp
    :label: def-set-intersection
    
    Giao của hai tập hợp :math:`A` và :math:`B` là tập hợp các phần tử thuộc cả :math:`A` và :math:`B`.

    .. math:: A \cap B = \{ x : x \in A \text{ và } x \in B \}.

.. _set1:

.. figure:: ../../figures/set/venn_diagram-1.*

    Phép giao hai tập hợp

:numref:`set1` là biểu đồ Venn tương ứng của phép giao hai tập hợp. Khi giao của hai tập hợp :math:`A` và :math:`B` là rỗng thì ta nói hai tập rời nhau. Kí hiệu :math:`A \cap B = \emptyset`.

.. prf:definition:: Hợp của hai tập hợp
    :label: def-union-set

    Hợp của hai tập hợp :math:`A` và :math:`B` là tập hợp các phần tử thuộc :math:`A` hoặc :math:`B`.

    .. math:: A \cup B = \{ x : x \in A \text{ hoặc } x \in B \}.

:numref:`set2` là biểu đồ Venn tương ứng của phép hợp hai tập hợp.

.. _set2: 

.. figure:: ../../figures/set/venn_diagram-2.*

    Phép hợp hai tập hợp

.. prf:definition:: Hiệu của hai tập hợp
    :label: def-set-minus
    
    Hiệu (hay phần bù) của tập hợp :math:`A` đối với tập hợp :math:`B` là tập hợp các phần tử thuộc :math:`A` nhưng không thuộc :math:`B`.

    .. math:: A \backslash B = \{ x : x \in A \text{ và } x \not\in B \}.

:numref:`set3` là biểu đồ Venn tương ứng của hiệu hai tập hợp.

.. _set3: 

.. figure:: ../../figures/set/venn_diagram-3.*

    Phép hiệu hai tập hợp
