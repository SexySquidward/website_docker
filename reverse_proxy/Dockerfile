FROM nginx
RUN mkdir ~/nginx-ssl/conf.d
COPY default.conf /nginx-ssl/conf.d
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
