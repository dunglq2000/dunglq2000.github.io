Ứng dụng 1: sắp xếp topo và bài toán xếp lịch
=============================================

Thứ tự topo
-----------

Thứ tự topo (topological ordering) của một đồ thị có hướng là một thứ tự sắp xếp của các đỉnh sao cho với mọi cung từ :math:`u` đến :math:`v` trong đồ thị, :math:`u` luôn nằm trước :math:`v` trong thứ tự.

Đồ thị có hướng :math:`G = (V, E)` được gọi là Directed Acyclic Graph (DAG) khi đồ thị đó không có chu trình (có hướng). Khi đó nếu :math:`G` là một DAG thì :math:`G` có thứ tự topo.

Ví dụ cho đồ thị sau:

.. _fig-topo-order:

.. figure:: figures/topo-order.*

   Ví dụ DAG
    
Một thứ tự topo hợp lệ: 

.. math:: 0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 7 \to 6.

Thuật toán sắp xếp Topo
-----------------------

Xét đồ thị :math:`G = (V, E)`. Ta xây dựng ý tưởng tìm thứ tự topo cho các đỉnh đồ thị.

#. Với mỗi đỉnh :math:`u \in V`, ta duyệt :math:`\mathrm{DFS}(u)`.
#. Khi duyệt :math:`\mathrm{DFS}(u)`, với mỗi đỉnh :math:`v` kề với :math:`u` ta có hai trường hợp:

   #. :math:`v` chưa được thăm: ta duyệt DFS đỉnh :math:`v`.
   #. :math:`v` đã được thăm: ta có hai trường hợp:

      #. Vòng lặp for thăm :math:`v` trước :math:`u` (thứ tự từ điển): trường hợp này không tạo ra chu trình mà do thứ tự duyệt đỉnh.
      #. :math:`v` có đường đi từ :math:`v` tới :math:`u` trong quá trình duyệt DFS. Vì có cung :math:`(u, v)` nên ở đây tồn tại chu trình, đồ thị không phải DAG.
   
Như vậy, nếu đỉnh :math:`u` đứng trước tất cả đỉnh :math:`v` kề với nó thì ta gán thứ tự topo của :math:`u` là :math:`L_u = c` và giảm :math:`c` đi một đơn vị (khởi tạo :math:`c = \lvert V \rvert` là số lượng đỉnh). Vì :math:`c > 0` nên ban đầu ta khởi tạo :math:`L_u = 0` với mọi :math:`u \in V`.

Vì ta phải duyệt hết tất cả đỉnh kề của :math:`u` thì mới gán :math:`L_u = c \neq 0` được, do đó với mỗi đỉnh :math:`v` kề :math:`u` mà (1) :math:`v` đã thăm, và (2) :math:`v` chưa có thứ tự topo, thì đồng nghĩa :math:`v` nằm trong chu trình chứa :math:`u`.

.. prf:algorithm:: Sắp xếp topo trên đồ thị có hướng
   :label: algo-graph-topo-sort

   **Input.** Đồ thị có hướng :math:`G = (V, E)`. Giả sử các đỉnh được đánh số từ :math:`0`

   **Output.** Thứ tự topo các đỉnh trong :math:`G`

   Bước khởi tạo

   #. Khởi tạo mảng :math:`L \gets \emptyset` chứa thứ tự topo đã sắp xếp.
   #. Khởi tạo mảng :math:`d_u \gets 0` với mọi :math:`u \in V` đánh dấu đỉnh đã thăm (:math:`0` nếu chưa được thăm và :math:`1` nếu đã được thăm)
   #. Khởi tạo mảng :math:`t_u \gets 0` với mọi :math:`u \in V` đánh dấu thứ tự topo của mỗi đỉnh
   #. Khởi tạo :math:`c \gets \lvert V \rvert`

   Thuật toán tìm thứ tự topo

   #. Với mọi đỉnh :math:`u`, nếu :math:`d_u = 0` (:math:`u` chưa được thăm) thì gọi hàm :math:`\mathrm{DFS}(u)`
   #. Hàm :math:`\mathrm{DFS}(u)` thực hiện:
      
      #. :math:`d_u \gets 1` (đánh dấu :math:`u` đã được thăm)
      #. Xét mọi đỉnh :math:`v` kề :math:`u` (từ :math:`u` đi tới :math:`v`)
         
         #. Nếu :math:`d_v = 1` (:math:`v` đã thăm) và :math:`t_v = 0` (:math:`v` chưa có thứ tự topo)
            
            :math:`\Rightarrow` Phát hiện chu trình, đồ thị không phải DAG, thoát chương trình
               
         #. Nếu :math:`d_v = 0`, gọi :math:`\mathrm{DFS}(v)`.

      #. Chèn :math:`u` vào phía trước :math:`L`
      #. :math:`L_u \gets c`
      #. :math:`c \gets c - 1`

