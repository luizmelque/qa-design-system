# Identidade Visual — QA Design System

Guia de referência para manter consistência em todos os componentes SVG deste repositório.

---

## Cores

| Nome | Token | Hex | Uso |
|---|---|---|---|
| Ink | `--ink` | `#0F1B33` | Texto principal, ícones sobre fundo claro |
| Brand | `--brand` | `#2F5FFF` | Cor primária — chips, bordas, ícones de destaque |
| Accent | `--accent` | `#00C2B8` | Acento secundário — checkmarks, indicadores de "verificado" |
| Muted | `--muted` | `#64748B` | Texto e traços secundários |
| Paper | `--paper` | `#F7F8FA` | Fundo claro (cards, headers) |
| White | `--white` | `#FFFFFF` | Texto sobre fundo escuro/brand |

## Monograma

Em vez de um "LM" literal, o símbolo da marca combina um colchete de código com um checkmark — remete a "código verificado", o núcleo do trabalho de QA:

```
<✓>
```

Use esse símbolo como assinatura visual em banners, favicon e materiais de marca. Arquivo pronto: [`brand-mark.svg`](./brand-mark.svg) (raiz do repositório).

## Tipografia

Como o GitHub não carrega fontes externas (`@font-face`) dentro de SVGs isolados, todos os componentes usam a stack de sistema, que renderiza de forma consistente em qualquer navegador:

```
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif
```

- **Headers de seção:** peso 700 (bold), 22–24px
- **Badges:** peso 600 (semibold), 13–14px
- **Botões:** peso 600 (semibold), 14px

## Traço e forma

- **Espessura de linha:** sempre `2px` (ícones grandes) ou `1.6–2.2px` (ícones pequenos dentro de badges)
- **Cap/join:** sempre `round`
- **Raio de borda:**
  - `999px` (pill) → badges, botões
  - `12px` → cards, chips de ícone em headers
- **Ícones:** desenhados como line-art simples e minimalista — nunca logos oficiais de marcas de terceiros (GitHub, LinkedIn, etc.), para evitar uso indevido de marca registrada. Usamos formas genéricas que remetem ao conceito (rede, código, pasta) mantendo o mesmo traço em todo o sistema.

## Componentes já criados

| Categoria | Arquivo | Status |
|---|---|---|
| Brand | `brand-mark.svg` | ✅ |
| Dividers | `divider-blue.svg` | ✅ |
| Headers | `about.svg` | ✅ |
| Headers | `projects.svg` | ✅ |
| Headers | `skills.svg` | ✅ |
| Headers | `roadmap.svg` | ✅ |
| Headers | `philosophy.svg` | ✅ |
| Headers | `contact.svg` | ✅ |
| Badges | `playwright.svg` | ✅ |
| Badges | `cypress.svg` | ✅ |
| Badges | `sql.svg` | ✅ |
| Badges | `postman.svg` | ✅ |
| Badges | `javascript.svg` | ✅ |
| Badges | `typescript.svg` | ✅ |
| Badges | `docker.svg` | ✅ |
| Badges | `git.svg` | ✅ |
| Badges | `nodejs.svg` | ✅ |
| Badges | `jira.svg` | ✅ |
| Buttons | `github.svg` | ✅ |
| Buttons | `linkedin.svg` | ✅ |
| Buttons | `portfolio.svg` | ✅ |
| Buttons | `email.svg` | ✅ |
| Cards | project-card, feature-card, empty-card | 🚧 |
| Timeline | `career.svg` | 🚧 |
| Roadmap (componente visual) | `roadmap.svg` | 🚧 |
| Stats | github-stats, activity | 🚧 |

Todos os headers, badges de tecnologia e botões estão prontos e seguem o mesmo padrão visual. Faltam apenas os componentes mais complexos — cards, timeline, roadmap (o gráfico visual, não o header) e stats — que entram na próxima sprint.
