Lý thuyết đồ thị
****************

Phần này mình sử dụng các quyển sách dành cho học sinh chuyên Tin :cite:`TLCT1`.


Các định nghĩa cơ bản
=====================

.. prf:definition:: Đồ thị
    :label: def-graph

    **Đồ thị** (hay **graph**, hay **граф**) :math:`G = (V, E)` gồm một tập hợp các đỉnh :math:`V` và tập hợp các cạnh :math:`E` nối các đỉnh với nhau.


Đồ thị vô hướng
---------------

.. prf:example:: 
    :label: exp-graph

    Đồ thị sau có:

    1. Tập hợp các đỉnh

    .. math:: V = \{ v_1, v_2, v_3, v_4, v_5, v_6 \}.

    2. Tập hợp các cạnh

    .. math:: E = \{ e_{12}, e_{23}, e_{24}, e_{26}, e_{56} \}.

.. _undirected-graph: 

.. figure:: ../../figures/graph/undirected-graph.*

    Đồ thị vô hướng

Ở ví dụ trên, cạnh :math:`e_{ij}` nối đỉnh :math:`v_i` và đỉnh :math:`v_j`. Trong trường hợp này hướng của cạnh không quan trọng nên việc viết :math:`e_{ij}` và :math:`e_{ji}` là tương đương. Đồ thị lúc này gọi là **đồ thị vô hướng** (hay **undirected graph**).

Hai đỉnh được gọi là **kề nhau** (hay **adjacent**) nếu có cạnh nối giữa chúng.

Ở ví dụ trên thì hai đỉnh :math:`v_1` và :math:`v_2` kề nhau, nhưng đỉnh :math:`v_1` không kề với :math:`v_3` vì không có cạnh :math:`e_{13}`.

Khi đó cạnh nối hai đỉnh kề nhau được gọi là cạnh **liên thuộc** (hay **incident**).

Ở đồ thị vô hướng, ta nói **bậc** (hay **degree**) của đỉnh :math:`v` là số cạnh liên thuộc với đỉnh :math:`v`, và kí hiệu là :math:`\deg (v)`.

Ở :numref:`undirected-graph` ta thấy :math:`\deg (v_1) = 1`, :math:`\deg (v_2) = 3`, :math:`\deg (v_3) = 1`, :math:`\deg (v_4) = 1`, :math:`\deg (v_5) = 1`, :math:`\deg (v_6) = 2`. Tổng quát ta có định lí sau.

.. prf:theorem:: 
    :label: thm-vertice-edges

    Giả sử :math:`G = (V, E)` là đồ thị vô hướng, khi đó tổng tất cả các bậc của các đỉnh trong  :math:`V` sẽ bằng hai lần số cạnh:

    .. math:: \sum_{v \in V} \deg (v) = 2 \lvert E \rvert.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Khi lấy tổng tất cả các bậc thì mỗi cạnh :math:`e_{ij}` sẽ được tính một lần cho đỉnh :math:`v_i` và một lần cho đỉnh :math:`v_j`. Từ đó suy ra kết quả.

.. prf:corollary:: 
    :label: cor-vertice

    Trong đồ thị vô hướng thì số đỉnh có bậc lẻ là số chẵn.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử :math:`v_1` là tập các đỉnh có bậc lẻ và :math:`v_2` là tập các đỉnh có bậc chẵn. Khi đó :math:`_1 \cup V_2 = V` và :math:`V_1 \cap V_2 = \emptyset`. Theo định lí trên thì

    .. math:: \sum_{v_1 \in V_1} \deg (v_1) + \sum_{v_2 \in V_2} \deg (v_2) = 2 \lvert E \rvert

    là số chẵn, mà tổng bậc của các đỉnh bậc chẵn :math:`\sum\limits_{v_2 \in V_2} \deg (v_2)` cũng là số chẵn nên suy ra tổng :math:`\sum\limits_{v_1 \in V_1} \deg (v_1)` cũng là chẵn.

    Do mỗi giá trị :math:`\deg (v_1)` là lẻ với mọi :math:`v_1 \in V_1` nên tổng của chúng là chẵn khi và chỉ khi số phần tử của :math:`v_1` là chẵn. Ta có điều phải chứng minh.


Đồ thị có hướng
---------------

Nếu chúng ta quan tâm đến hướng thì khi vẽ cạnh :math:`e_{ij}` ta vẽ mũi tên từ đỉnh :math:`v_i` tới đỉnh :math:`v_j`. Đồ thị khi đó gọi là **đồ thị có hướng** (hay **directed graph**).

.. _directed-graph: 

.. figure:: ../../figures/graph/directed-graph.*

    Đồ thị có hướng

