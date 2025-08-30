
def main():
    print("✅ Трекер привычек на день")
    print("—" * 50)
    print("Отмечай выполненные дела. В конце посчитаю успех!")

    # Список привычек
    habits = [
        "Выпить стакан воды",
        "Сделать зарядку",
        "Прочитать 10 страниц книги",
        "Не смотреть в телефон первые 30 минут",
        "Написать план на день",
        "Поблагодарить кого-то",
        "Прогуляться 10 минут",
        "Закрыть все вкладки, кроме нужных"
    ]

    completed = []  # Список выполненных

    print("\nВот твои задачи на сегодня:")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit}")

    print("\nПроходи по списку и отмечай, что сделал (введи номер).")
    print("Нажми Enter без ввода, чтобы закончить.\n")

    while True:
        user_input = input("✅ Выполнил номер (или Enter, чтобы завершить): ").strip()
        if not user_input:
            break
        try:
            num = int(user_input)
            if 1 <= num <= len(habits):
                if num not in completed:
                    completed.append(num)
                    print(f"  Отлично! '{habits[num-1]}' — засчитано.")
                else:
                    print("  Уже засчитано!")
            else:
                print(f"  Нет такого номера. От 1 до {len(habits)}")
        except ValueError:
            print("  Введи число или оставь пустым.")

    # Финальный результат
    print("\n" + "🎯 Твой результат за день:")
    print("—" * 50)
    print(f"Всего дел: {len(habits)}")
    print(f"Сделано: {len(completed)}")
    success_rate = len(completed) / len(habits) * 100
    print(f"Успешность: {success_rate:.1f}%")

    # Оценка
    if success_rate == 100:
        print("🔥 Идеально! Ты герой дня!")
    elif success_rate >= 70:
        print("👍 Отлично! Двигаешься вперёд!")
    elif success_rate >= 40:
        print("🙂 Хорошо, но можно лучше!")
    else:
        print("💡 Начни с малого — завтра будет лучше!")

    print("\nТы молодец, что стараешься! 💪")

if __name__ == "__main__":
    main()
