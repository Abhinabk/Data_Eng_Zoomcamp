#the base docker imjage to run
FROM python:3.13.11-slim 

#get the UV docker image (only the binary) to /bin folder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

#the working directory
WORKDIR /app 

#insted of doing uv run uv insalls python in /app/.venv add that to path
ENV PATH="/app/.venv/bin:$PATH"

#now copy the dependey files to curr dir
COPY "pyproject.toml" "uv.lock" ".python-version" ./
#install dependeies from the locekd file 
RUN uv sync --locked

#copy the pipeline file to run 
COPY docker_workshop/pipeline/pipeline.py pipeline.py 

#entry point what to run when docker image runs first 
ENTRYPOINT [ "python","pipeline.py" ]

#docker buld command- docker build -t test:pandas -f docker_workshop/pipeline/Dockerfile .
#docker run command- docker run -it test:pandas 10

