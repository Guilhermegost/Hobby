# Publicar no Render

O serviço existente pode continuar ligado ao repositório e à branch `main`. Antes de publicar a versão nova:

1. No serviço `ahoby`, crie ou selecione um banco PostgreSQL no Render e copie a URL interna.
2. Em **Environment**, configure `DATABASE_URL` com essa URL e `SECRET_KEY` usando a opção **Generate**. O Render define `RENDER` e `RENDER_EXTERNAL_HOSTNAME` automaticamente; o projeto desativa `DEBUG` quando executa no Render.
3. Em **Settings**, use `bash build.sh` como **Build Command** e `gunicorn meu_site.wsgi:application --bind 0.0.0.0:$PORT` como **Start Command**.
4. Salve as configurações e confira a aba **Deploys** para acompanhar a publicação.

O build instala as dependências, reúne os arquivos estáticos e aplica as migrações. O Render pode publicar automaticamente quando um commit chega à branch conectada, se **Auto-Deploy** estiver ativo.

## Dados existentes e fotos

O banco PostgreSQL começa vazio. Trocar o serviço de SQLite para PostgreSQL não copia as contas nem as publicações automaticamente. Faça backup/exportação dos dados da instalação atual antes de mudar `DATABASE_URL`.

As fotos enviadas pelo formulário ficam em `MEDIA_ROOT`. O sistema de arquivos comum do serviço Render não deve ser tratado como armazenamento permanente para uploads; configure armazenamento persistente para mídia antes de depender dessas fotos após uma nova publicação.

Não envie `db.sqlite3`, segredos, ambiente virtual, arquivos `__pycache__` ou novas fotos da pasta `media/post_fotos` ao GitHub.
