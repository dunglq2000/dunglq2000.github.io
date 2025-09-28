Nonlinearity của hàm boolean
============================

Biến đổi Fourier
----------------

Với mỗi vector :math:`\bm{a} = (a_1, \ldots, a_n) \in \mathbb{F}_2^n`, ta kí hiệu :math:`\langle \bm{a}, \bm{x} \rangle` là hàm sau:

.. math:: 
	:label: fur:eq1

	\langle \bm{a}, \bm{x} \rangle = a_1 x_1 \oplus a_2 x_2 \oplus \ldots \oplus a_n x_n.

Mỗi hàm boolean :math:`f(\bm{x}) = f(x_1, x_2, \ldots, x_n)` sẽ được biểu diễn dưới dạng duy nhất với

.. math:: 
	:label: fur:eq2

	f(\bm{x}) = 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} F_f (\bm{a}) \cdot (-1)^{\langle \bm{a}, \bm{x} \rangle},

trong đó

.. math:: 
	:label: fur:eq3

	F_f (\bm{a}) = \sum_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x}) \cdot (-1)^{\langle \bm{a}, \bm{x} \rangle}.

Khi đó, tập hợp :math:`\{F_f (\bm{a}), \bm{a} \in \mathbb{F}_2^n \}` được gọi là **phổ Fourier** (hay **spectre Fourier**) của hàm boolean :math:`f`.

.. prf:remark:: 
	:label: rmk-fourier

	Đầu tiên ta có nhận xét rằng, với vector :math:`\bm{z}` cố định thì

	.. math:: 
		:label: fur:eq4

		\sum_{\bm{a} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{z} \rangle} = \begin{cases}
			0, \quad & \text{nếu } \bm{z} \neq \bm{0} \\
			2^n, \quad & \text{nếu } \bm{z} = \bm{0}.
		\end{cases}

.. admonition:: Chứng minh
	:class: danger, dropdown

	Để chứng minh nhận xét này, ta thấy rằng nếu :math:`\bm{z} \neq \bm{0}` thì có ít nhất một bit :math:`z_i \neq 0`.

	Ta chọn vector

	.. math:: \Delta = (0, \ldots, 0, 1, 0, \ldots, 0)

	với bit :math:`1` nằm ở vị trí :math:`i`.
	
	Khi đó với mọi vector :math:`\bm{a} \in \mathbb{F}_2^n` tồn tại duy nhất vector :math:`\bm{a}' \in \mathbb{F}_2^n` sao cho :math:`\bm{a} \oplus \bm{a}' = \Delta`.

	Ta suy ra :math:`\langle \bm{a} \oplus \bm{a}', \bm{z} \rangle = \langle \Delta, \bm{z} \rangle = 1` vì :math:`z_i \cdot 1 = 1`, các vị trí còn lại :math:`z_j \cdot 0 = 0`. 

	Lý do ta chọn vector :math:`\Delta` như vậy là vì

	.. math:: \langle \bm{a} \oplus \bm{a}', \bm{z} \rangle = \langle \bm{a}, \bm{z} \rangle \oplus \langle \bm{a}', \bm{z} \rangle = 1,

	tương đương với :math:`\langle \bm{a}, \bm{z} \rangle = 1 \oplus \langle \bm{a}', \bm{z} \rangle`.
	
	Do đó :math:`\langle \bm{a}, \bm{z} \rangle` và :math:`\langle \bm{a}', \bm{z} \rangle` là hai bit khác nhau, dẫn tới :math:`(-1)^{\langle \bm{a}, \bm{z} \rangle}` và :math:`(-1)^{\langle \bm{a}', \bm{z} \rangle}` là hai số trái dấu nhau nên tổng chúng là :math:`0`. Chúng ta có :math:`2^n / 2` cặp như vậy và tổng cuối cùng là :math:`0`.

	Trong trường hợp :math:`\bm{z} = \bm{0}` thì :math:`\langle \bm{a}, \bm{z} \rangle = \bm{0}` với mọi :math:`\bm{a} \in \mathbb{F}_2^n`. Do đó :math:`(-1)^{\langle \bm{a}, \bm{z} \rangle} = (-1)^0 = 1` với mọi vector :math:`\bm{a}`. Hàm boolean :math:`n` biến có :math:`2^n` vector :math:`\bm{a}` nên tổng là :math:`2^n \cdot 1 = 2^n`.

