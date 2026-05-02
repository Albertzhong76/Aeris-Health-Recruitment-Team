# 读取 input.txt 文件内容
def solve():
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split()
    
    t = int(lines[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(lines[i])
        
        # 判断 n 能否由 4 和 6 组成
        # 4 和 6 的最大公约数为 2，因此 n 必须是偶数才能有解
        if n % 2 != 0 or n == 2:
            results.append("-1")
            continue
        
        # 最小数量：尽量多用 6，但用完 6 后剩余部分必须能被 4 整除
        # 实际上，4 和 6 的最小组合是 4，因此最小数量是尽量多用 6，但需要保证剩余是 4 的倍数
        # 对于大于等于 4 的偶数，总是可以通过调整得到解，但 n=2 不行，n=4 最小=1，n=6 最小=1
        # 但我们要最小化总数，所以尽量用大单位（6）减少个数
        
        # 最大数量：尽量多用 4，但需要保证 n - 4*k 是 6 的倍数
        # 最小数量：尽量多用 6，但需要保证剩余是 4 的倍数
        
        # 特殊情况 n=0? 题目 n>=1，不用考虑
        
        # 找最小数量（最多 6）
        min_count = float('inf')
        for cnt6 in range(n // 6, -1, -1):
            remaining = n - cnt6 * 6
            if remaining % 4 == 0:
                min_count = cnt6 + remaining // 4
                break
        
        # 找最大数量（最多 4）
        max_count = -1
        for cnt4 in range(n // 4, -1, -1):
            remaining = n - cnt4 * 4
            if remaining % 6 == 0:
                max_count = cnt4 + remaining // 6
                break
        
        if min_count == float('inf') or max_count == -1:
            results.append("-1")
        else:
            results.append(f"{min_count} {max_count}")
    
    # 输出结果
    with open('output.txt', 'w') as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    solve()
