Ý tưởng xây dựng các hệ mật mã dựa trên mã sửa sai
==================================================

Đặt :math:`\bm{G}` là ma trận sinh của linear code 
:math:`[n, k]_q` :math:`\mathcal{C}` có thể sửa :math:`t` 
lỗi.

Nếu code với ma trận sinh :math:`\bm{G}` không có 
các cấu trúc đại số hoặc tổ hợp thì theo định lí 
trên về độ khó NP của bài toán nhận dạng syndrome 
decode, bài toán decode linear code :math:`[n, k]_q` 
là rất khó.

Khi đó nếu mã hóa thông điệp :math:`m` có thể 
thực hiện qua việc: :math:`\bm{m} \to \bm{c} = \bm{m} \bm{G} + \bm{e}`, 
:math:`\mathrm{wt}(\bm{e}) = t`, :math:`\bm{e} \in V_n(q)`.

Khi đó, cho trước vector :math:`\bm{c}`, việc 
tìm một vector :math:`\bm{m}` là bài toán decode 
trên linear code :math:`[n, k]_q` với ma trận sinh 
:math:`\bm{G}`, không có các cấu trúc đại số 
hoặc tổ hợp. Suy ra việc phá mã rất khó.

Vấn đề là ở phía bên việc tìm lại :math:`\bm{m}` 
từ :math:`\bm{c}` rất khó nên cần một phương án 
để giải mã lại thông điệp ban đầu.
