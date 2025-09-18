
## Descrição
Aplicação Flask simples para testes iniciais do projeto EasyOrder.  
No Dia 3, focamos em rodar a API localmente, sem usar Docker, devido a limitações de hardware.

---

## Tecnologias
- Python 3.11
- Flask 3.1.2
- Git
- (Opcional) VS Code ou outro editor de código

---

## Estrutura do projeto

Este projeto consiste em um pipeline de CI/CD usando Docker e GitHub Actions, com objetivo de:

Buildar a imagem Docker do projeto.

Enviar (push) a imagem para o Amazon ECR.

(Opcional) Fazer deploy em um cluster ECS da AWS.

Observação: Por limitações do ambiente utilizado (notebook local sem suporte à virtualização), não foi possível criar ou acessar o cluster ECS real. Portanto, o deploy no ECS está configurado, mas não foi executado de fato.

2. Estrutura do Projeto
Projeto_Devops/
│
├── .github/workflows/
│   └── docker-deploy.yml      # Workflow do GitHub Actions
│
├── app.py                     # Código principal da aplicação
├── Dockerfile                 # Configuração do container Docker
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo

3. Como o Pipeline Funciona

O arquivo .github/workflows/docker-deploy.yml possui as seguintes etapas:

Checkout do código → baixa os arquivos do repositório.

Configuração da AWS CLI → conecta o workflow à AWS usando secrets.

Login no Amazon ECR → autentica para enviar imagens Docker.

Build e push da imagem Docker → cria a imagem e envia para o ECR.

Deploy no ECS (opcional) → atualiza o serviço no cluster ECS.

Como o cluster não foi criado, essa etapa apenas mostra a mensagem:

Deploy ignorado, cluster fictício ainda não existe.

4. Limitações

O deploy no ECS não pôde ser executado porque o notebook/ambiente usado para o desenvolvimento não suporta virtualização.

O workflow está configurado com um nome fictício de cluster (Devops-pipeline), permitindo que as etapas anteriores (build e push da imagem) funcionem normalmente.

O pipeline está pronto para funcionar 100% assim que um cluster ECS real for criado e o nome atualizado.

5. Testando Localmente

Mesmo sem o cluster ECS, você pode testar todo o pipeline localmente:

Passo 1 — Instalar ferramentas

Docker: https://www.docker.com/products/docker-desktop

AWS CLI: https://aws.amazon.com/cli/

docker --version
aws --version

Passo 2 — Configurar credenciais AWS
aws configure


Insira suas credenciais e região (sa-east-1).

Passo 3 — Build da imagem Docker
docker build -t devops-pipeline:latest .
docker images

Passo 4 — Login e push para o ECR
aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.sa-east-1.amazonaws.com
aws ecr create-repository --repository-name devops-pipeline
docker tag devops-pipeline:latest <aws_account_id>.dkr.ecr.sa-east-1.amazonaws.com/devops-pipeline:latest
docker push <aws_account_id>.dkr.ecr.sa-east-1.amazonaws.com/devops-pipeline:latest

Passo 5 — Deploy ECS (opcional)
aws ecs update-service --cluster Devops-pipeline --service devops-service --force-new-deployment --image <aws_account_id>.dkr.ecr.sa-east-1.amazonaws.com/devops-pipeline:latest


Vai dar erro se o cluster não existir, mas no workflow do GitHub Actions isso não quebra o pipeline.

6. Conclusão

O pipeline está pronto e funcional para build e push da imagem Docker.

O deploy no ECS está configurado, mas não foi testado devido às limitações do ambiente.

Basta criar um cluster ECS real e atualizar o nome no workflow para ter o pipeline completo e funcional