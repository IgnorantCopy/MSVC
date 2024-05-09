# PyQt配置

## 1.下载PyQt5 / pyqt5_tools

* 在终端中运行命令：

  ```
  pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple/
  pip install pyqt5_tools -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```

* 或者先配置全局下载地址：

  ```
  pip config set global.index_url https://pypi.tuna.tsinghua.edu.cn/simple/
  # 然后直接 pip install
  pip install PyQt5
  pip install pyqt5_tools
  ```

## 2.添加环境变量

* 找到下载的PyQt5和pyqt5_tools包：路径一般为\<python path\>\Lib\site-packages\\<PyQt5/pyqt5_tools\>

  ![1](PyQt配置.assets/1.png)

* 复制路径，添加到环境变量path中

  ![2](PyQt配置.assets/2.png)

## 3.添加PyQt工具到IDE中

### VsCode

* 安装VsCode相关插件PYQT Integration

  ![1](PyQt配置.assets/vscode01.png)

* 进行扩展设置

  ![2](PyQt配置.assets/vscode02.png)

* pyrcc路径设置: 输入pyrcc的路径(一般为\<python path\>\Scripts\pyrcc.exe)，pyrcc用于图片等资源的转换

* pyuic路径设置: 输入pyuic5的路径(一般为\<python path\>\Scripts\pyui5.exe)，pyuic5用于把qt designer设计的.ui文件转换为.py文件

* Qtdesigner路径设置: 输入qt designer的路径(一般为\<python path\>\Lib\site-packages\qt5_applications\Qt\bin\designer.exe)，用于便捷打开qt designer

  ![3](PyQt配置.assets/vscode03.png)
  ![4](PyQt配置.assets/vscode04.png)
  ![5](PyQt配置.assets/vscode05.png)

* 调试：尝试创建一个.ui文件

  ![6](PyQt配置.assets/vscode06.png)
  ![7](PyQt配置.assets/vscode07.png)
  ![8](PyQt配置.assets/vscode08.png)

* 调试：根据.ui文件生成.py文件

  ![9](PyQt配置.assets/vscode09.png)
  ![10](PyQt配置.assets/vscode10.png)

  ​																			—— edit by `朱善哲`

### PyCharm

* 在File->Settings->Tools->External Tools中添加三个external tools: QtDesigner、pyrcc、pyuic

  ![3](./PyQt%E9%85%8D%E7%BD%AE.assets/3.png)

  ![4](./PyQt%E9%85%8D%E7%BD%AE.assets/4.png)

  * QtDesigner

  ![Pycharm01](PyQt配置.assets/Pycharm01.png)

  * pyrcc: Arguments: \$FileName\$​ -o \$FileNameWithoutExtension\$_rc.py

  ![Pycharm02](PyQt配置.assets/Pycharm02.png)

  * pyuic: Arguments: \$FileName​\$ -o \$FileNameWithoutExtension\$.py

  ![Pycharm03](PyQt配置.assets/Pycharm03.png)

* 使用：Tools->External Tools->QtDesigner 来打开qt designer

  ![3](PyQt配置.assets/3-1715244391759.png)

  ​																			—— edit by `马楷恒`

  ### 