def Test(q,w,e,a,s,d,z,x,c,v):
    import pandas as pd
    import numpy as np
    from sklearn import tree
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import classification_report, confusion_matrix
    
    df = pd.read_csv("covid19.csv")
    print(df.head())

    inputs = df.drop('Chuan doan',axis='columns')

    target = df['Chuan doan']

    inputs_n = inputs.drop([],axis='columns')

    inputs_n

    target

    model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=10)

    X_train, X_test, y_train, y_test = train_test_split(  
    inputs_n, target,random_state = 47, test_size =0.7)

    model.fit(X_train, y_train)

    model.score(inputs_n,target)

    x = float(q+w+e+a+s+d+z+x+c+v)
    print(x)

    dudoan = model.predict([[q,w,e,a,s,d,z,x,c,v]])


    listToString = ''
    print(listToString.join(dudoan))
    
##    print("Ti le chuan doan: " + str(accuracy_score(y_test,x))+ "%")
    tile = (x/float(len(y_test)))*100
    tile2 = (format(tile, '.6f')+"%")
    return listToString.join(dudoan), tile2

##def main():
##    q = input('Nhập q: ')
##    w = input('Nhập w: ')
##    e = input('Nhập e: ')
##    a = input('Nhập a: ')
##    s = input('Nhập s: ')
##    d = input('Nhập d: ')
##    z = input('Nhập z: ')
##    x = input('Nhập x: ')
##    c = input('Nhập c: ')
##    v = input('Nhập v: ')
##    Test(q,w,e,a,s,d,z,x,c,v)
##main()

