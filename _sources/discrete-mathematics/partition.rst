Phân hoạch
**********


Số Stirling
===========


Số Stirling loại 1
------------------

Xét tập các hoán vị trên tập hữu hạn :math:`n` phần tử.

Số hoán vị chứa :math:`k` chu trình độc lập là số Stirling loại 1, kí hiệu là :math:`\mathcal{S}_n^{(k)}`.

Các bước khởi đầu là

* :math:`\mathcal{S}_0^{(0)} = 1` (có đúng một cách chia tập :math:`0` phần tử vào :math:`0` chu trình);
* :math:`\mathcal{S}_n^{(0)} = \mathcal{S}_0^{(n)} = 0` (không có cách nào chia tập :math:`n` phần tử vào :math:`0` chu trình và chia tập :math:`0` phần tử vào :math:`n` chu trình).

Công thức đệ quy của số Stirling là:

.. math:: \mathcal{S}_{n+1}^{(k)} = n \cdot \mathcal{S}_n^{(k)} + \mathcal{S}_{n}^{(k-1)}.

.. admonition:: Chứng minh
    :class: danger, dropdown

    Giả sử tập có :math:`n+1` phần tử là :math:`A = \{ 1, 2, \ldots, n, n+1\}`.

    Khi đó để phân hoạch :math:`n + 1` phần tử này vào :math:`k` chu trình độc lập thì có hai trường hợp:

    1. Đầu tiên xếp các phần tử :math:`1`, :math:`2`, ..., :math:`n` vào :math:`k` chu trình độc lập thì có :math:`\mathcal{S}_n^{(k)}` cách chọn. Tiếp theo ta cho phần tử :math:`n + 1` vào một vị trí bất kì trong :math:`k` chu trình trên thì có :math:`n` cách chọn. Vậy trường hợp này là :math:`n \cdot \mathcal{S}_n^{(k)}`.
    2. Ta phân :math:`n` phần tử :math:`1`, :math:`2`, ..., :math:`n` vào :math:`k - 1` chu trình độc lập và phần tử :math:`n + 1` sẽ vào chu trình thứ :math:`k`. Trường hợp này có :math:`\mathcal{S}_n^{(k-1)} \cdot 1` cách chọn.

    Như vậy tổng số cách phân :math:`n + 1` phần tử vào :math:`k` chu trình độc lập là hợp của hai trường hợp trên. Ta có điều phải chứng minh.

.. prf:example:: 
    :label: exp-stirling-1

    Có bao nhiêu hoán vị của :math:`\mathcal{S}_5` chứa đúng ba chu trình độc lập?

    Ta có các trường hợp sau:

    1. Hoán vị có dạng :math:`(1)(2)(3, 4, 5)`. Ta chọn hai phần tử làm hai chu trình độc lập, có :math:`C^2_5 = 10` cách chọn. Tiếp theo chọn ba phần tử cho chu trình cuối, có :math:`2!` cách chọn. Vậy trường hợp này có :math:`10 \cdot 2 = 20` cách chọn.
    2. Hoán vị có dạng :math:`(1)(2, 3)(4, 5)`. Ta chọn một phần tử làm chu trình độc lập có :math:`C^1_5 = 5` cách chọn. Tiếp theo chọn hai phần tử cho chu trình tiếp theo trong :math:`4` phần tử còn lại, có :math:`C^2_4 = 6` cách chọn. Hai phần tử còn lại là :math:`C^2_2 = 1` cách chọn. Lưu ý là hai chu trình độc lập có thể đổi chỗ cho nhau nên cần chia thêm :math:`2!` nữa, ví dụ :math:`(1, 2)(3, 4)` hoàn toàn giống với :math:`(3, 4)(1, 2)`. Số cách chọn cho trường hợp này là :math:`5 \cdot 6 / 2 = 15` cách chọn.

    Như vậy số hoán vị của :math:`\mathcal{S}_5` chứa đúng ba chu trình độc lập là :math:`20 + 15 = 35`.

    Ta so sánh kết quả với số Stirling. Ta cần tìm :math:`\mathcal{S}_5^{(3)}`.

    Ta có:

    .. math:: 

        \mathcal{S}_5^{(3)} = & 4 \cdot \mathcal{S}_4^{(3)} + \mathcal{S}_4^{(2)} \\
            = & 4 \cdot \left(3 \cdot \mathcal{S}_3^{(3)} + \mathcal{S}_3^{(2)}\right) + 3 \cdot \mathcal{S}_3^{(2)} + \mathcal{S}_3^{(1)} \\
            = & 4 \cdot \left(3 \cdot 1  + 2 \cdot \mathcal{S}_2^{(2)} + \mathcal{S}_2^{(1)}\right) + 3 \cdot \left(2 \cdot \mathcal{S}_2^{(2)} + \mathcal{S}_2^{(1)}\right) + 2 \cdot \mathcal{S}_2^{(1)} + \mathcal{S}_2^{(0)} \\
            = & 4 \cdot \left(3 + 2 \cdot 1 + 1 \cdot \mathcal{S}_1^{(1)} + \mathcal{S}_1^{(0)}\right) + 3 \cdot \left(2 \cdot 1 + \mathcal{S}_1^{(1)} + \mathcal{S}_1^{(0)}\right) + \mathcal{S}_1^{(1)} + \mathcal{S}_1^{(0)} + 0 \\
            = & 4 \cdot (3 + 2 + 1) + 3 \cdot (2 + 1 + 0) + 2 \cdot 1 + 0 + 0 = 35.

    Kết quả số Stirling khớp với việc giải bằng tổ hợp và không đòi hỏi các suy luận phức tạp.

.. prf:remark:: 
    :label: rmk-stirling-1

    Số Stirling loại 1 cho phép tính số lượng phân hoạch theo đệ quy thay vì giải các bài toán tổ hợp phức tạp. Điều này hiệu quả khi các số :math:`n` và :math:`k` trở nên lớn.

.. prf:property:: Tính chất của số Stirling loại 1
    :label: prop-stirling-1

    .. math:: \sum_{k=1}^{n}\mathcal{S}_n^{(k)} = n!.
        
    Công thức này chỉ số hoán vị có thể có của một tập :math:`n` phần tử.


Số Stirling loại 2
------------------

Số Stirling loại 2 thể hiện số cách phân bổ :math:`n` phần tử vào :math:`k` tập hợp rời nhau, kí hiệu là :math:`s(n, k)`.

Công thức đệ quy của số Stirling loại 2 là:

.. math:: s(n+1, k) = k \cdot s(n, k) + s(n, k-1).

.. admonition:: Chứng minh
    :class: danger, dropdown

    Cách chứng minh khá tương tự số Stirling loại 1. Tuy nhiên ở đây việc phân một phần tử vào một tập hợp không xét tới thứ tự, điều này khác với chu trình cần xem xét thứ tự. Như vậy ta vẫn có hai trường hợp

    1. Phân các phần tử :math:`1`, :math:`2`, ..., :math:`n` vào :math:`k` tập hợp. Sau đó phần tử :math:`n + 1` sẽ được phân vào một trong :math:`k` tập đó nên có :math:`k` cách chọn.
    2. Phân các phần tử :math:`1`, :math:`2`, ..., :math:`n` vào :math:`k - 1` tập hợp và phần tử :math:`n + 1` vào tập hợp thứ :math:`k + 1`.

    Từ đây ta có công thức số Stirling loại 2.

Các bước cơ sở cho số Stirling loại 2 cũng tương tự loại 1:

* :math:`s(n, n) = 1`;
* :math:`s(n, 0) = s(0, n) = 0`.
