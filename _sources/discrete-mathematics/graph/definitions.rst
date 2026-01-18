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

Ở :numref:`hình %s <undirected-graph>` ta thấy :math:`\deg (v_1) = 1`, :math:`\deg (v_2) = 3`, :math:`\deg (v_3) = 1`, :math:`\deg (v_4) = 1`, :math:`\deg (v_5) = 1`, :math:`\deg (v_6) = 2`. Tổng quát ta có định lí sau.

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

Với ví dụ ở :numref:`hình %s <directed-graph>` thì:

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

Ở đồ thị trên :numref:`hình %s <subgraph-1>`, mình lấy các đỉnh :math:`v_1`, :math:`v_2`, :math:`v_4` và :math:`v_5`, và lấy các cạnh :math:`e_{24}`, :math:`e_{45}` thì mình có đồ thị con trên :numref:`hình %s <subgraph-2>`. Các bạn có thể thấy ở đồ thị ban đầu thì :math:`v_1` nối với :math:`v_2`, nhưng ở đồ thị con thì không có cạnh nối giữa hai đỉnh này.

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
