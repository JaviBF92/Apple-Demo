import json

#print(Hook['params'])
#print(Hook['req'])


with open('db.json') as data_file:
	database = json.load(data_file)


def find_products(item, find_by, more_info=False):
	products = [i for i in database["products"] if str(item) in i[find_by].lower()]
	if not more_info:
		products = [{key:i[key] for key in ["product-name","image","link","prices"]} for i in products]
	return products
   
request = Hook['params']

status = 'ok'

if 'rq' in request:
	rq = request['rq']
	if rq in database["categories"]:
		body = find_products(rq,"category")

	elif rq == 'search':
		if 'search' in request:
			body = find_products(request['search'],"product-name")
			if not body:
				body = "empty"

		else:
			status = 'error'
			body = 'wrong parameters in request'

	elif rq == 'info':
		if 'prod' in request:
			body = find_products(request['prod'], "product_name", True)
    	
	else:
		status = "error"
		body = "request not found"
else:
	status = "error"
	body = "wrong parameters in request"
    
    
res = json.dumps({"status":status, "body":body})


print(res)

