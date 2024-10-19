# Ajedrez-Augusto Giuffrida

Flujo de clases
Aquí tienes un simple flujo de comunicación entre clases:


## Classes work flow


```mermaid
graph TD;
    Main-->Chess;
    Main-->Tool;
    Chess-->Board;
    Chess-->Player;
    Chess-->Piece;
    Board-->Cell;
    Cell-->Piece;

```


| **Metric**        | **Badge**|
|-------------------|------------------|
| **CircleCI**      | [![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/tree/main) |
| **Maintainability** | [![Maintainability](https://api.codeclimate.com/v1/badges/7a72c784af7a29857334/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/maintainability)|
| **Test Coverage**  | [![Test Coverage](https://api.codeclimate.com/v1/badges/7a72c784af7a29857334/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/test_coverage)|