Ở hình trên:

- chỉ có cạnh từ :math:`v_1` tới :math:`v_2` là :math:`e_{12}` chứ không có cạnh từ :math:`v_2` tới :math:`v_1`
- có cạnh từ :math:`v_6` tới :math:`v_5` là :math:`e_{65}` và cũng có cạnh từ :math:`v_5` tới :math:`v_6` là :math:`e_{56}`.

Lúc này tập đỉnh là

.. math:: V = \{ v_1, v_2, v_3, v_4, v_5, v_6 \},

và tập cạnh là

.. math:: E = \{ e_{12}, e_{23}, e_{24}, e_{52}, e_{56}, e_{65} \}.

Đối với đồ thị có hướng thì cạnh :math:`e_{ij}` là cạnh đi ra từ đỉnh :math:`i` và đi vào đỉnh :math:`j`. Đỉnh :math:`i` gọi là đỉnh đầu, đỉnh :math:`j` gọi là đỉnh cuối.

.. prf:definition:: Bán bậc vào, bán bậc ra
    :label: def-in-out-degree

    **Bán bậc ra** (hay **out-degree**) của đỉnh :math:`v` là số lượng cạnh đi ra khỏi nó và kí hiệu là :math:`\deg^+(v)`.

    **Bán bậc vào** (hay **in-degree**) của đỉnh :math:`v` là số lượng cạnh đi vào nó và kí hiệu là :math:`\deg^-(v)`.

Với ví dụ ở :numref:`directed-graph` thì:

- :math:`\deg^+(v_1) = 1`, :math:`\deg^-(v_1) = 0`;
- :math:`\deg^+(v_2) = 2`, :math:`\deg^-(v_2) = 1`;
- :math:`\deg^+(v_3) = 0`, :math:`\deg^-(v_3) = 1`;
- :math:`\deg^+(v_4) = 0`, :math:`\deg^-(v_4) = 1`;
- :math:`\deg^+(v_5) = 2`, :math:`\deg^-(v_5) = 1`;
- :math:`\deg^+(v_6) = 1`, :math:`\deg^-(v_6) = 1`.

.. prf:theorem:: 
    :label: thm-in-out-degree

    Nếu :math:`G = (V, E)` là đồ thị có hướng thì tổng tất cả các bán bậc ra của các đỉnh bằng tổng tất cả các bán bậc vào, và cũng bằng tổng số cung của đồ thị

    .. math:: \sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = \lvert E \rvert.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Mỗi cạnh của đồ thị đi ra từ đúng một đỉnh nên :math:`\sum\limits_{v \in V} \deg^+(v) = \lvert E \rvert`.

    Tương tự, mỗi cạnh của đồ thị đi vào đúng một đỉnh nên :math:`\sum\limits_{v \in V} \deg^-(v) = \lvert E \rvert`.

    Kết hợp hai đẳng thức trên ta có điều phải chứng minh.


Đường đi và chu trình
---------------------

Một dãy có thứ tự các đỉnh :math:`v_{i_0}`, :math:`v_{i_1}`, ..., :math:`v_{i_n}` sao cho :math:`e_{i_t i_{t+1}} \in E` với mọi :math:`t = 0, 1, \ldots, n-1` được gọi là **đường đi**. Lúc này đường đi có :math:`n+1` đỉnh :math:`v_{i_0}`, :math:`v_{i_1}`, ..., :math:`v_{i_n}` và :math:`n` cạnh :math:`e_{i_0 i_1}`, :math:`e_{i_1 i_2}`, ..., :math:`e_{i_{n-1} i_n}`.

Nếu tồn tại một đường đi từ đỉnh :math:`v_{i_0}` tới đỉnh :math:`v_{i_n}` thì ta nói đỉnh :math:`v_{i_n}` **đến được** (hay **reachable**) từ đỉnh :math:`v_{i_0}` và kí hiệu là :math:`v_{i_0} \leadsto v_{i_n}`.

1. Đỉnh :math:`v_{i_0}` được gọi là đỉnh đầu của đường đi.
2. Đỉnh :math:`v_{i_n}` được gọi là đỉnh cuối của đường đi.
3. Các đỉnh :math:`v_{i_1}`, ..., :math:`v_{i_{n-1}}` được gọi là đỉnh trong của đường đi.

Đường đi được gọi là đường đi **đơn** (hay **simple**) nếu tất cả các đỉnh trên đường đi hoàn toàn phân biệt.

:numref:`path` thể hiện hai đường đi đơn từ đỉnh :math:`v_1` tới đỉnh :math:`v_3`:

