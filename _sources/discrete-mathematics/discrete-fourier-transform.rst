Biến đổi Fourier rời rạc
************************

Phần này mình dịch từ :cite:`Vasilenko`.


Giới thiệu
==========

Cho số :math:`t \in \mathbb{N}` và :math:`n = 2^t`.

Gọi :math:`R` là vành với đơn vị :math:`1`. Vành :math:`R` 
chứa phần tử :math:`2^{-1}` là nghịch đảo của phần tử :math:`2`. 
Hơn nữa vành :math:`R` cũng chứa phần tử :math:`\zeta_{2n}` là 
một nghiệm cố định nào đó của phương trình :math:`x^n + 1 = 0`. 
Đặt :math:`\zeta_n = \zeta_{2n}^2`.

.. prf:example:: 
    :label: DFT-exp-ring

    Trên :math:`\mathbb{C}` thì :math:`\zeta_{2n} = e^{\pi i/n}` 
    là một nghiệm của phương trình :math:`x^n + 1 = 0`. Khi đó 
    :math:`\zeta_n = \zeta_{2n}^2 = e^{2\pi i /n}`.

.. prf:lemma::
    :label: DFT-lem-z2n

    Phần tử :math:`\zeta_{2n}` sinh ra một nhóm vòng (cyclic group) 
    với order :math:`2n` trong nhóm nhân của vành :math:`R`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Do :math:`\zeta_{2n}` là nghiệm của phương trình :math:`x^n + 1 = 0` 
    nên :math:`\zeta_{2n}^n = -1`, hay :math:`\zeta_{2n}^{2^t} = -1`. 
    Từ đó suy ra :math:`\left(\zeta_{2n}^{2^t}\right)^2 = 1` 
    nên order của phần tử :math:`\zeta_{2n}` là :math:`2^{t+1} = 2n`.

Giả sử :math:`(f_0, \ldots, f_{n-1}) \in R^n` là vector bất kì. 
Khi đó:

**Biến đổi Fourier loại 1** của vector trên là vector :math:`n` 
chiều :math:`(\hat f_0, \ldots, \hat f_{n-1})` thuộc :math:`R^n` 
xác định bởi:

.. math:: \hat f_i = \sum_{j=0}^{n-1} \zeta_n^{ij} f_j, \quad i = 0, 1, \ldots, n-1.

**Biến đổi Fourier loại 2** của vector trên là vector :math:`n` 
chiều :math:`(\check f_1, \check f_3, \ldots, \check f_{2n-1})` 
thuộc :math:`R^n` xác định bởi:

.. math:: \check f_i = \sum_{j=0}^{n-1} \zeta_{2n}^{ij} f_j, \quad i = 1, 3, \ldots, 2n-1.

.. prf:example:: 
    :label: exp-DFT-3

    Mình lấy ví dụ với vector :math:`(f_0, f_1, f_2) = (1, 2, 3)` thuộc 
    :math:`\mathbb{C}^3`.

    Chọn nghiệm :math:`\zeta_{2n} = e^{\pi i / 3}` của 
    phương trình :math:`x^3 + 1 = 0`. Khi đó 
    :math:`\zeta_n = \zeta_{2n}^2 = e^{2\pi i / 3}`.

    Biến đổi Fourier loại 1 lúc này là:

    .. math:: 
        
        \hat{f}_0 & = \left(e^{2\pi i/3}\right)^{0 \cdot 0} \cdot 1 + \left(e^{2\pi i/3}\right)^{0 \cdot 1} \cdot 2 + \left(e^{2\pi i/3}\right)^{0 \cdot 2} \cdot 3 \\
        & = 1 + 2 + 3 = 6. \\
        \hat{f}_1 & = \left(e^{2\pi i/3}\right)^{1 \cdot 0} \cdot 1 + \left(e^{2\pi i/3}\right)^{1 \cdot 1} \cdot 2 + \left(e^{2\pi i/3}\right)^{1 \cdot 2} \cdot 3 \\
        & = 1 + 2 \cdot e^{2\pi i/3} + 3 \cdot 3 \cdot e^{4\pi i/3} \\
        \hat{f}_2 & = \left(e^{2\pi i/3}\right)^{2 \cdot 0} \cdot 1 + \left(e^{2\pi i/3}\right)^{2 \cdot 1} \cdot 2 + \left(e^{2\pi i/3}\right)^{2 \cdot 2} \cdot 3 \\
        & = 1 + 2 \cdot e^{4\pi i/3} + 3 \cdot e^{2\pi i/3}.
        
    Chú ý rằng :math:`e^{2\pi i} = 1` nên biểu thức cuối 
    của :math:`\hat{f}_2` rút gọn còn :math:`e^{2\pi i / 3}` (:math:`8 \equiv 2 \bmod 3`).

    Tiếp theo ta biểu diễn :math:`e^{4\pi i / 3}` 
    theo :math:`e^{2\pi i / 3}` như sau. Ta xét

    .. math:: 
        
        e^{2zi} & = \cos 2z + i\sin 2z \\
        & = 2\cos^2 z - 1 + 2i \sin z \cos z \\
        & = 2\cos z (\cos z + i\sin z) - 1 \\
        & = 2\cos z \cdot e^{zi} - 1.
        
    Thay :math:`z = 2\pi / 3` vào kết quả trên 
    ta được

    .. math:: e^{4\pi i / 3} = 2\cos \frac{2\pi}{3} \cdot e^{2\pi i/3} - 1 = -e^{2\pi i / 3} - 1.

    Như vậy kết quả của biến đổi Fourier rời rạc 
    bên trên là

    .. math:: (\hat{f}_0, \hat{f}_1, \hat{f}_2) =  (6, -e^{2\pi i / 3} - 2, e^{2\pi i / 3} - 1).

Ở ví dụ trên chúng ta tính biến đổi Fourier cho 
vector có độ dài không phải lũy thừa của :math:`2`. 
Sau đây chúng ta sẽ xem xét một ví dụ với vector 
có độ dài là lũy thừa của :math:`2` và ở phần sau 
sẽ tối ưu tính toán với biến đổi Fourier nhanh.

.. prf:example:: 
    :label: exp-DFT-4

    Mình lấy ví dụ với vector :math:`(f_0, f_1, f_2, f_3) = (1, 2, 3, 4)` 
    thuộc :math:`\mathbb{C}^4`.

    Chọn nghiệm :math:`\zeta_{2n} = e^{i\pi / 4}` của phương 
    trình :math:`x^4 + 1 = 0`. Khi đó :math:`\zeta_n = \zeta_{2n}^2 = e^{i \pi / 2} = i`.

    Biến đổi Fourier loại 1 lúc này là:

    .. math:: 

        \hat{f}_0 & = 1 \cdot 1 + 2 \cdot 1 + 3 \cdot 1 + 4 \cdot 1 = 10, \\
        \hat{f}_1 & = 1 \cdot 1 + 2 \cdot i + 3 \cdot (-1) + 4 \cdot (-i) = -2 - 2i, \\
        \hat{f}_2 & = 1 \cdot 1 + 2 \cdot (-1) + 3 \cdot 1 + 4 \cdot (-1) = -2, \\
        \hat{f}_3 & = 1 \cdot 1 + 2 \cdot (-i) + 3 \cdot (-1) + 4 \cdot i = -2 + 2i. 

