# verify_chat_history.py
import json
import sys
import psycopg

# Конфигурация подключения к вашей БД на сервере
DB_CONFIG = {
    "host": "192.168.0.92",
    "port": 5432,
    "dbname": "study_db",
    "user": "postgres",
    "password": "pg_2026!",
}


def get_conn_str() -> str:
    return (
        f"host={DB_CONFIG['host']} port={DB_CONFIG['port']} "
        f"dbname={DB_CONFIG['dbname']} user={DB_CONFIG['user']} "
        f"password={DB_CONFIG['password']}"
    )


def verify_database():
    print("=" * 60)
    print(" Начинаем проверку истории чата в PostgreSQL...")
    print("=" * 60)

    try:
        # Установка соединения
        with psycopg.connect(get_conn_str()) as conn:
            with conn.cursor() as cur:

                # 1. Проверяем общую статистику
                cur.execute("SELECT COUNT(*) FROM tutor_sessions;")
                total_sessions = cur.fetchone()[0]

                cur.execute("SELECT COUNT(*) FROM session_messages;")
                total_messages = cur.fetchone()[0]

                print(f"[СТАТИСТИКА]")
                print(f" -> Всего уникальных сессий в БД: {total_sessions}")
                print(f" -> Всего сохраненных сообщений: {total_messages}")
                print("-" * 60)

                if total_sessions == 0:
                    print("⚠️ Внимание: Таблица сессий пуста. Студенты еще не общались с Тьютором.")
                    return

                # 2. Находим самую последнюю сессию
                cur.execute("""
                    SELECT session_id, user_id, course_tag, variant, started_at 
                    FROM tutor_sessions 
                    ORDER BY started_at DESC 
                    LIMIT 1;
                """)
                latest_session = cur.fetchone()

                session_id, user_id, course_tag, variant, started_at = latest_session
                print(f"[ИНФОРМАЦИЯ О ПОСЛЕДНЕМ ДИАЛОГЕ]")
                print(f" -> ID Сессии (UUID): {session_id}")
                print(f" -> ID Студента:       {user_id}")
                print(f" -> Предмет (Курс):   {course_tag}")
                print(f" -> Вариант задания:  {variant if variant else 'Не указан'}")
                print(f" -> Время начала:     {started_at}")
                print("-" * 60)

                # 3. Вытаскиваем все сообщения для этой сессии в хронологическом порядке
                cur.execute("""
                    SELECT role, content, rag_context_used, created_at 
                    FROM session_messages 
                    WHERE session_id = %s 
                    ORDER BY created_at ASC;
                """, (session_id,))
                messages = cur.fetchall()

                # ИСПРАВЛЕНИЕ: Преобразуем session_id в строку str() перед слайсингом [:8]
                session_str_id = str(session_id)
                print(f"[ХРОНОЛОГИЯ ПЕРЕПИСКИ (Сессия {session_str_id[:8]}...)]\n")

                for idx, (role, content, rag_context, created_at) in enumerate(messages, 1):
                    time_str = created_at.strftime("%H:%M:%S")

                    if role == "user":
                        print(f"[{idx}] 📱 СТУДЕНТ ID {user_id} ({time_str}):")
                        print(f"    {content.strip()}")

                        # Если использовался RAG, выведем факт его использования
                        if rag_context:
                            try:
                                # Предполагаем, что контекст сохранен как JSON-массив
                                chunks = json.loads(rag_context) if isinstance(rag_context, str) else rag_context
                                print(f"    🔍 [RAG]: Использовано чанков контекста: {len(chunks)}")
                            except Exception:
                                pass
                    else:
                        print(f"[{idx}] 👨‍🏫 ИИ-ТЬЮТОР ({time_str}):")
                        # Делаем небольшой отступ для ответа Тьютора, чтобы диалог читался легче
                        indented_content = "\n    ".join(content.strip().split("\n"))
                        print(f"    {indented_content}")

                    print("-" * 60)

    except psycopg.OperationalError as exc:
        print(f"🚨 Ошибка подключения к базе данных на 192.168.0.92:\n{exc}", file=sys.stderr)
    except Exception as exc:
        print(f"🚨 Произошла непредвиденная ошибка при проверке:\n{exc}", file=sys.stderr)


if __name__ == "__main__":
    verify_database()