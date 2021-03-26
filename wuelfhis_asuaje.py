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
    HR_DEG = float(360 / 12) #30 arco de la aguja horaria
    MI_DEG = float(HR_DEG / 60) # 0.5 d
    HR_MN_DG = float(360 / 60) #6 degrees
    HR_SEC_DG = float(360 / 60) #6 degrees

    for i in range (0,60): #iter over  minutes
        minute = i * HR_MN_DG
        tmphr = i * MI_DEG + (hour * HR_DEG) 
        #print hour,i,minute,tmphr
        if minute == hour * HR_DEG:    

            mins = i
            secs =  None
            angle = tmphr
            
            return {
                "hours": hour,
                "mins": mins, #int
                "secs": secs, #int
                "min_angle": angle # float
             }
            
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

        print(hour_overlap(i))
        test_dict_instance()
        your_test_one(i)
        your_test_two(i)