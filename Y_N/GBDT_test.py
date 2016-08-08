# -*- coding: utf-8 -*-

from sklearn import metrics 
import numpy as np 
import time  

# GBDT(Gradient Boosting Decision Tree) Classifier样例 
def gradient_boosting_classifier(train_x, train_y):  
    from sklearn.ensemble import GradientBoostingClassifier  
    #随机森林中树的数量
    model = GradientBoostingClassifier(n_estimators=100)  
    model.fit(train_x, train_y)  
    return model  

#
def gradient_boosting_regressor(train_x, train_y):  
    from sklearn.ensemble import GradientBoostingRegressor
    #随机森林中树的数量
    model = GradientBoostingRegressor(n_estimators=100)  
    model.fit(train_x, train_y)  
    return model  

if __name__ == '__main__':
    train_x=[[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
    #1表示奇数，2表示偶数
    train_y=[1,2,1,2,1,2]
    test_x=[[8,8],[14,14],[33,33],[22,22],[44,44],[55,55]]
    test_y=[2,2,1,2,2,1]
    #用于回归的时候加类型强制转换
    train_x = np.float32(train_x)
    train_y = np.float32(train_y)
    test_x = np.float32(test_x)
    test_y = np.float32(test_y)
    num_train,num_feat = np.shape(train_x)
    num_test,num_feat = np.shape(test_x)
    is_binary_class = (len(np.unique(train_y)) == 2)  
    print '******************** Data Info *********************'  
    print '#training data: %d, #testing_data: %d, dimension: %d' % (num_train, num_test, num_feat)  
    start_time = time.time()  
    #分类
    # model = gradient_boosting_classifier(train_x, train_y)  
    #回归
    model = gradient_boosting_regressor(train_x, train_y) 
    print 'training took %fs!' % (time.time() - start_time)
    #  
    predict = model.predict(test_x)  
    for item in predict:
        print item
    # accuracy = metrics.accuracy_score(test_y, predict)  
    # print 'accuracy: %.2f%%' % (100 * accuracy) 
