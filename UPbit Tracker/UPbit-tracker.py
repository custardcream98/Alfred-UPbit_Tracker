# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, ICON_ERROR, web


def format_strings_from_quote(ticker, data):
	price = '{:,.0f}'.format(data[0]['trade_price'])
	high = '{:,.0f}'.format(data[0]['high_price'])
	low = '{:,.0f}'.format(data[0]['low_price'])
	change = '{:,.2f}'.format(data[0]['change_rate'])
	
	formatted = {}
	formatted['title'] = '{}: {} KRW ({}%)'.format(ticker, price, change)
	formatted['subtitle'] = '24hr high: {} KRW | 24hr low: {} KRW'.format(high, low)
	return formatted

def get_time(data):
	time = data[0]['candle_date_time_kst']
	wf.add_item(title="Info Time : " + time, icon='icon/clock.png')

def main(wf):
	# Get query from Alfred
	if len(wf.args):
		query = wf.args[0]
		ticker = query.upper()
	else:
		query = None

	if query:
		url = "https://api.upbit.com/v1/candles/days?market=KRW-" + ticker
		r = web.get(url)

		r.raise_for_status()
		result = r.json()

		get_time(result)

		try:
			formatted = format_strings_from_quote(ticker, result)
			wf.add_item(title=formatted['title'],
				subtitle=formatted['subtitle'],
				arg='https://upbit.com/exchange?code=CRIX.UPBIT.KRW-' + ticker,
				valid=True,
				icon=ICON_WEB)
		except:
			wf.add_item(title='Couldn\'t find a quote for that symbol.',
				subtitle='Please try again.',
				icon=ICON_ERROR)
	else:
		coinlist = ['KRW-BTC','KRW-ETH','KRW-ADA','KRW-XRP','KRW-DOGE','KRW-DOT','KRW-BCH','KRW-LINK','KRW-LTC','KRW-XLM']
		
		url = 'https://api.upbit.com/v1/candles/days?market=KRW-BTC'
		r = web.get(url)
		r.raise_for_status()
		result = r.json()
		get_time(result)		

		for coin in coinlist:
			url = 'https://api.upbit.com/v1/candles/days?market={}'.format(coin)
			r = web.get(url)

			r.raise_for_status()
			result = r.json()

			ticker = result[0]['market'][4:]
			formatted = format_strings_from_quote(ticker, result)
			wf.add_item(title=formatted['title'],
				subtitle=formatted['subtitle'],
				arg='https://upbit.com/exchange?code=CRIX.UPBIT.KRW-' + ticker,
				valid=True,
				icon='icon/{}.png'.format(ticker.lower()))

	wf.send_feedback()


if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))
