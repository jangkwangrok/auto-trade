# -*- coding: utf-8 -*-
import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume -> 당일 시가, 고가, 저가, 종가, 거래량)
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
df['range'] = (df['high'] - df['low']) * 0.3
df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032
# ror(수익율), np,where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] , 1) # - fee

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 계산
print("MDD(%): ", df['dd'].max())

#엑셀 출력
df.to_excel("dd.xlsx")