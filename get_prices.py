#!/usr/bin/python3.6
'''
This script gets polo-data for all the currency pairs in
the designated list. It goes from Tuesday, May 13, 2014 4:53:20 PM
(1400000000), if available, up to the day run. Data is hlocvwa.

Author: Jon Geenty

'''

import urllib.request

pairs = ['BTC_ETH','BTC_XMR','BTC_XRP','BTC_LTC','USDT_BTC',
         'BTC_BCH','USDT_ETH','BTC_DASH','BTC_LSK',
         'USDT_BCH','BTC_DGB','BTC_BTS','BTC_STRAT',
         'USDT_XRP','BTC_ETC','BTC_SC','BTC_STR',
         'USDT_XMR','BTC_FCT','USDT_LTC','BTC_ZRX',
         'BTC_ZEC','BTC_BCN','BTC_NAV','BTC_SYS',
         'BTC_XEM','BTC_MAID','BTC_REP','BTC_PINK',
         'BTC_DOGE','ETH_BCH','BTC_SJCX','BTC_NXT',
         'BTC_GNT','ETH_ETC','ETH_ZRX','BTC_GAME',
         'BTC_LBC','USDT_DASH','BTC_DCR','BTC_EXP',
         'BTC_STEEM','BTC_BURST','USDT_ZEC','USDT_ETC',
         'BTC_ARDR','BTC_NXC','USDT_NXT','ETH_GNT',
         'BTC_FLO','BTC_GNO','BTC_AMP','BTC_VTC',
         'BTC_POT','BTC_VIA','BTC_XBC','BTC_EMC2',
         'ETH_LSK','ETH_REP','BTC_NEOS','USDT_STR',
         'BTC_NOTE','BTC_BELA','USDT_REP','ETH_ZEC',
        'BTC_CLAM','BTC_OMNI','BTC_FLDC','BTC_GRC',
         'BTC_PASC','BTC_HUC','XMR_ZEC','BTC_XCP',
        'BTC_RADS','BTC_VRC','XMR_LTC','BTC_BLK',
         'BTC_PPC','ETH_GNO','BTC_NAUT','BTC_BTCD',
         'BTC_BCY','BTC_BTM','BTC_RIC','BTC_XPM',
         'BTC_XVC','BTC_NMC','BTC_SBD','ETH_STEEM',
         'XMR_DASH','XMR_MAID','XMR_BCN','XMR_NXT',
         'XMR_BTCD','XMR_BLK']


for i in pairs:
    try:
        stub = 'https://poloniex.com/public?command=returnChartData&currencyPair='
        pair_string = i
        cap = '&start=1400000000&end=9999999999&period=14400'
        url_string = stub + pair_string + cap
        headers = {}
        headers[
            'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url_string, headers = headers)
        url =urllib.request.urlopen(req)
        #url = urllib.request.urlopen(url_string, headers = headers)
        filename = 'data/' + pair_string + 'price.txt'
        saveFile = open(filename, 'w')
        saveFile.write(str(url.read()))
        saveFile.close()
    except Exception as e:
        print("error - could not get "+ str(i))

