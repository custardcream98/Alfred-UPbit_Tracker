# encoding: utf-8
import time
import sys
from workflow import Workflow, ICON_ERROR, web

def format_strings_from_quote(ticker, data, coinNameDict):
	price = '{:,.0f}'.format(data[0]['trade_price'])
	high = '{:,.0f}'.format(data[0]['high_price'])
	low = '{:,.0f}'.format(data[0]['low_price'])
	change = '{:.2f}'.format(data[0]['change_rate']*100)

	# Wiredly, UPbit API returns None for 'change_price' if it's zero.
	# If I don't do like below, it may raise 'ValueError'
	change_price = '0' if float(change) == 0 else '{:,.0f}'.format(data[0]['change_price'])

	sign = '+' if float(change) >= 0 else ''
	
	formatted = {}
	formatted['title'] = u'{} ({}): {}원 ( {}{}%, {}{}원 )'.format(coinNameDict[ticker], ticker, price, sign, change, sign, change_price)
	formatted['subtitle'] = u'일봉 고가: {}원 | 일봉 저가: {}원'.format(high, low)
	return formatted

def get_time(data):
	time = data[0]['candle_date_time_kst'].split('T')
	wf.add_item(title=u"가격 기준 시각 : " + time[0] + ', ' + time[1], icon='clock.png')

def main(wf):
	# Get coin name traded in KRW
	coinNameDict = dict()
	url = "https://api.upbit.com/v1/market/all"
	r = web.get(url)
	
	r.raise_for_status()
	result = r.json()
	for upbitCoin in result:
		if upbitCoin['market'][0:3] == 'KRW':
			coinNameDict[upbitCoin['market'][4:]] = upbitCoin['korean_name']

	# Get query from Alfred
	if len(wf.args):
		query = wf.args[0]
		ticker = query.upper()
	else:
		query = None

	if query:
		try:
			url = "https://api.upbit.com/v1/candles/days?market=KRW-" + ticker
			r = web.get(url)
	
			r.raise_for_status()
			result = r.json()

			get_time(result)


			formatted = format_strings_from_quote(ticker, result, coinNameDict)
			wf.add_item(title=formatted['title'],
				subtitle=formatted['subtitle'],
				arg='https://upbit.com/exchange?code=CRIX.UPBIT.KRW-' + ticker,
				valid=True,
				icon= 'icon/{}.png'.format(ticker.lower()))

		except:
			wf.add_item(title=u'입력하신 티커와 일치하는 가상화폐를 찾지 못했습니다.',
				subtitle=u'티커는 끝까지 입력해주세요.',
				icon=ICON_ERROR)

	else:
		coinlist = ['BTC','ETH','ADA','XRP','DOGE','DOT','BCH','LINK','LTC','XLM']

		url = 'https://api.upbit.com/v1/candles/days?market=KRW-BTC'
		r = web.get(url)
		r.raise_for_status()
		result = r.json()
		get_time(result)		

		for coin in coinlist:
			url = 'https://api.upbit.com/v1/candles/days?market={}'.format('KRW-' + coin)
			while True:
				r = web.get(url)
				if r.status_code == 429:
					time.sleep(0.05) # a little delay to avoid HTTPError 429 'too many requests'
					continue
				elif r.status_code == 200:
					break
				else:
					r.raise_for_status()

			result = r.json()

			ticker = result[0]['market'][4:]
			formatted = format_strings_from_quote(ticker, result, coinNameDict)
			wf.add_item(title=formatted['title'],
				subtitle=formatted['subtitle'],
				arg='https://upbit.com/exchange?code=CRIX.UPBIT.KRW-' + ticker,
				valid=True,
				icon='icon/{}.png'.format(ticker.lower()))

	wf.send_feedback()


if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))
