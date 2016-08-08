# -*- coding: utf-8 -*-

import performance
from sklearn import metrics 

#结合SVM和GBDT的分类结果
def merge_svm_GBDT():
	merge_result=[]
	threshold_minus=1.496
	threshold_plus=1.65
	#svm的结果
	svm_predict=[]
	f_svm=open('temporary/svm_predict','r')
	for line in f_svm.readlines():
		svm_predict.append(line.strip())
	#GBDT的结果
	f_GBDT=open('temporary/GBDT_predict1000','r')
	index=0
	for line in f_GBDT.readlines():
		num=float(line.strip())
		if num < threshold_minus:
			merge_result.append('1')
		elif num > threshold_plus:
			merge_result.append('2')
		else:
			merge_result.append(svm_predict[index])
		index+=1
	#测试集的类别标签
	test_y=[]
	f_test=open('temporary/test.sample','r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	#评价指标为准确率、召回率、F值
	class_dict={'1':'1','2':"2"}
	precision_dict=performance.calc_precision(merge_result,test_y,class_dict)
	recall_dict=performance.calc_recall(merge_result,test_y,class_dict)
	fscore_dict=performance.calc_fscore(merge_result,test_y,class_dict)
	print("有情绪微博——————————————————")
	print("准确率：%r"%(precision_dict['2']))
	print("召回率：%r"%(recall_dict['2']))
	print("F值：   %r"%(fscore_dict['2']))
	print("无情绪微博——————————————————")
	print("准确率：%r"%(precision_dict['1']))
	print("召回率：%r"%(recall_dict['1']))
	print("F值：   %r"%(fscore_dict['1']))
	accuracy = metrics.accuracy_score(test_y, merge_result)  
	print 'accuracy: %.2f%%' % (100 * accuracy) 


if __name__ == '__main__':
	merge_svm_GBDT()