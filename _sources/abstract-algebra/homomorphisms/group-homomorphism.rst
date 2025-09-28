==================
Group homomorphism
==================

-------------
Đồng cấu nhóm
-------------

.. prf:definition:: Homomorphism, Đồng cấu nhóm
    :label: def-group-homomorphism
    
    Xét hai nhóm :math:`(G, \star)` và :math:`(H, *)` 
    và một ánh xạ :math:`f: G \to H`.

    Ánh xạ :math:`f` được gọi là **đồng cấu** 
    (hay **homomorphism**) nếu với mọi :math:`g_1`, :math:`g_2` 
    thuộc :math:`G` ta có :math:`f(g_1 \star g_2) = f(g_1) * f(g_2)`.

Do :math:`g_1`, :math:`g_2` là các phần tử thuộc 
:math:`G` nên toán tử giữa chúng là :math:`\star`. 
Trong khi đó :math:`f(g_1)`, :math:`f(g_2)` là các 
phần tử thuộc :math:`H` nên toán tử giữa chúng là :math:`*`.

.. prf:remark:: 
    :label: rmk-group-homomorphism

    1. Gọi :math:`e_G` là phần tử đơn vị của :math:`G` và 
       :math:`e_H` là phần tử đơn vị của :math:`H`. Khi đó 
       :math:`f(e_G) = e_H`.
    2. Với mọi phần tử :math:`g \in G`, nếu :math:`g^{-1}` 
       là nghịch đảo của :math:`g` trong :math:`G` thì 
       :math:`f(g^{-1}) = f(g)^{-1}`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    1. Nếu :math:`e_G` là phần tử đơn vị của :math:`G` thì 
       với mọi :math:`g \in G` ta có :math:`g \star e_G = e_G \star g = g`. 
       Ta lấy :math:`f` cả ba vế và theo định nghĩa homomorphism thu được
    
    .. math:: f(g \star e_G) = f(e_G \star g) = f(g) \Rightarrow f(g) * f(e_G) = f(e_G) * f(g) = f(g).
        
    Đẳng thức trên đúng với mọi :math:`g \in G` nên đúng 
    với mọi :math:`f(g)`, suy ra :math:`f(e_G)` là phần tử 
    đơn vị trong nhóm :math:`(H, *)` và do đó :math:`f(e_G) = e_H`.
    
    2. Từ việc tìm ra phần tử đơn vị, ta cũng chứng minh 
       được tính chất nghịch đảo trên.

---------------------
Các loại homomorphism
---------------------

Tương tự như ánh xạ, chúng ta có các loại homomorphism sau

.. prf:definition:: Monomorphism, Đơn cấu
    :label: def-group-monomorphism
    
    Ánh xạ được gọi là **đơn cấu** (hay **monomorphism**) nếu 
    nó là ánh xạ one-to-one (đơn ánh). Nói cách khác, với mọi 
    :math:`g_1`, :math:`g_2 \in G` mà :math:`g_1 \neq g_2` thì 
    :math:`f(g_1) \neq f(g_2)`.

.. prf:definition:: Epimorphism, Toàn cấu
    :label: def-group-epimorphism
    
    Ánh xạ được gọi là **toàn cấu** (hay **epimorphism**) nếu 
    nó là ánh xạ onto (toàn ánh). Nói cách khác, với mọi 
    :math:`h \in H` thì tồn tại :math:`g \in G` mà :math:`f(g) = h`.

.. prf:definition:: Isomorphism, Đẳng cấu
    :label: def-group-isomorphism
    
    Ánh xạ được gọi là **đẳng cấu** (hay **isomorphism**) nếu 
    nó là ánh xạ one-to-one và onto (song ánh). Nói cách khác, 
    ánh xạ này vừa là đơn cấu, vừa là toàn cấu.

