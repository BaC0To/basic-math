class Employee:
    """Basic Employee Class
    params: first name, last name, paycheck
    class attribure = 1.05 (const)"""
    

    raise_amt = 1.05

    def __init__(self, first, last, paycheck) -> None:
        self.first = first
        self.last = last
        self.paycheck = paycheck

    def email(self):
        """returns Employee object mail@gmail.com"""
        return "{}.{}@gmail.com".format(self.first.lower(), self.last.lower())
    

    def applay_rise(self):
        """calculates new paycheck"""
        self.new_paycheck = self.paycheck * self.raise_amt
        return self.new_paycheck