Đối với vector độ dài :math:`n = 2^2` thì :math:`t = 2`, 
chúng ta cần :math:`n - 1` phép cộng và :math:`n` phép 
nhân với lũy thừa của :math:`\zeta_{n}` để tính mỗi 
:math:`\hat{f}_i`, với :math:`i = 0, 1, 2, 3`. Tổng 
quát, ta cần tất cả :math:`(n + n - 1) \cdot n` phép 
tính cộng và nhân với lũy thừa của :math:`\zeta_n`. 
Độ phức tạp để tính biến đổi Fourier rời rạc là :math:`O(n^2)`.

.. prf:remark:: 
    :label: DTF-F-hat-check

    Các phần tử :math:`\hat f_i` là giá trị của đa 
    thức :math:`F(x) = \sum\limits_{j=0}^{n-1} f_j x^j \in R[x]` 
    tại điểm :math:`x = \zeta_n^i`, các phần tử 
    :math:`\check f_i` là giá trị của đa thức 
    :math:`F(x)` tại :math:`x = \zeta_{2n}^i` 
    khi :math:`i` lẻ.

.. prf:lemma::
    :label: fi

    Ta có biểu diễn ngược như sau:

    .. math:: 
        :label: fi-fhat

        f_i = n^{-1} \sum_{j=0}^{n-1} \hat f_j \zeta_n^{-ij},

    .. math:: 
        :label: fi-fcheck

        f_i = n^{-1} \sum_{\substack{1 \leqslant j \leqslant 2n-1 \\ j \ \text{lẻ}}} \check f_j \zeta_{2n}^{-ij},

    với :math:`n^{-1} = (2^{-1})^t \in R`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`k \in \mathbb{Z}`. Khi đó 
    :math:`\zeta_{2n}^{-k} = \zeta_{2n}^{2nr - k}` 
    với :math:`r \in \mathbb{Z}`, :math:`2nr - k \geqslant 0`.

    Ngoài ra, vì order của phần tử :math:`\zeta_n` 
    trong phép nhân là :math:`n` nên ta có:

    .. math:: 
        :label: l0

        \sum_{j = 0}^{n - 1} \zeta_n^{lj} = n \quad \text{khi} \quad l \equiv 0 \pmod n,

    .. math:: 
        :label: l1
        
        \sum_{j = 0}^{n - 1} \zeta_n^{lj} = 0 \quad \text{khi} \quad l \not\equiv 0 \pmod n.

    Phương trình :eq:`fi-fhat` thỏa mãn vì:

    .. math:: \sum_{j=0}^{n-1} \hat f_j \zeta_n^{-ij} = \sum_{j=0}^{n-1} \sum_{k=0}^{n-1} f_k \zeta_n^{jk} \zeta_n^{-ij} = \sum_{k=0}^{n-1} f_k \sum_{j=0}^{n-1} \zeta_n^{(k-i)j} = n f_i

    theo :eq:`l0` và :eq:`l1`, cụ thể là khi 
    :math:`k - i \equiv 0 \bmod n`.

    Đẳng thức :eq:`fi-fcheck` có được từ

    .. math::  
        
        \sum_{\substack{1 \leqslant j \leqslant 2n - 1 \\ j \ \text{lẻ}}} \check f_j \zeta_{2n}^{-ij} & = \sum_{k=0}^{n-1} \check f_{2k+1} \zeta_{2n}^{-i(2k+1)} \\ 
        & = \sum_{k=0}^{n-1} \sum_{l=0}^{n-1} f_l \zeta_{2n}^{l(2k+1)} \zeta_{2n}^{-i(2k+1)} \\
        & = \sum_{l=0}^{n-1} f_l \zeta_{2n}^{l-i} \sum_{k=0}^{n-1} \zeta_n^{(l-i) k}. 

    Từ :eq:`l0` và :eq:`l1` suy ra được đẳng thức :eq:`fi-fcheck`, cũng là khi :math:`l - i \equiv 0 \bmod n`.

Việc tính toán biến đổi Fourier rời rạc bằng :eq:`fi-fhat` 
và :eq:`fi-fcheck` cần :math:`O(n^2)` phép tính 
cộng và nhân trong vành :math:`R`. Phần sau sẽ 
trình bày phương pháp tính biến đổi Fourier rời 
rạc với độ phức tạp :math:`O(n \log n)`. Phương 
pháp này được gọi là **biến đổi Fourier nhanh** 
(hay **Fast Fourier Transform**, **FFT**, 
**быстрое преобразование Фурье**).


Biến đổi Fourier nhanh
======================

