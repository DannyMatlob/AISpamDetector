import time
from joblib import dump, load

def SVM(trainingX, trainingY, testingX, testingY):
    # "Support Vector Classifier"
    print("----\nSVM: \n----")
    from sklearn.svm import SVC  
    clf = SVC(kernel='linear') 

    #Start clock to time training
    start_time = time.time() 

    # fitting x samples and y classes 
    clf.fit(trainingX, trainingY) 

    #Log time taken for training
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Total Training time: ", elapsed_time, "seconds")

    #Save Model
    dump(clf, 'SVM.joblib') 

    #Test model
    test(clf, testingX, testingY)

def RFC(trainingX, trainingY, testingX, testingY):
    # Random Forest Classifier
    print("----\nRFC: \n----")
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier()

    #Start clock to time training
    start_time = time.time() 

    #Train
    rf.fit(trainingX, trainingY)

    #Log time taken for training
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Total Training time: ", elapsed_time, "seconds")

    #Save Model
    dump(rf, 'RFC.joblib') 

    print("Testing RF")
    #Test model
    test(rf, testingX, testingY)

def test(model,testingX, testingY):
    #Run tests
    print("Model Generated, Running Tests")
    testN = len(testingY)
    success = 0
    print("Testing on ", testN, "Samples")
    for i in range(testN):
        prediction = model.predict(testingX[i].reshape(1,-1))
        if prediction == testingY[i]:
            success+=1
    print('Success Percentage: ',(success/testN)*100, "%")
