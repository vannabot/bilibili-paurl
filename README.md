# papa_re.py
爬取相关搜索页面下的所有信息（title、link、av号）
# json_xlwt.py
将json数据转换成xls文件
# Bilibili
下载B站视频到本地




## 代码完整的运行方法：  
1. 修改bilibili.py中的 aid 参数为你想要下载的视频编号，视频编号可在对应视频url尾部找到，  
如 [https://www.bilibili.com/video/av6538245](https://www.bilibili.com/video/av6538245)   
对应的视频编号为6538245。

2. 运行 bilibili.py 文件，该文件会在当前文件夹下创建对应的视频存储目录，并且将aid对应的  
视频的所有视频片段下载到本地。默认启用5个进程进行下载，可以修改bilibili.py文件中的process_count  
参数进行调整。  

3. 待所有视频都已下载完成之后，修改merge_flv.py文件中的 root_dir 参数为你刚刚下载视频时自动  
创建的那个根目录文件名，然后运行merge_flv.py文件。该文件会把同为一个视频的flv视频片段文件合并  
成mp4文件并保存在同一文件夹下。