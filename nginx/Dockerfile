FROM nginx:alpine

# Удаляем дефолтный конфиг
RUN rm /etc/nginx/conf.d/default.conf

# Копируем конфиг
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80