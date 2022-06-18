# -*- coding: utf-8 -*-
'''
   本脚本用来合并pdf文件，支持带一级子目录的
   每章内容分别放在不同的目录下，目录名为章节名
   最终生成的pdf，按章节名生成书签
'''

import os
import sys
import codecs
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import glob


def getFileName(filepath):
    '''
        获取当前目录下的所有pdf文件
    '''
    file_list = glob.glob(filepath + "/*.pdf")
    # 默认安装字典序排序，也可以安装自定义的方式排序
    # file_list.sort()
    return file_list


def get_dirs(filepath='', dirlist_out=[], dirpathlist_out=[]):
    # 遍历filepath下的所有目录
    for dir in os.listdir(filepath):
        dirpathlist_out.append(filepath + '\\' + dir)

    return dirpathlist_out


def merge_childdir_files(path):
    '''
        每个子目录下合并生成一个pdf
    '''
    dirpathlist = get_dirs(path)
    if len(dirpathlist) == 0:
        print("当前目录不存在子目录")
        sys.exit()
    for dir in dirpathlist:
        mergefiles(dir, dir)


def mergefiles(path, output_filename, import_bookmarks=False):
    # 遍历目录下的所有pdf将其合并输出到一个pdf文件中，输出的pdf文件默认带书签，书签名为之前的文件名
    # 默认情况下原始文件的书签不会导入，使用import_bookmarks=True可以将原文件所带的书签也导入到输出的pdf文件中
    merger = PdfFileMerger()
    filelist = getFileName(path)
    if len(filelist) == 0:
        print("当前目录及子目录下不存在pdf文件")
        sys.exit()
    for filename in filelist:
        f = codecs.open(filename, 'rb')
        file_rd = PdfFileReader(f)
        short_filename = os.path.basename(os.path.splitext(filename)[0])
        if file_rd.isEncrypted == True:
            print('不支持的加密文件：%s' % (filename))
            continue
        merger.append(file_rd,
                      bookmark=short_filename,
                      import_bookmarks=import_bookmarks)
        print('合并文件：%s' % (filename))
        f.close()
    # out_filename = os.path.join(os.path.abspath(path), output_filename)
    merger.write(output_filename + ".pdf")
    print('合并后的输出文件：%s' % (output_filename))
    merger.close()


if __name__ == "__main__":
    # 每个章节一个子目录，先分别合并每个子目录文件为一个pdf，然后再将这些pdf合并为一个大的pdf，这样做目的是想生成每个章节的书签

    # 1.指定目录
    # 原始pdf所在目录
    path = "D:\复旦\模块课\微生物\pdf"
    # 输出pdf路径和文件名
    output_filename = "D:\复旦\模块课\微生物\pdf"

    # 2.生成子目录的pdf
    # merge_childdir_files(path)

    # 3.子目录pdf合并为总的pdf
    mergefiles(path, output_filename)
