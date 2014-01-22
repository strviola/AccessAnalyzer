'''
Created on 2013/12/26

@author: SuzukiRyota
'''


from sklearn import cluster
from sklearn.preprocessing import StandardScaler


def dbscan(raw_points, eps, minpts):
    points = StandardScaler().fit_transform(raw_points)

    dbscan = cluster.DBSCAN(eps=eps, min_samples=minpts)
    divided = dbscan.fit(points)
    labels = divided.labels_  # 'labels' is simple list
    
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    # count up noises
    n_noise = 0
    for l in labels:
        if l == -1:
            n_noise += 1

    return divided, n_noise


def count_false(points, labels_true, dbscan_result, latex):
    labels_est = dbscan_result.labels_

    false_negative = 0
    false_positive = 0
    for p, l_true, l_est in zip(points, labels_true, labels_est):
        fp = [p, l_true, l_est]
        if l_true == -1 and l_est != -1:
            false_negative += 1
            if not latex:
                print('N', fp)
        elif l_true != -1 and l_est == -1:
            false_positive += 1
            if not latex:
                print('P', fp)

    return false_positive, false_negative


def step_dbscan(point_list, eps_list, minpts_list,
                contain_cheat=True, labels_true=None, latex=False):

    # When just one EPS or MINPTS given: convert 1-length list
    if not isinstance(eps_list, list):
        eps_list = [eps_list]
    if not isinstance(minpts_list, list):
        minpts_list = [minpts_list]

    if latex:
        # LaTeX format
        print(r'\begin{tabular}{c|'),
        print('%s}' % ('c' * len(minpts_list)))
        print(r'$\Eps \backslash \MinPts$'),
        for minpts in minpts_list:
            print(' & %d' % minpts),
        print(r'\\')


    for eps in eps_list:
        if latex:
            print('%.2f' % eps),
        for minpts in minpts_list:
            # DBSCAN: count noise
            cluster_result, n_noise = dbscan(point_list, eps, minpts)
            fp, fn = count_false(point_list, labels_true, cluster_result, latex)
            if latex:
                # for LaTeX tabular format
                if contain_cheat:
                    # output FP and FN
                    print(' & (%d, %d)' % (fp, fn)),
                else:
                    print(' & %d' % n_noise),
            else:
                if contain_cheat:
                    print('False Positive: %d' % fp)
                    print('False Negative: %d' % fn)
                else:
                    print('Noises at eps=%f, minpts=%d: %d' % (eps, minpts, n_noise))

        if latex:
            print(r'\\')
    if latex:
        print(r'\end{tabular}')
