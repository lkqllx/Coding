def quicksort(array):
    front_idx = 0
    end_idx = len(array) - 1
    _quicksort(array, front_idx, end_idx)

def _quicksort(array, start, end):
    if start >= end:
        """非常重要的一步来检查是不是排序完成"""
        return

    pivot = partition(array, front_idx=start, pivot_idx=end)
    _quicksort(array, start, pivot - 1) # 左边的排序
    _quicksort(array, pivot + 1, end) # 右边的排序


def partition(array, front_idx, pivot_idx):
    """
    返回最重要的pivot的位置，为了递归的来排序
    :param array:
    :param front_idx:
    :param pivot_idx:
    :return:
    """
    while pivot_idx - front_idx > 1:
        """当有三个或以上位置的时候"""
        if array[pivot_idx] < array[front_idx]:
            """
            input = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 5]
            pivot_idx = len(input) - 1 -> 5
            After one step
            input ->  [{14}, 4, 1, 3, 9, 20, 25, 6, 21, {5}, {12}]
            
            we can save space complexity by doing so.
            """
            array[pivot_idx], array[pivot_idx - 1], array[front_idx] = array[front_idx], array[pivot_idx], array[pivot_idx - 1]
            pivot_idx -= 1
        else:
            front_idx += 1

    if array[pivot_idx] < array[front_idx]:
        """当两个位置的时候"""
        array[pivot_idx], array[front_idx] = array[front_idx], array[pivot_idx]
        pivot_idx -= 1
    return pivot_idx


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14, 5]
quicksort(test)
print(test)