- đường đi thứ nhất là :math:`v_1`, tới :math:`v_2` và tới :math:`v_3`
- đường đi thứ hai là :math:`v_1`, tới :math:`v_2`, đi xuống :math:`v_4`, đi lên :math:`v_6` và quay lại :math:`v_3`.

.. _path: 

.. figure:: ../../figures/graph/path.*

    Đường đi từ :math:`v_1` tới :math:`v_3`

Đường đi được gọi là **chu trình** (hay **circuit**) nếu đỉnh đầu trùng với đỉnh cuối, nghĩa là :math:`v_{i_0} = v_{i_n}`.


Đẳng cấu đồ thị
---------------

.. prf:definition:: 
    :label: def-graph-isomorphism
    
    Hai đồ thị :math:`G = (V, E)` và :math:`G' = (V', E')` được gọi là **đẳng cấu** (hay **isomorphic**) nếu tồn tại một song ánh :math:`f : V \to V'` sao cho số cung nối đỉnh :math:`u` với đỉnh :math:`v` trên :math:`E` bằng số cung nối đỉnh :math:`f(u)` với đỉnh :math:`f(v)` trên :math:`E'`.

Nói cách khác, kí hiệu :math:`e_{ij}` là cạnh nối đỉnh :math:`v_i` và :math:`v_j` trên :math:`E`. Đặt :math:`v_i' = f(v_i)` và :math:`v_j' = f(v_j)` là các đỉnh thuộc :math:`V'`. Khi đó :math:`e_{ij}'` là cạnh thuộc :math:`E'` nối đỉnh :math:`v'_i` và đỉnh :math:`v'_j`. Nếu giữa :math:`v_i` và :math:`v_j` không có cạnh nào thì cũng không có cạnh nối :math:`v_i'` và :math:`v_j'`.

Bài toán đẳng cấu đồ thị (graph isomorphism problem) là một trong những bài toán khó hiện nay (tháng 1 năm 2025) về việc tìm lời giải trong thời gian đa thức. Nếu cho trước hai đồ thị thì nhiệm vụ của bài toán là xác định xem hai đồ thị có đẳng cấu hay không. Rõ ràng nếu số đỉnh nhỏ thì chúng ta có thể thử từng hoán vị (song ánh) của tập đỉnh, nhưng khi số đỉnh lớn thì việc thử sai tất cả hoán vị là không thể.


Đồ thị con
----------

.. prf:definition:: Đồ thị con
    :label: def-subgraph

    Đồ thị :math:`G' = (V', E')` là **đồ thị con** (hay **subgraph**, hay **подграф**) của đồ thị :math:`G = (V, E)` nếu :math:`V' \subseteq V` và :math:`E' \subseteq E`.

Nói cách khác, đồ thị con thu được từ đồ thị ban đầu bằng việc lấy một lượng nhất định đỉnh và cạnh.

Ở đồ thị trên :numref:`subgraph-1`, mình lấy các đỉnh :math:`v_1`, :math:`v_2`, :math:`v_4` và :math:`v_5`, và lấy các cạnh :math:`e_{24}`, :math:`e_{45}` thì mình có đồ thị con trên :numref:`subgraph-2`. Các bạn có thể thấy ở đồ thị ban đầu thì :math:`v_1` nối với :math:`v_2`, nhưng ở đồ thị con thì không có cạnh nối giữa hai đỉnh này.

.. _subgraph-1:

.. figure:: ../../figures/graph/subgraph-1.*

    Đồ thị ban đầu

.. _subgraph-2:

.. figure:: ../../figures/graph/subgraph-2.*
 
    Đồ thị con

Đồ thị đầy đủ
-------------

Đồ thị vô hướng được gọi là **đầy đủ** (hay **complete**, hay **полный**) nếu mọi cặp đỉnh đều kề nhau.

Đồ thị đầy đủ gồm :math:`n` đỉnh kí hiệu là :math:`K_n`.

.. figure:: ../../figures/graph/complete-graph.*
    
    Ví dụ :math:`K_6`

Dễ thấy số cạnh của đồ thị đầy đủ :math:`n` đỉnh là :math:`C^2_n`.

Đồ thị hai phía
---------------

Đồ thị vô hướng được gọi là **hai phía** (hay **bipartite**) nếu tập đỉnh của nó có thể chia thành hai tập rời nhau :math:`V_1` và :math:`V_2` sao cho không tồn tại cạnh nối hai đỉnh của :math:`V_1`, và cũng không tồn tại cạnh nối hai đỉnh của :math:`V_2`.

Nếu :math:`\lvert V_1 \rvert = n_1` và :math:`\lvert V_2 \rvert = n_2` và giữa mọi cặp đỉnh :math:`(v_1, v_2)`, trong đó :math:`v_1 \in V_1` và :math:`v_2 \in V_2`, đều có cạnh nối thì đồ thị hai phía đó được gọi là đồ thị hai phía đầy đủ, kí hiệu là :math:`K_{v_1, v_2}`.

