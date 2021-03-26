# 1. Create a Python function that gets an integer between 1 - 12 (as an hour) and returns the exact time in hours
#    and minutes at which the hands of the clock overlap at this hour
#   (for example, for 1, the result will be close to 1:06)
# 2. create a unit test for this function, using 'assert', or the Python 'unittest' framework
# 3. [BONUS]
#    a. add also seconds calculation to the return value of the function.
#    b. calculate the angle of the hands in 360 degrees system
#       taking 12:00 (noon, midnight) as a point of reference
# ATTENTION: You do not need to import any modules to implement this task

# declaration:
def hour_overlap(hour):
    #implement body of the method
    HR_DEG = float(360 / 12)    # 30  grados arco de la aguja horaria
    MI_DEG = float(HR_DEG / 60) # 0.5 grados que se mueve la aguja hoaria por minuto o vuelta del minutero
    HR_MN_DG = float(360 / 60)  #6 degrees que se mueve el minutero cada minuto
    HR_SEC_DG = float(360 / 60) #6 degrees que se mueve la aguja del segundero cada segundo pero mas rapido que el minutero
                                #la relacion es 1 a 60 entre minuterio y segundero obviamente
                                # en un minuto:
                                #segundero hace 360 grados
                                #minutero hace 6 grados
                                #horario hace 0.5 grados
                                #en un segundo:
                                #segundero 6 grados
                                #minutero 6/60 grados
                                #horario 6/60/60 grados
    i=float(0.00)
    while i < 61:
        minute = i * HR_MN_DG
        tmphr = i * MI_DEG + (hour * HR_DEG) 
        #print hour,i,minute,tmphr
        if minute > tmphr :    

            mins = int(i)
            secs =  (i-int(i))*60
            angle = tmphr
            
            return {
                "hours": hour,
                "mins": mins, #int
                "secs": secs, #int
                "min_angle": angle # float
             }

        i+=0.1

def hour_overlap2(hour):
    #implement body of the method
    HR_DEG = float(360 / 12)    # 30  grados arco de la aguja horaria
    MI_DEG = float(HR_DEG / 60) # 0.5 grados que se mueve la aguja hoaria por minuto o vuelta del minutero
    HR_MN_DG = float(360 / 60)  #6 degrees que se mueve el minutero cada minuto
    HR_SEC_DG = float(360 / 60) #6 degrees que se mueve la aguja del segundero cada segundo pero mas rapido que el minutero
                                #la relacion es 1 a 60 entre minuterio y segundero obviamente
                                # en un minuto:
                                #segundero hace 360 grados
                                #minutero hace 6 grados
                                #horario hace 0.5 grados
                                #en un segundo:
                                #segundero 6 grados
                                #minutero 6/60 grados
                                #horario 6/60/60 grados
    hr = mn = gr_hr = gr_mn = float(0.00)
    hour = min =0
    for h in range(0,3):        
        for m in range(00,61):
            if m == 60:
                hour+=1
                mn = float(0.00)

            for s in range(00,61):
                se = s * 6
                #hr += float(6)/float(60)/float(60)
                mn = float(se)/float(60)
                hr = mn/60*5
                print se,mn,hr
                if s == 60:
                    min+=1
                    gr_hr+=hr
                    gr_mn+=mn
                if se == mn == hr :
                    print "******\n"


            
def test_dict_instance():
    try:
        res = hour_overlap(1)
        assert isinstance(res, dict)
    except AssertionError as e:
        print("Oh, snap! the test has failed. exception: {}").format(e)


def your_test_one(i):
    try:
        res = hour_overlap(i)
        assert isinstance(res["mins"], int)
    except AssertionError as e:
        print("Test 1 failed mins are not integer: {}").format(e)
    


def your_test_two(i):
    try:
        res = hour_overlap(i)
        assert isinstance(res["min_angle"], float)
    except AssertionError as e:
        print("Test 2 failed min_angle is not float: {}").format(e)
    


if __name__ == '__main__':
    for i in range(1, 12):
        print(hour_overlap2(i))
        test_dict_instance()
        your_test_one(i)
        your_test_two(i)