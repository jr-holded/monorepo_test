FROM python:3.10-slim
# above line should always be the first line of this Dockerfile

# Copy all resources and profile file into image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Installing all necessary dependencies
RUN pip install -r requirements.txt

CMD ["python"]