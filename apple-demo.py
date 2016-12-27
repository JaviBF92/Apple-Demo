import json

#print(Hook['params'])
#print(Hook['req'])


database = {"products":[{"name":"MacBook",
                    "category":"Mac",
                    "image":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ac/macbook/select/macbook-select-spacegray-201604?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1473974029537",
                    "link":"http://www.apple.com/es/macbook/",
                    "prices":1499,
                    "screen-size":12,
                    "processor":{"processor-name":"Intel Core m3",
                                "cores":2,
                                "freq":"1.1 GHz"},
                    "ram":"8 GB LPDDR3",
                    "disk-size":"256 GB",
                    "size":"1.31 x 28.05 x 19.65",
                    "weight":0.92
					},
                   {"name":"MacBook Air",
                    "category":"Mac",
                    "image":"",
                    "link":"http://www.apple.com/es/macbook-air/",
                    "prices":1099,
                    "screen-size":13.3,
					"processor":{"processor-name":"Intel Core i5",
                                "cores":2,
                                "freq":"1.6 GHz"},
                    "ram":"8 GB LPDDR3",
                    "disk-size":"256 GB",
                    "size":"1.7 x 32.5 x 22.7",
                    "weight":1.35
					},
                   {"name":"iMac",
                    "category":"Mac",
                    "image":"",
                    "link":"http://www.apple.com/es/imac/",
                    "prices":1279,
                    "screen-size":21.5,
					"processor":{"processor-name":"Intel Core i5",
                                "cores":2,
                                "freq":"1.6 GHz"},
                    "ram":"8 GB LPDDR3",
                    "disk-size":"1 TB",
                    "GPU":"Intel HD Graphics 6000",
                    "size":"45 x 52.8 x 17.5",
                    "weight":5.68
					}
                  ],
			"categories":[{"name":"Mac",
					"img":"http://www.apple.com/euro/macbook-air/c/generic/images/overview_wireless_hero_enhanced.png"
					},
					{"name":"iPhone",
					"img":"https://d3nevzfk7ii3be.cloudfront.net/igi/ipv5OG2NckM3DfE2.large"},
					{"name":"iPad",
					"img":"https://d3nevzfk7ii3be.cloudfront.net/igi/Mwfvd5qH3sPoRlF1.large"
					}
                    ]
}


def find_products(item, find_by, more_info=False):
	products = [i for i in database["products"] if str(item) in i[find_by].lower()]
	if not more_info:
		products = [{key:i[key] for key in ["name","image","link","prices"]} for i in products]
	return products

request = Hook['params']

status = 'ok'

if 'rq' in request:
    rq = request['rq']
    if rq in [i["name"].lower() for i in database['categories']]:
        body = find_products(rq,"category")

    elif rq == 'search':
        if 'search' in request:
            body = find_products(request['search'],"name")
            if not body:
                body = "empty"

        else:
            status = 'error'
            body = 'wrong parameters in request'

    elif rq == 'info':
        if 'prod' in request:
            body = find_products(request['prod'], "name", True)
        else:
            status = 'error'
            body = 'wrong parameters in request'
    elif rq == 'cat':
        body = database['categories']
    else:
        status = 'error'
        body = 'request not found'
else:
    status = 'error'
    body = 'wrong parameters in request'


res = json.dumps({"status":status, "body":body})


print(res)
