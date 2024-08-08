# Notas

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