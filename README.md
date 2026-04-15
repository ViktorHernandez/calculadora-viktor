# Calculadora — Viktor Raúl Hernández Vargas
**Matrícula:** Al03003728 | **Universidad Tecmilenio**

Aplicación web que implementa calculadora aritmética, binaria y lógica, desplegada en AWS S3 mediante un pipeline CI/CD con GitHub → CodeBuild → S3.

## Estructura del repositorio

```
calculadora-viktor/
  app/
      index.html      página principal
      style.css       estilos
      logo.png        logo Tecmilenio
  Dockerfile          imagen Docker para desarrollo local
  server.py           servidor Python local
  backup.py           script que genera backup.log en cada deploy
  buildspec.yml       instrucciones para AWS CodeBuild
  .gitignore
  README.md
```

## Funcionalidades

**Calculadora aritmética** — suma, resta, multiplicación, división, porcentaje con historial de expresión.

**Calculadora binaria** — AND, OR, XOR, NOT, SHL, SHR, suma y resta. Muestra resultado en decimal, binario y hexadecimal.

**Calculadora lógica** — AND, OR, NOT, NAND, NOR, XOR, XNOR, implicación y bicondicional con tabla de verdad completa.

## Correr localmente con Docker

```bash
docker build -t calculadora-viktor .
docker run -p 8080:8080 calculadora-viktor
```

Abre http://localhost:8080 en tu navegador.

## Correr localmente con Python

```bash
python server.py
```

## Pipeline AWS

| Etapa | Servicio |
|-------|---------|
| Source | GitHub (a través de GitHub App) |
| Build | AWS CodeBuild |
| Deploy | Amazon S3 Static Website |

**Recursos:**
- Bucket S3: `calculadora-viktor-2026`
- CodeBuild: `calculadora-viktor-build`
- Pipeline: `calculadora-viktor-pipeline`

## backup.log

Cada ejecución del pipeline genera una entrada en `backup.log` con timestamp, Build ID, commit y lista de archivos desplegados. El archivo se sube al bucket S3 al final de cada build.
