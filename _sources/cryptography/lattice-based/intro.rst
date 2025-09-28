=================================
Nhập môn mật mã dựa trên lattice
=================================

**Kí hiệu**. Vector hàng được kí hiệu bởi chữ thường in đậm, ví dụ :math:`\bm{x}`, :math:`\bm{y}`, :math:`\bm{v}`. Ma trận được kí hiệu bởi chữ hoa in đậm, ví dụ :math:`\bm{A}`, :math:`\bm{B}`.

.. prf:definition:: Lattice
	:label: def-lattice

	Xét tập hợp các vector độc lập tuyến tính :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d` trên :math:`\mathbb{R}^n`. Ta nói **lattice** (hay **lưới**) :math:`\mathcal{L} \subset \mathbb{R}^n` được sinh bởi các vector :math:`\bm{v}_1`, :math:`\bm{v}_2`, ..., :math:`\bm{v}_d` nếu

	.. math:: \mathcal{L} = \{ a_1 \bm{v}_1 + a_2 \bm{v}_2 + \ldots + a_d \bm{v}_d : a_i \in \mathbb{Z} \}.

Nói cách khác, lattice là không gian vector được sinh bởi tổ hợp tuyến tính với hệ số nguyên.

Tập các vector

.. math:: \{ \bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d \}
	
được gọi là **tập sinh** hay **cơ sở** (basis, базис) của lattice :math:`\mathcal{L}`.

Số lượng vector trong cơ sở được gọi là **số chiều** của lattice và kí hiệu là :math:`d = \dim(\mathcal{L})`.

Lattice được gọi là **full-rank** nếu :math:`\dim(\mathcal{L}) = n`.

Xét ma trận :math:`\bm{V}` có các hàng là các vector :math:`\bm{v}_1`, ..., :math:`\bm{v}_d`, nghĩa là :math:`\bm{V} \in \mathbb{R}^{d \times n}`.

.. prf:definition:: Định thức của lattice
	:label: def-lattice-det
	
	**Định thức của lattice** :math:`\mathcal{L}` được xác định bởi công thức :math:`\displaystyle{\det(\mathcal{L}) = \sqrt{\lvert \det\left(\bm{V} \bm{V}^\top \right)\rvert}}`.

Nếu lattice full-rank thì :math:`\det(\mathcal{L}) = \det(\bm{V})`.

.. prf:remark:: 
	:label: rmk-dim-lattice
	
	Cơ sở của một lưới không là duy nhất nhưng số lượng vector trong mỗi cơ sở là như nhau và bằng số chiều của lattice.

Nếu :math:`\bm{V}` và :math:`\bm{W}` là hai ma trận cơ sở của cùng lattice :math:`\mathcal{L}` thì tồn tại ma trận :math:`\bm{A}` với hệ số nguyên (tức :math:`\bm{A} \in \mathbb{Z}^{d \times d}`) có định thức bằng :math:`1` sao cho :math:`\bm{W} = \bm{A} \cdot \bm{V}`. Chúng ta có thể dễ dàng chứng minh điều này khi biểu diễn các vector trong :math:`\bm{W}` thành tổ hợp tuyến tính các vector trong :math:`\bm{V}`.

Giả sử :math:`\{ \bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d \}` là một cơ sở của :math:`\mathcal{L}`. Tương tự, :math:`\{ \bm{w}_1, \bm{w}_2, \ldots, \bm{w}_d \}` là một cơ sở khác của :math:`\mathcal{L}`.

.. admonition:: Chứng minh
	:class: danger, dropdown

	Ta có thể viết mỗi :math:`\bm{w}_i` là tổ hợp tuyến tính của các vector :math:`\bm{v}` như sau

	.. math:: 
		
		\bm{w}_1 & = a_{11} \bm{v}_1 + a_{12} \bm{v}_2 + \ldots + a_{1d} \bm{v}_d \\
		\bm{w}_2 & = a_{21} \bm{v}_1 + a_{22} \bm{v}_2 + \ldots + a_{2d} \bm{v}_d \\
		\vdots & \\
		\bm{w}_d & = a_{d1} \bm{v}_1 + a_{d2} \bm{v}_2 + \ldots + a_{dd} \bm{v}_d
		
	Khi đó, nếu viết các vector :math:`\bm{w}_i` thành hàng của ma trận :math:`\bm{W}` và :math:`\bm{v}_j` thành hàng của ma trận :math:`\bm{V}` thì biểu diễn trên tương đương với:

	.. math:: 

		\bm{W} = \begin{pmatrix}
			a_{11} & a_{12} & \cdots & a_{1d} \\
			a_{21} & a_{22} & \cdots & a_{2d} \\
			\vdots & \vdots & \ddots & \vdots \\
			a_{d1} & a_{d2} & \cdots & a_{dd}
		\end{pmatrix} \cdot \bm{V}.

	Đặt

	.. math:: 
		
		\bm{A} = \begin{pmatrix}
			a_{11} & a_{12} & \cdots & a_{1d} \\
			a_{21} & a_{22} & \cdots & a_{2d} \\
			\vdots & \vdots & \ddots & \vdots \\
			a_{d1} & a_{d2} & \cdots & a_{dd}
		\end{pmatrix}.

	Do :math:`\bm{W}` và :math:`\bm{V}` là các cơ sở của :math:`\mathcal{L}` nên nếu các vector :math:`\bm{w}_i` có thể biểu diễn qua các vector :math:`\bm{v}_j` thì ngược lại, các vector :math:`\bm{v}_j` cũng có thể được biểu diễn qua các vector :math:`\bm{w}_i`. Suy ra ma trận :math:`\bm{A}` là ma trận khả nghịch. Do :math:`a_{ij} \in \mathbb{Z}` theo định nghĩa lattice, :math:`\det(\bm{A}) \in \mathbb{Z}`.

	Hơn nữa, vì:

	.. math:: 
		
		I = \bm{A} \cdot \bm{A}^{-1} \Rightarrow 1 = \det (\bm{A}) \cdot \det (\bm{A}^{-1})

	nên :math:`\det(\bm{A}) = \pm 1`.

Mỗi lattice :math:`\mathcal{L}` có một lattice đối ngẫu (dual lattice), kí hiệu là

.. math:: \mathcal{L}^* = \{ \bm{w} \in \mathbb{R}^n : \langle \bm{w}, \bm{x} \rangle \in \mathbb{Z} \ \text{với mọi} \ \bm{x} \in \mathcal{L} \}.

.. prf:definition:: Fundamental domain
	:label: def-lattice-fundamental-domain

	Cho lattice :math:`\mathcal{L}` có số chiều là :math:`d` với cơ sở gồm các vector $\{ \bm{v}_1, \bm{v}_2, \ldots, \bm{v}_d \}$. Ta gọi **fundamental domain** (hay **fundamental parallelepiped**) của :math:`\mathcal{L}` ứng với cơ sở trên là tập

	.. math:: \mathcal{F} (\bm{v}_1, \ldots, \bm{v}_d) = \{ t_1 \bm{v}_1 + \ldots + t_d \bm{v}_d : 0 \leqslant t_i < 1 \}.

Trong mặt phẳng :math:`Oxy` với hai vector :math:`\bm{u}` và :math:`\bm{v}` không cùng phương thì fundamental domain là hình bình hành tạo bởi hai vector đó.

.. prf:remark:: 
	:label: rmk-lattice-fundamental-domain

	Gọi :math:`\mathcal{L} \subset \mathbb{R}^n` là lattice với số chiều là :math:`n` và gọi :math:`\mathcal{F}` là fundamental domain của :math:`\mathcal{L}`. Khi đó mọi vetor :math:`\bm{w} \in \mathbb{R}^n` đều có thể viết dưới dạng
		
	.. math:: \bm{w} = \bm{t} + \bm{v}

	với :math:`\bm{t}` duy nhất thuộc :math:`\mathcal{F}` và :math:`\bm{v}` duy nhất thuộc :math:`\mathcal{L}`.

Một cách tương đương, hợp của các fundamental domains

.. math:: \mathcal{F} + \bm{v} = \{ \bm{t} + \bm{v} : \bm{t} \in \mathcal{F} \}

với :math:`\bm{v}` là các vector trong :math:`\mathcal{L}`, sẽ bao phủ hết :math:`\mathbb{R}^n`.

.. admonition:: Chứng minh
	:class: danger, dropdown

	Để chứng minh nhận xét trên, giả sử :math:`\{ \bm{v}_i : 1 \leqslant i \leqslant n \}` là cơ sở của :math:`\mathcal{L}`. Khi đó các :math:`\bm{v}_i` độc lập tuyến tính nên cũng là cơ sở của :math:`\mathbb{R}^n`.
		
	Ta viết các vector :math:`\bm{w} \in \mathbb{R}^n` dưới dạng tổ hợp tuyến tính của :math:`\bm{v}_i` và tách hệ số trước mỗi vector thành phần nguyên và phần lẻ. Phần nguyên cho vector trong :math:`\mathcal{L}` và phần lẻ cho vector trong :math:`\mathcal{F}`.
		
	Để chứng minh tính duy nhất của tổ hợp, xét hai cách biểu diễn khác nhau của :math:`\bm{w}` và chứng minh hai cách đó là một.

.. prf:theorem:: Bất đẳng thức Hadamard
	:label: thm-hadamard-ineq

	Cho lattice :math:`\mathcal{L}`, lấy cơ sở bất kỳ của :math:`\mathcal{L}` là các vector :math:`\bm{v}_1`, ..., :math:`\bm{v}_n` và gọi :math:`\mathcal{F}` là fundamental domain cho :math:`\mathcal{L}`. Khi đó

	.. math:: \det L = \text{Vol} (\mathcal{F}) \leqslant \lVert \bm{v}_1 \rVert \cdot \lVert \bm{v}_2 \rVert \cdots \lVert \bm{v}_n \rVert.

Cơ sở càng gần với trực giao thì bất đẳng thức Hadamard trên càng trở thành đẳng thức.

.. prf:definition:: Đa thức cyclotomic
	:label: def-cyclotomic-poly
	
	Với mỗi số nguyên dương :math:`N`, đa thức cyclotomic thứ :math:`N` là đa thức tối giản :math:`\Phi_N` duy nhất trong :math:`\mathbb{Z}[x]` sao cho :math:`x^N - 1` chia hết cho :math:`\Phi_N` nhưng :math:`x^k - 1` không chia hết cho :math:`\Phi_N` với mọi :math:`k < N`.

.. prf:example:: 
	:label: exp-cyclotomic-poly

	Ví dụ, xét :math:`x^3 - 1 = (x - 1)(x^2 + x + 1)`:

	- với :math:`k = 1`, ta có :math:`(x^2 + x + 1) \nmid (x - 1)`;
	- với :math:`k = 2`, ta có :math:`(x^2 + x + 1) \nmid (x^2 - 1)`;
	- với :math:`k = 3`, theo phân tích nhân tử trên thì :math:`(x^2 + x + 1) \mid (x^3 - 1)`.

	Như vậy :math:`\Phi_3 = x^2 + x + 1`.

.. prf:remark:: 
	:label: rmk-cyclotomic-poly

	Nếu :math:`d` là số nguyên tố thì :math:`\Phi_d = 1 + x + x^2 + \ldots + x^{d-1}`.

.. prf:remark:: 
	:label: rmk-cyclotomic-poly-Q

	Các đa thức tối giản không chỉ đối với :math:`\mathbb{Z}` mà còn đối với :math:`\mathbb{Q}`. Ta cũng có thể chứng minh được rằng:

	.. math:: x^N - 1 = \prod_{d \mid N} \Phi_d(x).

.. prf:definition:: 
	:label: def-lambda-i
	
	Với :math:`i = 1, \ldots, n`, định nghĩa :math:`\lambda_i(\mathcal{L})` là :math:`\lambda` nhỏ nhất sao cho :math:`\mathcal{L}` chứa ít nhất :math:`i` vector độc lập của chuẩn Euclid (Euclidean norm) tại hầu hết :math:`\lambda`. Cụ thể :math:`\lambda_1(\mathcal{L})` là độ dài vector khác không ngắn nhất trong :math:`\mathcal{L}`.