.. prf:theorem::
    :label: DFT-fhat-fcheck

    Biến đổi Fourier rời rạc :math:`(\hat f_0, \ldots, \hat f_{n-1})` 
    có thể được tính bằng:

    - :math:`nt` phép cộng trong vành :math:`R`;
    - :math:`nt` phép nhân với lũy thừa của 
      :math:`\zeta_n` trong vành :math:`R`.

    Biến đổi Fourier rời rạc :math:`(\check f_1, \ldots, \check f_{2n-1})` 
    có thể được tính bằng:

    - :math:`nt` phép cộng trong vành :math:`R`;
    - :math:`nt` phép nhân với lũy thừa của 
      :math:`\zeta_{2n}` trong vành :math:`R`.

    Nếu có :math:`(\hat f_i)` và :math:`(\check f_i)` 
    thì có thể tính được vector :math:`(f_0, \ldots, f_{n-1})` 
    bằng:

    - :math:`nt` phép cộng trong vành :math:`R`;
    - :math:`nt` phép nhân với lũy thừa của 
      :math:`\zeta_{2n}` trong vành :math:`R`;
    - :math:`n` phép nhân với :math:`n^{-1} \in R`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt

    .. math:: 
        
        F(x) = \sum_{j=0}^{n-1} f_i x^i & = \sum_{\substack{0 \leqslant j \leqslant n-1 \\ j \ \text{chẵn}}} f_j x^j + \sum_{\substack{0 \leqslant j \leqslant n-1 \\ j \ \text{lẻ}}} f_j x^j \\
        & = F_0(x^2) + x F_1(x^2),
        

    với :math:`\deg F_0(x), \deg F_1(x) < \dfrac{n}{2} = 2^{t-1}`.

    Khi đó

    .. math:: 
        :label: DFT-F

        F(\zeta_n^i) = F_0(\zeta_n^{2i}) + \zeta_n^i F_1(\zeta_n^{2i}),

    với :math:`i = 0, \ldots, n-1`.

    Đặt :math:`\zeta_{n/2} = \zeta_n^2`. Khi đó

    .. math:: \left\{ \zeta_n^{2i} : 0 \leqslant i \leqslant n - 1 \right\} = \left\{ \zeta_{n/2}^i : 0 \leqslant i \leqslant \dfrac{n}{2} - 1\right\}.

    Dựa trên quy nạp ta sẽ chứng minh biến đổi Fourier 
    rời rạc loại 1, tức là tính :math:`(F(\zeta_n^0), \ldots, F(\zeta_n^{n-1}))`, 
    theo công thức :eq:`DFT-F` bằng :math:`n` phép cộng 
    trong vành :math:`R` và :math:`n` phép tính nhân với 
    lũy thừa của :math:`\zeta_n` trong vành :math:`R` nếu 
    ta đã biết các giá trị :math:`F_0(\zeta_{n/2}^i)` và 
    :math:`F_1(\zeta_{n/2}^i)` với :math:`i = 0, \ldots, \dfrac{n}{2} - 1`.

    Khi :math:`t = 1` và :math:`n = 2 = 2^t` (bước cơ sở quy nạp) 
    thì để tính :math:`(\hat f_0, \hat f_1)` ta cần tìm 
    :math:`F_0 + \zeta_2^i F_1` với :math:`F_0` và :math:`F_1` 
    là các phần tử thuộc vành :math:`R`, :math:`i = 0, 1`. 
    Như vậy, với :math:`n = 2` thì cần:

    - :math:`2 = nt` phép nhân với lũy thừa của :math:`\zeta_n = \zeta_2` 
      trong vành :math:`R`, ứng với :math:`\zeta_2^i F_1` khi :math:`i = 0, 1`;
    - :math:`2 = nt` phép cộng trong vành :math:`R`, ứng với 
      :math:`F_0 {\color{red}+} \zeta_2^i F_1`.

    Giả sử với mọi :math:`j < t`, để tính biến đổi Fourier 
    rời rạc loại 1 trên vector :math:`2^j` chiều ta cần:

    - :math:`2^j \cdot j` phép nhân với lũy thừa của 
      :math:`\zeta_{2^j} = \left(\zeta_n\right)^{2^{t-j}}` 
      trong vành :math:`R`;
    - :math:`2^j \cdot j` phép cộng trong vành :math:`R`.

    Khi đó, nếu :math:`j = t` thì việc tính 
    :math:`(\hat f_0, \ldots, \hat f_{n-1})` theo 
    công thức :eq:`DFT-F` bao gồm tính :math:`F_0(\zeta_{n/2}^i)` 
    và :math:`F_1(\zeta_{n/2}^i)` với :math:`i = 0, \ldots, n-1`. 
    Nói cách khác là tính biến đổi Fourier cho 
    vector độ dài :math:`n / 2` gồm các hệ số :math:`F_0(x)` 
    và :math:`F_1(x)` cộng thêm:

    - :math:`n` phép cộng trong vành :math:`R`;
    - :math:`n` phép nhân với lũy thừa của 
      :math:`\zeta_n` trong vành :math:`R`.

    Khi đó, theo giả thiết quy nạp, việc tính vector 
    :math:`(\hat f_0, \ldots, \hat f_{n-1})` cần 
    không nhiều hơn:

    - :math:`n` phép cộng trong vành :math:`R`;
    - cộng với :math:`n` phép nhân trong vành :math:`R`;
    - cộng với :math:`2 \cdot 2^{t-1} \cdot (t-1)` 
      phép nhân với lũy thừa của :math:`\zeta_n` trong 
      vành :math:`R`.

    Như vậy cần tổng cộng :math:`n + n(t - 1) = nt` phép 
    cộng trong vành :math:`R` và :math:`n + n(t-1) = nt` 
    phép nhân với lũy thừa của :math:`\zeta_n` trong vành 
    :math:`R`. Như vậy mệnh đề đầu tiên của định lý được 
    chứng minh.

    Mệnh đề thứ hai chứng minh tương tự, ta thay 
    :math:`\zeta_n` thành :math:`\zeta_{2n}`.

    Mệnh đề thứ ba suy ra từ hai mệnh đề trên và :prf:ref:`fi`.

.. prf:example:: 
    :label: exp-FFT-4

    Xét vector :math:`(f_0, f_1, f_2, f_3) = (1, 2, 3, 4)` 
    thuộc :math:`\mathbb{C}^4` như bên trên.

    Ở đây, :math:`n = 4 = 2^2` và :math:`t = 2`.

    Chọn nghiệm :math:`\zeta_{8} = e^{i\pi / 4}` của phương 
    trình :math:`x^4 + 1 = 0`. Khi đó 
    :math:`\zeta_4 = \zeta_{8}^2 = e^{i \pi / 2} = i`.

    Ta chia vector thành hai phần:

    - vector con gồm các phần tử ở vị trí chẵn là 
      :math:`(f_0, f_2) = (1, 3)`;
    - vector con gồm các phần tử ở vị trí lẻ là 
      :math:`(f_1, f_3) = (2, 4)`.

    Đặt :math:`\zeta_2 = \zeta_{4}^2 = -1`.

    Khi đó, với vector con :math:`(f_0, f_2) = (1, 3)` 
    ta tính:

    .. math:: 

        F_0 & = f_0 + \zeta_{2}^0 \cdot f_2 = 1 + 1 \cdot 3 = 4, \\
        F_1 & = f_0 + \zeta_{2}^1 \cdot f_2 = 1 + (-1) \cdot 3 = -2.
    
    Tương tự, với vector con 
    :math:`(f_1, f_3) = (2, 4)` ta tính

    .. math:: 

        F_2 & = f_1 + \zeta_{2}^0 \cdot f_3 = 2 + 1 \cdot 4 = 6, \\
        F_3 & = f_1 + \zeta_{2}^1 \cdot f_3 = 2 + (-1) \cdot 4 = -2.

    Kết hợp hai vector :math:`(F_0, F_2)` và 
    :math:`(F_3, F_4)` ta tính được biến đổi 
    Fourier nhanh.

    .. math:: 

        \hat{f}_0 & = F_0 + \zeta_4^0 \cdot F_2 = 4 + 1 \cdot 6 = 10, \\
        \hat{f}_2 & = F_0 + \zeta_4^2 \cdot F_2 = 4 + (-1) \cdot 6 = -2, \\
        \hat{f}_1 & = F_1 + \zeta_4^1 \cdot F_3 = -2 + i \cdot (-2) = -2 - 2 i, \\
        \hat{f}_3 & = F_1 + \zeta_4^3 \cdot F_3 = -2 + (-i) \cdot (-2) = -2 + 2i.

    Ở đây, hệ số :math:`\hat{f}_i` ở vị trí lẻ 
    sẽ được tính nhờ các :math:`F_i` ở vị trí lẻ 
    cùng với lũy thừa lẻ của :math:`\zeta_n`, và 
    ngược lại, hệ số :math:`\hat{f}_i` ở vị trí 
    chẵn sẽ được tính nhờ các :math:`F_i` ở vị 
    trí chẵn cùng với lũy thừa chẵn của :math:`\zeta_n`.
    
    Như vậy kết quả là
    
    .. math:: (\hat{f}_0, \hat{f}_1, \hat{f}_2, \hat{f}_3) = (10, -2 - 2i, -2, -2 + 2i),

    giống với ví dụ ở trên. Tuy nhiên chúng ta chỉ 
    dùng :math:`4` phép cộng và :math:`4` phép nhân 
    với :math:`\zeta_{2}` để tính các :math:`F_i`, 
    cộng thêm :math:`4` phép cộng và :math:`4` phép 
    nhân với :math:`\zeta_4` để tính các :math:`\hat{f}_i`. 
    Như vậy tổng cộng ta dùng :math:`8 = n t` phép cộng, 
    và :math:`8 = n t` phép nhân cho các lũy thừa của 
    :math:`\zeta_4` (vì :math:`\zeta_{2}` cũng là lũy 
    thừa của :math:`\zeta_4`).


