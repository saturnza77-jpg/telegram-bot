from ollama import chat


def call_llm(prompt, model="gemma3:12b"):

    response = chat(
        model=model,
        messages=[
            {"role": "system", "content": """
تو یک دستیار فارسی‌زبان هستی.

پاسخ تمام سوالات را به زبان فارسی بده.

مهم:
- از Markdown استفاده نکن.
- از علامت * استفاده نکن.
- از علامت ** استفاده نکن.
- از علامت _ برای قالب‌بندی استفاده نکن.
- از Bullet List با علامت * استفاده نکن.
- از تیترهای Markdown استفاده نکن.
- متن را به صورت ساده و خوانا بنویس.
- برای جدا کردن موارد، هر مورد را در یک خط جدید بنویس.
- از شماره‌گذاری معمولی مثل 1.، 2.، 3. می‌توانی استفاده کنی.

فقط متن ساده فارسی تولید کن.
"""
},
            {"role": "user", "content": prompt},
        ],
    )

    return response.message.content
