import requests


def get_nbu_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        rates = {}

        for item in data:
            if item["cc"] in ["EUR", "USD", "PLN"]:
                rates[item["cc"]] = item["rate"]
        return rates
    except Exception as e:
        print(f"Помилка з'єднання з API НБУ: {e}")
        return None


def main():
    print("=== Конвертер іноземної валюти в гривню ===")
    rates = get_nbu_rates()

    if not rates:
        return

    print(f"Актуальні курси НБУ: USD: {rates['USD']}, EUR: {rates['EUR']}, PLN: {rates['PLN']}")

    currency = input("Введіть тип валюти для конвертації (EUR, USD, PLN): ").strip().upper()
    if currency not in rates:
        print("Помилка: Ця валюта не підтримується програмою.")
        return

    try:
        amount = float(input(f"Введіть кількість {currency}: "))

        total_uah = amount * rates[currency]
        print(f"Результат: {amount} {currency} = {total_uah:.2f} UAH")
    except ValueError:
        print("Помилка: Введіть коректне число.")


if __name__ == "__main__":
    main()