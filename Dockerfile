FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AugustoGiuffrida.git

WORKDIR /ajedrez-2024-AugustoGiuffrida

RUN pip install -r requirements.txt

CMD ["python", "-m", "game.cli", "--no-menu"]

# docker buildx build -t ajedrez-2024-augustogiuffrida .
# docker run -i ajedrez-2024-augustogiuffrida
# docker stop ajedrez-2024-augustogiuffrida
# docker rm ajedrez-2024-augustogiuffrida
