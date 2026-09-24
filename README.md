# Painel Terra e Clima

Painel em português de monitoramento de fenômenos naturais: ciclones, enchentes, terremotos, vulcões, tsunamis e ondas de calor, com o **El Niño 2026–27** em destaque.

- Mapa-múndi centrado no Pacífico com as regiões Niño e os eventos do dia
- Plantão do planeta com filtros por tipo de evento
- Boletins do El Niño (NOAA CPC e IRI Columbia), probabilidades por trimestre e linha do tempo
- Links para imagens de satélite oficiais

## Como usar

É uma página estática, num único arquivo: abra `index.html` no navegador ou publique com GitHub Pages.

Os eventos ficam no bloco JSON `<script type="application/json" id="dados">` dentro do `index.html`. Para atualizar o plantão basta editar essa lista.

## Segurança

- Sem backend, formulários ou chaves de API
- Textos dos eventos inseridos com `textContent` (sem `innerHTML` com dados externos)
- Links externos só em `https` e abertos com `rel="noopener noreferrer"`

## Fontes

NOAA CPC, IRI Columbia, AEMET, INMET, CEMADEN, USGS, NHC e veículos de imprensa citados em cada evento.

Criado por Felipe Aringhieri Calderan · FarincalTec