.. figure:: ../../figures/graph/bipartite.*
    
    Ví dụ đồ thị hai phía đầy đủ :math:`K_{3, 2}`

Theo quy tắc nhân, số cạnh của đồ thị hai phía đầy đủ là :math:`v_1 \cdot v_2` vì mỗi đỉnh ở :math:`V_1` đều có :math:`v_2` cạnh nối với nó, và có tất cả :math:`v_1` đỉnh trong :math:`V_1`.

Đồ thị phẳng
------------

Đồ thị được gọi là **đồ thị phẳng** (hay **planar graph**, hay **планарный граф**) nếu chúng ta có thể vẽ đồ thị trên mặt phẳng sao cho:

1. Mỗi đỉnh tương ứng với một điểm trên mặt phẳng, không có hai đỉnh cùng tọa độ.
2. Mỗi cạnh tương ứng với một đường liên tục nối hai đỉnh và hai cạnh bất kì không giao nhau.

Phép vẽ đồ thị phẳng này được gọi là biểu diễn phẳng của đồ thị.

.. prf:theorem:: Định lí Kuratowski
    :label: thm-kuratowski

    Một đồ thị vô hướng là đồ thị phẳng khi và chỉ khi nó không chứa đồ thị con đẳng cấu với :math:`K_{3, 3}` hoặc :math:`K_5`.

.. prf:theorem:: Công thức Euler
    :label: thm-euler-formula

    Nếu một đồ thị vô hướng liên thông là đồ thị phẳng và biểu diễn phẳng của đồ thị đó gồm :math:`v` đỉnh và :math:`e` cạnh chia mặt phẳng thành :math:`f` phần thì

    .. math:: v - e + f = 2.

Công thức Euler này chúng ta cũng thấy ở hình học không gian đối với một khối đa diện. Nếu :math:`v` là số đỉnh (vertices), :math:`e` là số cạnh (edges) và :math:`f` là số mặt (faces) thì :math:`v - e + f = 2`.

1. Hình tứ diện có :math:`4` đỉnh, :math:`6` cạnh và :math:`4` mặt nên :math:`4 - 6 + 4 = 2`.
2. Hình lập phương có :math:`8` đỉnh, :math:`12` cạnh và :math:`6` mặt nên :math:`8 - 12 + 6 = 2`.

.. prf:theorem:: 
    :label: thm-plane-graph

    Nếu đồ thị vô hướng :math:`G = (V, E)` là đồ thị phẳng có ít nhất :math:`3` đỉnh thì

    .. math:: \lvert E \rvert \leqslant 3 \lvert V \rvert - 6.

    Ngoài ra nếu :math:`G` không có chu trình độ dài :math:`3` thì

    .. math:: \lvert E \rvert \leqslant 2 \lvert V \rvert - 4.

Tính liên thông của đồ thị
===========================

Tính liên thông trên đồ thị vô hướng
------------------------------------

.. prf:definition:: Đồ thị liên thông
    :label: def-graph-connected

    Một đồ thị vô hướng được gọi là **liên thông** (hay **connected**, hay **связанный**) nếu giữa hai đỉnh bất kì của đồ thị tồn tại đường đi.

Đồ thị chỉ gồm một đỉnh duy nhất cũng được coi là đồ thị liên thông.

.. figure:: ../../figures/graph/connected-graph.*

    Đồ thị liên thông

.. prf:definition:: Thành phần liên thông
    :label: def-connected-component

    Cho đồ thị :math:`G = (V, E)`. Nếu đồ thị con :math:`G' = (V', E')` của :math:`G` là đồ thị liên thông thì :math:`G'` được gọi là **thành phần liên thông** (hay **connected component**, **связанный компонент**) của đồ thị :math:`G`.

.. _connected-component:

.. figure:: ../../figures/graph/connected-component.*
 
    Các thành phần liên thông trên đồ thị

Trên :numref:`connected-component` có ba thành phần liên thông:

- thành phần liên thông thứ nhất gồm hai đỉnh :math:`v_1`, :math:`v_2`, và cạnh :math:`e_{12}`
- thành phần liên thông thứ hai gồm ba đỉnh :math:`v_3`, :math:`v_4`, :math:`v_6`, và các cạnh :math:`e_{36}`, :math:`e_{46}`
- thành phần liên thông thứ ba chỉ gồm đỉnh :math:`v_5`.

