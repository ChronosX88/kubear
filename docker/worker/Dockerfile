FROM medved_base:latest

RUN pacman -S --noconfirm --needed git libpcap linux-headers clang tor

RUN git clone https://github.com/robertdavidgraham/masscan && \
    cd masscan && \
    make -j && \
    mv bin/masscan /usr/bin/masscan

ADD files/run.sh /tmp/run.sh

CMD ["/tmp/run.sh"]
