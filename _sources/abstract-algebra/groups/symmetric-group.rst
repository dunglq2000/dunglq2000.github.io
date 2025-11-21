Nhóm hoán vị
============

Nhóm hoán vị
------------

Xét tập hợp :math:`\{ 1, 2, \ldots, n \}`.

Ta gọi :math:`\mathcal{S}_n` là tập tất cả hoán vị của tập hợp trên. Như vậy :math:`\mathcal{S}_n` có :math:`n!` phần tử.

Nếu ta lấy hoán vị gốc là :math:`(1, 2, \ldots n)`, mỗi hoán vị đều có thể được biểu diễn bằng hai hàng như sau:

.. math:: 

    \sigma = \begin{pmatrix}
        1 & 2 & \ldots & n \\
        \sigma(1) & \sigma(2) & \ldots & \sigma(n)
    \end{pmatrix}.

Ta định nghĩa toán tử trên :math:`\mathcal{S}_n`. Với hai hoán vị :math:`\sigma` và :math:`\tau`, hoán vị :math:`\sigma \star \tau` là vị trí của :math:`\sigma` theo :math:`\tau`. Nói cách khác, nếu

.. math:: 

    \sigma = \begin{pmatrix}
        1 & 2 & \ldots & n \\
        \sigma(1) & \sigma(2) & \ldots & \sigma(n)
    \end{pmatrix}

và 

.. math:: 

    \tau = \begin{pmatrix}
        1 & 2 & \ldots & n \\
        \tau(1) & \tau(2) & \ldots & \tau(n)
    \end{pmatrix}


thì 

.. math:: 

    \sigma \star \tau =
    \begin{pmatrix}
        1 & 2 & \ldots & n \\
        \sigma(\tau(1)) & \sigma(\tau(2)) & \ldots & \sigma(\tau(n))   
    \end{pmatrix}


Tập các hoán vị :math:`\mathcal{S}_n` và toán tử như trên tạo thành một nhóm và được gọi là **nhóm hoán vị**.

.. prf:example:: 
    :label: exp-symmetric-group
    
    Xét nhóm hoán vị :math:`\mathcal{S}_5`.

    Gọi :math:`x = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 2 & 5 \end{pmatrix}` và :math:`y = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 4 & 3 & 2 \end{pmatrix}`.
    
    Khi đó, đặt :math:`z = x \star y` thì

    .. math:: 
        
        & z(1) = x(y(1)) = x(5) = 5, \\
        & z(2) = x(y(2)) = x(1) = 4, \\
        & z(3) = x(y(3)) = x(4) = 2, \\
        & z(4) = x(y(4)) = x(3) = 1, \\ 
        & z(5) = x(y(5)) = x(2) = 3.
        
    Như vậy
    
    .. math:: 
        
        z = x \star y = \begin{pmatrix}
            1 & 2 & 3 & 4 & 5 \\ 5 & 4 & 2 & 1 & 3
        \end{pmatrix}.

.. prf:remark:: 
    :label: rmk-perm-2-rows
    
    Trong một hoán vị, khi biểu diễn trên hai hàng thì thứ tự viết không quan trọng, miễn là đảm bảo :math:`i` tương ứng với :math:`\sigma(i)` trên từng cột.

.. prf:example:: 
    :label: exp-perm-operation

    Xét hoán vị :math:`\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 1 & 2 & 5 \end{pmatrix}` thuộc :math:`\mathcal{S}_5`.

    Ta có :math:`\sigma(1) = 4`, :math:`\sigma(2) = 3`, :math:`\sigma(3) = 1`, :math:`\sigma(4) = 2` và :math:`\sigma(5) = 5`. Như vậy hai cách viết sau là giống nhau

    .. math:: 

        \sigma = 
        \begin{pmatrix}
            1 & 2 & 3 & 4 & 5 \\
            4 & 3 & 1 & 2 & 5
        \end{pmatrix} = 
        \begin{pmatrix}
            3 & 4 & 5 & 1 & 2 \\
            1 & 2 & 5 & 4 & 3
        \end{pmatrix}.

