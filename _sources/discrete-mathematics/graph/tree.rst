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

Một đồ thị có thể có nhiều cây khung. Ở :numref:`hình %s <spanning-tree-1>` ta xóa đi cạnh :math:`e_{23}` và :math:`e_{46}` (hai cạnh màu đỏ) thì thu được một cây khung. Tương tự, ở :numref:`hình %s <spanning-tree-2>` ta xóa đi hai cạnh màu đỏ là :math:`e_{13}` và :math:`e_{23}` thì cũng thu được một cây khung khác.

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