.. prf:theorem:: Định lí Cayley
    :label: thm-cayley
    
    Mọi nhóm hữu hạn đều đẳng cấu (isomorphism) với một nhóm 
    con nào đó của nhóm hoán vị.

.. admonition:: Chứng minh định lí Cayley
    :class: danger, dropdown

    Giả sử ta có nhóm hữu hạn :math:`G = \{ g_1, g_2, \ldots g_n \}`.
    
    Với mỗi :math:`g \in G`, ta xây dựng hoán vị :math:`\varphi_g` theo :math:`g`:

    .. math:: 
    
        \begin{pmatrix}
            g_1 & g_2 & \ldots & g_i & \ldots & g_n \\
            g_1 g & g_2 g & \ldots & g_i g & \ldots & g_n g
        \end{pmatrix} = \varphi_g

    Ta chọn :math:`g', g'' \in G`. Khi đó:

    .. math:: 
        
        \varphi_{g' g''} = & \begin{pmatrix}
            g_1 & g_2 & \ldots & g_i & \ldots & g_n \\
            g_1 g' g'' & g_2 g' g'' & \ldots & g_i g' g'' & \ldots & g_n g' g''
        \end{pmatrix} \\ = & \begin{pmatrix}
            g_1 & g_2 & \ldots & g_i & \ldots & g_n \\
            g_1 g' & g_2 g' & \ldots & g_i g' & \ldots & g_n g'
        \end{pmatrix} \\ \times &  \begin{pmatrix}
            g_1 g' & g_2 g' & \ldots & g_i g' & \ldots & g_n g' \\
            (g_1 g') g'' & (g_2 g') g'' & \ldots & (g_i g') g'' & \ldots & (g_n g') g''
        \end{pmatrix}.

    Do

    .. math:: 
        
        \begin{pmatrix}
            g_1 & g_2 & \ldots g_i & \ldots & g_n \\
            g_1 g' & g_2 g' & \ldots g_i g' & \ldots & g_n g'
        \end{pmatrix} = \varphi_{g'},

    và

    .. math:: 
        
        \begin{pmatrix}
            g_1 g' & g_2 g' & \ldots & g_i g' & \ldots &  g_n g' \\
            (g_1 g') g'' & (g_2 g') g'' & \ldots & (g_i g') g'' & \ldots & (g_n g') g''
        \end{pmatrix} = \varphi(g'')

    nên :math:`\varphi_{g' g''} = \varphi(g') \cdot \varphi(g'')` 
    nên :math:`\varphi` là đồng cấu (homomorphism).

    Để chứng minh :math:`\varphi` là song ánh, ta chứng 
    minh :math:`\varphi` là đơn ánh và toàn ánh.

    Giả sử :math:`\varphi(g) = \varphi(g')`. Theo định 
    nghĩa hoán vị thì :math:`g = g'` nên :math:`\varphi` 
    là đơn ánh.

    Giả sử ta có hoán vị

    .. math:: 
        
        \sigma = \begin{pmatrix}
            g_1 & g_2 & \ldots & g_n \\
            g_1 g' & g_2 g' & \ldots & g_n g'
        \end{pmatrix},

    ta nhân với :math:`g'^{-1}` thì tìm được hoán vị 
    ngược của :math:`\sigma`. Như vậy :math:`\varphi` 
    là toàn ánh.

    Kết luận: :math:`\varphi` là song ánh và là đẳng 
    cấu (isomorphism).

.. prf:definition:: Automorphism, Tự đẳng cấu
    :label: def-group-automorphism
    
    Ánh xạ được gọi là **tự đẳng cấu** (hay **automorphism**) 
    nếu nó là song ánh từ nó lên chính nó. Ta kí hiệu tự đồng 
    cấu nhóm :math:`G` là :math:`\mathrm{Aut}(G)`.

---------------
Hạt nhân và ảnh
---------------

Xét một homomorphism :math:`f` từ nhóm :math:`(G, \star)` 
tới nhóm :math:`(H, *)`.

.. prf:definition:: Kernel, Hạt nhân
    :label: def-group-homomorphism-kernel
    
    **Hạt nhân** (hay **kernel**) của :math:`f` là tập hợp các 
    phần tử của :math:`G` cho ảnh là :math:`e_H`, kí hiệu là 
    :math:`\ker f`. Nói cách khác

    .. math:: 

        \ker f = \{ g \in G : f(g) = e_H \}.

    Như vậy $\ker f$ là tập con của :math:`G`.

.. prf:remark:: 
    :label: rmk-homomorphism
    
    :math:`K = \ker f` là normal subgroup của :math:`G`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Để chứng minh, ta thấy rằng theo định nghĩa 
    homomorphism, với :math:`g_1, g_2 \in K` thì 
    :math:`f(g_1) = f(g_2) = e_H`.

    Ta có
    
    .. math:: f(g_1 \star g_2) = f(g_1) * f(g_2) = e_H * e_H = e_H.
        
    Như vậy :math:`g_1 \star g_2 \in K` nên 
    :math:`K` là nhóm con của :math:`G`.

    Tiếp theo để chứng minh :math:`K` là normal 
    subgroup, ta chứng minh :math:`g K g^{-1} = K` 
    với mọi :math:`g \in G`.

    Do :math:`g K g^{-1} = \{ g \star k \star g^{-1} : k \in K \}`, 
    lấy :math:`f` mỗi phần tử bên trong ta có

    .. math:: f(g \star k \star g^{-1}) = f(g) * f(k) * f(g^{-1}) = f(g) * e_H * f(g^{-1}) = f(g) * f(g^{-1}),

    mà theo tính chất của homomorphism thì
    
    .. math:: f(g^{-1}) = f(g)^{-1} \Rightarrow f(g \star k \star g^{-1}) = f(g) * f(g)^{-1} = e_H,
        
    suy ra :math:`g \star k \star g^{-1} \in K` với mọi 
    :math:`g \in G`, với mọi :math:`k \in K`. Do đó 
    :math:`g K g^{-1} = K` và ta có điều phải chứng minh.

.. prf:definition:: Image, Ảnh
    :label: def-group-homomorphism-image

    **Ảnh** (hay **image**) của :math:`f` là tập hợp tất 
    cả giá trị nhận được khi biến các phần tử thuộc 
    :math:`G` thành phần tử thuộc :math:`H`. Nói cách khác

    .. math:: \mathrm{im} f = \{ f(g) : g \in G \}.

    Như vậy :math:`\mathrm{im} f` là tập con của :math:`H`.

Dựa trên hai khái niệm này, chúng ta có một định lý quan trọng 
trong lý thuyết nhóm là **Định lí thứ nhất về sự đẳng cấu** 
(First isomorphism theorem).

.. prf:theorem:: Định lí thứ nhất về sự đẳng cấu
    :label: thm-first-isomorphism
    
    Với hai nhóm :math:`(G, \star)` và :math:`(H, *)`. 
    Xét homomorphism :math:`f: G \to H`. Khi đó 
    :math:`\mathrm{im} f` đẳng cấu (isomorphism) với 
    nhóm thương :math:`G / \ker f`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Gọi :math:`G`, :math:`H` là hai nhóm và homomorphism :math:`f: G \to H`.
    
    Đặt :math:`K = \ker f`. Ta xét biến đổi

    .. math:: \theta:\,\mathrm{im} f \to G / K, f(g) \to g K

    với :math:`g \in G`.

    Ta cần chứng minh biến đổi này là ánh xạ xác định 
    (well-defined, nghĩa là tuân theo quy tắc ánh ánh 
    xạ, mỗi phần tử tập nguồn biến thành **một và chỉ một** 
    phần tử tập đích), là homomorphism, là đơn ánh và là toàn ánh.

    Đầu tiên ta chứng minh ánh xạ xác định. Giả sử ta 
    có :math:`g_1 K = g_2 K`, do :math:`g_1` và :math:`g_2` 
    thuộc cùng coset nên :math:`g_1^{-1} g_2 \in K`, 
    hay :math:`f(g_1^{-1} g_2) = e_H`.

    Với :math:`f` là homomorphism, ta có 

    .. math:: f(g_1^{-1} g_2) = f(g_1^{-1}) f(g_2) = f(g_1)^{-1} f(g_2) = e_H.

    Suy ra :math:`f(g_1) = f(g_2)`. Như vậy nếu 
    :math:`f(g_1) = f(g_2)` thì :math:`\theta (f(g_1)) = \theta (f(g_2))`.

    Tiếp theo ta chứng minh :math:`\theta` là homomorphism. 
    Do :math:`K` là normal subgroup của :math:`G` nên với mọi 
    :math:`g_1`, :math:`g_2` thuộc :math:`G` thì 
    :math:`g_1 g_2 K = (g_1 K) (g_2 K)`.

    Do :math:`f(g_1 g_2) = f(g_1) f(g_2)` nên

    .. math:: \theta (f(g_1 g_2)) = g_1 g_2 K = (g_1 K) (g_2 K) = \theta (f(g_1)) \theta (f(g_2)).

    Suy ra :math:`\theta` là homomorphism.

    Dễ thấy với mọi :math:`g \in G` ta đều tìm được 
    :math:`f(g)` và :math:`g K` tương ứng. Do đó 
    :math:`\theta` là toàn ánh.

    Để chứng minh :math:`\theta` là đơn ánh, giả sử 
    :math:`g_1 K = g_2 K` ta có :math:`g_1^{-1} g_2 \in K` 
    nên :math:`f(g_1^{-1} g_2) = e_H`, suy ra
    
    .. math:: f(g_1^{-1}) f(g_2) = e_H \Rightarrow f(g_1)^{-1} f(g_2) = e_H \Rightarrow f(g_1) = f(g_2).
        
    Như vậy :math:`\theta` là đơn ánh.

    Kết luận, :math:`\theta` là song ánh. Định lí thứ nhất 
    về sự đẳng cấu được chứng minh.

.. prf:example:: Bài tập sưu tầm từ LAPLAS
    :label: exp-laplas-1

    Chứng minh rằng :math:`\mathrm{GL}_n(\mathbb{C})/H \cong \mathbb{R}^+`, 
    với :math:`H` là nhóm con các ma trận có định thức bằng :math:`1`.

.. admonition:: Giải
    :class: danger

    Để ý rằng :math:`H` là nhóm con chuẩn tắc của 
    :math:`\mathrm{GL}_n(\mathbb{C})`. Xét ánh xạ:

    .. math:: f: \mathrm{GL}_n(\mathbb{C}) \to \mathbb{R}^+, f(\bm{A}) = \lvert\det(\bm{A})\rvert.

    Vì :math:`\det(\bm{A} \cdot \bm{B}) = \det(\bm{A}) \cdot \det(\bm{B})` 
    nên :math:`f` là đồng cấu nhóm. Khi đó với mọi số thực dương :math:`r`, 
    tồn tại ma trận :math:`\bm{A} \in \mathrm{GL}_n(\mathbb{C})` sao cho 
    :math:`f(\bm{A}) = \lvert\det(\bm{A})\rvert = r`, ví dụ như

    .. math:: 

        \begin{pmatrix}
            r & 0 & \cdots & 0 \\
            0 & 1 & \cdots & 0 \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & 0 & \cdots & 1
        \end{pmatrix}.

    Như vậy :math:`f` cũng là toàn cấu.

    Ở đây :math:`\ker f = H` nên theo định lí thứ nhất về 
    sự đẳng cấu, ta có

    .. math:: \mathrm{GL}_n(\mathbb{C}) / H \cong \mathbb{R}^+.