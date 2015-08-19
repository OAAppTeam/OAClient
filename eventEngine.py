# encoding: UTF-8

# 系统模块
from Queue import Queue, Empty

# 自己开发的模块
from eventType import *


########################################################################
class Event:
    """事件对象"""

    #----------------------------------------------------------------------
    def __init__(self, type_=None):
        """Constructor"""
        self.type_ = type_      # 事件类型
        self.dict_ = {}         # 字典用于保存具体的事件数据

