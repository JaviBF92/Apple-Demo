import json


#print(Hook['req'])
#Hook={"params":{"rq":"search","search":"im"}}

database = {"products":[{"title":"MacBook",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ac/macbook/select/macbook-select-spacegray-201604?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1473974029537",
                    "link":"http://www.apple.com/es/macbook/",
                    "price":"1499 €",
                    "screen-size":12,
                    "processor":{"processor-name":"Intel Core m3",
                                "cores":2,
                                "freq":"1.1 GHz"},
                    "ram":"8 GB LPDDR3",
                    "disk-size":"256 GB",
                    "size":"1.31 x 28.05 x 19.65",
                    "weight":0.92
					},
                   {"title":"MacBook Air",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ac/macbook/air/macbook-air-gallery5-2014?wid=1292&hei=766&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1476297407895",
                    "link":"http://www.apple.com/es/macbook-air/",
                    "price":"1099 €",
                    "screen-size":13.3,
					"processor":{"processor-name":"Intel Core i5",
                                "cores":2,
                                "freq":"1.6 GHz"},
                    "ram":"8 GB LPDDR3",
                    "disk-size":"256 GB",
                    "size":"1.7 x 32.5 x 22.7",
                    "weight":1.35
					},
                   {"title":"iMac",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/I/MA/IMAC/IMAC?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=dSMkx2",
                    "link":"http://www.apple.com/es/imac/",
                    "price":"1279 €",
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


def find_products(item, find_by):

    products = [i for i in database["products"] if str(item) in i[find_by].lower()]
    products = [{key:i[key] for key in ["title","image_url","link","price"]} for i in products]

    return products[:3]


def generate_product_template(products):

    elem = products

    for i in elem:
        i['buttons']= [
            {
            "type": "postback",
            "title": "More info",
            "payload": "info_"+i['title']
            },
            {
                "type": "web_url",
                "url": i['link'],
                "title": "Buy"
            }
        ]
        i['subtitle'] = i['price']
        del i['link']
        del i['price']

    template = {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": elem
        }
    }
    return template



request = Hook['params']

status = 'ok'

if 'rq' in request:
    rq = request['rq']
    if rq in [i["name"].lower() for i in database['categories']]:
        body = generate_product_template(find_products(rq,"category"))

    elif rq == 'search':
        if 'search' in request:
            body = generate_product_template(find_products(request['search'],"title"))
            if not body:
                body = 'empty'

        else:
            status = 'error'
            body = 'wrong parameters in request'

    elif rq == 'info':
        if 'prod' in request:
            #body = find_products(request['prod'], "title", True)
            pass
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
