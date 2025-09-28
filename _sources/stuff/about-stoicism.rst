Chủ nghĩa khắc kỷ và phân phối nhị thức
***************************************


Phân phối nhị thức
==================

Sự tiêu cực trong chủ nghĩa khắc kỷ và phân phối 
nhị thức có liên hệ mật thiết nhau tới mức không 
ngờ.

Mình xin phép nhắc lại về phân phối nhị nhức 
(binomial distribution).

    Nếu một sự kiện có khả năng xảy ra là :math:`p` 
    với :math:`0 \leqslant p \leqslant 1` thì trong 
    một dãy :math:`n` sự kiện như vậy độc lập nhau, 
    xác suất để có :math:`k` sự kiện xảy ra là

    .. math:: 

        P(\xi = k) = C^k_n \cdot p^k \cdot (1 - p)^{n-k}.

Một ví dụ đơn giản của phân phối nhị thức là bài kiểm 
tra trắc nghiệm. Giả sử một đề thi có :math:`10` câu, 
mỗi câu có bốn đáp án A, B, C, D, và chỉ có một đáp án 
đúng cho mỗi câu.

Khi đó, :math:`n = 10` và xác suất để chọn ngẫu nhiên 
đáp án đúng cho mỗi câu là :math:`p = 1/4`. Gọi 
:math:`k` là số câu trả lời đúng khi chọn ngẫu nhiên 
đáp án từng câu.

Mình sẽ thử lập bảng phân bố xác suất với :math:`k = 0, 1, \ldots, 10`.

.. only:: html

    .. table:: 
        :class: centered-table

        .. include:: binom.rst.inc

.. only:: latex

    .. tabularcolumns:: |c|c|c|c|c|c|c|

    .. include:: binom.rst.inc

Đối với trường hợp :math:`k = 10`, tức là lúc chúng ta 
"lụi" đúng hết cả :math:`10` câu, các bạn có thấy xác 
suất nhỏ tới mức chán chả buồn nói không? Như vậy có 
thể thấy xác suất một điều tốt xảy ra luôn rất thấp.
