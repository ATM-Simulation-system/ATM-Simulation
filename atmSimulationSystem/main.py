from atm import ATM

def main():
    atm = ATM.get_instance()

    acc = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if atm.authenticate(acc, pin):
        print("Authentication successful.")
        while True:
            print("\n1. Balance\n2. Withdraw\n3. Deposit\n4. Exit")
            choice = input("Choose transaction: ")

            if choice == '1':
                print("Balance:", atm.perform_transaction("balance"))
            elif choice == '2':
                amt = int(input("Enter amount to withdraw: "))
                if atm.perform_transaction("withdraw", amt):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
            elif choice == '3':
                amt = int(input("Enter amount to deposit: "))
                atm.perform_transaction("deposit", amt)
                print("Deposit successful.")
            elif choice == '4':
                print("Exiting. Thank you.")
                break
            else:
                print("Invalid option.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
