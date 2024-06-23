1 词汇表
===========

.. * `CQ` - Complete Queue 完成队列
.. * `WQ` - Work Queue 工作队列
.. * `WR` - Work Request 工作请求
.. * `QP` - Queue Pairs 队列对（Send-Receive）
.. * `SQ` - Send Queue 发送队列
.. * `RQ` - Receive Queue 接收队列
.. * `PD` - Protection Domain 保护域，将QP和MR结合在一起
.. * `MR` - Memory Region 内存区域。一块经注册过的且本地网卡可以读写的内存区域。包含R_Key和L_Key。
.. * `SGE` - Scatter/Gather Elements 分散/聚集元素。
.. * `R_Key` - Remote Key
.. * `L_Key` - Local Key
.. * `CA` - (Host) Channel Adapter, an inifiniband network interface card.
.. * `NIC` - Network Interface Card 网卡。
.. * `LID` - Local Identifier.
.. * `CM` - Connection Manager.

.. csv-table::
    :header: "术语", "描述"
    :widths: 20,60
    :class: tight-table

    "Access Layer 访问层 ", "用于访问互连结构（VPI™、InfiniBand®、以太网、FCoE）的低级操作系统基础设施
    （管道pumping）。它包括支持上级网络协议、中间件和管理代理所需的所有基本传输服务。"
    "AH (Address Handle 地址句柄)", "描述 UD QP 中使用的远端路径的对象"
    "CA (Channel Adapter 通道适配器)", "终止 InfiniBand 链路并执行传输层功能的设备"
    "CM (Communication Manager 通信管理器)", "负责为 RC 和 UC QP 服务类型建立、维护和释放通信的实体。
    服务 ID 解析协议使 UD 服务的用户能够找到支持其所需服务的 QP。终端节点的每个 IB 端口都有一个 CM。"
    "Compare & Swap 比较和交换", "指示远程 QP 读取一个 64 位值，将其与提供的比较数据进行比较，如果相等，
    则将其替换为 QP 中提供的交换数据。"
    "CQ (Completion Queue 完成队列)", "包含 CQE 的队列 (FIFO)"
    "CQE (Completion Queue Entry 完成队列条目)", "CQ 中的一个条目，描述有关已完成 WR 的信息（状态大小等）"
    "DMA (Direct Memory Access 直接内存访问)", "允许硬件将数据块直接移入或移出内存，绕过 CPU"
    "Fetch & Add", "指示远程 QP 读取一个 64 位值，并将其替换为 QP 中提供的 64 位值与增加的数据值的总和。"
    "GUID (Globally Unique IDentifier 全局唯一标识符)", "唯一标识子网中的设备或组件的 64 位数字"
    "GID (Global IDentifier 全局标识符)", "用于识别网络适配器上的端口、路由器上的端口或多播组的 128 位标识符。
    GID 是有效的 128 位 IPv6 地址（根据 RFC 2373），具有在 IBA 中定义的附加属性/限制，以促进高效的发现、通信
    和路由。"
    "GRH (Global Routing Header 全局路由头)", "用于跨子网边界传递数据包并用于传递多播消息的数据包头。此数据
    包头基于 IPv6 协议。"
    "TODO"

© Copyright 2023, NVIDIA. 最后更新于 2023 年 5 月 23 日。