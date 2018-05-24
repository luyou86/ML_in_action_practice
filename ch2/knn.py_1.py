from numpy import *
import operator


def classify0(inx, dataset, labels, k):

    data_set_size = dataset.shape[0]
    a = tile(inx,(data_set_size,1))
    diff_mat = tile(inx, (data_set_size, 1)) - dataset
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sorted_dist_indicies = distances.argsort()
    class_count = {}
    for i in range(k):
        print 'i:{}'.format(i)
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label,0) + 1

    sorted_class_count = sorted(class_count.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sorted_class_count[0][0]


def create_dataset():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])

    labels = ['A','A','B','B']
    return group, labels

if __name__ == '__main__':
    group, labels = create_dataset()



    print classify0([0, 0], group, labels, 3)


