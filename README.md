# Ajedrez

## CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/tree/develop)

## Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/7a72c784af7a29857334/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/maintainability)

## Test Coverage 
[![Test Coverage](https://api.codeclimate.com/v1/badges/7a72c784af7a29857334/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AugustoGiuffrida/test_coverage)

## Entorno virtual

1. Crear un entorno virtual:
```shell
python3 -m venv nombre_del_entorno
```

2.  Activar el entorno virtual en macOS y Linux:
```shell
source nombre_del_entorno/bin/activate
```

3. Desactivar el entorno virtual:
```shell
deactivate
```

## Coverage 

1. Encontrar tests:
```shell
coverage run -m unittest discover -s tests
```

2. Hacer reporte:
```shell
coverage report -m
```

3. Ejecucion directa
```shell
python -m unittest tests/test_example.py
```

4. Reporte y ejecucion:
```shell
coverage run -m unittest && coverage xml && coverage report -m
```