Ví dụ với đồ thị không có chu trình
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig-topo-sort-1:

.. figure:: figures/topo-order.*

   Đồ thị không có chu trình

Đầu tiên khởi tạo :math:`c = \lvert V \rvert = 8`, :math:`d_u \gets 0` và :math:`t_u \gets 0` với :math:`0 \leqslant u \leqslant 7`. Xét các đỉnh từ :math:`0` tới :math:`7`:

#. Xét đỉnh :math:`0`: vì :math:`d_0 = 0` nên gọi :math:`\mathrm{DFS}(0)`:

   #. :math:`\color{red}d_0 \gets 1`
   #. Xét :math:`1` kề với :math:`0`: vì :math:`d_1 = 0` và :math:`t_1 = 0` nên gọi :math:`\mathrm{DFS}(1)`:

      #. :math:`\color{red}d_1 \gets 1`
      #. Xét :math:`2` kề với :math:`1`: vì :math:`d_2 = 0` và :math:`t_2 = 0` nên gọi :math:`\mathrm{DFS}(2)`:

         #. :math:`\color{red}d_2 \gets 1`
         #. Xét :math:`3` kề với :math:`2`: vì :math:`d_3 = 0` và :math:`t_3 = 0` nên gọi :math:`\mathrm{DFS}(3)`:

            #. :math:`\color{red}d_3 \gets 1`
            #. Xét :math:`4` kề với :math:`3`: vì :math:`d_4 = 0` và :math:`t_4 = 0` nên gọi :math:`\mathrm{DFS}(4)`

               #. :math:`\color{red}d_4 \gets 1`
               #. Không còn đỉnh nào kề với :math:`4`: chèn :math:`4` vào trước :math:`L` thu được :math:`(4)`; :math:`\color{blue}t_4 \gets 8`; :math:`\color{green}c \gets 7`

            #. Không còn đỉnh nào kề với :math:`3`: chèn :math:`3` vào trước :math:`L` thu được :math:`(3, 4)`; :math:`\color{blue}t_3 \gets 7`; :math:`\color{green}c \gets 6`

         #. Xét :math:`5` kề với :math:`2`: vì :math:`d_5 = 0` nên gọi :math:`\mathrm{DFS}(5)`:

            #. :math:`\color{red}d_5 \gets 1`
            #. Không còn đỉnh nào kề với :math:`5`: chèn :math:`5` vào trước :math:`L` thu được :math:`(5, 3, 4)`; :math:`\color{blue}t_5 \gets 6`; :math:`\color{green}c \gets 5`

         #. Không còn đỉnh nào kề với :math:`2`: chèn :math:`2` vào trước :math:`L` thu được :math:`(2, 5, 3, 4)`; :math:`\color{blue}t_2 \gets 5`; :math:`\color{green}c \gets 4`
   
      #. Xét :math:`3` kề với :math:`1`: vì :math:`\color{red}d_3 = 1` và :math:`\color{blue}t_3 = 7 \neq 0` nên bỏ qua
      #. Không còn đỉnh nào kề với :math:`1`, chèn :math:`1` vào trước :math:`L` thu được :math:`(1, 2, 5, 3, 4)`; :math:`\color{blue}t_1 \gets 4`; :math:`\color{green}c \gets 3`

   #. Xét :math:`2` kề với :math:`0`, vì :math:`\color{red}d_2 = 1` và :math:`\color{blue}t_2 = 5 \neq 0` nên bỏ qua
   #. Không còn đỉnh nào kề với :math:`0`, chèn :math:`0` vào trước :math:`L` thu được :math:`(0, 1, 2, 5, 3, 4)`; :math:`\color{blue}t_0 \gets 3`; :math:`\color{green}c \gets 2`

