# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/23 11:04
# File: 0782.py
# Desc: CV



class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # ���̵ĵ�һ�����һ��
        rowMask = colMask = 0
        for i in range(n):
            rowMask |= board[0][i] << i
            colMask |= board[i][0] << i
        reverseRowMask = ((1 << n) - 1) ^ rowMask
        reverseColMask = ((1 << n) - 1) ^ colMask
        rowCnt = colCnt = 0
        for i in range(n):
            currRowMask = currColMask = 0
            for j in range(n):
                currRowMask |= board[i][j] << j
                currColMask |= board[j][i] << j
            # ���ÿһ�к�ÿһ�е�״̬�Ƿ�Ϸ�
            if currRowMask != rowMask and currRowMask != reverseRowMask or \
               currColMask != colMask and currColMask != reverseColMask:
                return -1
            rowCnt += currRowMask == rowMask  # ��¼���һ����ͬ������
            colCnt += currColMask == colMask  # ��¼���һ����ͬ������

        def getMoves(mask: int, count: int) -> int:
            ones = mask.bit_count()
            if n & 1:
                # ��� n Ϊ��������ÿһ���� 1 �� 0 ����Ŀ���Ϊ 1�������������н���
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                if ones == n // 2:
                    # ż��λ��Ϊ 1 ����С��������
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # ����λ��Ϊ 1 ����С��������
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                # ��� n Ϊż������ÿһ���� 1 �� 0 ����Ŀ��ȣ������������н���
                if ones != n // 2 or count != n // 2:
                    return -1
                # ż��λ��Ϊ 1 ����С��������
                count0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                # ����λ��Ϊ 1 ����С��������
                count1 = n // 2 - (mask & 0x55555555).bit_count()
                return min(count0, count1)

        rowMoves = getMoves(rowMask, rowCnt)
        colMoves = getMoves(colMask, colCnt)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves

