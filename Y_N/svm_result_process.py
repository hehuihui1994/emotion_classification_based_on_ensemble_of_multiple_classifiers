# -*- coding: utf-8 -*-

import performance
from sklearn import metrics  

def process_svm_result(fileTest,filePredict):
	#测试集的类别标签
	test_y=[]
	f_test=open(fileTest,'r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[0])
	#预测的标签
	predict=[]
	f_predict=open(filePredict,'r')
	for line in f_predict.readlines():
		predict.append(line.strip())
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
	fileTest='temporary/test.sample'
	filePredict='temporary/predict_GBDT_classifier'
	process_svm_result(fileTest,filePredict)