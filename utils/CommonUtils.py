import os


#
# 处理时间
#



def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return time_str

    (mins, secs) = time_str.split(splitter)
    return (mins + '.' + secs);


#
# 处理时间
#
def deal_data(data):
    return_value = []
    for item_str in data:
        return_value.append(sanitize(item_str))
    return return_value


#
# 读取文件信息
#
def load_data(path):
    if os.path.exists(path):
        with open(path) as data:
            return data.readline()


#
# 在res文件目录中加载目标文件
#
def load_res_file(target_dir, file_name):
    file_path = ''

    for root, dirs, files in os.walk(target_dir):
        if file_name in files:
            file_path = root + file_name

    if file_path != '':
        try:
            with open(file_path) as data:
                return data.readline()
        except IOError as err:
            print(file_path + " 读取失败: " + str(err))


#
# 加载教练数据
#
def load_coach_data(file_name, target_dir=os.getcwd() + "/res/"):
    # 加载数据
    data = load_res_file(target_dir, file_name)

    if data is not None:
        # 去空并分组
        data = data.strip().split(',')

        # 使用字典数据结构
        from model.Athlete import Athlete
        data_obj = Athlete(data.pop(0), data.pop(0), data)
        return data_obj
