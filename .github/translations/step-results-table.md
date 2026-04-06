{%- set all_passed = (results_table | selectattr("passed") | length) == (results_table | length) %}

{%- if all_passed %}

## Passo {{ step_number }} - Aprovado ✅

{%- else %}

## Passo {{ step_number }} - Falhou ❌

{%- endif %}

{%- if all_passed %}
<img src="https://octodex.github.com/images/inflatocat.png" align="right" height="150px" alt="Imagem do Inflatocat indicando que o passo foi aprovado" />
{%- else %}

<img src="https://octodex.github.com/images/spidertocat.png" align="right" height="100px" alt="Imagem do Spidertocat indicando que o passo falhou" />
Algumas verificações falharam. Revise os resultados abaixo e tente novamente.

Hora de encontrar o bug! 🤔
{%- endif %}

| Status | Descrição |
| ------ | --------- |

{%- for row in results_table %}
| {% if row.passed -%}✅ - OK{%- else -%}❌ - Falhou{%- endif %} | {{ row.description }} |
{%- endfor %}

{%- if tips and tips.length %}

### Dicas

{%- for tip in tips %}

- {{ tip }}
  {%- endfor %}

{%- endif %}
