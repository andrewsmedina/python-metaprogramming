hypermedia client
=================

xml hypermedia response:
------------------------

    <xml>
    <pedido>
    <produto>sabre de luz</produto>
    <valor>1.99</valor>
    <links>
    <link href="/pedido/1/pagamento" rel="pagamento"/>
    </links>
    </pedido>
    </xml>


json hypermedia response:
-------------------------

    {
        "properties": {
            "produto": {
                "type": "string"
            },
            "valor": {
                "type": "float"
            }
        },
        links: [

        ]
    }


python client eg:
-----------------

    product = client(data)
    product.payment() #calls the payment

    products.search() #type error search name parameter is required
    prodcuts.search(name="lightsaber") # searchs for lightsaber
