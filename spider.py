import pandas as pd
import csv
for i in range(1,3):  # 爬取全部页
    tb = pd.read_html('http://xxx.com/a=1&c=%s' % (str(i)))[3]
    tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
print(1)