Đẳng thức :eq:`fur:eq4` đã được chứng minh. Ta quay lại bài toán.

.. admonition:: Chứng minh
	:class: danger, dropdown

	Với mọi vector :math:`\bm{x} \in \mathbb{F}_2^n`, ta khai triển từ vế phải của :eq:`fur:eq2` và từ :eq:`fur:eq3`:

	.. math:: 
		
		& 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} F_f (\bm{a}) \cdot (-1)^{\langle \bm{a}, \bm{x} \rangle} \\ = & 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} \left( \sum_{\bm{y} \in \mathbb{F}_2^n} f(\bm{y}) \cdot (-1)^{\langle \bm{a}, \bm{y} \rangle} \right) \cdot (-1)^{\langle \bm{a}, \bm{x} \rangle} \\
		= & 2^{-n} \sum_{\bm{y} \in \mathbb{F}_2^n} f(\bm{y}) \sum_{\bm{a} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{y} \oplus \bm{x} \rangle}.
		
	Theo :eq:`fur:eq4`, nếu ta coi :math:`\bm{y} \oplus \bm{x} = \bm{z}` thì

	.. math:: 

		\sum_{\bm{a} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{y} \oplus \bm{x} \rangle} = \begin{cases}
			0, \quad & \text{nếu } \bm{y} \oplus \bm{x} \neq \bm{0} \\
			2^n, \quad & \text{nếu } \bm{y} \oplus \bm{x} = \bm{0},
		\end{cases}

	nghĩa là trong tổng trên thì chỉ có :math:`\bm{y}` thỏa :math:`\bm{y} \oplus \bm{x} = \bm{0}` thì :math:`f(\bm{y})` không bị triệt tiêu. Nói cách khác là :math:`\bm{y} = \bm{x}` và do đó tổng trên còn lại :math:`2^{-n} (f(\bm{x}) \cdot 2^n) = f(\bm{x})` và ta có điều phải chứng minh.

.. prf:example:: 
	:label: exp-fourier

	Xét hàm boolean :math:`f(x_1, x_2) = (1, 0, 0, 1)`.

	Xét :math:`\bm{a} = (0, 0)`. Ta có:

	Với :math:`\bm{x} = (0, 0)`,
    
	.. math:: f(\bm{x}) = 1, \ \langle \bm{a}, \bm{x} \rangle = 0 \cdot 0 + 0 \cdot 0 = 0.

	Với :math:`\bm{x} = (0, 1)`,
    
	.. math:: f(\bm{x}) = 0, \langle \bm{a}, \bm{x} \rangle = 0 \cdot 0 + 0 \cdot 1 = 0.

	Với :math:`\bm{x} = (1, 0)`,

	.. math:: f(\bm{x}) = 0, \langle \bm{a}, \bm{x} \rangle = 0 \cdot 1 + 0 \cdot 0 = 0.

	Với :math:`\bm{x} = (1, 1)`,
	
	.. math:: f(\bm{x}) = 1, \langle \bm{a}, \bm{x} \rangle = 0 \cdot 1 + 0 \cdot 1 = 0.

	Ta suy ra 

	.. math:: F_f (\bm{a}) = 1 \cdot (-1)^0 + 0 \cdot (-1)^0 + 0 \cdot (-1)^0 + 1 \cdot (-1)^0 = 2

	khi :math:`\bm{a} = (0, 0)`.

	Tương tự, ta có các giá trị :math:`F_f (\bm{a})` sau:

	- với :math:`\bm{a} = (0, 1)`, :math:`F_f (\bm{a}) = F_f (0, 1) = 0`;
	- với :math:`\bm{a} = (1, 0)`, :math:`F_f (\bm{a}) = F_f (1, 0) = 0`;
	- với :math:`\bm{a} = (1, 1)`, :math:`F_f (\bm{a}) = F_f (1, 1) = 2`.

	Bây giờ ta đã có đủ :math:`F_f(\bm{a})` với :math:`\bm{a} \in \mathbb{F}_2^2` nên ta có thể kiểm chứng với mọi :math:`\bm{x} \in \mathbb{F}_2^2` thỏa công thức :eq:`fur:eq2`.