#. Xét các đỉnh :math:`1`, :math:`2`, :math:`3`, :math:`4` và :math:`5` đều đã được thăm nên ta bỏ qua
#. Xét đỉnh :math:`6`, vì :math:`d_6 = 0` nên gọi :math:`\mathrm{DFS}(6)`:

   #. :math:`\color{red}d_6 \gets 1`
   #. Không còn đỉnh nào kề với :math:`6`, chèn :math:`6` vào trước :math:`L` thu được :math:`(6, 0, 1, 2, 5, 3, 4)`; :math:`\color{blue}t_6 \gets 2`; :math:`\color{green}c \gets 1`

#. Xét đỉnh :math:`7`, vì :math:`d_7 = 0` nên gọi :math:`\mathrm{DFS}(7)`:

   #. :math:`\color{red}d_7 \gets 1`
   #. Xét :math:`6` kề với :math:`7`, vì :math:`\color{red}d_6 = 1` và :math:`\color{blue}t_6 = 2 \neq 0` nên bỏ qua
   #. Không còn đỉnh nào kề với :math:`7`, chèn :math:`7` vào trước :math:`L` thu được :math:`(7, 6, 0, 1, 2, 5, 3, 4)`, :math:`\color{blue}t_7 \gets 1`; :math:`\color{green}c \gets 0`

Nhận xét:

#. Đồ thị trên có hai phần rời nhau, do đó thứ tự giữa mỗi phần tử trong tập :math:`\{ 0, 1, 2, 3, 4, 5 \}` không liên quan đến tập :math:`\{ 6, 7 \}`.
#. Đỉnh :math:`6` được duyệt trước đỉnh :math:`7` và nhận được thứ tự topo. Do đó khi duyệt đỉnh :math:`7`, vì :math:`6` kề :math:`7` và đã có thứ tự topo nên không phải chu trình.

Tiếp theo ta sẽ xét một ví dụ khác với chu trình.

Ví dụ với đồ thị có chu trình
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig-topo-sort-2:

.. figure:: figures/topo-order-2.*

   Đồ thị có chu trình

Đầu tiên khởi tạo :math:`c = \lvert V \rvert = 3`, :math:`d_u \gets 0` và :math:`t_u \gets 0` với :math:`0 \leqslant u \leqslant 2`. Xét các đỉnh từ :math:`0` tới :math:`2`:

#. Xét đỉnh :math:`0`: vì :math:`d_0 = 0` nên gọi :math:`\mathrm{DFS}(0)`:

   #. :math:`\color{red}d_0 \gets 1`
   #. Xét :math:`1` kề với :math:`0`: vì :math:`d_1 = 0` và :math:`t_1 = 0` nên gọi :math:`\mathrm{DFS}(1)`:

      #. :math:`\color{red}d_1 \gets 1`
      #. Xét :math:`2` kề với :math:`1`: vì :math:`d_2 = 0` và :math:`t_2 = 0` nên gọi :math:`\mathrm{DFS}(2)`:

         #. :math:`\color{red}d_2 \gets 1`
         #. Xét :math:`0` kề với :math:`2`: vì :math:`\color{red}d_0 = 1` và :math:`t_0 = 0`, ta phát hiện chu trình và kết thúc thuật toán.

Ở ví dụ này, thuật toán đã gặp điều kiện :math:`d_v = 1` và :math:`t_v = 0` (:prf:ref:`algo-graph-topo-sort`), và phát hiện chu trình.

Đánh giá thuật toán
^^^^^^^^^^^^^^^^^^^

1. Mỗi đỉnh :math:`u \in V` ta chỉ duyệt qua một lần nên độ phức tạp là :math:`O(\lvert V \rvert)`.
2. Với mỗi đỉnh :math:`u \in V`, ta duyệt tất cả đỉnh kề một lần, tương ứng duyệt tất cả các cung một lần, nên độ phức tạp là :math:`O(\lvert E \rvert)`.
3. Như vậy tổng độ phức tạp của giải thuật trên là :math:`O(\lvert V \rvert + \lvert E \rvert)`.

Ứng dụng giải bài toán xếp lịch
-------------------------------

Thuật toán sắp xếp topo được ứng dụng hỗ trợ cho rất nhiều giải thuật quy hoạch động trên mảng trật tự topo.

