import numpy as np
import pandas as pd

def generate_orders():
    total_amount = 4400000 * 0.997
    unit_price_x = 15.7
    unit_price_y = 71.8

    orders = []
    total_x = 0
    total_y = 0
    total_generated_amount = 0

    while total_generated_amount < total_amount:
        x = np.random.randint(0, 200000 - total_x)
        y = np.random.randint(0, 25000 - total_y)

        order_amount = unit_price_x * x + unit_price_y * y

        # 控制订单金额在3000元-20000元之间
        if 3000 <= order_amount <= 15000:
            orders.append([x, y, order_amount])

            total_x += x
            total_y += y
            total_generated_amount += order_amount

    # 调整订单使得总金额接近目标
    orders[-1][-1] += total_amount - total_generated_amount

    return orders

def main():
    orders = generate_orders()

    # 保存结果到Excel
    df = pd.DataFrame(orders, columns=["X", "Y", "Amount"])
    df.to_excel("440W_hualian_and_guiyu.xlsx", index=False)

if __name__ == "__main__":
    main()
