from datetime import datetime, timedelta
import emoji

plus_days = 5000
wedding_day = datetime(2011, 4, 9)
the_day = wedding_day + timedelta(days=plus_days) 
result = emoji.emojize(f":ring: 우리 결혼한지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일")
print(result)
