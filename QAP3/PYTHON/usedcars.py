# Description:
# This program allows the Honest Harry's Used Car Sales to input the customer and the vehicle's total sale details, calculating the fees, taxes, the total sales price, to generate a receipt ID, and also display financing options with a calculated first payment date.
#
# Author: Patrick Tobin
# Date: 2025-07-14

from datetime import datetime, timedelta

# The program Constants 
HST_RATE = 0.15
TRANS_FEE = 165.00
LICS_FEE = 75.00
LUX_TAX_THRSHLD = 20000.00
LUX_TAX_RATE = 0.01

# This is the functions to format the phone number 
def form_phone(phone):
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

# This is the function to create a unique receipt ID 
def create_recpt_id(plate, phone):
    return f"{plate[:2]}-{plate[2:5]}-{phone[-4:]}"

# These are the functions to calculate the fees, the taxes, and the total.
def cal_fees(price, trade_in):
    price_aft_trade = price - trade_in
    lux_tax = 0.0
    if price > LUX_TAX_THRSHLD:
        lux_tax = price * LUX_TAX_RATE
    subtotal = price_aft_trade + LICS_FEE + TRANS_FEE + lux_tax
    hst = subtotal * HST_RATE
    total = subtotal + hst
    return price_aft_trade, lux_tax, subtotal, hst, total

# This is the function to build the different financing options 
def cal_finan(total):
    plans = []
    for years in range(1, 5):
        payments = years * 12
        fees = 99.99
        total_price = total + fees
        monthly = total_price / payments
        plans.append((years, payments, fees, total_price, monthly))
    return plans

# This is the function to calculate the first payment date
def get_pay_date():
    today = datetime.today()
    first_of_nxt_mth = (today.replace(day=1) + timedelta(days=32)).replace(day=1)
    if today.day >= 25:
        first_of_nxt_mth = (first_of_nxt_mth + timedelta(days=32)).replace(day=1)
    return first_of_nxt_mth.strftime("%d-%b-%Y")

# This is the main program loop 
while True:
    print("Enter Customer Information:                                     ")
    first_name = input("Enter your first name (or enter 'END' to quit):    ").strip()
    if first_name.upper() == "END":
        print("The program has ended:                                      ")
        break  # This will exit the progams loop

    last_name = input("Your Last name:                           ").strip()
    phone = input("Your phone number (10 digits):                ").strip()
    plate = input("Your license plate number:                    ").strip()
    veh_make = input("The vehicle make:                          ").strip()
    veh_model = input("The vehicle model:                        ").strip()
    veh_year = int(input("The vehicle year:                      "))
    price = float(input("The vehicles selling price ($):         "))
    trade_in = float(input("The total trade in value ($):        "))
    salesperson = input("Your Salesperson name:                  ").strip()

    # These are the programs calculations 
    phone_form = form_phone(phone)
    plate_form = plate.upper()
    receipt_id = create_recpt_id(plate_form, phone)
    price_aft_trade, lux_tax, subtotal, hst, total = cal_fees(price, trade_in)
    finan_opt = cal_finan(total)
    first_pay_date = get_pay_date()
    invoice_date = datetime.today().strftime("%a %b, %Y")

    # This will print the receipt 
    print("\n" + "Honest Harry Car Sales".center(80))
    print("Used Car Sale and Receipt".center(80))
    print(f"The invoice Date: {invoice_date}".ljust(40) + f"Receipt No: {receipt_id}".rjust(40))
    print("-" * 80)
    print(f"The vehicle was sold to: {first_name[0]}. {last_name.upper():<20} ({phone_form})")
    print(f"The car Details: {veh_year} {veh_make} {veh_model}")
    print("-" * 80)
    print(f"{'The sale price:':<40}${price:>10,.2f}")
    print(f"{'The trade allowance:':<40}${trade_in:>10,.2f}")
    print(f"{'The price after Trade:':<40}${price_aft_trade:>10,.2f}")
    print(f"{'The license Fee:':<40}${LICS_FEE:>10,.2f}")
    print(f"{'The transfer Fee:':<40}${TRANS_FEE:>10,.2f}")
    if lux_tax > 0:
        print(f"{'The luxury Tax:':<40}${lux_tax:>10,.2f}")
    print(f"{'Subtotal:':<40}${subtotal:>10,.2f}")
    print(f"{'HST:':<40}${hst:>10,.2f}")
    print(f"{'Total sales price:':<40}${total:>10,.2f}")
    print("-" * 80)
    print("Financing Options".center(80))
    print("-" * 80)
    print(f"{'# Years':<10}{'# Payments':<15}{'Fee':<10}{'Total Price':<20}{'Monthly':<10}")
    for years, payments, fees, total_price, monthly in finan_opt:
        print(f"{years:<10}{payments:<15}${fees:<9.2f}${total_price:<19,.2f}${monthly:<.2f}")
    print(f"\nFirst payment date: {first_pay_date}")
    print("-" * 80)
    print("Best used cars at the best prices!".center(80))