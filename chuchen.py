from opcua import Client
import time
import os

# 连接到OPC UA服务器
url = "opc.tcp://10.19.7.250:49320"  # 替换为实际的Endpoint URL
client = Client(url)
client.connect()
print("数采服务器连接成功")

# 浏览OPC节点
root = client.get_root_node()
objects_node = root.get_child(["0:Objects"])
node_children = objects_node.get_children()
#for child in node_children:
#    print(child.get_browse_name().Name)

tpd_node = objects_node.get_child(["2:HI_TPDCC", "2:PLC"])
tpx_node = objects_node.get_child(["2:HI_TPXCC", "2:PLC"])
slxx_node = objects_node.get_child(["2:HI_SLXXPXCC", "2:PLC", "2:MES"])
rmp_node = objects_node.get_child(["2:HI_RMPXCC", "2:PLC", "2:MES"])
slzd_node = objects_node.get_child(["2:HI_SLZDXPXCC", "2:PLC", "2:MES"])
#plc_children = plc_node.get_children()
#for child in plc_children:
#    print(child.get_browse_name().Name)

while True:
    #清屏
	#os.system('cls' if os.name == 'nt' else 'clear')

    # 读取变量值
    ckyl_node = tpd_node.get_child(["2:CKYL"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌出口压力: ", value)
    
    ckyl_node = tpd_node.get_child(["2:RKYL"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌入口压力: ", value)
    
    ckyl_node = tpd_node.get_child(["2:YC"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌风口压差： ", value)
    
    ckyl_node = tpd_node.get_child(["2:HDWD1"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌灰斗温度1： ", value)
    
    ckyl_node = tpd_node.get_child(["2:HDWD2"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌灰斗温度2： ", value)
    
    ckyl_node = tpd_node.get_child(["2:HDWD3"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌灰斗温度3： ", value)
    
    ckyl_node = tpd_node.get_child(["2:HDWD4"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌灰斗温度4： ", value)
    
    ckyl_node = tpd_node.get_child(["2:XTYXYC"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌系统远程运行： ", value)
    
    ckyl_node = tpd_node.get_child(["2:XTYXBD"])
    value = ckyl_node.get_value()
    print("\r特喷喷锌系统本地运行： ", value)

    
    
    #plc_children = plc_node.get_children()
    #for child in plc_children:
    #    print(child.get_browse_name().Name)
    
    # 读取变量值
    ckyl_node = tpx_node.get_child(["2:CKYL"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌出口压力: ", value)
    
    ckyl_node = tpx_node.get_child(["2:RKYL"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌入口压力: ", value)
    
    ckyl_node = tpx_node.get_child(["2:YC"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌风口压差： ", value)
    
    ckyl_node = tpx_node.get_child(["2:HDWD1"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌灰斗温度1： ", value)
    
    ckyl_node = tpx_node.get_child(["2:HDWD2"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌灰斗温度2： ", value)
    
    ckyl_node = tpx_node.get_child(["2:HDWD3"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌灰斗温度3： ", value)
    
    ckyl_node = tpx_node.get_child(["2:HDWD4"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌灰斗温度4： ", value)
    
    ckyl_node = tpx_node.get_child(["2:XTYXYC"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌系统远程运行： ", value)
    
    ckyl_node = tpx_node.get_child(["2:XTYXBD"])
    value = ckyl_node.get_value()
    print("\r小特喷喷锌系统本地运行： ", value)


    #plc_children = slxx_node.get_children()
    #for child in plc_children:
    #    print(child.get_browse_name().Name)
    
    # 读取变量值
    ckyl_node = slxx_node.get_child(["2:CKYL"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌出口压力: ", value)
    
    ckyl_node = slxx_node.get_child(["2:RKYL"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌入口压力: ", value)
    
    ckyl_node = slxx_node.get_child(["2:YC"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌风口压差： ", value)
    
    ckyl_node = slxx_node.get_child(["2:HDWD1"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌灰斗温度1： ", value)
    
    ckyl_node = slxx_node.get_child(["2:HDWD2"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌灰斗温度2： ", value)
    
    ckyl_node = slxx_node.get_child(["2:HDWD3"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌灰斗温度3： ", value)
    
    ckyl_node = slxx_node.get_child(["2:HDWD4"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌灰斗温度4： ", value)
    
    ckyl_node = slxx_node.get_child(["2:XTYXYC"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌系统远程运行： ", value)
    
    ckyl_node = slxx_node.get_child(["2:XTYXBD"])
    value = ckyl_node.get_value()
    print("\r水冷小线喷锌系统本地运行： ", value)


    #plc_children = plc_node.get_children()
    #for child in plc_children:
    #    print(child.get_browse_name().Name)
    
    # 读取变量值
    ckyl_node = rmp_node.get_child(["2:CKYL"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌出口压力: ", value)
    
    ckyl_node = rmp_node.get_child(["2:RKYL"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌入口压力: ", value)
    
    ckyl_node = rmp_node.get_child(["2:YC"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌风口压差： ", value)
    
    ckyl_node = rmp_node.get_child(["2:HDWD1"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌灰斗温度1： ", value)
    
    ckyl_node = rmp_node.get_child(["2:HDWD2"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌灰斗温度2： ", value)
    
    ckyl_node = rmp_node.get_child(["2:HDWD3"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌灰斗温度3： ", value)
    
    ckyl_node = rmp_node.get_child(["2:HDWD4"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌灰斗温度4： ", value)
    
    ckyl_node = rmp_node.get_child(["2:XTYXYC"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌系统远程运行： ", value)
    
    ckyl_node = rmp_node.get_child(["2:XTYXBD"])
    value = ckyl_node.get_value()
    print("\r热模大线喷锌系统本地运行： ", value)


    # 读取变量值
    ckyl_node = slzd_node.get_child(["2:CKYL"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌出口压力: ", value)
    
    ckyl_node = slzd_node.get_child(["2:RKYL"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌入口压力: ", value)
    
    ckyl_node = slzd_node.get_child(["2:YC"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌风口压差： ", value)
    
    ckyl_node = slzd_node.get_child(["2:HDWD1"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌灰斗温度1： ", value)
    
    ckyl_node = slzd_node.get_child(["2:HDWD2"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌灰斗温度2： ", value)
    
    ckyl_node = slzd_node.get_child(["2:HDWD3"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌灰斗温度3： ", value)
    
    ckyl_node = slzd_node.get_child(["2:HDWD4"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌灰斗温度4： ", value)
    
    ckyl_node = slzd_node.get_child(["2:XTYXYC"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌系统远程运行： ", value)
    
    ckyl_node = slzd_node.get_child(["2:XTYXBD"])
    value = ckyl_node.get_value()
    print("\r水冷中大线喷锌系统本地运行： ", value)
    
    time.sleep(60)

# 断开连接
client.disconnect()