Bài toán decode trên linear code
===================================

.. prf:definition:: 
    :label: def-dec-lincode-1

    **Bài toán decode trên linear code** :math:`[n, k]_q` 
    **với ma trận sinh** :math:`\bm{G}` **trong điều kiện kênh 
    truyền có** :math:`t` **lỗi** là bài toán cho trước vector 
    :math:`\bm{y} \in V_n(q)`, ta tìm vector :math:`\bm{m} \in V_k(q)` 
    sao cho vector :math:`\bm{e} = \bm{y} - \bm{m} \bm{G}` có 
    trọng số Hamming bằng :math:`t`.

    **Input:** 
    
    * vector :math:`\bm{y} \in V_n(q)`;
    * ma trận sinh :math:`\bm{G}` cỡ :math:`k \times n`;
    * số tự nhiên :math:`t \in \mathbb{N}`.

    **Output:** 
    
    * vector :math:`\bm{m} \in V_k(q)` sao cho vector 
      :math:`\bm{e} = \bm{y} - \bm{m} \bm{G}` có 
      trọng số Hamming bằng :math:`t`.

.. prf:definition:: 
    :label: def-dec-lincode-2

    **Bài toán decode trên linear code** :math:`[n, k]_q` 
    **với ma trận parity-check** :math:`\bm{H}` **trong điều kiện 
    kênh truyền có** :math:`t` **lỗi** là bài toán cho trước 
    vector :math:`\bm{y} \in V_n(q)`, ta tìm vector :math:`\bm{e} \in V_n(q)` 
    sao cho :math:`\bm{e} \bm{H}^\top = \bm{y} \bm{H}^\top` 
    và vector :math:`\bm{e}` có trọng số Hamming bằng :math:`t`, 
    hay :math:`\mathrm{wt}(\bm{e}) = t`.

    **Input:** 
    
    * vector :math:`\bm{y} \in V_n(q)`, ma trận parity-check 
      :math:`\bm{H}` cỡ :math:`(n - k) \times n` và số tự nhiên 
      :math:`t \in \mathbb{N}`.

    **Output:** 
    
    * vector :math:`\bm{e} \in V_n(q)` có trọng số Hamming 
      bằng :math:`t`, hay :math:`\mathrm{wt}(\bm{e}) = t`, 
      sao cho :math:`\bm{e} \bm{H}^\top = \bm{y} \bm{H}^\top`.

Từ các bài toán decode linear code liên hệ với 
bài toán decode syndrome code.

.. prf:definition:: 
    :label: def-syndrom-decode

    **Bài toán tối ưu** (hay **bài toán tổng quát**) của 
    syndrome decode :math:`[n, k]_q` với ma trận parity-check 
    :math:`\bm{H}` là bài toán cho trước vector :math:`\bm{s} \in V_n(q)`, 
    ta tìm vector :math:`\bm{e} \in V_n(q)` sao cho 
    :math:`\bm{H} \bm{e}^\top = \bm{s}^\top` và vector :math:`\bm{e}` có 
    trọng số Hamming nhỏ nhất có thể, hay :math:`\mathrm{wt}(\bm{e}) \to \min`.

    **Input:** 

    * :math:`\bm{s} \in V_n(q)` là syndrome;
    * :math:`\bm{H}` là ma trận parity-check 
      cỡ :math:`(n - k) \times n` của :math:`[n, k]_q` code :math:`\mathcal{C}`

    **Output:**

    * vector :math:`\bm{e} \in V_n(q)` thỏa mãn 
      :math:`\bm{H} \bm{e}^\top = \bm{s}^\top` và 
      vector :math:`\bm{e}` có trọng số Hamming nhỏ nhất có thể, 
      hay :math:`\mathrm{wt}(\bm{e}) \to \min`.

.. prf:definition:: 
    :label: def-syndrom-search

    **Bài toán tìm kiếm syndrome decode** :math:`sSD(\bm{H}, \bm{s}, t)` 
    là bài toán tìm kiếm theo vector :math:`\bm{s} \in V_r(q)` 
    vector :math:`\bm{e} \in V_n(q)` có trọng số Hamming bằng 
    :math:`t`, hay :math:`\mathrm{wt}(\bm{e}) = t` 
    và :math:`\bm{H} \bm{e}^\top = \bm{s}^\top`.

    **Input:**

    - :math:`\bm{H}` là ma trận cỡ :math:`r \times n` 
      trên :math:`\mathbb{F}_q`;
    - :math:`\bm{s} \in V_r(q)` là syndrome;.
    - :math:`t \in \mathbb{N}` là trọng số Hamming

    **Output:** 
    
    * vector :math:`\bm{e} \in V_n(q)` có trọng số Hamming 
      bằng :math:`t`, hay :math:`\mathrm{wt}(\bm{e}) = t`, 
      và :math:`\bm{H} \bm{e}^\top = \bm{s}^\top`.

.. prf:definition:: 
    :label: def-syndrom-recognize

    **Bài toán nhận dạng syndrome decode** (hay **распознавательная 
    задача синдромного декодирования**) hay đơn giản là 
    **bài toán syndrome decode** (hay **задача синдромного декодирования**) 
    :math:`SD(\bm{H}, \bm{s}, t)` là bài toán xác định theo syndrome 
    :math:`\bm{s} \in V_r(q)` xem có tồn tại hay không vector 
    :math:`\bm{e} \in V_n(q)` có trọng số Hamming bằng :math:`t` 
    và thỏa mãn :math:`\bm{H} \bm{e}^\top = \bm{s}^\top`.

    **Input:**

    * :math:`\bm{H}` là ma trận cỡ :math:`r \times n` 
      trên :math:`\mathbb{F}_q`
    * :math:`\bm{s} \in V_r(q)` là syndrome;
    * :math:`t \in \mathbb{N}` là trọng số Hamming.

    **Output:** tồn tại hay không vector :math:`\bm{e} \in V_n(q)` 
    có trọng số Hamming :math:`\mathrm{wt}(\bm{e}) = t` 
    và thỏa :math:`\bm{H} \bm{e}^\top = \bm{s}^\top`.

.. prf:theorem:: Định lí từ :cite:`1055873`
    :label: thm-syndrome-dec

    Bài toán nhận dạng syndrome code 
    :math:`SD(\bm{H}, \bm{s}, t)` là NP-complete.
