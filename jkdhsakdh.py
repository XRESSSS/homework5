from decimal import Decimal, ROUND_HALF_UP

# Константи з калорійністю продуктів (кКал на 100 г продукту)
CALORIES_STRAUS_EGG = 160
CALORIES_RABBIT = 173
CALORIES_SEA_BASS = 97
CALORIES_RED_PEPPER = 31
CALORIES_PARSLEY = 36
CALORIES_BANANA = 96
CALORIES_WAFFLES = 291
CALORIES_WHEAT_BREAD = 240
CALORIES_PISTACHIOS = 557
CALORIES_KEFIR = 42

# Вартість 1 кКал в гривнях
COST_PER_CALORIE = Decimal('0.32541')

# Збереження назв продуктів для виведення повідомлень
PRODUCT_NAMES = {
    CALORIES_STRAUS_EGG: "страусине Яйце",
    CALORIES_RABBIT: "Кролик",
    CALORIES_SEA_BASS: "Окунь морський",
    CALORIES_RED_PEPPER: "Перець червоний солодкий",
    CALORIES_PARSLEY: "Петрушка (зелень)",
    CALORIES_BANANA: "Банани",
    CALORIES_WAFFLES: "Вафлі",
    CALORIES_WHEAT_BREAD: "Хліб пшеничний з борошна I сорту",
    CALORIES_PISTACHIOS: "Фісташки",
    CALORIES_KEFIR: "Кефір 2,5%"
}

def main():
    total_calories = 0
    total_cost = Decimal('0.00')

    for cal_value in PRODUCT_NAMES.keys():
        portion = Decimal(input(f"Введіть обсяг порції {PRODUCT_NAMES[cal_value]} в грамах: "))
        cal_in_portion = Decimal(cal_value / 100) * portion
        total_calories += cal_in_portion

        product_cost = cal_in_portion * COST_PER_CALORIE
        total_cost += product_cost

        print(f"Калорійність {PRODUCT_NAMES[cal_value]}: {cal_in_portion:.2f} кКал")
        print(f"Вартість {PRODUCT_NAMES[cal_value]}: {product_cost:.2f} грн\n")

    print(f"Загальна калорійність замовлення: {total_calories:.2f} кКал")
    print(f"Загальна вартість замовлення: {total_cost.quantize(Decimal('.00'), rounding=ROUND_HALF_UP)} грн")

    if total_calories < 1000:
        print("Ви, мабуть, залишитеся голодним.")
    elif 1000 <= total_calories <= 1500:
        print("Це саме ваш варіант вечері.")
    else:
        print("Ви стільки не з'їсте, і це все гроші в смітник.")

if __name__ == "__main__":
    main()
