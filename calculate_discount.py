def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
    - price: float, the original price of the item
    - discount_percent: float, the discount percentage to be applied

    Returns:
    - float, the final price after applying the discount
    """
    if discount_percent >= 20:  # Check if the discount is 20% or higher
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # If the discount is less than 20%, return the original price
        return price

def main():
    # Prompt the user to enter the original price of the item
    original_price = float(input("Kindly enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Kindly enter the discount percentage: "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(original_price, discount_percent)

    # Check if a discount was applied
    if final_price != original_price:
        # If a discount was applied, print the final price after applying the discount
        print("The final price after applying {}% discount: ksh {:.2f}".format(discount_percent, final_price))
    else:
        # If no discount was applied, print the original price
        print("There is no discount applied. The final price: ksh {:.2f}".format(final_price))

if __name__ == "__main__":
    main()
