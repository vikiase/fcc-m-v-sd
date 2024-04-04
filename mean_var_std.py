import numpy as np
def calculate(values):
    if len(values) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        #normalne za sebou
        flat = np.array(values)
        #3x3
        mat = flat.reshape((3, 3))
        calculations = dict()
        #osa 0 jsou sloupce a osa 1 jsou radky
        calculations['mean'] = [list(np.mean(mat,axis=0)), list(np.mean(mat, axis=1)), np.mean(flat)]
        calculations['variance'] = [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), np.var(flat)]
        calculations['standard deviation'] = [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), np.std(flat)]
        calculations['max'] = [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), np.max(flat)]
        calculations['min'] = [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), np.min(flat)]
        calculations['sum'] = [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), np.sum(flat)]

        return calculations


