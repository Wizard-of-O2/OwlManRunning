FROM node:18
RUN mkdir /root/omr
WORKDIR /root/omr
ADD . .
RUN npm i && npm run build
EXPOSE 3000
CMD node build