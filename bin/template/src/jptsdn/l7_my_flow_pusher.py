#!/usr/bin/python3
# coding: utf-8
##################################################################
# 使用方法:
# from l7_my_flow_pusher import StaticFlowPusher, Switch, Controller  # 不能用 -, ......
# pusher = StaticFlowPusher()
# ctl = Controller()  # 剩下的看 main 中的测试
##################################################################
URL_STATIC_FLOW_PUSHER_JSON = 'http://localhost:8080/wm/staticflowpusher/json'
URL_SWITCHS = 'http://127.0.0.1:8080/wm/core/controller/switches/json'
URL_STATIC_FLOW_PUSHER_LIST_JSON = 'http://localhost:8080/wm/staticflowpusher/list/%s/json'
URL_STATIC_FLOW_PUSHER_CLEAR_JSON = 'http://localhost:8080/wm/staticflowpusher/clear/%s/json'
import requests, json, re, subprocess
class StaticFlowPusher:
    def get(self, DPID ='all'):
        url_flow = URL_STATIC_FLOW_PUSHER_LIST_JSON % DPID
        conn = requests.get(url_flow)
        print(json.loads(conn.content))  # there need to be improved
    def removeflowbyname(self, name):
        str = '''curl -X DELETE -d '{"name": "%s"}' ''' % name + URL_STATIC_FLOW_PUSHER_JSON  # @ReservedAssignment
        conn = subprocess.check_output(str)  # print conn[1]  # print type(conn)  # print len(conn)  # print type(conn[1])
        ret = re.findall('{.*?}', conn[1], re.S)[0]
        print(ret)
    def removeflowbyDPID(self, DPID = 'all'):
        url_clear = URL_STATIC_FLOW_PUSHER_CLEAR_JSON % DPID
        conn = requests.get(url_clear)
        print(conn.content)
    def addflow(self, data):
        print(data['name'], end=' ')
        data = json.dumps(data)  # print type(data)
        conn =  requests.post(URL_STATIC_FLOW_PUSHER_JSON, data=data)
        print(conn.content)
    def generateflow(self, switch_id, flow_name, port_num, actions):
        switch_id = str(switch_id)
        payload = {
            "switch": switch_id,
            "name": flow_name,
            "cookie": "0",
            "priority": "32768",
            "in_port": port_num,
            "active": "true",
            "actions": actions
            }
        return payload
class Switch:
    def __init__(self, DPID=None): self._DPID = DPID
    @property
    def DPID(self): return self._DPID
    def __str__(self): return self.DPID
    def __repr__(self): return '"{}"'.format(self.DPID)
class Controller:
    def __init__(self):
        self.switches = []
        self.__get_switch_list()
    def __get_switch_list(self):
        # url_ext = 'curl ' + url + ' | python -mjson.tool'; print commands.getstatusoutput(url_ext)  # it works in the terminal of Ubuntu
        switches = requests.get(URL_SWITCHS).json()  # print type(switches)  # print switches and you will get more infornation
        # print(json.dumps(switches, indent=4))  # output the format json
        for swtich in switches :
            switch = Switch(swtich['switchDPID'])  # print type(switch)
            # print switch  will return the str of instance because of the __str__ attribute
            self.switches.append(switch)
if __name__ == "__main__":
    pusher = StaticFlowPusher()
    ctl = Controller()
    ###########################
    # 1. add/delete flow quickly
    ###########################
#     for switch in range(len(ctl.switches)):
#         for port in range(1, 4):
#             flow = pusher.generateflow(ctl.switches[switch],
#                                        's{0}p{1}f1'.format(switch, port),
#                                        port,
#                                        'output=flood')
#             pusher.addflow(flow)
# #             pusher.removeflowbyname(flow['name'])
# #         pusher.removeflowbyDPID(ctl.switches[switch])
#     pusher.removeflowbyDPID()
    ####################
    # 2. get switchs flow
    ####################
# #     for switch in range(len(ctl.switches)):
# #         pusher.get(ctl.switches[switch])  # get the single switch flows
#     pusher.get()  # get all switchs flows
    #####################################################################################
    # 3. define some single flow or flows that have no law or you have some flow with json
    # example
    #####################################################################################
#     flow1 = {
#         "switch": "00:00:00:00:00:00:00:01",
#         "name": "flow-mod-1",
#         "cookie": "0",
#         "priority": "32767",
#         "in_port": "1",
#         "active": "true",
#         "actions": "output=3"
#         }
#     pusher.addflow(flow1)