Đôi khi việc bỏ đi một đỉnh và tất cả cạnh liên thuộc với nó sẽ tăng số lượng thành phần liên thông hơn so với đồ thị ban đầu. Các đỉnh như vậy gọi là **đỉnh cắt** (hay **cut vertices**), hoặc **nút khớp** (hay **articulation nodes**).

Tương tự, khi bỏ đi một cạnh mà số lượng thành phần liên thông tăng lên thì cạnh đó gọi là **cạnh cắt** (hay **cut edges**) hoặc **cầu** (hay **bridge**).

Ở :numref:`bridge` là một đồ thị liên thông, nếu chúng ta xóa cạnh :math:`e_{24}` (cạnh màu đỏ) thì chúng ta sẽ có hai thành phần liên thông:

- thành phần liên thông thứ nhất gồm hai đỉnh :math:`v_1` và :math:`v_2`
- thành phần liên thông thứ hai gồm bốn đỉnh :math:`v_3`, :math:`v_4`, :math:`v_5` và :math:`v_6`.

.. _bridge:

.. figure:: ../../figures/graph/bridge.*
 
    Ví dụ về cầu

Đồ thị có thể có nhiều cầu. Ở :numref:`bridge`, thay vì xóa cạnh :math:`e_{24}`, nếu ta xóa cạnh :math:`e_{46}` thì cũng làm tăng số thành phần liên thông. Do đó cạnh :math:`e_{46}` cũng là cầu. Tương tự cho cạnh :math:`e_{12}`, ...

Tính liên thông trên đồ thị có hướng
------------------------------------

Một đồ thị có hướng được gọi là:

- **liên thông mạnh** (hay **strongly connected**) nếu tồn tại đường đi giữa hai đỉnh bất kì của đồ thị;
- **liên thông yếu** (hay **weakly connected**) nếu phiên bản vô hướng của nó là đồ thị liên thông.

Bài toán xác định các thành phần liên thông
-------------------------------------------

Bài toán xác định các thành phần liên thông của đồ thị là một bài toán quan trọng trong lý thuyết đồ thị. Bài toán sẽ tìm tất cả thành phần liên thông của đồ thị vô hướng.

Để liệt kê các thành phần liên thông của đồ thị vô hướng :math:`G = (V, E)` ta thực hiện các bước sau:

1. Bắt đầu từ một đỉnh bất kì, ta tìm tất cả đỉnh đến được từ đỉnh đó. Như vậy chúng ta tìm được một thành phần liên thông.
2. Loại những đỉnh ở thành phần liên thông đầu tiên và xét một trong những đỉnh còn lại. Lặp lại công việc ở bước 1, ta tìm tất cả đỉnh đến được từ đỉnh đang xét. Như vậy chúng ta tìm được thêm một thành phần liên thông.
3. Thực hiện đến khi đã xét hết tất cả đỉnh trong đồ thị.

Ở đây, để tìm tất cả đỉnh đến được từ một đỉnh nào đó trong đồ thị ta sử dụng thuật toán DFS (Depth First Search, Duyệt Sâu) hoặc BFS (Breadth First Search, Duyệt Rộng).

Cây
===

.. prf:definition:: Cây
    :label: def-graph-tree

    **Cây** (hay **tree**, hay **дерево**) là đồ thị vô hướng, liên thông, và không có chu trình đơn.

.. figure:: ../../figures/graph/tree.*
    
    Ví dụ về cây

.. prf:definition:: Cây khung
    :label: def-cay-khung

    Xét đồ thị :math:`G = (V, E)` và :math:`T = (V', E')` là đồ thị con của :math:`G`. Nếu :math:`T` là cây thì ta gọi :math:`T` là **cây khung** hoặc **cây bao trùm** (hay **spanning tree**) của đồ thị :math:`G`.

Điều kiện cần và đủ để một đồ thị vô hướng có cây khung là đồ thị đó phải liên thông.

Một đồ thị có thể có nhiều cây khung. Ở :numref:`spanning-tree-1` ta xóa đi cạnh :math:`e_{23}` và :math:`e_{46}` (hai cạnh màu đỏ) thì thu được một cây khung. Tương tự, ở :numref:`spanning-tree-2` ta xóa đi hai cạnh màu đỏ là :math:`e_{13}` và :math:`e_{23}` thì cũng thu được một cây khung khác.

.. _spanning-tree-1:

.. figure:: ../../figures/graph/spanning-tree-1.*
 
    Cây khung thứ nhất

.. _spanning-tree-2:

.. figure:: ../../figures/graph/spanning-tree-2.*
 
    Cây khung thứ hai

