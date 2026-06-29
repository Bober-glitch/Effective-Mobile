FROM python:3.14-slim

# Создаём непривилегированного пользователя
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем приложение
COPY app.py .

# Меняем владельца файлов на нового пользователя
RUN chown -R appuser:appgroup /app

# Переключаемся на непривилегированного пользователя
USER appuser

# Порт (документация)
EXPOSE 8080

# Запуск приложения
CMD ["python", "app.py"]