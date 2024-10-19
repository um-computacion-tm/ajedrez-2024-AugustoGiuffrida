FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AugustoGiuffrida.git ajedrez

WORKDIR /ajedrez

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && echo 'Press any key to continue...' && read -n 1 && python -m game.cli"]

#Añadir no cache porque docker toma el ultimo contenor cacheado

# docker buildx build --no-cache -t ajedrez-2024-augustogiuffrida .
# docker run -it ajedrez-2024-augustogiuffrida
# docker stop ajedrez-2024-augustogiuffrida
# docker rm ajedrez-2024-augustogiuffrida