Biến đổi Fourier và phép nhân đa thức
=====================================

.. prf:lemma::
    :label: DFT-mult-poly

    Một phép nhân trong vành :math:`R[x]/(x^{2^t} + 1)` 
    có thể được tính bởi:

    - :math:`n = 2^t` phép nhân trong vành :math:`R`;
    - :math:`3nt` phép cộng trong vành :math:`R`;
    - :math:`3nt` phép nhân với lũy thừa của 
      :math:`\zeta_{2n}` trong vành :math:`R`;
    - :math:`n` phép nhân với :math:`n^{-1}` 
      trong vành :math:`R`.

.. prf:remark:: 
    :label: DFT-no-mult-poly

    Bổ đề không áp dụng khi :math:`R = \mathbb{Z}` và 
    :math:`R = \mathbb{Q}` vì hai vành này không có 
    phần tử :math:`\zeta_{2n}` (căn bậc :math:`n` của 
    đơn vị).

Sau đây ta chứng minh :prf:ref:`DFT-mult-poly`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`\sum\limits_{i=0}^{n-1} f_i x^i` và 
    :math:`\sum\limits_{i=0}^{n-1} g_i x^i` với 
    :math:`F, G \in R[x]` và là biểu diễn của phần 
    tử trong lớp nhân tử :math:`R[x]/(x^{2^t} + 1)`.

    Đặt :math:`H = \sum\limits_{i=0}^{n-1} h_i x^i \in R[x]` 
    sao cho :math:`F \cdot G \equiv H \pmod{x^n+1}`. Nói 
    cách khác :math:`H` là tích :math:`F \cdot G` trong 
    vành và ta sẽ tính :math:`H`.

    Biến đổi Fourier loại 2 cho vector 
    :math:`(f_0, \ldots, f_{n-1})` và :math:`(g_0, \ldots, g_{n-1})` 
    cho ta đẳng thức:

    .. math:: \check f_i \cdot \check g_i = F(\zeta_{2n}^i) \cdot G(\zeta_{2n}^i) = H(\zeta_{2n}^i) = \check h_i

    với :math:`i` lẻ, :math:`1 \leqslant i \leqslant 2n-1`, 
    vì :math:`\zeta_{2n}^n + 1 = 0`.

    Như vậy nếu ta biết tất cả :math:`\check f_i` và 
    :math:`\check g_i` thì có thể tính mọi :math:`\check h_i` 
    với :math:`n` phép nhân trong vành :math:`R`.

    Theo :prf:ref:`DFT-fhat-fcheck`, các phần tử 
    :math:`\check f_i` và :math:`\check g_i` có thể 
    tính với :math:`2tn` phép cộng trong vành :math:`R` 
    và :math:`2tn` phép nhân với lũy thừa của 
    :math:`\zeta_{2n}` trong vành :math:`R`.

    Cũng theo :prf:ref:`DFT-fhat-fcheck`, các phần tử 
    :math:`h_i` có thể tính, với điều kiện đã biết 
    :math:`\check h_i`, với

    * :math:`tn` phép cộng trong vành :math:`R`;
    * :math:`tn` phép nhân với lũy thừa của 
      :math:`\zeta_{2n}` trong vành :math:`R`
    * :math:`n` phép nhân với phần tử 
      :math:`n^{-1}` trong vành :math:`R`.

    Ta có điều phải chứng minh.

.. prf:corollary:: 
    :label: DFT-cor-1

    Đặt :math:`T` là vành giao hoán với đơn vị, 
    :math:`2^{-1} \in T`, :math:`\zeta_{4n} = \zeta_{2^{t + 2}} \in T` 
    là nghiệm phương trình :math:`x^{2n} + 1 = 0`. 
    Nếu :math:`F(x), G(x) \in T[x]`, :math:`\deg F(x) < n`, 
    :math:`\deg G(x) < n` thì tích :math:`F(x) \cdot G(x)` 
    có thể tính với:

    - :math:`2n` phép nhân trong :math:`T`;
    - :math:`6n(t+1)` phép cộng trong :math:`T`;
    - :math:`6n(t+1)` phép nhân với lũy thừa 
      của :math:`\zeta_{4n}` trong :math:`T`;
    - :math:`2n` phép nhân với :math:`(2^{-1})^{t+1}` 
      trong :math:`T`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Vì chặn trên của bậc đa thức :math:`F(x)` và 
    :math:`G(x)` nên bậc của :math:`F(x) \cdot G(x)` 
    sẽ nhỏ hơn :math:`2n`. Khi chia 
    :math:`F(x) \cdot G(x)` cho :math:`2^{2n} + 1` 
    ta thu được chính đa thức :math:`F(x) \cdot G(x)`. 
    Khi đó tích :math:`F(x) \cdot G(x)` trong 
    :math:`R[x]` có thể tính với một phép nhân 
    trong :math:`R[x] / (x^{2n} + 1)`. 
    Từ :prf:ref:`DFT-lem-z2n`, ta thay :math:`n` 
    thành :math:`2n` và :math:`t` thay thành 
    :math:`t+1`, kết hợp :prf:ref:`DFT-mult-poly` 
    ta có điều phải chứng minh.

Đặt :math:`T` là vành giao hoán với đơn vị 
:math:`1` và có phần tử :math:`2^{-1}`.

