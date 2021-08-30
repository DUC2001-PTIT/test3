def centuryFromYear(year):
    nguyen = year//100
    du = year%100
    if du != 0 :
        return nguyen +1
    else :
        return nguyen 
        