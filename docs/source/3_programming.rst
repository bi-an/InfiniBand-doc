3 RDMA 感知编程概述
===================

VPI 架构允许直接以用户模式访问硬件。Mellanox 提供动态加载库，通过 verbs API 创建对硬件的访问。
本文档包含通过操作系统编程接口公开的 verbs 及其相关输入、输出、描述和功能。

.. warning::
    本编程手册及其 Verbs 仅适用于用户空间。请参阅内核空间 Verbs 的头文件。

| 使用 verbs 进行编程可以自定义和优化 RDMA-Aware 网络。这种自定义和优化只能由在 VPI 系统方面具有
  高级知识和经验的程序员完成。
| 为了执行 RDMA 操作，首先需要建立与远程主机的连接以及设置适当的权限。实现此目的的机制是队列对 (QP)。
  对于熟悉标准 IP 堆栈的人来说，QP 大致相当于套接字。需要在连接的两端初始化 QP。在实际设置 QP 之前，
  可以使用通信管理器 (CM) 交换有关 QP 的信息。
| 一旦建立了 QP，就可以使用 verbs API 执行 RDMA 读取、RDMA 写入和原子操作。也可以执行类似于套接字读
  取/写入的序列化发送/接收操作。

.. toctree::
   :maxdepth: 1

   3_programming/3_1_operations.rst
   3_programming/3_2_transport.rst
   3_programming/3_3_concepts.rst
   3_programming/3_4_application.rst
