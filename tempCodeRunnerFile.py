import sys
import random
 
g=float(9.8) #重力加速度
Trt=float(298.15) #室温
    
mair=float(4.939) #空気の質量
Cair=float(4982) #mair＊cp air
Rair=float(288.3) #空気の気体定数
    
mar=float(6.844) #Arの質量
Car=float(3558) #mar＊cp Ar
Rar=float(207.9) #Arの気体定数

top=240000.0 #乱数の最大値
under=239276.5463954446 #乱数の最小値

cnt=10 #カウンタ（10回チェックしたら停止させる）

while cnt>0:
    Q=random.uniform(under,top) #Qに乱数の値を入れる

    print(under,'<Q<',top) #乱数の範囲を出力

    Tair=float(Trt+(Q/Cair)) #室温＋ΔTair
    Tar=float(Trt+(Q/Car)) #室温＋ΔTar

    Fair=float(g*mair*((Tair/Trt)-1)) #空気の風船の浮力
    Far=float(g*mar*(((Rar*Tar)/(Trt*Rair))-1)) #Arの風船の浮力

    DF=Fair+Far #浮力の大きさの差

    print('Q=',Q) #Qの値を出力
    print('Fair=',Fair) #空気の風船の浮力を出力
    print('Far=',Far) #Arの風船の浮力を出力
    print('Fair+Far=',DF,'\n')  #浮力の大きさの差を出力
   
    cnt=cnt-1 #カウンタの値を１減らす

    if DF==0:
        break
    elif DF>0:
        top=Q #Fair＋Far>0のとき乱数の最大値をQに更新
    elif DF<0:
        under=Q #Fair＋Far<0のとき乱数の最小値をQに更新
