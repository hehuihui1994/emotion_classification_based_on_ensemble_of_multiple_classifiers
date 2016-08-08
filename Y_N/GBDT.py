# -*- coding: utf-8 -*-

from sklearn import metrics  
import numpy as np 
import performance
import pytc
import time  

# GBDT(Gradient Boosting Decision Tree) Classifier样例 
def gradient_boosting_classifier(train_x, train_y):  
    from sklearn.ensemble import GradientBoostingClassifier  
    #子树数量，值越大，模型越好，但是代码越慢 
    model = GradientBoostingClassifier(n_estimators=1000,max_depth=3)  
    model.fit(train_x, train_y)  
    return model 

def gradient_boosting_regressor(train_x, train_y):  
    from sklearn.ensemble import GradientBoostingRegressor
    #随机森林中树的数量
    model = GradientBoostingRegressor(n_estimators=1000)  
    model.fit(train_x, train_y)  
    return model  

#处理for_train_x,变成mxn维度的数组
def process_for_train_x_or_test_x(for_train_x,len_term_set):
	row=len(for_train_x)
	col=len_term_set
	train_x=[[0 for j in range(col)] for i in range(row)]
	for i in range(0,row):
		for j in range(0,col):
			#train_sample中的特征从1开始，对应于向量中的0
			if for_train_x[i].has_key(j+1):
				train_x[i][j]=for_train_x[i][j+1]
	return train_x

#GBDT
#fname_samp_train, fname_samp_test是处理成标准格式的训练集和测试集数据
def gradient_boosting_hhh(fname_samp_train, fname_samp_test,len_term_set):
	#for_train_x每一行是词典，train_y是list
	for_train_x,train_y=pytc.load_samps(fname_samp_train, fs_num=0)
	for_test_x,test_y=pytc.load_samps(fname_samp_test, fs_num=0)
	train_x=process_for_train_x_or_test_x(for_train_x,len_term_set)
	test_x=process_for_train_x_or_test_x(for_test_x,len_term_set)
	#回归
	# train_x = np.float32(train_x)
	# train_y = np.float32(train_y)
	# test_x = np.float32(test_x)
	# test_y = np.float32(test_y)
	num_train,num_feat = np.shape(train_x)
	num_test,num_feat = np.shape(test_x)
	print '******************** 数据信息 *********************'  
	print '#训练集数据: %d, #测试集数据: %d, 维度: %d' % (num_train, num_test, num_feat)  
	start_time = time.time()  
	#分类
	model = gradient_boosting_classifier(train_x, train_y) 
	#回归
	# model = gradient_boosting_regressor(train_x, train_y) 
	print '训练耗时 %fs!' % (time.time() - start_time)  
	predict = model.predict(test_x) 
	#输出预测标签
	fw_predict=open('predict_classifier','w')
	for item in predict:
		print>>fw_predict,item
	# #设置阈值
	# threshold= 1.539
	# f_w=open('temporary/GBDT_predict1000','w')
	# f_w_label=open('temporary/GBDT_predict_label1000','w')
	# for item in predict:
	# 	print >>f_w,item
	# 	if item>=threshold:
	# 		item=2
	# 	else:
	# 		item=1
	# 	print>>f_w_label,item
	#测试集的类别标签
	test_y=[]
	f_test=open('temporary/test.sample','r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	# #预测的标签
	# predict=[]
	# f_predict=open('temporary/GBDT_predict','r')
	# for line in f_predict.readlines():
	# 	predict.append(line.strip())
	#评价指标为准确率、召回率、F值
	class_dict={'1':'1','2':"2"}
	precision_dict=performance.calc_precision(predict,test_y,class_dict)
	recall_dict=performance.calc_recall(predict,test_y,class_dict)
	fscore_dict=performance.calc_fscore(predict,test_y,class_dict)
	print("有情绪微博——————————————————")
	print("准确率：%r"%(precision_dict['2']))
	print("召回率：%r"%(recall_dict['2']))
	print("F值：   %r"%(fscore_dict['2']))
	print("无情绪微博——————————————————")
	print("准确率：%r"%(precision_dict['1']))
	print("召回率：%r"%(recall_dict['1']))
	print("F值：   %r"%(fscore_dict['1']))
	accuracy = metrics.accuracy_score(test_y, predict)  
	print 'accuracy: %.2f%%' % (100 * accuracy) 



if __name__ == '__main__':
	#产生svm标准格式,返回特征的个数
    len_term_set=pytc.demo_hhh()
    #模型训练以及预测
    fname_samp_train="temporary/train.sample"
    fname_samp_test="temporary/test.sample"
    gradient_boosting_hhh(fname_samp_train, fname_samp_test,len_term_set)