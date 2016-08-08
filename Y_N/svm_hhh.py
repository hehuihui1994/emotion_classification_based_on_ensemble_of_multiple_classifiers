# -*- coding: utf-8 -*-

import performance
import subprocess

'''
./svm-scale -l 0 -u 1 temporary_hhh/train.sample > temporary_hhh/train.scale
./svm-scale -l 0 -u 1 temporary_hhh/test.sample > temporary_hhh/test.scale

python grid.py ../temporary_hhh/train.scale

./svm-train -c  32   -g  0.03125   temporary_hhh/train.scale


./svm-predict temporary_hhh/test.scale train.scale.model emotion_predict_svm
'''

def process(file_train,file_test,file_predict):
	string1='./svm-scale -l 0 -u 1 '+file_train+' > temporary_hhh/train.scale'
	subprocess.call(string1)
	string2='./svm-scale -l 0 -u 1 '+file_test+' > temporary_hhh/test.scale'
	subprocess.call(string2)
	string3='python tools/grid.py temporary_hhh/train.scale > temporary_hhh/svm_cg'
	subprocess.call(string3)
	#读c g
	string4='./svm-train -c  '+string(c)  +' -g ' + string(g)+ ' temporary_hhh/train.scale'





if __name__ == '__main__':
	file_train="temporary_hhh/train.sample"
	file_test="temporary_hhh/test.sample"
	file_predict="temporary_hhh/predict"
	process(file_train,file_test,file_predict)