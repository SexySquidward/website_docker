FROM nginx

VOLUME /etc/letsencrypt/live/haqio.duckdns.org:/etc/ssl/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/
