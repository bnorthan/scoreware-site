def ageToCat(age):
    if (0<age<30):
        return "a_open"
    if (30<=age<40):
        return "b_30_39"
    if (40<=age<50):
        return "c_40_49"
    if (50<=age<60):
        return "d_50_59"
    if (60<=age<70):
        return "e_60_69"
    if (age>=70):
        return "f_70+"