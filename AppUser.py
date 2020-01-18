import PaymentMethod as pm
import Transaction as trans
import TransCategory as transCat

class AppUser:
    name = ""
    email = ""
    pmList = []

    def __init__(self):
        name = ""
        email = ""
        pmList = []
