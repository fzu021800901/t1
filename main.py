import jc
import sys

'''从命令行读取参数'''
try:
    file_path_0 = sys.argv[1]
    file_path_1 = sys.argv[2]
    out_put_path = sys.argv[3]

except:
    print("缺少参数!")

'''测试路径'''
#file_path_0 = open('sim_0.8/orig.txt', 'r', encoding='utf-8').read()
#file_path_1 = open('sim_0.8/orig_0.8_rep.txt', 'r', encoding='utf-8').read()

'''对文本进行停词删除操作'''
doc0 = jc.dec_stopwords(file_path_0)
doc1 = jc.dec_stopwords(file_path_1)

doc_0 = " ".join(doc0)
doc_1 = " ".join(doc1)

'''计算得出相似度'''
xx = jc.sim_value(doc_0,doc_1)
print(xx)

try:
    output_file = open(out_put_path, "w")
    output_file.write("%.2f" % (xx))
    output_file.close()
except:
    print("%s打开失败 " % (sys.argv[3]))

print("OK")

'''
file_path_0 = open('sim_0.8/orig.txt', 'r', encoding='utf-8').read()
file_path_1 = open('sim_0.8/orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()

file_path_11 = JB.del_stopwords(file_path_1)
file_path_00 = JB.del_stopwords(file_path_0)

print(file_path_11)

JB.cre_dictionary(file_path_11,file_path_00)
'''

