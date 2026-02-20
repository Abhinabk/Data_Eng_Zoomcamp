build:
	docker build -t test:pandas -f docker_workshop/pipeline/Dockerfile .

run:
	docker run -it test:pandas 10

all: build run
