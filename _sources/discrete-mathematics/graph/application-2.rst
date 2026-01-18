
Ứng dụng 2: tối ưu bằng thuật toán Kruskal
==========================================

Đặt vấn đề: trường Đại học U đang cho xây dựng tòa nhà mới và chuẩn bị đi dây điện. Vấn đề là kinh phí nhà trường cần dùng cho nhiều việc khác nên nhà trường cần tính toán chi phí cho việc đi dây là ít nhất. Độ dài dây cần có để đi ngầm qua các phòng tầng 3 của tòa nhà có cấu trúc như sau:

.. figure:: figures/kruskal_problem.*

Để giảm chi phí nhà trường cần xác định những đường dây nào sẽ được kéo sao cho tổng độ dài là thấp nhất. Việc này được giao cho bộ môn toán-lý tính toán và thuật toán Kruskal được sử dụng cho mục đích này.

Để giải quyết bài toán này, đầu tiên chúng ta thử mô hình hóa bài toán. Nếu ta coi các phòng là các đỉnh đồ thị và độ dài dây nối giữa các phòng là trọng số của đồ thị đó. Ta quy ước như sau để dễ cài đặt trên máy tính:

.. math::

    \text{Phòng C305} \Longleftrightarrow 0, \ \text{Phòng C306} \Longleftrightarrow 1, \ \text{Phòng C307} \Longleftrightarrow 2, \ \text{Phòng C308} \Longleftrightarrow 3 \\
    \text{Phòng C309} \Longleftrightarrow 4, \ \text{Phòng C310} \Longleftrightarrow 5, \ \text{Phòng C311} \Longleftrightarrow 6, \ \text{Phòng C312} \Longleftrightarrow 7
    
Từ quy ước trên ta có ma trận trọng số sau

.. math:: 

    \left(\begin{array}{cccccccc}
        0 & 23 & 0 & 0 & 47 & 40 & 51 & 0 \\
        23 & 0 & 0 & 0 & 0 & 0 & 49 & 0 \\
        0 & 0 & 0 & 25 & 10 & 0 & 0 & 65 \\
        0 & 0 & 25 & 0 & 0 & 0 & 0 & 0 \\
        47 & 0 & 10 & 0 & 0 & 0 & 0 & 27 \\
        40 & 0 & 0 & 0 & 0 & 0 & 35 & 0 \\
        51 & 49 & 0 & 0 & 0 & 35 & 0 & 0 \\
        0 & 0 & 65 & 0 & 27 & 0 & 0 & 0
    \end{array}\right).

.. \subsubsection{Xử lý trên máy tính}

Sau khi mô hình bài toán trở thành đồ thị trên máy tính, ta sử dụng chương trình sau để tính toán cây khung nhỏ nhất bằng thuật toán Kruskal.

Đầu tiên ta nhập vào file ``input.txt`` số đỉnh đồ thị và ma trận trọng số như sau:

.. code-block:: text

    8
    0 23 0 0 47 40 51 0
    23 0 0 0 0 0 49 0
    0 0 0 25 10 0 0 65
    0 0 25 0 0 0 0 0
    47 0 10 0 0 0 0 27
    40 0 0 0 0 0 35 0
    51 49 0 0 0 35 0 0
    0 0 65 0 27 0 0 0

Tiếp đến, đọc đồ thị lên từ file ``input.txt`` rồi tính toán. Code của thuật toán như sau:

.. code-block:: cpp

    #include <stdio.h>
    #include <vector>
    #include <algorithm>

    using namespace std;

    struct edge
    {
        int u, v;   // đỉnh u nối với đỉnh v
        int weight; // trọng số cạnh (u, v)
        edge(int u, int v, int weight) : u(u), v(v), weight(weight) {}
    };

    vector<edge> edges;
    vector<int> parent;

    bool IsLarger(edge a, edge b); // for std::sort
    int GetRoot(int p);
    void Join(int p, int q);

    int main()
    {
        int i = 0, j = 0, k = 0;
        int w;
        int nVertices;
        int weightSum = 0;
        FILE *file;
        file = fopen("input.txt", "r");
        if (file == NULL)
            return 1;

        fscanf(file, "%d", &nVertices);
        for (i = 0; i < nVertices; i++)
        {
            for (j = 0; j < nVertices; j++)
            {
                fscanf(file, "%d", &w);
                if (w != 0)
                {
                    edges.push_back(edge(i, j, w));
                }
            }
            parent.push_back(i);
        }

        k = edges.size();
        sort(edges.begin(), edges.end(), IsLarger);

        for(i = 0; i < k; i++)
            if (GetRoot(edges[i].u) != GetRoot(edges[i].v))
            {
                Join(edges[i].u, edges[i].v);
                weightSum += edges[i].weight;
                printf("Edge: %d-%d. Weight: %d\n", edges[i].u, edges[i].v, edges[i].weight);
            }
        printf("Sum of weights: %d\n", weightSum);
        
        fclose(file);
        return 0;
    }

    bool IsLarger(edge a, edge b)
    {
        return a.weight < b.weight;
    }

    int GetRoot(int p) 
    { 
        if (parent[p] == p) return p; 
        else return parent[p] = GetRoot(parent[p]); 
    }

    void Join(int p, int q)
    { 
        parent[GetRoot(p)] = GetRoot(q); 
    }


Kết quả thu được như sau gồm:

- cạnh :math:`(2, 4)` với trọng số :math:`10`;
- cạnh :math:`(1, 0)` với trọng số :math:`23`;
- cạnh :math:`(2, 3)` với trọng số :math:`25`;
- cạnh :math:`(7, 4)` với trọng số :math:`27`;
- cạnh :math:`(6, 5)` với trọng số :math:`35`;
- cạnh :math:`(0, 5)` với trọng số :math:`40`;
- cạnh :math:`(4, 0)` với trọng số :math:`47`.

Như định nghĩa ở trên, các phòng sẽ được gán một số nguyên để dễ biểu diễn. Từ kết quả này ta thu được cây khung nhỏ nhất của đồ thị là:

.. figure:: figures/kruskal_result.*
