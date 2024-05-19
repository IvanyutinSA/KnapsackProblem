def display_pairs(ys: list[int], y_hats: list[int], lib_results: list[int] = [], index: bool = False):
    if index:
        for i, (y, y_hat) in enumerate(zip(ys, y_hats)):
            print(f'{i+1}\t{y}\t{y_hat}')
    elif len(lib_results) != 0:
        for y, y_hat, lib_res in zip(ys, y_hats, lib_results):
            print(f'{y}\t{y_hat}\t{lib_res}')
    else:
        for y, y_hat in zip(ys, y_hats):
            print(f'{y}\t{y_hat}')


