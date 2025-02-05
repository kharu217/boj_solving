N, M = map(int, input().split())
percentage = M / N

total_minutes = percentage * 24 * 60
hours = int(total_minutes // 60)
minutes = int(total_minutes % 60)
print(f"{hours:02}:{minutes:02}")
