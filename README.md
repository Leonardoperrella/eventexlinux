# EVENTEX

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/Leonardoperrella/eventexlinux.svg?branch=master)](https://travis-ci.org/Leonardoperrella/eventexlinux)

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/Leonardoperrella/eventexlinux wttd
cd wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Define um SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create <minha instancia>
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_key_gen.py`
heroku config:set DEBUG=False
# configuro email
git push heroku --force    

```
