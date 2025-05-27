FROM python:3.11.0-slim

# Make your customizations here, for example:
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt
CMD ["tail", "-f", "/dev/null"]