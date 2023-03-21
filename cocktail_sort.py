def cocktail_sort(arr):
    # устанавливаем флаг, показывающий, были ли сделаны обмены на текущей итерации
    swapped = True
    # устанавливаем границы, между которыми происходит сортировка
    start = 0
    end = len(arr) - 1
    while swapped:
        # переключаем флаг на false перед началом новой итерации
        swapped = False
        # сначала идем вправо и меняем местами элементы, если они находятся в неправильном порядке
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # если были сделаны обмены, устанавливаем новую правую границу
        if swapped:
            end -= 1
        # если обменов не было, мы закончили сортировку
        else:
            break
        # сначала идем влево и меняем местами элементы, если они находятся в неправильном порядке
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # устанавливаем новую левую границу
        start += 1