Biến đổi Walsh-Hadamard
-----------------------

Với mỗi hàm boolean :math:`f(x_1, x_2, \ldots, x_n) = f(\bm{x})` ta định nghĩa một hàm tương ứng như sau:

.. math:: f^*(\bm{x}) = (-1)^{f(\bm{x})}.

Ta định nghĩa :math:`\langle \bm{a}, \bm{x} \rangle` như trên.

Khi đó hàm :math:`f^*(\bm{x})` sẽ có dạng

.. math:: 
	:label: walsh:eq1

	f^*(\bm{x}) = 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} W_f (\bm{a}) (-1)^{\langle \bm{a}, \bm{x} \rangle},

trong đó

.. math:: 
	:label: walsh:eq2

	W_f (\bm{a}) = \sum_{\bm{x} \in \mathbb{F}_2^n} (-1)^{f(\bm{x}) \oplus \langle \bm{a}, \bm{x} \rangle}.

Tập hợp :math:`\{ W_f (\bm{a}), \bm{a} \in \mathbb{F}_2^n \}` được gọi là **phổ Walsh** (hay **spectre Walsh**) của hàm :math:`f(\bm{x})`.

Các giá trị :math:`W_f (\bm{a})` được gọi là **hệ số Walsh**.
	
.. admonition:: Chứng minh
	:class: danger, dropdown

	Tương tự như trên, ta khai triển vế phải của :eq:`walsh:eq1` và thay :eq:`walsh:eq2` vào

	.. math:: 
		
		
			& 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} W_f (\bm{a}) (-1)^{\langle \bm{a}, \bm{x} \rangle} \\
			= & 2^{-n} \sum_{\bm{a} \in \mathbb{F}_2^n} \left( \sum_{\bm{y} \in \mathbb{F}_2^n} (-1)^{f(\bm{y}) \oplus \langle \bm{a}, \bm{y} \rangle} \right) (-1)^{\langle \bm{a}, \bm{x} \rangle} \\
			= & 2^{-n} \sum_{\bm{y} \in \mathbb{F}_2^n} (-1)^{f(\bm{y})} \sum_{\bm{a} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{y} \oplus \bm{x} \rangle}.
		

	Cũng từ :eq:`fur:eq4`, tương tự như trên ta có

	.. math:: 

		\sum_{\bm{a} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{y} \oplus \bm{x} \rangle} = \begin{cases}
			0, & \quad \text{nếu } \bm{y} \oplus \bm{x} \neq \bm{0} \\
			2^n, & \quad \text{nếu } \bm{y} \oplus \bm{x} = \bm{0}.
		\end{cases}

	Do đó trong các :math:`\bm{y} \in \mathbb{F}_2^n` thì chỉ có :math:`\bm{y} = \bm{x}` không bị triệt tiêu nên kết quả là

	.. math:: 2^{-n} \cdot (-1)^{f(\bm{x})} \cdot 2^n = (-1)^{f(\bm{x})} = f^* (\bm{x}).

Các hệ số Walsh liên hệ với nhau bởi công thức

.. math:: 

	\sum_{\bm{a} \in \mathbb{F}_2^n} W_f (\bm{a}) W_f (\bm{a} \oplus \bm{d}) = 
	\begin{cases}
		2^{2n}, & \bm{d} = \bm{0} \\
		0, & \bm{d} \neq \bm{0}.
	\end{cases}

Trường hợp :math:`\bm{d} = \bm{0}` được gọi là **đẳng thức Parcel**:

