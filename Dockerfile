FROM python
WORKDIR app
COPY hello_pycharm.py .
ENTRYPOINT python hello_pycharm.py