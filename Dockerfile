FROM nginx
COPY index.html /usr/share/nginx/html/
COPY images /usr/share/nginx/html/images
COPY pages /usr/share/nginx/html/pages
COPY scripts /usr/share/nginx/html/scripts
COPY css /usr/share/nginx/html/css