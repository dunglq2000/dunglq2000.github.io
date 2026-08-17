Bài toán decode tổng quát
=========================

Khi vector :math:`\bm{x}` được truyền qua kênh truyền, 
không gì đảm bảo chúng ta sẽ nhận được chính xác 
:math:`\bm{x}` ở bên nhận, mà có thể là :math:`\bm{y}` nào đó.

Các codeword nằm trong một block code nào đó là tập con 
của :math:`V_n(q)`, trong khi ở bên nhận có thể là một 
vector bất kỳ trong :math:`V_n(q)`. Bài toán decode đặt ra 
câu hỏi, làm sao biết được vector :math:`\bm{y}` sẽ được 
decode thành vector nào trong block code.

.. prf:definition:: Bài toán decode
    :label: def-dec-prob-1

    Bài toán decode của :math:`(n)_q` code :math:`\mathcal{C}` 
    là bài toán cho trước vector :math:`\bm{y} \in V_n(q)`, 
    ta tìm codeword :math:`\bm{c} \in \mathcal{C}` của code 
    :math:`(n)_q` sao cho :math:`\rho_H (\bm{c}, \bm{y}) = \min\limits_{\bm{c}' \in \mathcal{C}} \rho_H (\bm{c}', \bm{y})` 
    với :math:`\rho_H` là khoảng cách Hamming.
    
    **Input:**
    
    * vector :math:`\bm{y} \in V_n(q)` nhận được từ kênh truyền;
    * :math:`\mathcal{C}` là :math:`(n)_q` code.

    **Output:** 
    
    * vector :math:`\bm{c} \in \mathcal{C}` là codeword 
      sao cho :math:`\displaystyle{\rho_H (\bm{c}, \bm{y}) = \min_{\bm{c}' \in \mathcal{C}} \rho_H(\bm{c}', \bm{y})}`.

.. prf:definition:: Bài toán decode
    :label: def-dec-prob-2

    Bài toán decode của :math:`(n)_q` code :math:`\mathcal{C}` 
    là bài toán cho trước vector :math:`\bm{y} \in V_n(q)`, 
    ta tìm codeword :math:`\bm{c} \in \mathcal{C}` của code 
    :math:`(n)_q` sao cho :math:`\mathrm{wt}(\bm{y} - \bm{c}) = \min\limits_{\bm{c}' \in \mathcal{C}} \mathrm{wt}(\bm{y} - \bm{c}')` 
    với :math:`\mathrm{wt}` là trọng số Hamming.

    **Input:** 
    
    * vector :math:`\bm{y} \in V_n(q)` là vector 
      nhận được từ kênh truyền; 
    * :math:`\mathcal{C}` là :math:`(n)_q` code.

    **Output:** 
    
    * vector :math:`\bm{c} \in \mathcal{C}` là codeword 
      sao cho :math:`\mathrm{wt}(\bm{y} - \bm{c}) = \min\limits_{\bm{c}' \in \mathcal{C}} \mathrm{wt} (\bm{y} - \bm{c}')`.

.. prf:definition:: Bài toán decode
    :label: def-dec-prob-3

    Bài toán decode của :math:`(n)_q` code :math:`\mathcal{C}` 
    là bài toán cho trước vector :math:`\bm{y} \in V_n(q)`, 
    ta tìm vector :math:`\bm{e} \in V_n(q)` sao cho :math:`\bm{y} - \bm{e} \in \mathcal{C}`, 
    nghĩa là :math:`\bm{y} - \bm{e}` là codeword, và vector 
    :math:`\bm{e}` có trọng số Hamming nhỏ nhất :math:`\mathrm{wt}(\bm{e}) \to \min`.

    **Input:** 
    
    * vector :math:`\bm{y} \in V_n(q)` là vector 
      nhận được từ kênh truyền; 
    * :math:`\mathcal{C}` là :math:`(n)_q` code.

    **Output:** 
    
    * vector :math:`\bm{e} \in V_n(q)` sao cho :math:`\bm{y} - \bm{e} \in \mathcal{C}`, 
      nghĩa là :math:`\bm{y} - \bm{e}` là codeword;
    * và vector :math:`\bm{e}` có trọng số Hamming nhỏ nhất 
      :math:`\mathrm{wt}(\bm{e}) \to \min`.

.. prf:remark:: 
    :label: rmk-dec-prob

    Các định nghĩa về bài toán decode ở trên tương đương nhau.

.. prf:definition:: Decoder
    :label: def-decoder

    **Decoder** của code :math:`(n)_q` :math:`\mathcal{C}` 
    là thuật toán mà với vector :math:`\bm{y} \in V_n(q)` 
    cho trước, tìm được codeword :math:`\bm{c} \in \mathcal{C}` 
    sao cho vector :math:`\bm{e} = \bm{y} - \bm{c}` có 
    trọng số Hamming nhỏ nhất có thể, nghĩa là 
    :math:`\bm{c} = \underset{\bm{u} \in \mathcal{C}}{\operatorname{argmin}} \mathrm{wt}(\bm{y} - \bm{u})`. 
    
    Decoder của code :math:`\mathcal{C}` sẽ giải bài toán decode trên code :math:`\mathcal{C}`.
