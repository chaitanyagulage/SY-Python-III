from abc import ABC, abstractmethod

# ==========================================
# 1. The Strategy Interface
# ==========================================
class PaymentStrategy(ABC):
    """
    The abstract base class (interface) that all payment strategies must implement.
    It guarantees that every concrete strategy will have a 'process_payment' method.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


# ==========================================
# 2. Concrete Strategies
# ==========================================
class CreditCardPayment(PaymentStrategy):
    """Concrete strategy for credit card payments."""
    def __init__(self, card_holder_name: str, card_number: str):
        self.card_holder_name = card_holder_name
        self.card_number = card_number

    def process_payment(self, amount: float) -> None:
        # In a real app, this would connect to a payment gateway (e.g., Stripe)
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        print(f"Processing ${amount:.2f} via Credit Card ({masked_card}) for {self.card_holder_name}.")


class PayPalPayment(PaymentStrategy):
    """Concrete strategy for PayPal payments."""
    def __init__(self, email_address: str):
        self.email_address = email_address

    def process_payment(self, amount: float) -> None:
        # In a real app, this would redirect to PayPal's API
        print(f"Processing ${amount:.2f} via PayPal account: {self.email_address}.")


class CryptoPayment(PaymentStrategy):
    """Concrete strategy for Cryptocurrency payments."""
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def process_payment(self, amount: float) -> None:
        # In a real app, this would interact with a blockchain API
        print(f"Processing ${amount:.2f} via Crypto Wallet ({self.wallet_address}).")


# ==========================================
# 3. The Context
# ==========================================
class ShoppingCart:
    """
    The Context class. It maintains a reference to one of the payment strategies
    and communicates with this object to execute the payment algorithm.
    """
    def __init__(self):
        self.items = []
        self._payment_strategy = None  # The strategy is initially unset

    def add_item(self, item_name: str, price: float):
        self.items.append({"name": item_name, "price": price})
        print(f"Added to cart: {item_name} (${price:.2f})")

    def calculate_total(self) -> float:
        return sum(item["price"] for item in self.items)

    def set_payment_strategy(self, strategy: PaymentStrategy):
        """Allows the payment strategy to be changed dynamically at runtime."""
        self._payment_strategy = strategy
        print(f"-> Payment strategy configured: {strategy.__class__.__name__}")

    def checkout(self):
        """Executes the payment using the configured strategy."""
        if not self._payment_strategy:
            print("Checkout failed: No payment strategy configured. Please select a payment method.")
            return

        total_amount = self.calculate_total()
        if total_amount == 0:
            print("Checkout failed: Cart is empty.")
            return

        print(f"\n--- Initiating Checkout (Total: ${total_amount:.2f}) ---")
        # The Context delegates the actual payment processing to the Strategy object
        self._payment_strategy.process_payment(total_amount)
        print("Payment successful. Thank you for your purchase!\n")
        self.items.clear()  # Empty the cart after successful checkout


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    # 1. Initialize the Context (Shopping Cart)
    cart = ShoppingCart()
    cart.add_item("Python Programming Book", 45.00)
    cart.add_item("Mechanical Keyboard", 120.50)

    # 2. Try to checkout without a strategy (Fails)
    cart.checkout()

    # 3. Configure a Credit Card Strategy and Checkout
    cc_strategy = CreditCardPayment("Alice Smith", "1234567812349876")
    cart.set_payment_strategy(cc_strategy)
    cart.checkout()

    # 4. New order, changing strategy dynamically at runtime
    cart.add_item("Wireless Mouse", 35.99)
    
    paypal_strategy = PayPalPayment("alice.smith@example.com")
    cart.set_payment_strategy(paypal_strategy)
    cart.checkout()

    # 5. Another order, using Crypto
    cart.add_item("Cloud Server Subscription", 15.00)
    
    crypto_strategy = CryptoPayment("0x1A2B3C4D5E6F7G8H9I0J")
    cart.set_payment_strategy(crypto_strategy)
    cart.checkout()