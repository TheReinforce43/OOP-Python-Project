class product:

    def __init__(self,name,price,quantity) -> None:
        self.product_name=name
        self.price=price
        self.quantity=quantity

    def __repr__(self) -> str:
        return f"{self.product_name} {self.price} {self.quantity}"      

class shop:

    def __init__(self,name) -> None:
        self.products=[]
        self.shop_name=name

    def add_product(self,product_name,price,quantity):
        product_shop=product(product_name,price,quantity)
        self.products.append(product_shop)
        
    def buy_product(self,product_name):
        flag=False
        for name in self.products:
            if name.product_name== product_name:
                flag=True
                break
        return flag

agora=shop('Agora')
agora.add_product('Fox',1000,2)
print(agora.buy_product('perfurme'))
agora.add_product('perfurme',500,1)
print(agora.buy_product('perfurme') )           
        