.. prf:theorem:: Daisy Chain Theorem
    :label: thm-daisy-chain

    Giả sử :math:`T = (V, E)` là đồ thị vô hướng với :math:`n` đỉnh. Khi đó các mệnh đề sau tương đương:

    1. :math:`T` là cây.
    2. :math:`T` không chứa chu trình đơn và có :math:`n - 1` cạnh.
    3. :math:`T` liên thông và mỗi cạnh của nó đều là cầu.
    4. Giữa hai đỉnh bất kì của :math:`G'` đều tồn tại đúng một đường đi đơn.
    5. :math:`T` không chứa chu trình đơn nhưng nếu ta thêm vào một cạnh thì ta thu được chu trình đơn.
    6. :math:`T` liên thông và có :math:`n - 1` cạnh.

Các mệnh đề trên có thể xem như các định nghĩa tương đương của cây. Trong nhiều trường hợp thì tính chất của cây có thể thu được từ các định nghĩa này nên mình sẽ chứng minh chuỗi mệnh đề này.

.. admonition:: Chứng minh 1 :math:`\Rightarrow` 2
    :class: danger, dropdown

    Từ :math:`T` là cây, theo định nghĩa thì :math:`T` không chứa chu trình đơn. Ta chứng minh cây :math:`T` có :math:`n` đỉnh thì sẽ có :math:`n - 1` cạnh bằng quy nạp.

    Với :math:`n = 1` thì cây chỉ có thể có :math:`0` cạnh (không nối đi đâu cả).

    Giả thiết quy nạp: với :math:`n \geqslant 1` thì cây :math:`T` với :math:`n` đỉnh có :math:`n - 1` cạnh. Đặt các đỉnh là :math:`v_1`, :math:`v_2`, ..., :math:`v_n`.

    Bây giờ ta thêm đỉnh :math:`v_{n+1}` vào cây :math:`T` để được cây mới :math:`T'`. Ta cần chứng minh cây mới có :math:`n` cạnh.

    Do :math:`T` liên thông nên giữa mọi cặp đỉnh :math:`u` và :math:`v` của :math:`T` đều có đường đi, giả sử là

    .. math:: u = v_{i_1} \to v_{i_2} \to \cdots \to v_{i_k} = v.

    Khi đó, nếu cả hai đỉnh :math:`u` và :math:`v` đều có cạnh nối với :math:`v_{n+1}` thì ta thu được chu trình

    .. math:: v_{n+1} \to u = v_{i_1} \to v_{i_2} \to \cdots \to v_{i_k} = v \to v_{n+1},

    như vậy sẽ không tạo thành cây. Nghĩa là từ :math:`v_{n+1}` chỉ có thể nối với một trong các đỉnh :math:`v_1`, ..., :math:`v_n` nên số cạnh chỉ có thể tăng lên :math:`1` để có được cây mới. Khi đó, với :math:`n + 1` đỉnh ta có :math:`n` cạnh, theo quy nạp ta có điều phải chứng minh.

.. admonition:: Chứng minh 2 :math:`\Rightarrow` 3
    :class: danger, dropdown

    Giả sử :math:`T` có :math:`k` thành phần liên thông :math:`T_1`, :math:`T_2`, ..., :math:`T_k`. Vì :math:`T` không chứa chu trình đơn nên các thành phần liên thông của :math:`T` cũng không chứa chu trình đơn, tức là :math:`T_1`, :math:`T_2`, ..., :math:`T_k` đều là cây.

    Gọi :math:`n_1`, :math:`n_2`, ..., :math:`n_k` lần lượt là số đỉnh của :math:`T_1`, :math:`T_2`, ..., :math:`T_k` thì

    - :math:`n_1 + \cdots + n_k = n`;
    - cây :math:`T_1` có :math:`n_1 - 1` cạnh (từ chứng minh 1 :math:`\Rightarrow` 2), tương tự cây :math:`T_2` có :math:`n_2 - 1` cạnh, ..., :math:`T_k` có :math:`n_k - 1` cạnh.

    Cộng số lượng cạnh của :math:`k` cây lại ta có tổng số cạnh của cây :math:`T`, kết hợp giả thiết ban đầu ta có

    .. math:: n_1 + n_2 + \cdots + n_k - k = n -k = n - 1.

    Như vậy :math:`k = 1`, nghĩa là :math:`T` liên thông. Từ đây, do :math:`T` không có chu trình nên nếu bỏ một cạnh bất kì thì đồ thị mới cũng không có chu trình. Đồ thị mới không thể liên thông vì nếu giả sử ngược lại (phản chứng) đồ thị mới liên thông thì nó sẽ phải là cây có :math:`n` đỉnh. Nhưng hiện tại đồ thị chỉ có :math:`n - 2` cạnh vì đã bỏ đi một cạnh, không phải :math:`n - 1`. Do đó cạnh bỏ đi là cầu.

