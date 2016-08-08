# -*- coding: utf-8 -*-

import pytc
from sklearn import metrics  
import performance

#合并预测的结果
def merge(fileYN,fileEmotion,fileOut):
	#总的情绪预测的结果
	result=[]
	#有无情绪分类结果
	f_Y_N=open(fileYN,'r')
	for line in f_Y_N.readlines():
		if line.strip()=='1':
			result.append('none')
		else:
			result.append('Y')
	#有情绪微博的预测
	dic_emotion={'1':'anger','2':'disgust','3':'fear','4':'happiness','5':'like','6':'sadness','7':'surprise'}
	f_emotion=open(fileEmotion,'r')
	emotion_text_predict=[]
	for line in f_emotion.readlines():
		emotion_text_predict.append(dic_emotion[line.strip()])
	#合并
	index=0
	for i in range(0,len(result)):
		if result[i]=='Y':
			result[i]=emotion_text_predict[index]
			index+=1

	fw=open(fileOut,'w')
	for item in result:
		print>>fw,item

def evaluation(fileTest,filePredict):
	#测试集的类别标签
	test_y=[]
	f_test=open(fileTest,'r')
	for line in f_test.readlines():
		lineSet=line.strip().split()
		test_y.append(lineSet[2])
	#预测的标签
	predict=[]
	f_predict=open(filePredict,'r')
	for line in f_predict.readlines():
		predict.append(line.strip())
	#评价指标为准确率、召回率、F值
	accuracy = metrics.accuracy_score(test_y, predict)  
	print 'accuracy: %.2f%%' % (100 * accuracy) 
	#输出各类指标
	print("weibo情绪识别任务------------")        	
	
	#宏平均
	class_dict1={'happiness':'happiness','like':'like','anger':'anger',
	'sadness':'sadness','fear':'fear','disgust':'disgust','surprise':'surprise'}
	macro_dict1=performance.calc_macro_average(predict,test_y,class_dict1)
	#微平均
	micro_dict1=performance.calc_micro_average(predict,test_y,class_dict1)

	
	#每一类情绪
	class_dict={'happiness':'happiness','like':'like','anger':'anger',
	'sadness':'sadness','fear':'fear','disgust':'disgust','surprise':'surprise',
	'none':'none'}
	#precision
	precision_dict=performance.calc_precision(predict,test_y,class_dict)
	print("macro_precision——%r"%(macro_dict1['macro_p']))
	print("micro_precision——%r"%(micro_dict1['micro_p']))
	for i in class_dict:
	    print("%r:%r"%(class_dict[i],precision_dict[class_dict[i]]))
	#recall
	recall_dict=performance.calc_recall(predict,test_y,class_dict)
	print("macro_recall——%r"%(macro_dict1['macro_r']))
	print("micro_recall——%r"%(micro_dict1['micro_r']))
	for i in class_dict:
	    print("%r:%r"%(class_dict[i],recall_dict[class_dict[i]]))   
	#f-measure
	fscore_dict=performance.calc_fscore(predict,test_y,class_dict)
	print("macro_fscore——%r"%(macro_dict1['macro_f1']))
	print("micro_fscore——%r"%(micro_dict1['micro_f1']))
	for i in class_dict:
	    print("%r:%r"%(class_dict[i],fscore_dict[class_dict[i]]))
	print("-------------------------")

if __name__ == '__main__':
	#对有情绪的微博进行进一步细分
	# pytc.demo_hhh()
	#合并预测的结果
	fileYN='temporary/predict_GBDT_classifier'
	# fileEmotion='temporary/emotion_predict_svm'
	fileEmotion='temporary/emotion_predict_nb_m'
	fileOut='temporary/all_predict'
	merge(fileYN,fileEmotion,fileOut)
	#评价指标
	fileTest='temporary/weibo_test_label.txt'
	filePredict='temporary/all_predict'
	evaluation(fileTest,filePredict)