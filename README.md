# automacaoinstagram
Automação para interagir automaticamente com o nicho de mercado, com o intuito de gerar engajamento. Foi utilizado o pacote selenium e a navegação através XPATH.

O código foi criado para testar uma automação de uma perfil do instagram, usando o selenium para navegar dentro da página, sleep para criar aleatoriedade nos intervalos de ações. O pseudocódigo se baseia em:

1) Entrar no instagram do usuário com login e senha
2) Visitar a página de explorar do instagram
3) Buscar por uma hashtag presente na lista de hashtags definidas pelo nicho do usuário
4) Selecionar aleatoriamente uma dessas hashtags
5) Entrar na postagem mais recente dessa hashtag
6) Curtir e comentar a postagem, utilizando um comentário aleatório da lista
7) Executar a tarefa por 5 vezes e depois voltar para a seleção de hashtag
8) Ao avançar dentro de 50 postagens, sair do loop
9) Ao final, imprimir a quantidade de fotos curtidas e comentários feitos
