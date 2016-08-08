# -*- coding: utf-8 -*-

import performance
from sklearn import metrics 

#选择GBDT的阈值
def select_para():
	#测试集的类别标签
	test_y=[]
	f_test=open('temporary/test.sample','r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	#GBDT预测值
	gbdt_result=[]
	f_GBDT=open('temporary/GBDT_predict1000','r')
	for line in f_GBDT.readlines():
		gbdt_result.append(float(line.strip()))
	final_threshold=0
	final_acc=0
	threshold=1
	while threshold <=2 :
		predict=[]
		for item in gbdt_result:
			if item>=threshold:
				predict.append('2')
			else:
				predict.append('1')
		accuracy = metrics.accuracy_score(test_y, predict)  
		if accuracy > final_acc:
			final_acc=accuracy
			final_threshold=threshold
		threshold+=0.001
	print final_acc
	print final_threshold

#重新选择阈值后计算
def get_GBDT_result():
	#测试集的类别标签
	test_y=[]
	f_test=open('temporary/test.sample','r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	#GBDT预测值
	gbdt_result=[]
	fw_gbdt=open('temporary/gbdt_predict','w')
	f_GBDT=open('temporary/GBDT_predict1000','r')
	for line in f_GBDT.readlines():
		if float(line.strip()) >=1.496:
			gbdt_result.append('2')
			print>>fw_gbdt,'2'
		else:
			gbdt_result.append('1')
			print>>fw_gbdt,'1'
	predict=gbdt_result
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

#选择threshold_minus   threshold=1.496
def select_threshold_minus():
	#测试集的类别标签
	test_y=[]
	f_test=open('temporary/test.sample','r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	#GBDT预测值
	gbdt_result=[]
	dic={}
	f_GBDT=open('temporary/GBDT_predict1000','r')
	index=0
	for line in f_GBDT.readlines():
		gbdt_result.append(float(line.strip()))
		dic[float(line.strip())]=test_y[index]
		index+=1
	dict1=sorted(dic.iteritems(), key=lambda d:d[0])
	# print dict1
	fw=open('yinbo_GBDT_kanyikan','w')
	for item in dict1:
		print >>fw,str(item[0])+" "+str(item[1])
	


	


if __name__ == '__main__':
	# select_para()
	# get_GBDT_result()
	select_threshold_minus()