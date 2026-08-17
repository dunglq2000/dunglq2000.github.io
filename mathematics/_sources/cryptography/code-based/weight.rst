Bài toán phổ trọng số của mã tuyến tính
=======================================

.. prf:definition:: 
    :label: def-spec-lincode-reg

    **Bài toán về phổ trọng số của linear code** 
    (hay **Задача о спектре весов линейного кода**) :math:`WS(\bm{H}, t)` 
    là bài toán nhận dạng trong code, với ma trận parity-check 
    :math:`\bm{H}`, có tồn tại hay không vector :math:`\bm{c} \in V_n(q)` 
    có trọng số Hamming bằng :math:`t` và thỏa mãn 
    :math:`\bm{H} \bm{c}^\top = \bm{0}`.

.. prf:theorem:: Định lí từ :cite:`1055873`
    
    Bài toán về phổ trọng số là NP-complete.
