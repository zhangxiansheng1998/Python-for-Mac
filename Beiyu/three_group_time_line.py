import pandas as pd
from datetime import datetime, timedelta
import random


def generate_time_ranges(start_time, end_time, num_intervals):
    delta = (end_time - start_time) / num_intervals
    time_ranges = [start_time + i * delta for i in range(num_intervals)]
    return time_ranges


def generate_order_data():
    # 设置时间范围和数量
    start_time_create_early = datetime(2023, 12, 30, 2, 0, 0)
    end_time_create_early = datetime(2023, 12, 30, 6, 0, 0)

    start_time_create_late = datetime(2023, 12, 30, 6, 0, 1)
    end_time_create_late = datetime(2023, 12, 30, 8, 0, 0)

    start_time_create_final = datetime(2023, 12, 30, 8, 0, 1)
    end_time_create_final = datetime(2023, 12, 30, 9, 59, 59)

    # 每个时间段生成的个数
    num_intervals_create_early = 3
    num_intervals_create_late = 13
    num_intervals_create_final = 20


    # 生成创建订单时间
    create_time_early = generate_time_ranges(start_time_create_early, end_time_create_early, num_intervals_create_early)
    create_time_late = generate_time_ranges(start_time_create_late, end_time_create_late, num_intervals_create_late)
    create_time_final = generate_time_ranges(start_time_create_final, end_time_create_final, num_intervals_create_final)

    # 随机生成支付订单时间，晚于创建订单时间1-5分钟
    pay_time = []
    for create in create_time_early + create_time_late + create_time_final:
        create_datetime = pd.to_datetime(create)
        pay_datetime = create_datetime + timedelta(minutes=random.randint(1, 5))
        pay_time.append(pay_datetime)

    # 将创建订单时间和支付订单时间合并成DataFrame
    data = {'创建订单时间': create_time_early + create_time_late + create_time_final, '支付订单时间': pay_time}
    df = pd.DataFrame(data)

    # 去除创建订单时间和支付订单时间相同的情况
    df = df[df['创建订单时间'] != df['支付订单时间']]

    return df


def save_to_excel(df, filename='36_group_timeline.xlsx'):
    # 将DataFrame保存为Excel文档
    df.to_excel(filename, index=False)


if __name__ == "__main__":
    order_data = generate_order_data()
    save_to_excel(order_data)

