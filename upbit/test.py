import pyupbit

import pyupbit

access = "2bpxnn6gmgNH6Tw5jtNzlbQ5ykPgbh4OLSUeWs4e"          # 본인 값으로 변경
secret = "2cMIRaeVw8L5xRI1Q4WZgUkh63dMNbrfu5GyOcVr"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회