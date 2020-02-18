# -*- coding: utf-8 -*-
__author__ = "yangtao"


LOG_FILE_NAME = "copy_log_{time}.txt"
log_info = {}
log_file = ""

WIN_PATH_RE = "[A-Za-z]:((?:\\\\\\\\|/)[^\\\\/:*?\"<>|]+)+(?:\\\\\\\\|/)[^/\\\\\s]+"
LINUX_PATH_RE = "(/\w+)+/[^/\\\\\s]+"

#Regular Expression When Searching File Paths
FILE_PATH_RE = "%s|%s"%(WIN_PATH_RE, LINUX_PATH_RE)
#FILE_PATH_RE = "(\/([0-9a-zA-Z]+))+\/.+\.[a-zA-Z]+|[A-Za-z]:((\\.+)+|(/.+)+)\.[A-Za-z]+"

#json file strftime
TIME_FORMAT = "%y%m%d%H%M%S"

#json args
JSON_ARGS = {"sort_keys":True,
             "indent":4,
             "separators":(',', ': ')}

FILES_FLODER_NAME = "files"
RES_FLODER_NAME = "resources"