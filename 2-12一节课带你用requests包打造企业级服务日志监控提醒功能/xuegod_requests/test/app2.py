# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request,render_template,redirect,url_for,send_from_directory,abort,make_response
from werkzeug.utils import secure_filename
import json,os,time
from flask_cors import *
import pymysql
import shutil

app = Flask(__name__)

import contextlib
#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='106.14.118.36', port=3306, user='park', passwd='abc123456', db='maps',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()


import base64

#加密
def encry(cnf_org):
    f_org = open(cnf_org, 'rb')
    content = f_org.read()
    content1 = base64.b64encode(content)
    f_org.close()
    with open(cnf_org, 'wb+') as f_org:
        f_org.write(content1)

#解密
def deci(cnf_now):
    f_now = open(cnf_now, 'r')
    content = f_now.read()
    content1 = base64.b64decode(content)
    with open(cnf_now, 'wb+') as f:
        f.write(content1)

@app.route('/')
def home():
    return render_template("upload.html")
@app.route('/index')
def loginIndex():
    return render_template("login.html")

@app.route('/login', methods=['GET','POST'])
def login():
    username= request.args.get("username",'root')#获取前台json数据
    password = request.args.get("password",'123456')  # 获取前台json数据
    with mysql() as cursor:
        row_count = cursor.execute("select * from users where username='root'")
        if row_count:
            row_1 = cursor.fetchone()
            print(row_1)
            if row_1["password"]==password:
                return jsonify(200)
            else:
                print(2)
                return jsonify(400)
        else:
            print(3)
            return jsonify(204)

    conn.commit()
    cursor.close()
    conn.close()
import subprocess
import zipfile as zf
import platform as pf

class ZipObj():

    def __init__(self,filepathname,passwd):
        self.filepathname = filepathname
        self.passwd = passwd
    def enCrypt(self,deleteSource=False):
        """
            压缩加密，并删除原数据
            window系统调用rar程序

            linux等其他系统调用内置命令 zip -P123 tar source
            默认不删除原文件
        """
        target = self.filepathname#+'.zip'
        source = self.filepathname
        if pf.system()=="Windows":
            cmd = ['rar','a','-p%s'%(self.passwd.encode('utf-8')),target,source]
            p = subprocess.Popen(cmd,executable=r'C:\Program Files\WinRAR\WinRAR.exe')
            p.wait()
        else:
            cmd = ['zip','-P %s'%(self.passwd),target,source]
            p = subprocess.Popen(cmd)
            p.wait()
#            os.system(" ".join(cmd))
        if deleteSource:
            shutil.rmtree(source)
    def deCrypt(self):
        """
        使用之前先创造ZipObj类
        解压文件
        """
        zfile = zf.ZipFile(self.filepathname)
        zfile.extractall(self.filepathname+".zip",pwd=self.passwd.encode('utf-8'))


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        upload_path = os.path.join('./static/uploads',secure_filename(f.filename)).replace("\\","/")  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        encry(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')

@app.route('/jiami/', methods=['GET'])
def jiami():
    if request.method == "GET":
        filename=request.args.get("filename")
        password = request.args.get("password")
        path = os.path.join('./static/uploads', filename).replace("\\","/")
        zipo = ZipObj(path, password)
        print(path)
        zipo.enCrypt(deleteSource=True) ##
        # zipo.deCrypt()
        return jsonify("加密压缩成功")

@app.route('/jiemi/', methods=['GET'])
def jiemi():
    if request.method == "GET":
        filename=request.args.get("filename")
        password = request.args.get("password")
        path = os.path.join('./static/uploads', filename).replace("\\","/")
        zipo = ZipObj(path, password)
        # zipo.enCrypt(deleteSource=False)  ##
        zipo.deCrypt()
        return jsonify("加密压缩成功")


@app.route('/filepath', methods=['POST', 'GET'])
def fliepath():
    if request.method == "GET":
        path = os.listdir('./static/uploads')
        print(path)
        return jsonify({"data":path})
    abort(404)


if __name__ == "__main__":
    app.run(
    host = '0.0.0.0',
    port = 5000,
    debug = True
)