.. admonition:: Chứng minh 3 :math:`\Rightarrow` 4
    :class: danger, dropdown

    Gọi :math:`u` và :math:`v` là hai đỉnh bất kì trong :math:`T`. Vì :math:`T` liên thông nên sẽ có một đường đi đơn từ :math:`u` tới :math:`v` là

    .. math:: u = v_{i_1} \to v_{i_2} \to \cdots \to v_{i_k} = v.

    Giả sử tồn tại một đường đi đơn khác từ :math:`u` tới :math:`v` là

    .. math:: u = v_{j_1} \to v_{j_2} \to \cdots \to v_{j_l} = v.

    Khi đó nếu ta xóa đi một cạnh ở đường đi đơn đầu nhưng không nằm trên đường đi đơn thứ hai thì :math:`u` vẫn tới được :math:`v` nhờ vào đường đi đơn thứ hai. Nói cách khác :math:`u` và :math:`v` vẫn liên thông nên dữ kiện "mọi cạnh đều là cầu" mâu thuẫn.

    Nói rõ hơn, không mất tính tổng quát, giả sử đường đi đơn thứ nhất và thứ hai có cạnh chung là :math:`v_{i_2} \to v_{i_3}`, nghĩa là :math:`v_{i_2} = v_{j_2}` và :math:`v_{i_3} = v_{j_3}`. Khi đó nếu ta xóa cạnh :math:`v_{i_2} \to v_{i_3}` thì :math:`u` vẫn tới được :math:`v` và số lượng thành phần liên thông không tăng.

.. admonition:: Chứng minh 4 :math:`\Rightarrow` 5
    :class: danger, dropdown

    Cây :math:`T` sẽ không chứa chu trình đơn vì khi đó sẽ có hai đường đi đơn từ hai điểm bất kì trên chu trình đó (chúng ta có thể tưởng tượng đi cùng chiều và ngược chiều kim đồng hồ đều có thể đi từ 1 tới 3).

    Khi đó, hai đỉnh bất kì :math:`u` và :math:`v` luôn liên thông, nghĩa là tồn tại đường đi

    .. math:: u = v_{i_1} \to v_{i_2} \to \cdots \to v_{i_k} = v.

    Nếu ta thêm bất kì bất kì cạnh nào nối giữa hai đỉnh trên đường đi, không mất tính tổng quát giả sử là :math:`v_{i_1}` và :math:`v_{i_k}`, khi đó ta có chu trình vì

    .. math:: u = v_{i_1} \to v_{i_2} \to \cdots \to v_{i_k} = v \to v_{i_1}.

    Như vậy cứ thêm vào một cạnh ta sẽ có chu trình.

.. admonition:: Chứng minh 5 :math:`\Rightarrow` 6
    :class: danger, dropdown

    Giữa hai đỉnh bất kì :math:`u` và :math:`v` của :math:`T` có hai trường hợp:

    - :math:`u` và :math:`t` được nối bởi một cạnh;
    - :math:`u` và :math:`t` không kề nhau (không có cạnh nối). Ở trường hợp này, nếu chúng ta vẽ cạnh nối :math:`u` với :math:`v` thì theo giả thiết sẽ tạo ra chu trình. Điều này chỉ xảy ra khi và chỉ khi có một đường đi đơn từ :math:`u` tới :math:`v`.

    Như vậy trong cả hai trường hợp thì luôn tồn tại đường đi từ :math:`u` tới :math:`v`, nói cách khác là hai đỉnh liên thông. Điều này đúng với mọi đỉnh trong đồ thị nên :math:`T` liên thông.

    Do ta đã chứng minh được :math:`T` liên thông, và giả thiết là :math:`T` không chứa chu trình đơn, nên suy ra :math:`T` là cây. Như vậy :math:`T` có :math:`n - 1` cạnh.

.. admonition:: Chứng minh 6 :math:`\Rightarrow` 1
    :class: danger, dropdown

    Sử dụng phản chứng, giả sử :math:`T` không là cây. Khi đó :math:`T` không liên thông hoặc :math:`T` có chu trình. Do giả thiết :math:`T` liên thông nên ta chỉ xét trường hợp :math:`T` có chu trình.

    Nếu ta bỏ một cạnh trên chu trình này thì :math:`T` vẫn liên thông. Nếu :math:`T` vẫn còn chu trình thì ta lại bỏ đi một cạnh của chu trình đó. Tiếp tục cho đến khi :math:`T` không còn chu trình nào. Lúc này :math:`T` là cây nhưng lại có ít hơn :math:`n - 1` cạnh do chúng ta đã bỏ ít nhất một cạnh. Điều này vô lí vì ở chứng minh trên (1 :math:`\Rightarrow` 2), nếu :math:`T` là cây thì :math:`T` có :math:`n - 1` cạnh. Như vậy theo phản chứng suy ra :math:`T` là cây.

