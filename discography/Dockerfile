FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY env.yml .
RUN conda env create -f env.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Make sure the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "environnement correctly installed"

# The code to run when container is started:
COPY grabber.py .
COPY fun.py .
ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "grabber.py","-a","jeff","mills","-f,"disco.json"]