.. math:: \sum_{\bm{a} \in \mathbb{F}_2^n} (W_f (\bm{a}))^2 = 2^{2n}.

Tính chất của biến đổi Walsh-Hadamard
-------------------------------------

1. :math:`W_f(\bm{0}) = 2^n - 2 \mathrm{wt} (f)`, và :math:`W_f(\bm{0}) = 0` khi và chỉ khi :math:`f` là hàm cân bằng.
2. Nếu :math:`g = \bar{f}` thì :math:`W_g(\bm{a}) = -W_f(\bm{a})` với mọi :math:`\bm{a} \in \mathbb{F}_2^n`.
3. Nếu :math:`g(\bm{x}) = f(\bm{x} \oplus \bm{b})` với vector :math:`\bm{b}` nào đó, thì

.. math:: 
	
	W_g(\bm{a}) & = \sum_x (-1)^{f(\bm{x} \oplus \bm{b}) \oplus \langle \bm{a}, \bm{x} \rangle} \\
	& = \sum_x (-1)^{f(\bm{x}) \oplus \langle \bm{a}, \bm{x} \oplus \bm{b} \rangle} \\
	& = (-1)^{\langle \bm{a}, \bm{b} \rangle} W_f(\bm{a}).

4. Đặt :math:`f \in \mathcal{F}_n`, :math:`\bm{b} \in \mathbb{F}_2^n`, :math:`g(\bm{x}) = f(\bm{x}) \oplus \langle \bm{b}, \bm{x} \rangle`. Khi đó

.. math:: 
	
	W_g(\bm{a}) & = \sum_x (-1)^{f(\bm{x}) \oplus \langle \bm{b}, \bm{x} \rangle \oplus \langle \bm{a}, \bm{x} \rangle} \\
	& = \sum_x (-1)^{f(\bm{x}) \oplus \langle \bm{b} \oplus \bm{a}, \bm{x} \rangle} \\
	& = W_f(\bm{b} \oplus \bm{a}).
	
5. Đặt :math:`f(\bm{x}) = c` là hằng số. Hàm :math:`c \oplus \langle \bm{a}, \bm{x} \rangle` là hàm tuyến tính với mọi :math:`\bm{a} \neq \bm{0}`. Hệ quả là :math:`W_f(\bm{a}) = 0` với mọi vector :math:`\bm{a}` khác không, trừ khi

.. math:: 
	
	W_f(\bm{0}) = 2^n - 2 \mathrm{wt} (f) = \begin{cases}
      	- 2^n, & \, \text{nếu} \, c = 1, \\
      	\quad 2^n, & \, \text{nếu} \, c = 0.
   \end{cases}

6. Đặt :math:`f(\bm{x}) = c \oplus \langle \bm{b}, \bm{x} \rangle` là hàm affine. Khi đó, theo tính chất 4 và 5 suy ra :math:`W_f(\bm{a}) = 0` với mọi :math:`\bm{a} \neq \bm{0}`, và :math:`W_f(\bm{b}) = (-1)^c \cdot 2^n`.
7. Đặt :math:`f(\bm{x}, \bm{y}) = g(\bm{x}) \oplus h(\bm{y})` với :math:`g \in \mathcal{F}_n` và :math:`h \in \mathcal{F}_m` và hai tập hợp biến :math:`\bm{x}` và :math:`\bm{y}` không giao nhau. Nói cách khác :math:`f` là hàm boolean :math:`n+m` biến. Khi đó với mọi :math:`\bm{a} \in \mathbb{F}_2^n` và :math:`\bm{b} \in \mathbb{F}_2^n` thì

.. math:: 
	
	W_f(\bm{a} \bm{b}) & = \sum_{\bm{x}, \bm{y}} (-1)^{g(\bm{x}) \oplus h(\bm{y}) \oplus \langle \bm{a}, \bm{x} \rangle \oplus \langle \bm{b}, \bm{y} \rangle} \\
	& = \sum_{\bm{x}} (-1)^{g(\bm{x}) \oplus \langle \bm{a}, \bm{x} \rangle} \sum_{\bm{y}} (-1)^{h(\bm{y}) \oplus \langle \bm{b}, \bm{y} \rangle} \\
	& = W_g(\bm{a}) \cdot W_h(\bm{b}).

