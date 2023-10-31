
FROM public.ecr.aws/docker/library/python:3.9.13-slim

WORKDIR /app

# Install shared Hedral packages from AWS CodeArtifact
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["waitress-serve", "--port", "5001", "--call", "app:create_app"]