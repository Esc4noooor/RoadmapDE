import requests
import pandas as pd
import json
import os


def download_redash_table(api_key, query_id, base_url, output_file):
    """
    Выгружает таблицу из Redash через API
    """
    # Формируем URL
    url = f"{base_url}/api/queries/{query_id}/results.json"

    # Заголовки с API ключом
    headers = {
        'Authorization': f'Key {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        # Делаем запрос
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            data = response.json()

            # Извлекаем данные
            if 'query_result' in data and 'data' in data['query_result']:
                rows = data['query_result']['data']['rows']
                df = pd.DataFrame(rows)

                # Сохраняем в CSV
                df.to_csv(output_file, index=False, encoding='utf-8')
                print(f"✅ Данные сохранены в {output_file}")
                print(f"📊 Размер данных: {len(df)} строк, {len(df.columns)} колонок")

                return df
            else:
                print("❌ Не удалось найти данные в ответе")
                return None
        else:
            print(f"❌ Ошибка HTTP: {response.status_code}")
            print(f"📄 Ответ: {response.text}")
            return None

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None


# Настройки
REDASH_URL = "https://redash.public.karpov.courses"
QUERY_ID = 92480  # Замените на ваш ID
API_KEY = "yYHpEQIThENlU1dkhhA3Q2jkGwIpoTZQIMDi0m3a"  # Замените на ваш ключ
OUTPUT_FILE = "redash_table.csv"

# Запуск
df = download_redash_table(API_KEY, QUERY_ID, REDASH_URL, OUTPUT_FILE)

if df is not None:
    print("\n📋 Первые 5 строк:")
    print(df.head())
    print("\n📊 Информация о данных:")
    print(df.info())