Ta hiểu phép cộng trong :math:`T` là cả phép cộng 
lẫn phép trừ (cộng cho số đối). Ta cần bổ đề cơ 
sở sau.

.. prf:lemma::
    :label: Tx

    Nếu :math:`t \geqslant 2` thì một phép nhân 
    trong vành :math:`T[x] / (x^{2^t} + 1)` 
    có thể thực hiện với:

    - :math:`O(2^t \cdot t)` phép nhân trong 
      :math:`T`;
    - :math:`O(2^t \cdot t \cdot \log t)` phép 
      cộng trong :math:`T`.

.. prf:remark:: 
    :label: DFT-rem-Tx

    Kết quả trên có thể áp dụng với vành số 
    nguyên :math:`\mathbb{Z}` nếu ta xem :math:`T` 
    là vành như sau:

    .. math:: T = \left\{\frac{m}{2^k} : m \in \mathbb{Z}, k \in \mathbb{Z}_{\geqslant 0}\right\}, \quad T \supseteq \mathbb{Z}.

    Trên máy tính, mỗi phần tử của :math:`T` 
    được lưu chính xác, ví dụ dưới dạng cặp :math:`(m, k)`.

Ta sẽ xem xét định lí quan trọng tiếp theo 
rồi quay lại chứng minh :prf:ref:`Tx`.

.. prf:theorem:: 
    :label: DFT-thr-Tx
    
    Phép nhân hai đa thức có bậc không quá :math:`n` 
    trong vành :math:`T[x]`, với :math:`n \geqslant 3`, 
    được tính với :math:`M(n) = O(n \log n)` phép nhân 
    trong :math:`T` và :math:`A(n) = O(n \log n \log \log n)` 
    phép cộng trong :math:`T`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Gọi :math:`t \in \mathbb{N}` là số sao cho 
    :math:`2^{t-1} \leqslant 2n < 2^t`. Dễ thấy 
    :math:`t \geqslant 2` và :math:`2n < 2^t < 4n`.

    Do đó phép nhân hai đa thức có bậc không quá 
    :math:`n` theo modulo :math:`x^{2^t} + 1` là 
    phép nhân thông thường, kết quả không thay đổi 
    sau phép modulo.

    Theo :prf:ref:`Tx` thì ta có thể tính tích 
    với :math:`M(n) = O(2^t \cdot t) = O(n \log n)` 
    phép nhân trong :math:`T` và 
    :math:`A(n) = O(2^t \cdot t \log t) = O(n \cdot \log n \cdot \log \log n)` 
    phép cộng trong :math:`T`.

