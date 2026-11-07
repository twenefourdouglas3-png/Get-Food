print("KOBBY JONES RESTAURANTE")
#discount
distance = int(input("\nWhat is the distance of the customer's place from the resturante: "))
#order weight
order_weight = int(input("What is the weight of the order: "))
#if is a regular customer
is_customer = input("Is the person a customer (yes/no): ").lower()
delivery_fee = distance * order_weight
#discount for regular customers/ delivery fees 10%
discount_applied = False
if is_customer == "yes":
    discount = delivery_fee * 0.90
    discount_applied = True
    print("\nCustomers get 10% discount today")
    print(f'ORDER FEE: GHS{discount:.2f}')
    print("Thanks for choosing KOBBY JONES RESTURANTE, enjoy your day")
#non regular customers delivery fees
else:
    print(f"\nORDER FEE: GHS{delivery_fee:.2f}")
    print("Thanks for choosing KOBBY JONES RESTAURANTE, enjoy your day")
