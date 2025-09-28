Khoảng cách Hamming
====================

.. prf:definition:: Khoảng cách Hamming giữa hai vector
	:label: def-distance-two-vecs
	
	Với hai vector :math:`\bm{x}`, :math:`\bm{y}` thuộc :math:`\mathbb{F}_2^n`, đặt

	.. math:: d (\bm{x}, \bm{y}) = \mathrm{wt} (\bm{x} \oplus \bm{y})

	là **khoảng cách Hamming** giữa hai vector :math:`\bm{x}` và :math:`\bm{y}`. Trong đó :math:`\mathrm{wt}(\bm{z})` là trọng số vector :math:`\bm{z}`.

.. prf:definition:: Khoảng cách Hamming từ vector tới tập vector
	:label: def-distance-vec-to-set

	Xét :math:`M \subseteq \mathbb{F}_2^n`. Khi đó với mọi :math:`\bm{x} \in \mathbb{F}_2^n`, ta nói khoảng cách từ :math:`\bm{x}` tới :math:`M` là

	.. math:: d(\bm{x}, M) = \min_{\bm{y} \in M} d (\bm{x}, \bm{y}).

.. prf:definition:: Khoảng cách Hamming giữa hai hàm boolean
	:label: def-distance-two-func

	Xét hai hàm boolean :math:`n` biến là :math:`f(x_1, x_2, \ldots, x_n)` và :math:`g(x_1, x_2, \ldots, x_n)`. Khi đó khoảng cách Hamming từ hàm :math:`f` tới hàm :math:`g` là

	.. math:: d(f, g) = \mathrm{wt}(f \oplus g) = \sum_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x}) \oplus g(\bm{x}).
