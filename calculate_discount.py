
def calculate_discount(price,discount_percent):
    
    if discount_percent>=20:
        discount_amount =(discount_percent/100)*price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    

price = float(input("Enter the price of the item: "))
discount_percent=float(input("Enter the discount percentage:"))

final_price=calculate_discount(price,discount_percent)

if final_price == price:
    print(f"No discount applied. Final price is : ${price:.2f}")
else:
    print(f"Final price after discount is : ${final_price:.2f}")