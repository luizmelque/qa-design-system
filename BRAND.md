# Identidade Visual — QA Design System

Guia de referência para manter consistência em todos os componentes SVG deste repositório.

---

## ⚠️ v2 — Correções de robustez (leia antes de subir)

Esta versão corrige 3 problemas encontrados no README publicado:

### 1. Tamanho quebrando em alguns contextos (ex: botões gigantes)

**Causa:** nenhum SVG tinha os atributos `width`/`height` no elemento raiz — só `viewBox`. Sem tamanho intrínseco declarado, o navegador usa um padrão de **300×150px** quando o contexto não força um tamanho. Isso é o que deixou os botões (Email, LinkedIn, Portfolio) enormes.

**Correção:** todo arquivo agora declara `width` e `height` explícitos, iguais ao `viewBox`. Isso garante que cada componente renderiza no tamanho certo **mesmo sem** nenhum `width` na tag `<img>` do README — funciona em qualquer contexto (README, link direto, app mobile, outro site).

### 2. Texto invisível no tema escuro (headers e roadmap)

**Causa:** os headers de seção e os rótulos do roadmap usavam texto escuro (`#0F1B33`) direto sobre fundo transparente. No tema claro do GitHub isso é legível; no tema escuro, o texto se mistura com o fundo quase preto da página e desaparece.

**Correção:** headers e roadmap agora são **cards autocontidos** — fundo escuro fixo (`#0F1B33`) sempre presente, com texto branco por cima. Não dependem mais da cor de fundo da página, então funcionam de forma idêntica em tema claro, escuro, ou qualquer outro contexto. Esse é o mesmo princípio que já protegia os badges e botões (que sempre tiveram fundo próprio).

### 3. Live GitHub Stats não carregando

**Causa:** a instância pública do `github-readme-stats.vercel.app` é um serviço gratuito compartilhado por milhares de perfis — sofre rate-limiting e quedas com frequência (isso é documentado como problema conhecido pelos próprios mantenedores do projeto). Não é um bug do seu README; é uma limitação de infraestrutura de terceiros.

**Opções para resolver de vez** (ver conversa para detalhes):
- Fazer deploy da sua própria instância no Vercel (gratuito, ~2 minutos, remove o limite compartilhado)
- Usar GitHub Actions para gerar um SVG estático no seu próprio repositório em um horário fixo (não depende de terceiros online)
- Manter como está e aceitar que pode falhar ocasionalmente

---

## Cores

| Nome | Token | Hex | Uso |
|---|---|---|---|
| Ink | `--ink` | `#0F1B33` | Fundo dos cards autocontidos (headers, roadmap, badges) |
| Ink Track | `--ink-track` | `#1E2C4A` | Trilho de barras de progresso sobre fundo ink |
| Brand | `--brand` | `#2F5FFF` | Cor primária — chips, bordas, ícones, barras de progresso |
| Accent | `--accent` | `#00C2B8` | Acento secundário — checkmarks, indicadores "verificado"/"atual" |
| Muted | `--muted` | `#64748B` | Texto secundário sobre fundo claro |
| Muted Light | `--muted-light` | `#94A3B8` | Texto secundário sobre fundo ink (escuro) |
| Paper | `--paper` | `#F7F8FA` | Fundo claro (cards de projeto, botões) |
| White | `--white` | `#FFFFFF` | Texto sobre fundo escuro/brand |

## Regra de contraste (nova, obrigatória)

**Todo componente que contém texto deve ter seu próprio fundo opaco** — nunca texto direto sobre fundo transparente. Isso garante que o componente renderiza corretamente em qualquer contexto (tema claro, escuro, terceiros incorporando o SVG, impressão) sem depender da página em que está embutido.

## Regra de tamanho (nova, obrigatória)

