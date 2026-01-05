

from typing import List
def trap(height: List[int]) -> int:
    """
    与其一层层切片，不如计算每一列（每一个索引）能接多少水。
    对于下标为 i 的柱子，它能接的水量取决于：
        左边最高的柱子高度 L。
        右边最高的柱子高度 R。
        该柱子能接的水量为 min(L, R) - height[i]（如果结果大于 0）。

    本算法相当于，我们只知道边界两墙的信息，只计算两墙之中水量，短板效应从矮墙看起
    每遇到一个更高的墙，就划分新区间，重新开始两墙的计算
    """
    l = 0
    r = len(height) - 1

    max_l = max_r = 0

    volume = 0

    while l < r:
        # 处理较矮的一边, 这点很重要，相当于两墙之中看矮墙

        if height[l] < height[r]:
            # 左边
            if height[l] > max_l:
                # 如果更高，相当于要换区间，当前区间不能接水，所以只更新高度
                max_l = height[l]
            else:
                # 要更新水量 = 最高水位-高度
                volume += max_l - height[l]
            l += 1
        else:# 右边
            if height[r] > max_r:
                # 如果更高，相当于要换区间，当前区间不能接水，所以只更新高度
                max_r = height[r]
            else:
                # 要更新高度, 最高水位-高度
                volume += max_r - height[r]
            r -= 1

    return volume


def trap(height: List[int]) -> int:
    """horizotally search, exceed spatial limitation"""
    # select max num as the top layer
    max_layers = max(height)
    h_layer = dict() # height for each layer
    rain_volume = 0

    # record bucket for every layer
    for layer in range(max_layers):
        h_layer[layer] = []
        for bucket in height:
            if bucket >= layer + 1:
                h_layer[layer].append(1)
            else:
                h_layer[layer].append(0)
        
    # for ecah layer, check  1-0*-1 pairs
    for i, layer in h_layer.items():
        hollow = 0
        bucket_left = 0
        for bucket in layer:
            if bucket == 0 and bucket_left == 1:
                hollow += 1
                bucket_left = 1 #继续寻找下一个hollow
            elif bucket == 1 and bucket_left == 1 and hollow != 0:
                rain_volume += hollow
                hollow = 0
            elif bucket == 1:
                bucket_left = 1

    return rain_volume