for num in range(1, 101):
    string = ''

    # ここから記述
    if num%15 == 0: # numが3の倍数かつ5の倍数の時
      string = "FizzBuzz"

    elif num%3 == 0: # numが3の倍数だが5の倍数でないとき
      string = "Fizz"

    elif num%5 == 0: # numが5の倍数だが3の倍数でないとき
      string = "Buzz"

    else: # numが3の倍数でも5の倍数でもないとき
      string = num

    # ここまで記述

    print(string)
