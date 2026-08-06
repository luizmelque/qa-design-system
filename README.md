# QA Design System

Sistema de componentes visuais em **SVG** — headers, badges, botões, cards, divisores, timeline, roadmap e stats — usados em todos os repositórios de QA do [Luiz Melque](https://github.com/luizmelque).

O objetivo é simples: manter uma identidade visual única e consistente em todos os projetos, sem duplicar assets ou reinventar o layout a cada novo README.

---

## Por que este repositório existe

Em vez de cada repositório ter seus próprios ícones e banners soltos, este repo funciona como a **fonte oficial** de todos os componentes visuais. Qualquer projeto novo — de automação, API testing, documentação, etc. — referencia os SVGs daqui em vez de recriar do zero.

Vantagens:

- **Consistência** — mesmo traço, mesma cor, mesma tipografia em todo lugar.
- **Manutenção centralizada** — atualizou um badge aqui, atualiza em todos os repos que o usam.
- **Leveza** — SVG pesa poucos KB e escala em qualquer resolução, sem perda de qualidade.

---

## Estrutura

```
qa-design-system/
│
├── headers/      → títulos de seção (About, Projects, Skills, Roadmap, Contact...)
├── dividers/      → linhas separadoras entre seções
├── cards/        → cards de projeto e destaque
├── buttons/      → botões de link (GitHub, LinkedIn, Portfolio, Email)
├── badges/       → selos de tecnologia (Playwright, Cypress, SQL, Docker...)
├── roadmap/      → componente visual de roadmap
├── timeline/      → linha do tempo de carreira/estudos
└── stats/        → estatísticas (GitHub stats, atividade)
```

---

## Como usar em outro repositório

Todo arquivo SVG deste repositório pode ser referenciado diretamente pela URL **raw** do GitHub, sem precisar baixar ou copiar o arquivo.

### 1. Pegue a URL raw do componente

No GitHub, abra o arquivo `.svg` desejado, clique em **Raw** e copie a URL. O padrão é:

```
https://raw.githubusercontent.com/luizmelque/qa-design-system/main/<pasta>/<arquivo>.svg
```

### 2. Use no README de qualquer projeto

```markdown
![Playwright](https://raw.githubusercontent.com/luizmelque/qa-design-system/main/badges/playwright.svg)
```

### 3. Para elementos clicáveis (botões, links)

```markdown
[![GitHub](https://raw.githubusercontent.com/luizmelque/qa-design-system/main/buttons/github.svg)](https://github.com/luizmelque)
```

Assim, qualquer atualização visual feita aqui reflete automaticamente em todos os repositórios que usam o componente — sem precisar editar cada um manualmente.

---

## Componentes

> ✅ disponível · 🚧 em desenvolvimento

### Headers

| Componente | Status |
|---|---|
| about.svg | 🚧 |
| projects.svg | 🚧 |
| skills.svg | 🚧 |
| roadmap.svg | 🚧 |
| philosophy.svg | 🚧 |
| contact.svg | 🚧 |

### Dividers

| Componente | Status |
|---|---|
| divider-blue.svg | 🚧 |
| divider-gray.svg | 🚧 |
| divider-light.svg | 🚧 |

### Cards

| Componente | Status |
|---|---|
| project-card.svg | 🚧 |
| feature-card.svg | 🚧 |
| empty-card.svg | 🚧 |

### Buttons

| Componente | Status |
|---|---|
| github.svg | 🚧 |
| linkedin.svg | 🚧 |
| portfolio.svg | 🚧 |
| email.svg | 🚧 |

### Badges

| Componente | Status |
|---|---|
| playwright.svg | 🚧 |
| cypress.svg | 🚧 |
| postman.svg | 🚧 |
| javascript.svg | 🚧 |
| typescript.svg | 🚧 |
| sql.svg | 🚧 |
| docker.svg | 🚧 |
| git.svg | 🚧 |
| github.svg | 🚧 |
| nodejs.svg | 🚧 |
| jira.svg | 🚧 |

### Roadmap

| Componente | Status |
|---|---|
| roadmap.svg | 🚧 |

### Timeline

| Componente | Status |
|---|---|
| career.svg | 🚧 |

### Stats

| Componente | Status |
|---|---|
| github-stats.svg | 🚧 |
| activity.svg | 🚧 |

---

## Padrão de identidade visual

Todos os componentes seguem o mesmo guia de estilo:

- **Cor principal:** azul (a definir hex exato)
- **Traço:** consistente entre todos os ícones (mesma espessura)
- **Tipografia:** mesma fonte em todos os headers e cards
- **Formato:** SVG puro, sem dependências externas

---

## Repositórios que usam este design system

- [`luizmelque`](https://github.com/luizmelque/luizmelque) — perfil
- *(adicionar aqui conforme novos repos forem criados)*

---

## Licença

Este projeto está sob a licença especificada em [LICENSE](./LICENSE).