Tiếp theo chúng ta quay lại chứng minh :prf:ref:`Tx`.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Đặt :math:`F = F(x)` và :math:`G = G(x)` là 
    các đa thức bậc không quá :math:`2^t - 1`. Đặt

    .. math:: H = H(x) = \sum_{i=0}^{2^t - 1} H_i x^i

    với :math:`H = FG \pmod{x^{2^t} + 1}`. Ta cần 
    tính các hệ số :math:`H_0`, :math:`H_1`, ..., 
    :math:`H_{2^t - 1}` theo các hệ số của :math:`F` 
    và :math:`G`.

    Đặt :math:`k` là tham số tự nhiên với 
    :math:`1 \leqslant k < t` mà ta sẽ chọn ở dưới.

    Ta biểu diễn :math:`F` và :math:`G` dưới dạng

    .. math:: F = \sum_{i = 0}^{2^{t - k} - 1} f_i(x) x^{i \cdot 2^k}, \quad G = \sum_{i = 0}^{2^{t - k} - 1} g_i(x) x^{i \cdot 2^k}

    với

    - :math:`f_i(x), g_i(x) \in T[x]`;
    - :math:`\deg f_i(x) \leqslant 2^k - 1`;
    - :math:`\deg g_i(x) \leqslant 2^k - 1`.

    Thuật toán tính :math:`F \cdot G` được thực hiện 
    theo các bước sau.

    **Bước 1.** Nhân :math:`\sum\limits_{i=0}^{2^{t-k} - 1} f_i(x) Y_i` 
    với :math:`\sum\limits_{i=0}^{2^{t-k} - 1} g_i(x) Y_i` 
    trên vành :math:`T[x, Y] / (Y^{2^{t - k} - 1})`. 
    Kết quả được biểu diễn bởi 
    :math:`\widetilde{H} = \sum\limits_{i=0}^{2^{t-k} - 1} h_i(x) Y^i`.

    **Bước 2.** Thay :math:`Y = x^{2^k}` vào 
    :math:`\widetilde{H}` vào tính modulo 
    :math:`x^{2^t} + 1 = Y^{2^{t - k}} + 1`. Khi đó

    .. math:: F(x) \cdot G(x) = \sum_{l=0}^{2^{t-k} - 1} f_l(x) x^{2^k l} \cdot \sum_{j=0}^{2^{t-k} - 1} g_j(x) x^{2^k j} \equiv \sum_{i=0}^{2^{t-k} - 1} h_i(x) x^{2^k i} \pmod{(x^{2^k})^{2^{t-k}} + 1}.

    Từ bước 2 ta sẽ tính được 
    :math:`H(x) = \sum\limits_{i=0}^{2^t - 1} H_i x^i`. 
    Ta cần hiểu tại sao ở bước 2 dãy :math:`\{ h_i(x) \}` 
    theo modulo :math:`x^{2^t} + 1` tìm được hệ số 
    :math:`H_i` của :math:`H(x)`.

    Ở bước 1 ta nhân

    .. math:: \sum_{l=0}^{2^{t-k} - 1} f_l(x) Y^l \cdot \sum_{j=0}^{2^{t-k}-1} g_j(x) Y^j \equiv \sum_{i=0}^{2^{t-k} - 1} h_i(x) Y^i \pmod{Y^{2^{t-k}} + 1}.

    Ở đây :math:`l + j \leqslant 2^{t - k + 1} - 2 < 2^{t-k+1} - 1`. 
    Khi đó có hai trường hợp có thể xảy ra.

    **Trường hợp 1.** Nếu 
    :math:`0 \leqslant l + j \leqslant 2^{t-k} - 1` thì

    .. math:: Y^l \cdot Y_j \equiv Y^{l + j} \pmod{Y^{2^{t - k}} + 1}.

    **Trường hợp 2.** Nếu 
    :math:`2^{t - k} \leqslant l + j \leqslant 2 \cdot 2^{t - k} - 2` 
    thì

    .. math:: Y^{l + j} \equiv -Y^i \pmod{Y^{2^{t-k}} + 1},

    với :math:`i = l + j - 2^{t-k}`.

    Khi đó

    .. math:: h_i(x) = \sum_{\substack{l, j \\ j + j = i}} f_l(x) g_j(x) - \sum_{\substack{l, j \\ l + j = i + 2^{t - k}}} f_l(x) g_j(x),

    với :math:`i = 0, \ldots, 2^{t - k} - 1`.

    Từ đây suy ra

    .. math:: \deg h_i(x) \leqslant \deg f_l(x) = \deg g_j(x) \leqslant 2^{k+1} - 2 < 2^{k+1} - 1.

    Vì :math:`k < t` nên :math:`\deg h_i < 2^t - 1`.

    Bước 2 thực hiện không nhiều hơn :math:`2^t` 
    phép cộng trên :math:`T` vì nếu chúng ta đã 
    biết các giá trị 
    :math:`h_i(x) = \sum\limits_{j = 0}^{2^{k+1} - 1} h_{ij} x^j` 
    thì khi thay :math:`Y = x^{2^k}` ta có biểu thức

    .. math:: \sum_{i = 0}^{2^{t-k} - 1} \sum_{j=0}^{2^{k+1} - 1} h_{ij} x^{j + 2^k i} \pmod{x^{2^t} + 1}.

    Phép tính modulo :math:`x^{2^t} + 1` ta sẽ 
    được các biểu thức với :math:`j + 2^k i \geqslant 2^t`.

    Khi đó, với :math:`j + 2^k i = r 2^t + l`, 
    :math:`0 \leqslant l < 2^t`, nếu thay 
    :math:`x^{j + 2^k i}` thành :math:`(-1)^r \cdot x^l` 
    thì đại lượng :math:`(-1)^r \cdot h_{ij}` sẽ 
    được thêm vào hệ số của :math:`x^l` (tức là 
    thực hiện một phép cộng hoặc trừ). Các phép 
    cộng như vậy sẽ không lớn hơn số lượng số 
    hạng, tức là không lớn hơn 
    :math:`2^{t - k} \cdot 2^{k + 1} = 2^{t + 1}`.

    Ở đây, khi :math:`0 \leqslant i \leqslant 2^{t - k + 1}` 
    ta có bất đẳng thức

    .. math:: j + 2^k \cdot i \leqslant 2^{k + 1} - 1 + 2^{t - 1} - 2^k = 2^k + 2^{t - 1} - 1 \leqslant 2^t - 1

    vì :math:`k \leqslant t - 1`. Với những số 
    :math:`i` như vậy thì phép tính modulo là 
    không cần thiết.

    Lúc này còn các giá trị :math:`i` trong đoạn 
    :math:`2^{t - k - 1} \leqslant i \leqslant 2^{t - k} - 1`, 
    số lượng các giá trị này không nhiều hơn 
    :math:`2^{t - k - 1}`. Khi đó, cặp :math:`(i, j)` 
    ở bước 2 sẽ triệt tiêu theo modulo, và có không 
    nhiều hơn :math:`2^{t - k - 1} \cdot 2^{k + 1} = 2^t` 
    cặp. Như vậy ta đã chứng minh được ở bước 2 
    thực hiện không nhiều hơn :math:`2^t` phép 
    cộng trong :math:`T`.

    Bây giờ xét bước 1. Phép nhân ta không thực hiện 
    trong vành :math:`T[x, Y] / (Y^{2^{t - k}}  - 1)` 
    mà trong vành :math:`R[Y] / (Y^{2^{t - k}} - 1)` 
    với :math:`R = T[x] / (x^{2^{k+1}} + 1)`.

    Trong vành :math:`R` có phần tử 
    :math:`\zeta_{2^{k+2}} \equiv x \pmod{x^{2^{k+1}} + 1}` 
    là nghiệm phương trình :math:`X^{2^{k+1}} + 1 = 0`.

    Chọn :math:`k = \left[\dfrac{t}{2}\right] \geqslant 1`. 
    Khi đó

    .. math:: k \geqslant \frac{t-1}{2}, \quad k \leqslant \frac{t}{2} < t.

    Vì :math:`2^{t - k + 1} \leqslant 2^{k+2}` nên 
    trong :math:`R` có phần tử :math:`\zeta_{2^{t-k+1}}` 
    là một lũy thừa của phần tử :math:`\zeta_{2^{k+2}}`.

    Một phép nhân cho lũy thừa của phần tử 
    :math:`\zeta_{2^{t-k+1}}` trong vành 
    :math:`R` được thực hiện bởi :math:`2^{k+1}` 
    phép cộng trong :math:`T`.

    Vì :math:`x \equiv \zeta_{2^{k+2}} \pmod{x^{2^{k+1}} + 1}` nên

    .. math:: R = \left\{a_0 + a_1 \zeta_{2^{k+2}} + \cdots + a_{2^{k+1}} \zeta_{2^{k+2}}^{2^{k+1} - 1} : a_i \in T, i = 0, 1, \ldots, 2^{k+1} - 1\right\}.

    Phép nhân với :math:`\zeta_{2^{t-k+1}}^j = \zeta_{2^{k+2}}^{j}` 
    với đẳng thức :math:`\zeta_{2^{k+2}}^{2^{k+1}} = -1` 
    sẽ cho kết quả là hoán vị các hệ số 
    :math:`a_0`, :math:`a_1`, ..., :math:`a_{2^{k+1} - 1}` 
    và một số phần tử sẽ đổi dấu.

    Ta dùng :prf:ref:`DFT-mult-poly` để đánh giá độ 
    phức tạp của một phép nhân trong vành 
    :math:`R[Y] / (Y^{2^{t-k}} + 1)`.

    Ta cần thực hiện:

    - :math:`2^{t-k}` phép nhân trong :math:`R`;
    - :math:`3 \cdot (t - k) \cdot 2^{t-k}` phép 
      cộng trong :math:`R` (ở đây có 
      :math:`3 \cdot (t - k) \cdot 2^{t-k} \cdot 2^{k+1}` 
      phép cộng trong :math:`T` vì các phần tử của 
      vành :math:`R` được biểu diễn bởi đa thực bậc 
      không quá :math:`2^{k+1} - 1` trong :math:`T[x]`);
    - :math:`3 \cdot (t - k) \cdot 2^{t-k}` phép nhân 
      với lũy thừa của :math:`\zeta_{2^{t-k+1}}`;
    - :math:`2^{t-k}` phép nhân với :math:`(2^{-1})^{t-k}` 
      (lần nữa, cần :math:`2^{t-k} \cdot 2^{k+1} = 2^{t+1}` 
      phép nhân trong :math:`T` cho phần tử 
      :math:`(2^{-1})^{t-k}`).

    Tổng cộng ta cần:

    - :math:`2^{t-k}` phép nhân trong :math:`R`;
    - :math:`6 \cdot (t - k) \cdot 2^{k+1}` phép 
      cộng trong :math:`T`;
    - :math:`2^{t+1}` phép nhân cho 
      :math:`(2^{-1})^{t-k}` trong :math:`T`.

    Ta tính thêm :math:`2^t` phép cộng trong 
    :math:`T` ở bước 2, đặt

    .. math:: 
        :label: kt
        
        k(t) = k + 1 = \left[\frac{t}{2}\right] + 1 \geqslant 2.

    Khi đó, một phép nhân trong 
    :math:`T[x] / (x^{2^{k+1}} + 1)` được thực hiện 
    bởi :math:`2^{t - k(t) + 1}` phép nhân trong 
    vành :math:`R = T[x] / (x^{2^{k(t)}} + 1)`, 
    cộng với không nhiều hơn :math:`12 \cdot t \cdot 2^t` 
    phép cộng trong :math:`T`, cộng với 
    :math:`2^{t+1}` phép nhân trong :math:`T`.

    Khi :math:`t \geqslant 3` thì :math:`k(t) < t`. 
    Ta chuyển phép nhân ở trên trong vành 
    :math:`T[x] / (x^{2^t} + 1)` thành phép nhân 
    trong vành :math:`T[x] / (x^{2^{k(t)}} + 1)`, 
    và đi xuống tiếp cho tới khi gặp vành 
    :math:`T[x] / (x^4 + 1)`. Ở bước cuối 
    này phép nhân bất kì đều cần :math:`O(1)` 
    phép cộng và phép nhân trong :math:`T`.

    Ta kí hiệu :math:`M_1(2^j)` và :math:`A_1(2^j)` 
    là số lượng phép nhân và cộng trong :math:`T`, 
    tương ứng với số lượng cần thiết để thực hiện 
    phép nhân ở trên trong vành 
    :math:`T[x] / (x^{2^j} + 1)`.

    Khi đó, với :math:`t \geqslant 3` ta có 
    bất đẳng thức

    .. math::     
        
        M_1(2^t) & \leqslant 2^{t - k(t) + 1} \cdot M_1(2^{k(t)}) + 2^{t+1}, \\
        A_1(2^t) & \leqslant 2^{t - k(t) + 1} \cdot A_1(2^{k(t)}) + 12 \cdot t \cdot 2^t,
        
    với :math:`k(t)` định nghĩa ở :eq:`kt`.

    Đặt :math:`\alpha(j) = \dfrac{A_1(2^j)}{2^j}` 
    với :math:`j = 2, 3, \ldots`

    Khi đó :math:`\alpha(j) \leqslant 2\alpha(k(t)) + 12t`.

    Giả sử ta có bất đẳng thức sau với 
    :math:`2 \leqslant j \leqslant t`:

    .. math:: \alpha(j) \leqslant c \cdot j \log j

    với hằng số tuyệt đối :math:`c` nào đó.

    Khi đó ta có bất đẳng thức

    .. math:: \alpha(t) \leqslant 2c \cdot k(t) \cdot \log(k(t)) + 12t \leqslant 2c \left(\frac{t}{2} + 1\right) \log\left(\frac{t}{2} + 1\right) + 12t < c \cdot t\log t

    khi hằng số :math:`c` đủ lớn.

    Như vậy

    .. math:: A_1(2^t) \leqslant 2^t \cdot c \cdot t\log t = O(2^t \cdot t\log t)

    và ta đã chứng minh được ý thứ hai 
    của :prf:ref:`Tx` về phép cộng.

    Bây giờ, lại đặt :math:`\beta(j) = \dfrac{M_1(2^j)}{2^j}` 
    với :math:`j = 2, 3, \ldots`

    Ta có bất đẳng thức

    .. math:: \beta(t) \leqslant 2\beta(k(t)) + 2.

    Từ đây suy ra

    .. math:: \beta(t) \leqslant 2(2\beta(k(k(t))) + 2) + 2 = 2^2\beta(k(k(t))) + 2^2 + 2,

    và tương tự như vậy.

    Vì :math:`k(t) \leqslant \dfrac{t}{2} + 1` nên

    .. math:: k(k(t)) \leqslant \dfrac{1}{2}\left(\dfrac{t}{2} + 1\right) + 1 = \dfrac{t}{2^2} + 1 + \dfrac{1}{2}; \ldots; k(k(\ldots(k(t))\ldots)) < \dfrac{t}{2^j} + 2

    với mọi :math:`j \geqslant 1`. 
    Vì vậy khi :math:`j = \left[\log_2 t\right]` 
    ta có bất đẳng thức

    .. math:: \beta(t) \leqslant 2^j \cdot c_1 + 2 + 2^2 + \cdots + 2^j < 2^j \cdot c_1 + 2^{j+1} \leqslant c_2 t

    với :math:`c_1`, :math:`c_2` là các hằng số 
    tuyệt đối.

    Như vậy :math:`M_1(t) = O(t \cdot 2^t)` và 
    ta đã chứng minh xong ý đầu của :prf:ref:`Tx`.


