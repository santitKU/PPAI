keywords = [
    "money-back guarantee",
    "get rich quick",
    "cash bonus",
    "investment opportunity",
    "no credit check",
    "fast cash",
    "earn extra income",
    "free",
    "discount",
    "save big money",
    "buy direct",
    "act now",
    "special promotion",
    "limited time offer",
    "weight loss",
    "miracle",
    "viagra",
    "prescription",
    "medical breakthrough",
    "lose weight",
    "reverses aging",
    "adult",
    "xxx",
    "meet singles",
    "dating service",
    "hot babes",
    "nude",
    "your account has been compromised",
    "verify your identity",
    "click the link below",
    "confirm your password",
    "urgent update required",
    "your payment method",
    "win big",
    "casino",
    "blackjack",
    "lottery",
    "jackpot",
    "betting",
    "betting odds",
    "rolex",
    "debt consolidation",
    "increase sales",
    "lowest price",
    "you're a winner",
    "no catch",
    "this isn't a scam"
]
def spam_or_ham(email):

    email = email.lower()
    for i in keywords:
        if i in email:
            return True
    return False

Email = "Congratulation, You have won jackpot of 1 million dollar."

if spam_or_ham(Email)==True:
    print("Spam mail")
else:
    print("Ham")

