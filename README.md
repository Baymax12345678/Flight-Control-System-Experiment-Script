## 脚本使用教学

首先把MACH(1)值的后两位改为自己的学号，改好其他要求的参数。下面以修改SAVSI参数为例讲解脚本如何使用。

1. 通过python或者运行main.exe启动脚本

   此处以python为例，转到脚本所在文件夹，输入 `python .\main.py ` 执行脚本，执行后可以看见下图：

   ![image-20250321225516399](https://raw.githubusercontent.com/Baymax12345678/img_repo/master/img_windows/image-20250321225516399.png)

2. 设置参数值与步长

   脚本需要参数，此处起始值填 `1.1`，结束值填 `1.4`，步长填 `0.1`，脚本将依次修改 SAVSI 的值为 `1.1、1.2、1.3、1.4`。

3. 填入待修改参数的字符串

   此处待修改的参数为 SAVSI，故填入SAVSI。随后，找到 SAVSI 所在行，复制该行，填入 `替换字符串` 中，如下所示：

   ![image-20250321230049049](https://raw.githubusercontent.com/Baymax12345678/img_repo/master/img_windows/image-20250321230049049.png)

4. 选择配置参数文件(即 `Citation0.dcm`）的路径以及 `datcom.exe` 的路径

   点击浏览选择路径即可，如下图：

   ![image-20250321230257685](https://raw.githubusercontent.com/Baymax12345678/img_repo/master/img_windows/image-20250321230257685.png)

5. 点击开始执行

   执行结束后可以得到使用不同SAVSI值的结果，如图：

   ![image-20250321230403020](https://raw.githubusercontent.com/Baymax12345678/img_repo/master/img_windows/image-20250321230403020.png)

   

