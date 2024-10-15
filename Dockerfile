FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AugustoGiuffrida.git ajedrez

WORKDIR /ajedrez
RUN git pull

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.cli"]

# docker buildx build -t ajedrez-2024-augustogiuffrida .
# docker run -it ajedrez-2024-augustogiuffrida
# docker stop ajedrez-2024-augustogiuffrida
# docker rm ajedrez-2024-augustogiuffrida
