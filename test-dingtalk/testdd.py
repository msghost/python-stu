import sys
import requests as rq
import json
import time
import data  #取data文件中的相关密钥
# ci = data.CorpId
# cs = data.CorpSecret
# acc = data.access_token
acc = ""
userid = str(18101738452664402)  #WILL

#获取acc-token
r = rq.get("https://oapi.dingtalk.com/gettoken?corpid=" + data.CorpId +
           "&corpsecret=" + data.CorpSecret)
if r.status_code == 200:
    acc = r.json()
else:
    print("API获取失败")
    sys.exit()
acc = acc["access_token"]
print(acc)  #测试打印acc

#获取人员详细信息
r = rq.get("https://oapi.dingtalk.com/user/get?access_token=" + acc +
           "&userid=" + userid)
get_person_info = r.json()
get_person_name = get_person_info["name"]
print(get_person_name)

#获取人员打卡记录
post_data = {
    "userIds": [userid],
    "checkDateFrom": "2018-04-01 00:00:00",
    "checkDateTo": "2018-04-7 00:00:00"
}
post_json = json.dumps(post_data)
# print(post_json)
r = rq.post(
    "https://oapi.dingtalk.com/attendance/listRecord?access_token=" + acc,
    data=post_json)
# rr = r.text
# print(rr)
get_person_checkin = r.json()

#输出结果到文本

with open(r"c:/test/tmp.txt", "w") as f:
    f.writelines(str(get_person_checkin["recordresult"][0]))

with open(r"c:/test/test.txt", "w") as f:
    f.writelines("通过corpID及corpSecret换取的ACC为：" + acc + "\n")
    f.writelines("查询员工ID：" + userid + "\n")
    f.writelines("获取到的员工名称：" + get_person_name + "\n")
    f.writelines("获取到的员工考勤数据如下：\n")
    f.writelines("打卡时间：")
    # f.writelines(str(time.localtime(int(get_person_checkin["recordresult"][0]["userCheckTime"]))))
    w_time = int(str(get_person_checkin["recordresult"][0]["userCheckTime"])[0:10])
    f.writelines(str(time.asctime(time.localtime(w_time))))
    f.writelines("\n打卡地点："+get_person_checkin["recordresult"][0]["userAddress"])
    f.writelines("\n考勤类型："+get_person_checkin["recordresult"][0]["checkType"])
    f.writelines("\n考勤状态："+get_person_checkin["recordresult"][0]["timeResult"])
    f.writelines("\n打卡设备："+get_person_checkin["recordresult"][0]["sourceType"])
    # f.writelines()