**Todo componente deve declarar `width` e `height` no elemento `<svg>` raiz**, além do `viewBox`, com valores iguais às dimensões do `viewBox`. Isso garante tamanho correto por padrão, mesmo sem nenhum `width` na tag `<img>` que o referencia.

## Monograma

```
<✓>
```
Arquivo: [`brand-mark.svg`](./brand-mark.svg).

## Tipografia

```
-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif
```

## Traço e forma

- **Espessura de linha:** `2px` (ícones grandes) ou `1.6–2.2px` (ícones pequenos)
- **Cap/join:** sempre `round`
- **Raio de borda:** `999px` (pill) para badges/botões · `12–16px` para cards/headers/chips

---

## Componentes

| Categoria | Arquivo | Fundo | Animado? |
|---|---|---|---|
| Brand | `brand-mark.svg` | próprio (blue) | — |
| Dividers | `divider-blue.svg` | transparente (linha) | — |
| Dividers | `divider-blue-animated.svg` | transparente (linha) | ✅ brilho passando |
| Headers | `about.svg`, `projects.svg`, `skills.svg`, `roadmap.svg`, `philosophy.svg`, `contact.svg` | próprio (ink) | — |
| Headers | `typing-intro-en.svg`, `typing-intro-pt.svg` | transparente (texto azul) | ✅ efeito de digitação |
| Badges (tecnologia) | playwright, cypress, sql, postman, javascript, typescript, docker, git, nodejs, jira, **selenium, python, php, postgresql, github, trello, vscode** | próprio (ink) — pill com ✓ teal | — |
| Tags (categoria, sem ícone) | `tag-manual.svg`, `tag-exploratory.svg` / `tag-exploratorio.svg`, `tag-ux-analysis.svg` / `tag-analise-ux.svg`, `tag-checklist.svg`, `tag-test-matrix.svg` / `tag-matriz-testes.svg`, `tag-bug-report.svg`, `tag-api.svg` | próprio (ink-track, mais discreto) | — |
| Buttons | `github.svg`, `linkedin.svg`, `portfolio.svg`, `email.svg` | próprio (branco) | — |
| Cards | `project-card.svg`, `feature-card.svg` (templates) · `empty-card.svg` | próprio (paper) | — |
| Roadmap | `roadmap.svg` | próprio (ink) | — |
| Roadmap | `roadmap-animated.svg` | próprio (ink) | ✅ barras preenchendo |
| Timeline | `career.svg` | transparente (conector) | — |
| Timeline | `career-animated.svg` | transparente (conector) | ✅ nó atual pulsando |
| Stats | `github-stats.svg`, `activity.svg` (moldura, sem dados reais) | próprio (ink/paper) | — |

### Badges vs. Tags — quando usar cada um

- **Badge** (pill com ✓ teal): para tecnologias/ferramentas reais usadas (Playwright, Python, Docker...).
- **Tag** (pill discreta, sem ícone, texto mais claro/muted): para categorias ou tipos de artefato dentro de uma tabela (Manual, Checklist, Bug Report...) — mesma forma de pill, visual mais neutro para não competir com os badges de tecnologia na mesma linha.

**Nunca misture com badges do shields.io** (ou qualquer serviço externo com cantos retos) na mesma tabela/linha dos nossos badges — a inconsistência de forma (pill vs. retângulo) é o que causava o visual "feio" reportado. Sempre que precisar de uma tag/badge nova, gere no mesmo padrão pill deste repositório.

### Sobre `typing-intro-*.svg`

Efeito de digitação com uma frase fixa, 100% autocontido (sem depender de serviço externo). É uma alternativa mais simples ao `readme-typing-svg.demolab.com` que você já está usando (que faz rotação entre várias frases) — use o que preferir. A vantagem deste é zero dependência externa: nunca vai cair ou dar timeout.

### Sobre `career.svg` / `career-animated.svg`

Só a estrutura visual (linha + marcadores) — as datas e marcos ficam em markdown normal ao lado, não dentro do SVG.
