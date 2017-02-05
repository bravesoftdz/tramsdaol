Assume the temperature doesn’t vary within the same Zipcode / Assume the temperature for a Zipcode doesn’t vary within 1­hour windows.

O primeiro requisito ficou um pouco confuso pra mim com relação ao segundo, pode me dar mais detalhes sobre ele? 
Vamos assumir o segundo requisito como verdade, o que acha? (podemos explorar algum recurso de cache já que a temperatura não varia em 1 hora).

Must use the Google Geocoding API to get the zipcode for the given address / Must use Open Weather Map’s API in order to fetch the temperature for a certain Zipcode.

O uso do zipcode não é uma boa opção, fiz alguns testes com o zipcode de algumas cidade e bairros na API do Open Weather Map’s e muitos nem aparecem. Sem falar que a complexidade de implementação vai aumentar, pois preciso fazer uma consulta a mais para descobrir o zipcode de um endereço, mais detalhes aqui: http://gis.stackexchange.com/questions/33966/google-geocoder-lookup-get-postal-code-by-country-and-city

A solução perfeita para o nosso projeto é usar a Longitude e a Latitude fornecidas pelo Google Geocoding API, essa informação tem uma precisão incrível, e é mais fácil de consultar do que o zipcode.

Uma terceira opção é eliminar a necessidade de usar o Google Geocoding API usando o endereço que o usuário digitar para buscar direto na API do Open Weather Map’s, realizei testes e a precisão dessa busca é muito ruim, não recomendo.

A solução “like a glove” é o uso da Longitude de Latitude fornecidas pelo Google Geocoding API, posso partir para essa solução, eliminando o uso do zipcode?

Create a tool that exports usage by IP

Sobre a ferramenta que vai exportar o relatório de uso por IP, qual o nível de detalhe de tempo que interessa? Tem que ser os horários exatos ou só saber o número de acessos de um determinado IP por hora (ou minuto, etc) já serve? 
Quanto menos detalhes for necessário, mais simples fica o armazenamento e mais fácil de atender pra grande quantidade de acessos.
Posso partir do pressuposto que o usuário dessa ferramenta será um administrador de sistema/suporte técnico? (dessa forma não há necessidade de criar uma UI para isso).

Eu vou partir para uma arquitetura que tenho usado nos últimos projetos que trabalhei, é uma arquitetura SPA ideal para esse projeto, utilizando Python/Django/PostgreSQL/REST na camada do backend e Angular 2/Typescript ma camada do frontend.  