Mô tả bài toán: ở trường Đại học U nọ có một số học phần được gọi là "học phần tiên quyết" --- là học phần mà sinh viên bắt buộc phải học trước khi học một vài học phần khác. Các sinh viên cần phải sắp xếp lịch học sao cho phù hợp với yêu cầu "học phần tiên quyết". Là một nhân viên xếp lịch học, bạn hãy đưa ra số kì tối thiểu mà sinh viên cần học.

1. **Input**: :math:`N` môn học, :math:`M` quan hệ "tiên quyết" giữa hai môn :math:`u` và :math:`v`.
2. **Output**: Số kì tối thiểu cần học.

Đầu tiên ta cần một số nhận xét:
    
1. Nếu môn :math:`u` là môn tiên quyết của môn :math:`v` và được học ở học kì thứ :math:`i` (:math:`i \geqslant 1`), thì môn :math:`v` phải được học ở học kì :math:`k` với :math:`k > i`.
2. Với một dãy liên tục các môn :math:`a_i`, :math:`a_{i+1}`, ..., :math:`a_k` mà :math:`a_i` là môn tiên quyết của :math:`a_{i+1}` thì số kì tối thiểu mà sinh viên cần học chính là độ dài của dãy.
3. Không có trường hợp một dãy :math:`a_i`, :math:`a_{i+1}`, ...., :math:`a_i` (không được phép có chu trình).
4. Đáp án của bài toán chính là độ dài dài nhất của dãy các môn trên.

Dựa vào các nhận xét trên, ta có thể áp dụng thuật toán sắp xếp topo kết hợp ý tưởng quy hoạch động để giải quyết. Trong quá trình duyệt của thuật toán, ta luôn đảm bảo thứ tự topo --- cũng là thứ tự môn học, đồng thời ta có thể dùng một mảng để tính được số kì tối thiểu cần để kết thúc các môn học. Đáp án sẽ là phần tử lớn nhất của mảng này.

Ta sẽ xây dựng một mô hình đồ thị để lưu trữ thông tin trên máy tính. Các thông tin cần lưu trữ:

1. :math:`N` môn học tương ứng :math:`N` đỉnh.
2. :math:`M` quan hệ :math:`(u, v)` tương ứng môn :math:`u` là tiên quyết của môn :math:`v`, khi đó trên đồ thị ta vẽ cung :math:`u \to v`.
3. Đồ thị DAG để đảm bảo tính thực tế.
4. Số môn cần học trước môn :math:`u` để :math:`u` có thể được học.

Với các thông tin cần lưu trữ, thuật toán dưới đây dưới sẽ lưu trữ đồ thị dưới dạng danh sách kề.

1. ``vector<int> vs[maxn]`` --- mảng ``vs`` chứa :math:`M` cung; ``vs[u]`` chứa các đỉnh kề đỉnh ``u``;
2. ``int f[maxn]`` --- ``f[u]``  lưu số kì tối đa cần học sau môn ``u``.

Thuật toán:

1. B1: Nhập dữ liệu, lưu trữ dưới dạng danh sách kề.
2. B2: Duyệt các đỉnh, nếu đỉnh ``u`` chưa duyệt ta sẽ gọi hàm ``DFS(u)``.

   1. Với mỗi đỉnh ``u``, duyệt các đỉnh ``v`` kề với ``u``.
   2. Nếu ``v`` chưa được duyệt thì ta gọi hàm ``DFS(v)``.
   3. Ngược lại ta cập nhật ``f[u] = max(f[u], f[v]+1)``;
   4. Lặp lại B2 cho đến khi mọi đỉnh được duyệt.

3. B3: Cập nhật đáp án từ các ``f[u]``.

Ví dụ demo ở đoạn code sau.

