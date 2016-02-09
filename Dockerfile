FROM python:2.7
MAINTAINER benaduggan

ENV PYTHONUNBUFFERED 1

# Install linux dependencies
RUN apt-get update && apt-get install -y python-dev libncurses5-dev libxml2-dev libxslt-dev zlib1g-dev libjpeg-dev

# Make the directory for our code
RUN mkdir /data
WORKDIR /data

# Install pip dependencies
ADD application/requirements.txt /data/requirements.txt
RUN pip install -r requirements.t

# Make the log files for Gunicorn
RUN mkdir -p /srv/logs
RUN touch /srv/logs/gunicorn.log /srv/logs/access.log
RUN chown -R www-data:www-data /srv/logs/

# Copy application files over to container
COPY application/ /data/

# Run the application
CMD /data/bin/run.sh
