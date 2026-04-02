# Squad03-Backend-PS-EJECT
Repositório destinado á equipe de Back-End do Squad03 no processo seletivo da EJECT 2026.1

## Diagrama de Classe
``` mermaid
classDiagram

Reserva <.. Quarto
Reserva <.. Hospede
<<Service>> Reserva

class Quarto{
  -int quarto_id
  +int quarto_numero
  +float valor_diaria
  +tipo_de_quarto()
  +quarto_status()
}
class Hospede{
  -int hospede_id
  +str hospede_nome
  #int hospede_telefone
  #str hospede_email
}

class Reserva{
  -int reserva_id
  +bool check_in
  +bool check_out
  +float valor_total
  +reserva_status()

}
