import time
import bitso
from datetime import datetime

api = bitso.Api()
path = 'C:\\Users\\Yisus\\Desktop\\log.txt'

logfile = open(path, 'w')
logfile.write('')
logfile.close()

def log(message):
 logfile = open(path, 'a')
 logfile.write(message)
 logfile.close()

book = 'bch_mxn'
while True:
 try:
  # Calculates the value only
  tick = api.ticker(book)
  value = float(tick.last.to_eng_string())
  realtime = datetime.now().strftime("%I:%M%p on %B %d %Y")
  print value
  # ob = api.order_book(book)
  # # Capture the bids
  # s_bids = ''
  # counter = 0
  # for el in ob.bids:
  #  s_bids += ' P%d: [p:%.2f, a:%.2f]; ' % (counter, el.price, el.amount)
  #  counter += 1
  # # Capture the asks
  # s_asks = ''
  # counter = 0
  # for el in ob.bids:
  #  s_asks += 'P%d: [p:%.2f, a:%.2f]; ' % (counter, el.price, el.amount)
  #  counter += 1
  # s_message = '%s TICK: %f; BIDS: %s ASKS: %s \n' % (realtime, value, s_bids, s_asks)
  # print 'log'
  s_message = "%s, %f" % (realtime, value)
  log(s_message)
  time.sleep(60)
 except:
  api = bitso.Api()
  # Calculates the value only
  tick = api.ticker(book)
  value = float(tick.last.to_eng_string())
  realtime = datetime.now().strftime("%I:%M%p on %B %d %Y")
  print value
  # ob = api.order_book(book)
  # # Capture the bids
  # s_bids = ''
  # counter = 0
  # for el in ob.bids:
  #  s_bids += ' P%d: [p:%.2f, a:%.2f]; ' % (counter, el.price, el.amount)
  #  counter += 1
  # # Capture the asks
  # s_asks = ''
  # counter = 0
  # for el in ob.bids:
  #  s_asks += 'P%d: [p:%.2f, a:%.2f]; ' % (counter, el.price, el.amount)
  #  counter += 1
  # s_message = '%s TICK: %f; BIDS: %s ASKS: %s \n' % (realtime, value, s_bids, s_asks)
  # print 'log'
  s_message = "%s, %f\n" % (realtime, value)
  log(s_message)
  time.sleep(60*10)