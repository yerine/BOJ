def solution(brown, yellow):
    for y_heigth in range(1, int(yellow**0.5)+1):
        if yellow % y_heigth == 0 :
            y_wide = int(yellow / y_heigth)
            if (y_heigth + 2) * (y_wide + 2) == brown + yellow:
                return [y_wide + 2, y_heigth + 2]