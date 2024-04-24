def computers(num:int):
    return f'{num} компьютер' if num %10 ==1 and num!=11  else f'{num} компьютера' if num %10 in range(2,5) else f'{num} компьютеров'
