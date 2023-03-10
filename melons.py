import random
import datetime


"""Classes for melon orders."""
class AbstractMelonOrder:
    tax = None
    order_type = None
    shipped = False

    def __init__(self,species,qty,country_code = 'US'):
        self.species = species
        self.qty = qty
        self.country_code = country_code

    
  
    def get_base_price(self):
        now = datetime.datetime.now()
        weekday = now.isoweekday()
        hour = now.hour
        base_price = random.randint(5, 9)
        # print(base_price)
        
        if weekday <= 5 and hour >= 8 and hour < 11:
            base_price += self.qty * 4
            return base_price
        else:
            return base_price
           

   
    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        print(base_price)

        if self.species == "Christmas Melon":
            base_price *= 1.5
           
        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != 'US' and self.qty < 10:
            total += 3

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    # def __init__(self,species,qty,country_code):
    #     super().__init__(species,qty)
    #     """Initialize melon order attributes."""
    #     self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    
class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False
    

    def mark_inspection(self):
        self.passed_inspection = True


obj9 = GovernmentMelonOrder('Christmas Melon',105)



# class TooManyMelonsError(ValueError,AbstractMelonOrder):
    
#     if AbstractMelonOrder.qty > 100:
#         raise TooManyMelonsError
    

