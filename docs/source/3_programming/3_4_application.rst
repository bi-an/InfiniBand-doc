3.4 典型应用
-------------------

本文档提供了两个示例程序：

- RDMA_RC_example: 使用 VPI verbs API，演示如何执行 RC: Send、Receive、
  RDMA read 和 RDMA write 操作。
- multicast example: 使用 RDMA_CM verbs API，演示多播 UD。

一个典型的应用程序的结构如下。编程示例中实现每个步骤的函数以高亮表示。

#. 获取设备列表；

   第一步，必须获取本地主机上可用的 IB 设备。该列表中的每个设备包含一个名称和一个 GUID。
   比如设备名称可以是：mthca0、mlx4_1。

   示例实现: :code:`resources_create`

#. 打开被请求的设备；

   遍历设备列表，根据设备的 GUID 或名称选择设备并打开它。

   示例实现: :code:`resources_create`

#. 查询设备能力；

   查询支持的特性 (APM、SRQ) 和设备的能力。

   示例实现: :code:`resources_create`

#. 分配一个保护域来容纳你的资源；

   PD 允许用户对哪些组件能相互交换进行限制。这些组件包括： AH, QP, MR, MW 和 SRQ。

   示例实现: :code:`resources_create`

#. 注册一个内存区域；

   VPI 只能在被注册的内存中工作。进程的虚拟空间中的任何内存缓冲区都可以被注册。
   在注册过程中，用户设置内存权限并接收将来用来引用该内存缓冲区的本地和远程密钥 (lkey/rkey)。

   示例实现: :code:`resources_create`

#. 创建一个完成队列 (CQ)；

   完成队列用来容纳工作请求 (work quest, WR)。每个 WR 将产生一个完成队列项 (CQE) 放入到 CQ 中。
   CQE 将指定该 WR 是否成功完成。

   示例实现: :code:`resources_create`

#. 创建一个队列对；

   创建 QP 时会同时创建一对相关联的发送队列和接收队列。

   示例实现: :code:`resources_create`

#. 启动 QP；

   创建的 QP 不能直接使用，除非它经历了几个状态转换之后，最终变成"准备发送 (Ready to Send, RTS)" 状态 。

   示例实现:
   :code:`connect_qp` ,
   :code:`modify_qp_to_init` ,
   :code:`post_receive` ,
   :code:`modify_qp_to_rtr` 和
   :code:`modify_qp_to_rts`

#. 发布工作请求并轮询完成状态；

   使用创建好的 QP 进行通信操作。

   示例实现:
   :code:`post_send` 和
   :code:`poll_completion`

#. Cleanup；

   按照创建对象的相反顺序销毁对象：

   - 删除 QP；
   - 删除 CQ；
   - 注销 MR；
   - 释放 PD；
   - 关闭设备。

   示例实现: :code:`resources_destroy`