Chu trình độc lập
-----------------

Xét nhóm hoán vị :math:`\mathcal{S}_n` và hoán vị :math:`\sigma` thuộc :math:`\mathcal{S}_n`.

Khi đó tồn tại các tập :math:`\{ i_1, i_2, \ldots, i_k \} \subset \{1, 2, \ldots, n\}` sao cho :math:`\sigma(i_1) = i_2`, :math:`\sigma(i_2) = i_3`, ..., :math:`\sigma(i_{k-1}) = \sigma(i_k)` và :math:`\sigma(i_k) = i_1`.

.. prf:example:: 
    :label: exp-independent-cycles-2
    
    Xét :math:`\mathcal{S}_5$ và hoán vị $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 4 & 3 & 2 \end{pmatrix}`.

    Ta thấy rằng :math:`\sigma(1) = 5`, :math:`\sigma(5) = 2`, :math:`\sigma(2) = 1`. Như vậy ta có chu trình :math:`1 \to 5 \to 2 \to 1`.

    Tương tự, :math:`\sigma(3) = 4` và :math:`\sigma(4) = 3`. Như vậy ta có thêm chu trình :math:`3 \to 4 \to 3`.

    Hai chu trình trên không chứa phần tử chung nên chúng được gọi là hai **chu trình độc lập**.

.. prf:remark:: 
    :label: rmk-prod-independent-cycles

    Mọi hoán vị đều có thể viết được dưới dạng tích của các chu trình độc lập.
    
    Chu trình có thể chứa một phần tử, tức :math:`\sigma(i) = i` với mọi :math:`i`.

.. prf:example:: 
    :label: exp-prod-indepedent-cycles

    Hoán vị :math:`\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 4 & 3 & 2 \end{pmatrix}` như trên thì ta có thể viết lại thành :math:`\sigma = (1, 5, 2)(3, 4)`.

.. prf:remark:: 
    :label: exp-order-independent-cycles
    
    Thứ tự của chu trình trong tích không quan trọng. Điều này dễ thấy vì các chu trình độc lập nhau, do đó dù viết trước hay sau thì hoán vị vẫn nằm trong chu trình đó.

Để giải thích rõ hơn, chúng ta có thể xem mỗi chu trình độc lập như một hoán vị, trong đó các phần tử không thuộc chu trình đứng yên. 

Ví dụ với chu trình :math:`(1, 5, 2) = (1, 5, 2)(3)(4)` ở trên tương đương với

.. math:: 
    
    p_1 = \begin{pmatrix}
        1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 3 & 4 & 2
    \end{pmatrix},

và với chu trình :math:`(3, 4) = (3, 4)(1)(2)(5)` tương đương với

.. math:: 
    
    p_2 = \begin{pmatrix}
        1 & 2 & 3 & 4 & 5 \\ 1 & 2 & 4 & 3 & 5
    \end{pmatrix} = \begin{pmatrix}
        5 & 1 & 3 & 4 & 2 \\ 5 & 1 & 4 & 3 & 2
    \end{pmatrix}.

Do đó tích của chúng (hay toán tử trên nhóm hoán vị) sẽ cho ra kết quả hoán vị ban đầu:

.. math:: 
    
    \underbrace{\begin{pmatrix}
        1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 4 & 3 & 2
    \end{pmatrix}}_{\sigma} = \underbrace{\begin{pmatrix}
        1 & 2 & 3 & 4 & 5 \\ 5 & 1 & 3 & 4 & 2
    \end{pmatrix}}_{p_1} \star \underbrace{\begin{pmatrix}
        5 & 1 & 3 & 4 & 2 \\ 5 & 1 & 4 & 3 & 2 
    \end{pmatrix}}_{p_2}.

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