Ví dụ nhân đa thức với Sympy
============================

Để ví dụ, mình sẽ viết chương trình Python nhân hai đa thức 
bậc :math:`4` trên :math:`\mathbb{Q}` trong modulo :math:`x^4 + 1`.

Thuật toán ở các chứng minh trên là thuật toán Cooley-Tukey FFT.

Đầu tiên mình sẽ viết hàm đảo ngược bit (dùng cho radix-2 decimal-in-time).

.. code-block:: python

  def _reverse_bit(n: int, nbits: int) -> int:
    m = 0
    for _ in range(nbits):
        m = (m << 1) + (n & 1)
        n = n >> 1
    return m

  assert _reverse_bit(3, 3) == 6
  assert _reverse_bit(1, 3) == 4

FFT là thuật toán chia để trị -- để tính toán FFT cho vector 
độ dài :math:`n = 2^t`, ta sẽ tính trên hai vector độ dài 
:math:`n / 2` và kết hợp kết quả lại.

.. code-block:: python

  from sympy import pi, sin, cos, I, simplify
  from sympy.codegen.cfunctions import log2

  def _mult_W(v: list[int]) -> list[int]:
    n = len(v)
    w = cos(2 * pi / n) + I * sin(2 * pi / n)
    u = [0] * n
    for i in range(0, n // 2):
        u[i] = v[i] + w**i * v[i + n // 2]
        u[i + n // 2] = v[i] + w**(i + n // 2) * v[i + n // 2]
    return u

  def _fft(v: list[int]) -> list[int]:
      n = len(v)

      if n == 2:
          return _mult_W(v)
      else:
          u = _fft(v[:n // 2]) + _fft(v[n // 2:])
          return _mult_W(u)

  def fft(v: list[int]) -> list[int]:
      n = len(v)
      b = int(log2(n))
      idx = [_reverse_bit(i, b) for i in range(n)]
      v = [v[idx[i]] for i in range(n)]

      return list(map(simplify, _fft(v)))
      
  def _mult_iW(v: list[int]) -> list[int]:
      n = len(v)
      w = cos(-2 * pi / n) + I * sin(-2 * pi / n)
      u = [0] * n
      for i in range(0, n // 2):
          u[i] = v[i] + w**i * v[i + n // 2]
          u[i + n // 2] = v[i] + w**(i + n // 2) * v[i + n // 2]
      return u

  def _ifft(v: list[int]) -> list[int]:
      n = len(v)
      if n == 2:
          return _mult_iW(v)
      else:
          u = _ifft(v[:n // 2]) + _ifft(v[n // 2:])
          return _mult_iW(u)

  def ifft(v: list[int]) -> list[int]:
      n = len(v)
      b = int(log2(n))
      idx = [_reverse_bit(i, b) for i in range(n)]
      v = [v[idx[i]] for i in range(n)]

      return [simplify(i / n) for i in _ifft(v)]

Tiếp theo mình kiểm tra các hàm đã viết bên trên.

.. code-block:: python

  assert fft([2, 3, 0, 0]) == [5, 2 + 3*I, -1, 2 - 3*I]
  assert ifft([5, 2 + 3*I, -1, 2 - 3*I]) == [2, 3, 0, 0]

  import random
  v = [random.randint(-4, 4) for _ in range(8)]
  assert ifft(fft(v)) == v, fft(v)

Ví dụ, để nhân hai đa thức

.. math:: 

  a(x) & = 1 + 2x - x^2 + 3x^3, \\
  b(x) & = -1 - 4x + 3x^2 - 2x^3,

trong modulo :math:`x^4 + 1`, đầu tiên mình viết hệ số 
của mỗi đa thức thành vector theo số mũ tăng dần, như 
vậy

.. math:: 

  \bm{a} = (1, 2, -1, 3), \quad \bm{b} = (-1, -4, 3, -2).

Tiếp theo, mình sẽ thêm vào sau các vector :math:`\bm{a}` 
và :math:`\bm{b}` các số :math:`0` để đạt độ dài là lũy 
thừa của :math:`2` nhưng lớn hơn bậc của modulo. Ở đây 
modulo là :math:`x^4 + 1` nên mình sẽ thêm các số :math:`0` 
để đạt độ dài :math:`4 \cdot 2 = 8`.

.. math:: 

  \bm{a}' = (1, 2, -1, 3, 0, 0, 0, 0), \quad \bm{b}' = (-1, 4, 3, -2, 0, 0, 0, 0).

Tiếp theo, mình áp dụng FFT cho hai vector :math:`\bm{a}'` 
và :math:`\bm{b}'`.

.. code-block:: python

  a = [1, 2, -1, 3, 0, 0, 0, 0]
  b = [-1, -4, 3, -2, 0, 0, 0, 0]

  fa = fft(a)
  fb = fft(b)

Đặt

.. math:: 

  \bm{f}_a & = \mathsf{FFT}(\bm{a}') = (a_0, a_1, \ldots, a_7), \\
  \bm{f}_b & = \mathsf{FFT}(\bm{b}') = (b_0, b_1, \ldots, b_7).

Khi đó ta tính vector :math:`\bm{f}_c` theo là tích theo cặp 
của :math:`\bm{f}_a` và :math:`\bm{f}_b`, nghĩa là

.. math:: 

  \bm{f}_c = (c_0, c_1, \ldots, c_7), \ c_i = a_i \cdot b_i.
  
Tiếp theo, ta tính :math:`\bm{c}'` là biến đổi Fourier rời rạc 
ngược của :math:`\bm{f}_c`:

.. math:: 
  \bm{c}' = \mathsf{FFT}^{-1}(\bm{f}_c) = (C_0, C_1, \ldots, C_7).

Khi đó, ta tính vector :math:`\bm{c}` độ dài :math:`4` theo 
công thức

.. math:: 

  \bm{c} = (C_i - C_{i+4})_{i = 0}^3.

.. code-block:: python

  fc = [i * j for i, j in zip(fa, fb)]
  fc = list(map(simplify, ifft(fc)))
  c = [fc[i] - fc[i + 4] for i in range(4)]
  print(c)


Kết quả là vector :math:`(18, -17, 2, 5)`.

Kiểm tra kết quả bằng tay, mình có

.. math:: 

  a(x) \cdot b(x) & = (1 + 2x - x^2 + 3x^3) \cdot (-1 - 4x + 3x^2 - 2x^3) \\
    & = -1 - 4x + 3x^2 - 2x^3 \\
    & - 2x - 8x^2 + 6x^3 - 4x^4 \\
    & + x^2 + 4x^3 - 3x^4 + 2x^5 \\
    & - 3x^3 - 12x^4 + 9x^5 - 6x^6 \\
    & = -1 - 6x - 4x^2 + 5x^3 - 19x^4 + 11x^5 - 6x^6.

Trong modulo :math:`x^4 + 1` ta có thể thay thế 
:math:`x^4` thành :math:`-1`, như vậy kết quả trên tương đương

.. math:: 

  a(x) \cdot b(x) & = -1 - 6x - 4x^2 + 5x^3 - 19x^4 + 11x^5 - 6x^6 \\
    & = -1 - 6x - 4x^2 + 5x^3 - 19 \cdot (-1) + 11x \cdot (-1) - 6x^2 \cdot (-1) \\
    & = 18 - 17x + 2x^2 + 5x^3 \bmod x^4 + 1.

Nếu viết hệ số của kết quả dưới dạng vector 
theo số mũ tăng dần thì mình có :math:`(18, -17, 2, 5)`, 
bằng đúng phép tính với thuật toán Cooley-Tukey.

Một lý do khiến mình viết code trong khi 
nhiều thư viện Python như numpy, sympy, 
sagemath đã hỗ trợ là vì trong :cite:`Vasilenko` 
(tài liệu tham khảo chính của bài viết này) thì 
DFT thuận sử dụng :math:`\zeta_{2n}` là nghiệm 
của :math:`x^n + 1` nên nếu xét trên :math:`\mathbb{C}` 
thì :math:`\zeta_{2n} = e^{i \pi / n}`. Trong khi đó 
các tài liệu khác như wikipedia, numpy, sympy, ... 
sử dụng :math:`e^{-i \pi / n}` để tính DFT thuận. 
Ngược lại, :cite:`Vasilenko` sử dụng :math:`e^{-i \pi /n }` 
để tính DFT ngược, trong khi các tài liệu khác 
dùng :math:`e^{i \pi / n}`. Ở đây chúng ta có thể 
thấy dù là cách nào thì để thực hiện phép nhân nhanh 
đa thức modulo :math:`x^{2^t} + 1` đều cần cả DFT thuận 
và ngược, nên kết quả không thay đổi nhờ vào tính 
chất của DFT.