8. Đặt :math:`f(x_1, \ldots, x_n)` *giả phụ thuộc* vào biến :math:`x_i`. Khi đó :math:`W_f(\bm{a}) = 0` với mọi vector :math:`\bm{a}` mà :math:`a_i = 1`.

Nói cách khác, nếu đặt :math:`\bm{x}' = (x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n)` và :math:`\bm{a}' = (a_1, \ldots, a_{i-1}, a_{i+1}, \ldots, a_n)` và để ý rằng :math:`\langle \bm{a}, \bm{x} \rangle = \langle \bm{a}', \bm{x}' \rangle \oplus a_i x_i`. Khi đó nếu :math:`a_i = 1` thì

.. math:: 

	W_f(\bm{a}) & = \sum_{\bm{x}} (-1)^{f(\bm{x}) \oplus \langle \bm{a}, \bm{x} \rangle} \\ 
	& = \sum_{\substack{\bm{x}, \\ x_i = 0}} (-1)^{f(\bm{x}) \oplus \langle \bm{a}', \bm{x}' \rangle} + \sum_{\substack{\bm{x}, \\ x_i = 1}} (-1)^{f(\bm{x}) \oplus \langle \bm{a}', \bm{x}' \rangle \oplus 1} = 0.

Liên hệ giữa hệ số Fourier và hệ số Walsh
-----------------------------------------

.. prf:remark:: 
	:label: rmk-fourier-and-walsh

	Quan hệ giữa hệ số Fourier và hệ số Walsh là biểu thức sau

	.. math:: W_f (\bm{a}) = 2^n \Delta (\bm{a}) - 2 F_f (\bm{a})

	với 
	
	.. math:: 
		
		\Delta (\bm{a}) = \begin{cases}
			1, \quad \text{nếu } \bm{a} = \bm{0} \\
			0, \quad \text{nếu } \bm{a} \neq \bm{0}.
		\end{cases}

.. admonition:: Chứng minh
	:class: danger, dropdown

	Ta có

	.. math:: 
		
		W_f (\bm{a}) + 2 F_f (\bm{a}) = & \sum_{\bm{x} \in \mathbb{F}_2^n} (-1)^{f(\bm{x}) \oplus \langle \bm{a}, \bm{x} \rangle} + 2 \sum_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x}) (-1)^{\langle \bm{a}, \bm{x} \rangle} \\ = & \sum_{\bm{x} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{x} \rangle} [(-1)^{f(\bm{x})} + 2 f(\bm{x})].
		
	Để ý rằng, nếu :math:`f(\bm{x}) = 0` thì

	.. math:: (-1)^{f(\bm{x})} + 2 f(\bm{x}) = (-1)^0 + 2 \cdot 0 = 1,

	còn nếu :math:`f(\bm{x}) = 1` thì

	.. math:: (-1)^{f(\bm{x})} + 2 f(\bm{x}) = (-1)^1 + 2 \cdot 1 = 1.

	Nói cách khác biểu thức trên trở thành

	.. math:: W_f (\bm{a}) + 2 F_f (\bm{a}) = \sum_{\bm{x} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{x} \rangle}.

	Từ :eq:`fur:eq2` ta có

	.. math:: 
		
		\sum_{\bm{x} \in \mathbb{F}_2^n} (-1)^{\langle \bm{a}, \bm{x} \rangle} = \begin{cases}
			0, \quad &\text{nếu } \bm{a} \neq \bm{0} \\ 2^n, \quad & \text{nếu } \bm{a} = \bm{0}.
		\end{cases}

	Như vậy nếu đặt :math:`\Delta(\bm{a}) = \begin{cases} 1, \text{nếu } \bm{a} = \bm{0} \\ 0, \text{nếu } \bm{a} \neq \bm{0} \end{cases}` thì ta có điều phải chứng minh.
	
