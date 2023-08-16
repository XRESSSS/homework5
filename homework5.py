from decimal import Decimal
from pywebio.input import input as pw_input, slider, FLOAT
from pywebio.output import put_success, put_warning, put_error

PRICE_ONE_KILO_CALORIE = 0.32541

ENERGY_OSTRICH_EGG = 118
ENERGY_RABBIT = 197
ENERGY_BANANA = 87
ENERGY_PISTACHIOS = 555
ENERGY_WAFFLES = 425
ENERGY_PERCH = 123
ENERGY_KEFIR = 51
ENERGY_PEPPER = 26
ENERGY_PARSLEY = 45

ENERGY_BREAD = 246

total_energy = 0

portion_ostrich_egg = pw_input(f'Введите желаемую порцию страусиных яиц 🥚, грамм'
                               f'Калорийность {ENERGY_OSTRICH_EGG} кКал/100гр', type=FLOAT)
portion_ostrich_egg_energy = round(portion_ostrich_egg * ENERGY_OSTRICH_EGG / 100, 2)
total_energy = total_energy + portion_ostrich_egg_energy
put_success(f'Вы заказали {portion_ostrich_egg} граммов страусиных яиц🥚,\n'
            f'Калорийность порции {portion_ostrich_egg_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')


portion_rabbit = slider(f'Введите желаемую порцию кролика🐇, грамм'
                        f'Калорийность {ENERGY_RABBIT} кКал/100гр', min_value=0, max_value=2500)
portion_rabbit_energy = round(portion_rabbit * ENERGY_RABBIT / 100, 2)
total_energy = total_energy + portion_rabbit_energy
put_success(f'Вы заказали {portion_rabbit} граммов кролика🐇,\n'
            f'Калорийность порции {portion_rabbit_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')


portion_banana = pw_input(f'Введите желаемую порцию бананов🍌, грамм'
                          f'Калорийность {ENERGY_BANANA} кКал/100гр', type=FLOAT)
portion_banana_energy = round(portion_banana * ENERGY_BANANA / 100, 2)
total_energy = total_energy + portion_banana_energy
put_success(f'Вы заказали {portion_banana} граммов банана🍌,\n'
            f'Калорийность порции {portion_banana_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_pistachios = pw_input(f'Введите желаемую порцию фисташек, грамм'
                          f'Калорийность {ENERGY_PISTACHIOS} кКал/100гр', type=FLOAT)
portion_pistachios_energy = round(portion_pistachios * ENERGY_PISTACHIOS / 100, 2)
total_energy = total_energy + portion_pistachios_energy
put_success(f'Вы заказали {portion_pistachios} граммов фисташек,\n'
            f'Калорийность порции {portion_pistachios_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_waffles = pw_input(f'Введите желаемую порцию вафлей, грамм'
                          f'Калорийность {ENERGY_WAFFLES} кКал/100гр', type=FLOAT)
portion_waffles_energy = round(portion_waffles * ENERGY_WAFFLES / 100, 2)
total_energy = total_energy + portion_waffles_energy
put_success(f'Вы заказали {portion_waffles} граммов вафлей,\n'
            f'Калорийность порции {portion_waffles_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_perch = pw_input(f'Введите желаемую порцию окуня, грамм'
                          f'Калорийность {ENERGY_PERCH} кКал/100гр', type=FLOAT)
portion_perch_energy = round(portion_perch * ENERGY_PERCH / 100, 2)
total_energy = total_energy + portion_perch_energy
put_success(f'Вы заказали {portion_perch} граммов окуня,\n'
            f'Калорийность порции {portion_perch_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_kefir = pw_input(f'Введите желаемую порцию кефира, миллилитров'
                          f'Калорийность {ENERGY_KEFIR} кКал/100мл', type=FLOAT)
portion_kefir_energy = round(portion_kefir * ENERGY_KEFIR / 100, 2)
total_energy = total_energy + portion_kefir_energy
put_success(f'Вы заказали {portion_kefir} миллилитров кефира,\n'
            f'Калорийность порции {portion_kefir_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_pepper = pw_input(f'Введите желаемую порцию перца, грамм'
                          f'Калорийность {ENERGY_PEPPER} кКал/100гр', type=FLOAT)
portion_pepper_energy = round(portion_pepper * ENERGY_PEPPER / 100, 2)
total_energy = total_energy + portion_pepper_energy
put_success(f'Вы заказали {portion_pepper} граммов перца,\n'
            f'Калорийность порции {portion_pepper_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')

portion_parsley = pw_input(f'Введите желаемую порцию петрушки, грамм'
                          f'Калорийность {ENERGY_PARSLEY} кКал/100гр', type=FLOAT)
portion_parsley_energy = round(portion_parsley * ENERGY_PARSLEY / 100, 2)
total_energy = total_energy + portion_parsley_energy
put_success(f'Вы заказали {portion_parsley} граммов петрушки,\n'
            f'Калорийность порции {portion_parsley_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')


total_cost = Decimal(total_energy) * Decimal(PRICE_ONE_KILO_CALORIE)
rounded_total_cost = total_cost.quantize(Decimal('0.00'))
put_success(f'Обащая калорийность: {total_energy} кКал\n'
            f'Общая стоимость заказа: {rounded_total_cost} грн.')

portion_bread = pw_input(f'Введите желаемую порцию хлеба, грамм'
                          f'Калорийность {ENERGY_BREAD} кКал/100гр', type=FLOAT)
portion_bread_energy = round(portion_bread * ENERGY_BREAD / 100, 2)
total_energy = total_energy + portion_bread_energy
put_success(f'Вы заказали {portion_bread} граммов перца,\n'
            f'Калорийность порции {portion_bread_energy}\n'
            f'Общая накопленая калорийность заказа: {total_energy}')


if total_energy < 1000:
    put_warning("Вы, наверное останетесь голодным")
elif 1000 <= total_energy <= 1500:
    put_success("Это именно ваш вариант ужина")
else:
    put_error("Вы, столько не съедите, это деньги в мусорку")
