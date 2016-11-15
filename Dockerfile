FROM ubuntu:14.04
MAINTAINER Leticia Santiago

RUN apt-get update
RUN apt-get install python-webpy -y
RUN apt-get install python-soaplib -y
ADD /soapserver.py /opt/
RUN chmod 755 /opt/soapserver.py 

EXPOSE 8080

CMD ["/opt/soapserver.py"]
