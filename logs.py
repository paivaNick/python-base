import logging

# logging -> root logger
# minha instancia
log =logging.Logger("meu logger", logging.INFO )
# handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#formataçao
format = logging.Formatter(
    "%(asctime)s - %(message)s - %(levelname)s"
)
ch.setFormatter(format)

log.addHandler(ch)
log.critical("deu ruim!")
