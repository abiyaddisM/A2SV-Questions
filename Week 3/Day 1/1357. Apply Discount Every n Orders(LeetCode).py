# February 10 2025
# https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    count = 1
    n = 0
    discount = 0
    products = {}
    prices = []
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        for i in range(len(products)):
            self.products[products[i]] = i
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(len(product)):
            price = self.prices[self.products[product[i]]]
            total += price * amount[i]
        if self.count % self.n == 0:
            total = total * ((100 - self.discount) / 100)
        self.count += 1
        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)