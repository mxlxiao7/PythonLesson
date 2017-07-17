class NamedList(list):
    def __init__(self, a_name):
        # 初始化派生的类
        list.__init__([])
        self.name = a_name
