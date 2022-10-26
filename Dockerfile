FROM python
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-santino-rosso.git
WORKDIR /parcial-2-2022-santino-rosso
CMD ["python", "test.py"]


