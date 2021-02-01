import sys
import time

now = time.localtime()
sys.stdout.write("%04d/%02d/%02d done! \n" % (now.tm_year, now.tm_mon, now.tm_mday))  # 현재시간 출력