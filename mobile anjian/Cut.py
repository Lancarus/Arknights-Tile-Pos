#encoding= Utf-8
import json
import time
import pathlib

levels_path = pathlib.Path(__file__).parent / "levels0.json"#side=false����
#levels_path = pathlib.Path(__file__).parent / "levels1.json"#side=true����
with open(levels_path, encoding="UTF-8") as fp:
    start = time.time()
    level_table = json.loads(fp.read())
    for name,data in level_table.items():
        print (name)
        data=data["tiles"]
        data.reverse()#������������
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j]=data[i][j]["pos"]
                
                data[i][j][0],data[i][j][1]=1080-data[i][j][1],data[i][j][0]#ת��Ϊ������������,ԭ��Ϊ�������Ͻ�
        fw = open("../map/"+name+"0.txt", 'w',encoding="UTF-8") #����ͼ��+0�������굽txt
        #fw = open("../map/"+name+"1.txt", 'w',encoding="UTF-8") #����ͼ��+1��������txt
        fw.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))) # ���ַ���д���ļ���
        
    print(time.time()-start)