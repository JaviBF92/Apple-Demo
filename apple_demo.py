# -*- coding: utf-8 -*-
import json


#print(Hook['req'])
#Hook={"params":{"rq":"info_MacBook"}}

database = {"products":[{"title":"MacBook",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ac/macbook/select/macbook-select-spacegray-201604?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1473974029537",
                    "link":"http://www.apple.com/es/macbook/",
                    "price":"1499 €",
                    "Screen size":12,
                    "Processor":"Intel Core m3 Dual Core, 1.1 GHz",
                    "RAM":"8 GB LPDDR3",
                    "Capacity":"256 GB",
                    "Size":"1.31 x 28.05 x 19.65",
                    "Weight":"0.92 Kg"
					},
                   {"title":"MacBook Air",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ac/macbook/air/macbook-air-gallery5-2014?wid=1292&hei=766&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1476297407895",
                    "link":"http://www.apple.com/es/macbook-air/",
                    "price":"1099 €",
                    "Screen size":13.3,
					"Processor":"Intel Core i5 Dual Core, 1.6 GHz",
                    "RAM":"8 GB LPDDR3",
                    "Capacity":"256 GB",
                    "Size":"1.7 x 32.5 x 22.7",
                    "Weight":"1.35 Kg"
					},
                   {"title":"iMac",
                    "category":"Mac",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/I/MA/IMAC/IMAC?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=dSMkx2",
                    "link":"http://www.apple.com/es/imac/",
                    "price":"1279 €",
                    "Screen size":21.5,
					"Processor":"Intel Core i5 Dual Core, 1.6 GHz",
                    "RAM":"8 GB LPDDR3",
                    "Capacity":"1 TB",
                    "GPU":"Intel HD Graphics 6000",
                    "Size":"45 x 52.8 x 17.5",
                    "Weight":"5.68 Kg"
					},
                   {"title":"iPad Pro",
                    "category":"iPad",
                    "image_url":"http://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/pa/ipad/pro/ipad-pro-select-spacegray-201603_GEO_US?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1481049028689",
                    "link":"http://www.apple.com/es/ipad-pro/",
                    "price":"679 €",
                    "Screen size":9.7,
					"Processor":"A9X",
                    "RAM":"2 GB",
                    "Capacity":"32 GB",
                    "Size":"24 x 16.95 x 0.61",
                    "Weight":"437 g",
                    "Camera":"12 Mpx"
					},
                   {"title":"iPad Air 2",
                    "category":"iPad",
                    "image_url":"https://www.apple.com/euro/ipad-air-2/a/generic/images/og.jpg?201611302133",
                    "link":"http://www.apple.com/es/ipad-air-2/",
                    "price":"429 €",
                    "Screen size":9.7,
					"Processor":"A8X",
                    "RAM":"2 GB",
                    "Capacity":"32 GB",
                    "Size":"24 x 16.95 x 0.61",
                    "Weight":"444 g",
                    "Camera":"12 Mpx"
					},
                   {"title":"iPad mini 4",
                    "category":"iPad",
                    "image_url":"http://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/m/ob/mobile/ipad/mobile-ipad-mini-4-hero-2015_GEO_MX?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=1474916038114",
                    "link":"http://www.apple.com/es/ipad-mini-4/",
                    "price":"429 €",
                    "Screen size":7.9,
					"Processor":"A8",
                    "RAM":"2 GB",
                    "Capacity":"32 GB",
                    "Size":"24 x 16.95 x 0.61",
                    "Weight":"299 g",
                    "Camera":"8 Mpx"
					},
                   {"title":"iPhone 7",
                    "category":"iPhone",
                    "image_url":"https://www.o2.co.uk/shop/homepage/images/shop15/brand/apple/iphone7/apple-iphone-7-gallery-img-0.jpg",
                    "link":"http://www.apple.com/es/iphone-7/",
                    "price":"769 €",
                    "Screen size":4.7,
					"Processor":"A10",
                    "RAM":"2 GB",
                    "Capacity":"32 GB",
                    "Size":"13.83 x 6.71 x 0.71",
                    "Weight":"138 g",
                    "Camera":"12 Mpx"
					},
                   {"title":"iPhone 6 S",
                    "category":"iPhone",
                    "image_url":"http://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone6s/select/iphone6s-select-2015?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=WkFkh3",
                    "link":"http://www.apple.com/es/iphone6s/",
                    "price":"659 €",
                    "Screen size":4.7,
					"Processor":"A9",
                    "RAM":"2 GB",
                    "Capacity":"32 GB",
                    "Size":"13.83 x 6.71 x 0.71",
                    "Weight":"143 g",
                    "Camera":"12 Mpx"
					},
                   {"title":"iPhone SE",
                    "category":"iPhone",
                    "image_url":"http://store.storeimages.cdn-apple.com/4662/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphonese/select/iphonese-select-2016_FMT_WHH?wid=1200&hei=630&fmt=jpeg&qlt=95&op_sharpen=0&resMode=bicub&op_usm=0.5,0.5,0,0&iccEmbed=0&layer=comp&.v=p6Dlf3",
                    "link":"http://www.apple.com/es/iphone-se/",
                    "price":"489 €",
                    "Screen size":4,
					"Processor":"A9",
                    "RAM":"2 GB",
                    "Capacity":"16 GB",
                    "Size":"12.38 x 5.86 x 0.76",
                    "Weight":"113 g",
                    "Camera":"12 Mpx"
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
            "payload": "info_"+i['title'].replace(" ","_")
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

def get_additional_info(product):

    info = [i for i in database["products"] if str(product) == i['title']]

    if info:
        info = info[0]
        msg = [info[key] for key in ["title","price"]]
        msg = msg + [key + ": " + str(info[key]) for key in info if key not in ["title","price","link","category","image_url"]]
        text="\n".join(msg)
    else:
        text = None

    return text


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

    elif 'info' in rq:
        product = rq.split("_",1)[1].replace("_"," ")
        body = get_additional_info(product)

        if not body:
            status = 'error'
            body = 'the object does not exist in the database'
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