.. prf:remark:: 
	:label: rmk-property-walsh

	Khi :math:`\bm{a} = \bm{0}` thì với mọi :math:`\bm{x} \in \mathbb{F}_2^n` ta đều có :math:`\langle \bm{a}, \bm{x} \rangle = 0`. Do đó

	.. math:: F_f (\bm{0}) = \sum_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x}) (-1)^{\langle \bm{a}, \bm{x} \rangle} = \sum_{\bm{x} \in \mathbb{F}_2^n} f(\bm{x}) (-1)^0 = \mathrm{wt}(f),

	suy ra

	.. math:: 
		:label: walsh:eq4

		W_f (\bm{0}) = 2^n - 2 wt(f) \Leftrightarrow wt(f) = 2^{n-1} - \frac{1}{2} W_f (\bm{0}).

Hàm Bent
--------

Ta kí hiệu :math:`\mathcal{A}` là tập hợp tất cả các hàm boolean affine với :math:`n` biến, nghĩa là

.. math:: \mathcal{A} = \{ a_0 \oplus a_1 x_1 \oplus \cdots \oplus a_n x_n \, | \, a_0, a_1, \ldots, a_n \in \mathbb{F}_2 \}.

.. prf:definition:: Nonlinearity của hàm boolean

	**Nonlinearity** của hàm boolean :math:`f` bất kì được định nghĩa là khoảng cách Hamming từ :math:`f` tới :math:`\mathcal{A}`, hay nói cách khác :math:`N_f = d(f, \mathcal{A})`.

.. prf:remark:: 
	:label: rmk-bent

	Xét hàm :math:`f` với :math:`n` biến và phổ Walsh tương ứng của hàm :math:`f` là :math:`\{ W_f (\bm{a}), \bm{a} \in \mathbb{F}_2^n \}`. Khi đó

	.. math:: 
		:label: walsh:eq3

		N_f = 2^{n-1} - \frac{1}{2} \max_{\bm{a} \in \mathbb{F}_2^n} \lvert W_f (\bm{a}) \rvert.

.. prf:remark:: 
	:label: rmk-property-bent

	Từ đẳng thức Parcel ta có

	.. math:: 
		
		& 2^n \cdot \left(\max_{\bm{a} \in \mathbb{F}_2^n} (W_f (\bm{a}))^2\right) \geqslant \sum_{\bm{a} \in \mathbb{F}_2^n} (W_f (\bm{a}))^2 = 2^{2n} \\
		\Leftrightarrow & \max_{\bm{a} \in \mathbb{F}_2^n} (W_f (\bm{a}))^2 \geqslant \frac{2^{2n}}{2^n} = 2^n \\
		\Leftrightarrow & \max_{\bm{a} \in \mathbb{F}_2^n} \lvert W_f (\bm{a}) \rvert \geqslant 2^{n/2}.
		

Từ nhận xét trên và từ định nghĩa nonlinearity ở trên ta có

.. math:: N_f \leqslant 2^{n-1} - \frac{1}{2} 2^{n / 2}.

Hàm :math:`f` khiến dấu bằng xảy ra được gọi là **hàm Bent**. Điều kiện cần và đủ để tồn tại hàm Bent :math:`f` có :math:`n` biến là khi :math:`n = 2k`, tức là :math:`n` chẵn.

Tính chất quan trọng của hàm Bent là với mọi vector :math:`\bm{a}` thì

.. math:: W_f (\bm{a}) = \pm 2^{n/2}.

.. prf:example:: 
	:label: exp-bent-func

	Với :math:`n = 2`, hàm :math:`f(x_1, x_2) = x_1 \oplus x_1 x_2` là hàm Bent.
	
	Ta có thể tính toán và thấy rằng :math:`W_f (0, 0) = 2`, :math:`W_f (0, 1) = -2`, :math:`W_f (1, 0) = 2` và :math:`W_f (1, 1) = 2`.
