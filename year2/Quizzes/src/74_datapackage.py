class data_package():
    def build_data_pkg(self,mac_rx:str,ip_rx:str,mac_sx:str,ip_sx:str,data:str):
        N=len(data)//4
        if len(data)%4!=0:
            N+=1
        data_package=[]
        for i in range(N):
            data_package.append(f"{mac_rx}|{ip_rx}|{mac_sx}|{ip_sx}|{i}|{data[:4]}")
            data=data[4:]
        return data_package


test = data_package()
print(test.build_data_pkg(mac_rx='80:90:AA:F0:22:11',ip_rx='192.168.1.2',mac_sx='30:AA:1A:F1:00:AE',ip_sx='192.168.1.3',data='Hello world'))

