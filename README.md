### 知识工程课程数据
> * data 文件夹下包含数据集文件 `lubm.nt`, 查询文件 `query.rq`;
> * LUBM 是开源数据集, 自动生成的关于大学的虚拟数据, 具体可参考[**LUBM**官网](http://swat.cse.lehigh.edu/projects/lubm)
> * LUBM生成的数据是 `.owl` 格式, 这里我们需要的 `.nt` 格式的数据, 需要进行转换。转换程序为 `Owl2Nt.py`, 参考自[LUBM数据的生成](https://blog.csdn.net/liujiang0529/article/details/86567828)