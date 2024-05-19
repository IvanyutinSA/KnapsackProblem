def display_pairs(ys: list[int], y_hats: list[int], index: bool = False):
    if index:
        for i, (y, y_hat) in enumerate(zip(ys, y_hats)):
            print(f'{i+1}\t{y}\t{y_hat}')
    else:
        for y, y_hat in zip(ys, y_hats):
            print(f'{y}\t{y_hat}')