.. prf:theorem:: 
    :label: thm-number-cay-khung
    
    Số cây khung của đồ thị đầy đủ :math:`K_n` là :math:`n^{n-2}`.

Đồ thị Euler và đồ thị Hamilton
===============================

Đồ thị Euler
------------

Leonhard Euler là người đầu tiên mô hình hóa bài toán rời rạc này thành một hệ thống hoàn chỉnh là Lý thuyết đồ thị hiện nay.

.. prf:definition:: Chu trình Euler
    :label: def-euler-cycle

    Chu trình đi qua tất cả các cạnh của đồ thị, mỗi cạnh đúng một lần, được gọi là **chu trình Euler** (hay **Euler circuit**, **Euler circle**, **Euler tour**).

.. prf:definition:: Đường đi Euler
    :label: def-euler-path

    Đường đi đi qua tất cả các cạnh của đồ thị, mỗi cạnh đúng một lần, được gọi là **đường đi Euler**.

Lúc này, bài toán :math:`7` cây cầu nổi tiếng của thành phố Konigsberg (nay là thành phố Kaliningrad thuộc Liên bang Nga) trở thành bài toán xác định xem có tồn tại chu trình Euler hay không.

.. prf:definition:: Đồ thị Euler
    :label: def-euler-graph
    
    Đồ thị có chu trình Euler được gọi là **đồ thị Euler** (hay **Eulerian graph**, **unicursal graph**).

.. prf:definition:: Đồ thị nửa Euler
    :label: def-half-euler-graph

    Đồ thị có đường đi Euler được gọi là **đồ thị nửa Euler** (hay **Semi-Eulerian graph**, **Traversable graph**).

Các định lí và thuật toán trên đồ thị Euler
-------------------------------------------

.. prf:theorem:: 
    :label: thm-connected-graph-euler-cycle

    Một đồ thị vô hướng liên thông :math:`G = (V, E)` có chu trình Euler khi và chỉ khi mọi đỉnh của nó đều có bậc chẵn.

.. admonition:: [TODO] Chứng minh
    :class: danger, dropdown

    **Chiều thuận.** Nếu :math:`G` có chu trình Euler thì khi đi theo chu trình đó, mỗi đỉnh sẽ đi vào một lần và đi ra một lần nên bậc của nó tăng lên :math:`2`. Áp dụng cho mỗi lần gặp một đỉnh thì cuối cùng bậc của mỗi đỉnh phải là số chẵn

    [TODO] **Chiều ngược.** Nếu mọi đỉnh của đồ thị đều có bậc chẵn, ta cần xây dựng cách tìm chu trình Euler. 

.. prf:corollary:: 
    :label: cor-euler-path

    Một đồ thị vô hướng liên thông :math:`G = (V, E)` có đường đi Euler khi và chỉ khi nó có đúng hai đỉnh bậc lẻ.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Điều kiện của đường đi Euler "lỏng hơn" chu trình vì điểm đầu không cần phải trùng với điểm cuối. Do đó nếu :math:`G` có đường đi Euler thì đỉnh bắt đầu và kết thúc sẽ có bậc lẻ, các đỉnh còn lại có bậc chẵn. Ngược lại nếu đồ thị liên thông có đúng hai đỉnh bậc lẻ, khi đó ta vẽ cạnh nối hai đỉnh đó thì tất cả đỉnh của đồ thị đều có bậc chẵn, nghĩa là tồn tại chu trình Euler. Loại bỏ cạnh đó thì ta có đường đi Euler.

[TODO] Chu trình Euler và đường đi Euler của đồ thị có hướng liên thông yếu.

Đồ thị Hamilton
---------------

Khái niệm đường đi và chu trình Hamilton được đưa ra bởi William Rowan Hamilton (1856).

.. prf:definition:: Chu trình Hamilton và đồ thị Hamilton
    :label: def-hamilton-cycle-path

    Đồ thị :math:`G = (V, E)` được gọi là **đồ thị Hamilton** (hay **Hamilton graph**) nếu tồn tại chu trình đơn đi qua tất cả các đỉnh.

    Chu trình đơn đi qua tất cả các đỉnh gọi là **chu trình Hamilton** (hay **Hamiltonian circuit**, **Hamilton circle**).

Người ta quy ước rằng đồ thị chỉ gồm một đỉnh là đồ thị Hamilton nhưng đồ thị gồm hai đỉnh liên thông không phải là đồ thị Hamilton.
