# Rotinas de atualização dos dados de futebol
Esse é o repositorio com as rotinas de atualização dos dados de futebol do repositório [Kickster Data](https://github.com/pedrohgoncalvess/kickster-data). A necessidade desse repositório
é que não queremos apenas os dados históricos, mas queremos também acompanhar as ligas já que estudaremos qual as melhores apostas a se fazer com os dados que temos.

Vou explicar de maneira breve como se organiza o código, oque cada diretório representa e como as rotinas funcionam.

## routines dir

No diretório routines tem as rotinas de atualização dos dados. Eles estão separados em alguns segmentos pra ter uma organização melhor.
> teams: rotina que atualiza os dados dos times.
> fixtures: rotina de atualização das partidas.

### fixtures

#### rounds

A rounds pode parecer confuso, mas a nomenclatura é pra sugerir que 1 round possui diversas partidas e que a atualização acontece em rounds
e não em fixtures.