.. code-block:: cpp

   #include <vector>
   #include <iostream>

   using namespace std;

   int n, m;                   // số lượng đỉnh, số lượng cạnh
   vector<vector<int>> vs;     // danh sách kề
   vector<int> f;              // lưu thứ tự topo + đánh dấu đỉnh đã thăm

   void DFS(int u);

   int main()
   {
      cin >> n >> m;
      
      f.resize(n);
      vs.resize(n);

      for (int i = 0; i < n; i++) f[i] = 0;

      for (int i = 0; i < m; i++)
      {
         int u, v;
         cin >> u >> v;
         vs[u].push_back(v); // cung (u, v)
      }
      
      int ans = 0;
      for (int u = 0; u < n; u++)
         if (f[u] == 0 )
         {
               DFS(u);
               ans = max(ans , f[u]);
         }
      cout << "So ki toi thieu: " << ans << endl;
      return 0;
   }

   void DFS(int u)
   {
      f[u] = 1;
      for (int i = 0; i < vs[u].size(); i++)
      {
         int v = vs[u][i];
         if (f[v] == 0) // v chưa được thăm
               DFS(v);
         f[u] = max(f[v] + 1, f[u]); // cập nhật giá trị f[u]
      }
   }

Chúng ta thử chạy bộ dữ liệu ở :numref:`hình %s <fig-topo-sort-1>`. Đầu vào như sau:

.. code-block:: text

   8 8
   0 1
   0 2
   1 2
   1 3
   2 3
   3 4
   2 5
   7 6

Kết quả số kì tối thiểu là :math:`5`. Điều này hợp lý vì khi in mảng ``f`` các bạn sẽ thấy thứ tự topo như sau:

+--------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Môn học      | :math:`0` | :math:`1` | :math:`2` | :math:`3` | :math:`4` | :math:`5` | :math:`6` | :math:`7` |
+==============+===========+===========+===========+===========+===========+===========+===========+===========+
| Thứ tự topo  | :math:`5` | :math:`4` | :math:`3` | :math:`2` | :math:`1` | :math:`1` | :math:`1` | :math:`2` |
+--------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

- ở học kì 1 (thứ tự topo là :math:`5`) sinh viên học môn :math:`0` (không có môn tiên quyết);
- ở học kì 2 (thứ tự topo là :math:`4`) sinh viên học môn :math:`1` (môn tiên quyết là :math:`0`);
- ở học kì 3 (thứ tự topo là :math:`3`) sinh viên học môn :math:`2` (môn tiên quyết là :math:`0` và :math:`1`);
- ở học kì 4 (thứ tự topo là :math:`2`) sinh viên học môn :math:`3` (môn tiên quyết là :math:`1` và :math:`2`) và môn :math:`7` (không có môn tiên quyết);
- ở học kì 5 (thứ tự topo là :math:`1`) sinh viên học môn :math:`4` (môn tiên quyết là :math:`3`), môn :math:`5` (môn tiên quyết là :math:`2`) và môn :math:`6` (môn tiên quyết là :math:`7`).

.. figure:: figures/topo_schedule-1.*

   Thứ tự môn học từ thuật toán

Nhận xét thuật toán

1. Từ đỉnh ``u`` gọi hàm ``DFS(v)``, ta chắc chắn có ``f[u] <= f[v]``. Do đó ta chỉ cần lấy ``f[u]`` lớn nhất được gọi từ hàm ``main``.
2. Vì bài toán không yêu cầu đưa ra một thứ tự topo cụ thể, nên ta có thể lược bỏ một số thao tác không cần thiết trong giải thuật sắp xếp topo.
3. Thuật toán dựa trên vòng duyệt DFS của thuật toán topo do đó có độ phức tạp :math:`O(\lvert V \rvert + \lvert E \rvert)`.
4. Đây chỉ là một ứng dụng rất cơ bản của thuật toán sắp xếp topo. Từ bài toán này, ta có thể phát triển theo nhiều hướng khác, ứng dụng cho nhiều trường hợp hơn.
5. Trên thực tế có thể có nhiều thứ tự topo và thuật toán trên chỉ đưa ra một thứ tự đơn giản. Chúng ta có thể thấy ở bộ dữ liệu trên:

   * môn :math:`7` không có môn tiên quyết nên hoàn toàn có thể được học ở học kì 1 thay vì ở học kì 4, theo đó môn :math:`6` có thể học ở học kì 2, 3, 4, hoặc 5;
   * môn :math:`3` và :math:`5` đều có môn tiên quyết là :math:`2` nên có thể được học ở cùng học kì 4, thay vì phải để môn :math:`5` tới học kì :math:`5`.

   .. figure:: figures/topo_schedule-2.*

      Một thứ tự môn học khác